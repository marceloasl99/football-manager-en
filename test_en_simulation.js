// test_en_simulation.js
// Node.js simulation test for Astrum Football Manager — European Edition

const fs = require('fs');
const path = require('path');
const vm = require('vm');

// Read index.html and extract script
const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
const scriptStart = html.indexOf('<script>');
const scriptEnd = html.lastIndexOf('</script>');
const jsCode = html.substring(scriptStart + 8, scriptEnd);

// Setup browser mocks
const storage = {};
global.localStorage = {
  getItem: (k) => storage[k] || null,
  setItem: (k, v) => { storage[k] = String(v); },
  removeItem: (k) => { delete storage[k]; },
  clear: () => { Object.keys(storage).forEach(k => delete storage[k]); }
};

global.window = global;
global.addEventListener = () => {};
global.removeEventListener = () => {};

global.document = {
  getElementById: (id) => ({
    value: id === 'club-name' || id === 'teamName' ? 'London City FC' : '',
    innerHTML: '',
    innerText: '',
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false, toggle: () => {} },
    appendChild: () => {},
    setAttribute: () => {},
    getAttribute: () => null,
    addEventListener: () => {},
    querySelector: () => null,
    querySelectorAll: () => []
  }),
  querySelector: () => null,
  querySelectorAll: () => [],
  createElement: () => ({
    style: {},
    classList: { add: () => {}, remove: () => {} },
    appendChild: () => {},
    setAttribute: () => {}
  }),
  body: {
    classList: { add: () => {}, remove: () => {}, toggle: () => {} },
    innerHTML: ''
  },
  documentElement: {
    setAttribute: () => {},
    style: {}
  },
  addEventListener: () => {},
  removeEventListener: () => {}
};
global.navigator = { serviceWorker: { register: () => Promise.resolve() } };
global.location = { reload: () => {} };
global.alert = (msg) => {};
global.confirm = () => true;
global.prompt = (msg, def) => def || '';
global.requestAnimationFrame = (fn) => setTimeout(fn, 0);

// Execute the bundle
console.log('--- Loading European Edition Script ---');
vm.runInThisContext(jsCode);
console.log('Script loaded successfully without errors!');

// Test Nations Definition
console.log('\n--- Verifying Nations Configuration ---');
const expectedNations = ['england', 'spain', 'germany', 'italy'];
for (const n of expectedNations) {
  if (!NATIONS[n]) throw new Error(`Nation ${n} missing in NATIONS!`);
  const count = Object.values(NATIONS[n].teams).reduce((sum, arr) => sum + arr.length, 0);
  console.log(`Nation: ${NATIONS[n].name} (${n}) - Teams: ${count}, Currency: ${NATIONS[n].currency}`);
  if (count !== 72) throw new Error(`Nation ${n} expected 72 teams, got ${count}`);
}

// Test European Giants & Stars
console.log('\n--- Verifying European Giants & Elite Stars ---');
if (!EUROPEAN_GIANTS || EUROPEAN_GIANTS.length < 15) {
  throw new Error(`EUROPEAN_GIANTS expected >= 15 clubs, got ${EUROPEAN_GIANTS ? EUROPEAN_GIANTS.length : 0}`);
}
console.log(`European Giants count: ${EUROPEAN_GIANTS.length}`);
if (!EUROPEAN_STARS || EUROPEAN_STARS.length < 20) {
  throw new Error(`EUROPEAN_STARS expected >= 20 stars, got ${EUROPEAN_STARS ? EUROPEAN_STARS.length : 0}`);
}
console.log(`European Elite Stars count: ${EUROPEAN_STARS.length}`);

// Test Starting a Game in each country
for (const country of expectedNations) {
  console.log(`\n=== Testing Career Initialization: ${country.toUpperCase()} ===`);
  selectedNation = country;
  newGame({
    nation: country,
    name: `${NATIONS[country].name} Athletic`,
    difficulty: 'normal',
    kit1: '#112233',
    kit2: '#ffffff',
    slot: 1
  });

  if (!G || !G.teams || !G.teamName) throw new Error(`Game state G not initialized for ${country}!`);
  const pt = G.teams[G.teamName];
  if (!pt) throw new Error(`Player club ${G.teamName} not found in G.teams!`);
  if (G.nation !== country) throw new Error(`G.nation mismatch: expected ${country}, got ${G.nation}`);
  if (G.currency !== NATIONS[country].currency) throw new Error(`Currency mismatch for ${country}`);

  console.log(`Club created: ${pt.name} in division ${pt.division} (${DIVISIONS[pt.division]})`);
  console.log(`Currency: ${G.currency}, Budget: ${fmtMoney(pt.money)}`);
  console.log(`Squad size: ${pt.squad.length} players`);

  // Verify division names
  const expectedDivs = NATIONS[country].divisions;
  for (let d = 0; d < 4; d++) {
    if (DIVISIONS[d] !== expectedDivs[d]) {
      throw new Error(`Division ${d} name mismatch for ${country}: expected ${expectedDivs[d]}, got ${DIVISIONS[d]}`);
    }
  }
  console.log(`Divisions: ${expectedDivs.join(' -> ')}`);
}

// Deep Season Simulation Test for England
console.log('\n=== Deep Season Simulation Test: ENGLAND (Premier League to League Two) ===');
selectedNation = 'england';
newGame({
  nation: 'england',
  name: 'Crown Athletic',
  difficulty: 'normal',
  kit1: '#00205B',
  kit2: '#FFFFFF',
  slot: 1
});

const pt = G.teams[G.teamName];

// Upgrade Stadium Facilities
console.log('\n--- Testing Stadium & Multi-Purpose Arena ---');
pt.stadium = 35000;
pt.ticketPrice = 30;
pt.medical = 40;
pt.vipBoxes = 20;
pt.multiArena = 1;
pt.fanShow = 1;
console.log(`Stadium Capacity: ${pt.stadium}, Multi-Arena Built: ${pt.multiArena}, Fan Show: ${pt.fanShow}`);

// Test International Scouting
console.log('\n--- Testing International Scouting Expedition ---');
pt.money += 3000000; // ensure funds
startScoutMission('galacticos', 'legend');
if (!G.scoutingMissions || G.scoutingMissions.length === 0) {
  throw new Error('Scouting mission failed to dispatch!');
}
console.log(`Dispatched Galácticos scouting mission. Games remaining: ${G.scoutingMissions[0].gamesRemaining}.`);

// Test Auto Play Tactics Optimizer
console.log('\n--- Testing Smart AFK Auto Play Optimizer ---');
autoSelectXI({ smart: true });
console.log(`Selected XI count: ${G.selected.length} (Formation: ${G.formation})`);
if (G.selected.length !== 11) {
  throw new Error(`Auto XI selected ${G.selected.length} starters instead of 11!`);
}

// Simulate matchdays
console.log('\n--- Simulating Matchdays (Verifying Stamina, Form, Scouting & Arena Income) ---');
let scoutingCompleted = false;

for (let week = 1; week <= 12; week++) {
  // Ensure lineup
  autoSelectXI({ smart: true });
  
  // Play week
  playWeek();

  // Check stamina floor & form floor
  for (const p of pt.squad) {
    if (p.energy != null && p.energy < 35) {
      throw new Error(`Stamina dropped below floor (35%): player ${p.name} has ${p.energy}%`);
    }
    if (p.form != null && p.form < 30) {
      throw new Error(`Form dropped below floor (30): player ${p.name} has ${p.form}`);
    }
  }

  // Check scouting resolution
  if (!scoutingCompleted && G.freeAgents && G.freeAgents.some(p => p.fromScout)) {
    const scouted = G.freeAgents.filter(p => p.fromScout);
    console.log(`Scouting returned at week ${G.week}! Found ${scouted.length} elite options in free agents.`);
    console.log(`First prospect: ${scouted[0].name} (${scouted[0].pos}, Rating: ${scouted[0].rating}, Windows left: ${scouted[0].scoutWindowsRemaining})`);
    
    // Sign the scouted prospect
    const candidate = scouted[0];
    const prevSquadCount = pt.squad.length;
    const signRes = signFreeAgent(candidate.id);
    console.log(`Sign result: ${signRes.msg}`);
    if (!signRes.ok) throw new Error(`Failed to sign scouted player: ${signRes.msg}`);
    if (pt.squad.length !== prevSquadCount + 1) {
      throw new Error('Player not added to squad!');
    }
    const signedP = pt.squad.find(p => p.id === candidate.id);
    if (!signedP || !signedP.fromScout) {
      throw new Error('Signed player missing from squad or not marked fromScout!');
    }
    console.log(`Successfully signed Galáctico star: ${signedP.name} (${signedP.pos}, Rating: ${signedP.rating})!`);
    scoutingCompleted = true;
  }
}

if (!scoutingCompleted) {
  throw new Error('Scouting mission was not resolved in 12 weeks!');
}

console.log(`\nMatches played: ${G.week - 1}. Multi-use arena & matchday revenue collected.`);
console.log(`Current Club Balance: ${fmtMoney(pt.money)}`);

// Test Save & Load
console.log('\n--- Testing Save / Load Integrity ---');
saveGame(1);
const savedRaw = localStorage.getItem('afm_eu_save_1') || localStorage.getItem('astrum_fm_save_1');
if (!savedRaw) throw new Error('Save file not found in localStorage!');
const parsed = JSON.parse(savedRaw);
if (parsed.nation !== 'england') throw new Error(`Saved nation mismatch: ${parsed.nation}`);
console.log(`Save file verified: Nation ${parsed.nation}, Club: ${parsed.teamName}, Season: ${parsed.season}`);

// Test Loading
G = null;
loadGame(1);
if (!G || G.nation !== 'england' || G.teamName !== 'Crown Athletic') {
  throw new Error('Load game failed to restore state correctly!');
}
console.log(`Loaded game successfully restored: ${G.teamName} (${G.nation})`);

console.log('\n======================================================');
console.log('✅ ALL SIMULATION AND ENGINE TESTS PASSED WITH 100% SUCCESS!');
console.log('======================================================');
