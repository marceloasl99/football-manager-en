# -*- coding: utf-8 -*-
"""
Player names, stars, giants, scouting and stadium data for European Edition
"""

EUROPEAN_GIANTS = [
    {"name": "Real Madrid", "country": "Spain", "rating": 450},
    {"name": "Manchester City", "country": "England", "rating": 448},
    {"name": "FC Barcelona", "country": "Spain", "rating": 440},
    {"name": "Bayern Munich", "country": "Germany", "rating": 442},
    {"name": "Liverpool", "country": "England", "rating": 438},
    {"name": "Arsenal", "country": "England", "rating": 435},
    {"name": "Paris Saint-Germain", "country": "France", "rating": 434},
    {"name": "Inter Milan", "country": "Italy", "rating": 432},
    {"name": "Bayer Leverkusen", "country": "Germany", "rating": 430},
    {"name": "Atlético Madrid", "country": "Spain", "rating": 425},
    {"name": "Borussia Dortmund", "country": "Germany", "rating": 424},
    {"name": "Juventus", "country": "Italy", "rating": 422},
    {"name": "AC Milan", "country": "Italy", "rating": 420},
    {"name": "Sporting CP", "country": "Portugal", "rating": 415},
    {"name": "SL Benfica", "country": "Portugal", "rating": 412},
    {"name": "FC Porto", "country": "Portugal", "rating": 408},
    {"name": "Ajax", "country": "Netherlands", "rating": 405},
    {"name": "PSV Eindhoven", "country": "Netherlands", "rating": 402},
    {"name": "Feyenoord", "country": "Netherlands", "rating": 398},
    {"name": "Celtic", "country": "Scotland", "rating": 392}
]

EUROPEAN_STARS = [
    {"n": "Jude Bellingham", "pos": "MF"}, {"n": "Erling Haaland", "pos": "FW"},
    {"n": "Phil Foden", "pos": "MF"}, {"n": "Bukayo Saka", "pos": "FW"},
    {"n": "Declan Rice", "pos": "MF"}, {"n": "Cole Palmer", "pos": "MF"},
    {"n": "Harry Kane", "pos": "FW"}, {"n": "Trent Alexander-Arnold", "pos": "DF"},
    {"n": "John Stones", "pos": "DF"}, {"n": "Jordan Pickford", "pos": "GK"},
    {"n": "Ollie Watkins", "pos": "FW"}, {"n": "Kobbie Mainoo", "pos": "MF"},
    {"n": "Rodri", "pos": "MF"}, {"n": "Lamine Yamal", "pos": "FW"},
    {"n": "Pedri", "pos": "MF"}, {"n": "Gavi", "pos": "MF"},
    {"n": "Nico Williams", "pos": "FW"}, {"n": "Dani Olmo", "pos": "MF"},
    {"n": "Álvaro Morata", "pos": "FW"}, {"n": "Dani Carvajal", "pos": "DF"},
    {"n": "Robin Le Normand", "pos": "DF"}, {"n": "Unai Simón", "pos": "GK"},
    {"n": "Mikel Merino", "pos": "MF"}, {"n": "Ferran Torres", "pos": "FW"},
    {"n": "Florian Wirtz", "pos": "MF"}, {"n": "Jamal Musiala", "pos": "MF"},
    {"n": "Kai Havertz", "pos": "FW"}, {"n": "Leroy Sané", "pos": "FW"},
    {"n": "Joshua Kimmich", "pos": "MF"}, {"n": "Antonio Rüdiger", "pos": "DF"},
    {"n": "Jonathan Tah", "pos": "DF"}, {"n": "Manuel Neuer", "pos": "GK"},
    {"n": "Marc-André ter Stegen", "pos": "GK"}, {"n": "Niclas Füllkrug", "pos": "FW"},
    {"n": "Nicolò Barella", "pos": "MF"}, {"n": "Alessandro Bastoni", "pos": "DF"},
    {"n": "Federico Dimarco", "pos": "DF"}, {"n": "Gianluigi Donnarumma", "pos": "GK"},
    {"n": "Federico Chiesa", "pos": "FW"}, {"n": "Gianluca Scamacca", "pos": "FW"},
    {"n": "Davide Frattesi", "pos": "MF"}, {"n": "Lorenzo Pellegrini", "pos": "MF"},
    {"n": "Riccardo Calafiori", "pos": "DF"}, {"n": "Giacomo Raspadori", "pos": "FW"},
    {"n": "Kylian Mbappé", "pos": "FW"}, {"n": "Antoine Griezmann", "pos": "FW"},
    {"n": "Eduardo Camavinga", "pos": "MF"}, {"n": "Aurélien Tchouaméni", "pos": "MF"},
    {"n": "William Saliba", "pos": "DF"}, {"n": "Theo Hernández", "pos": "DF"},
    {"n": "Mike Maignan", "pos": "GK"}, {"n": "Ousmane Dembélé", "pos": "FW"},
    {"n": "Virgil van Dijk", "pos": "DF"}, {"n": "Frenkie de Jong", "pos": "MF"},
    {"n": "Cody Gakpo", "pos": "FW"}, {"n": "Xavi Simons", "pos": "MF"},
    {"n": "Nathan Aké", "pos": "DF"}, {"n": "Matthijs de Ligt", "pos": "DF"},
    {"n": "Bruno Fernandes", "pos": "MF"}, {"n": "Bernardo Silva", "pos": "MF"},
    {"n": "Rúben Dias", "pos": "DF"}, {"n": "Rafael Leão", "pos": "FW"},
    {"n": "Diogo Costa", "pos": "GK"}, {"n": "Vitinha", "pos": "MF"},
    {"n": "João Neves", "pos": "MF"}, {"n": "Gonçalo Ramos", "pos": "FW"},
    {"n": "Kevin De Bruyne", "pos": "MF"}, {"n": "Jérémy Doku", "pos": "FW"},
    {"n": "Leandro Trossard", "pos": "FW"}, {"n": "Amadou Onana", "pos": "MF"},
    {"n": "Luka Modrić", "pos": "MF"}, {"n": "Joško Gvardiol", "pos": "DF"},
    {"n": "Mateo Kovačić", "pos": "MF"}, {"n": "Dominik Livaković", "pos": "GK"}
]

FIRST_NAMES = [
    # English
    "James", "John", "Harry", "Jack", "Oliver", "George", "Charlie", "Jacob", "Thomas", "William",
    "Henry", "Alfie", "Joshua", "Mason", "Freddie", "Archie", "Arthur", "Leo", "Oscar", "Noah",
    "Marcus", "Trent", "Jude", "Phil", "Declan", "Cole", "Bukayo", "Callum", "Harvey", "Curtis",
    # Spanish
    "Alejandro", "Carlos", "Daniel", "David", "Javier", "Álvaro", "Adrián", "Pablo", "Sergio", "Diego",
    "Hugo", "Mateo", "Lucas", "Manuel", "Mario", "Marcos", "Pedri", "Gavi", "Lamine", "Nico",
    # German
    "Lukas", "Leon", "Finn", "Jonas", "Elias", "Maximilian", "Paul", "Felix", "Noah", "Ben",
    "Tim", "Florian", "Kai", "Jamal", "Leroy", "Joshua", "Antonio", "Ilkay", "Thomas", "Manuel",
    # Italian
    "Leonardo", "Francesco", "Alessandro", "Lorenzo", "Mattia", "Andrea", "Gabriele", "Riccardo",
    "Tommaso", "Edoardo", "Federico", "Nicolò", "Gianluigi", "Davide", "Matteo", "Giacomo", "Marco"
]

LAST_NAMES = [
    # English
    "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright",
    "Thompson", "Evans", "Walker", "White", "Roberts", "Green", "Hall", "Wood", "Jackson", "Clarke",
    "Kane", "Bellingham", "Foden", "Saka", "Rice", "Palmer", "Stones", "Pickford", "Watkins", "Bowen",
    # Spanish
    "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez",
    "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Álvarez", "Romero", "Yamal", "Morata",
    # German
    "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz",
    "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Musiala", "Wirtz", "Havertz",
    # Italian
    "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino",
    "Greco", "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Barella", "Bastoni", "Chiesa", "Dimarco"
]

FOREIGN_NAMES = [
    {"n": "Vinícius Jr", "c": "Brazil", "pos": "FW"},
    {"n": "Rodrygo", "c": "Brazil", "pos": "FW"},
    {"n": "Federico Valverde", "c": "Uruguay", "pos": "MF"},
    {"n": "Darwin Núñez", "c": "Uruguay", "pos": "FW"},
    {"n": "Alexis Mac Allister", "c": "Argentina", "pos": "MF"},
    {"n": "Julián Álvarez", "c": "Argentina", "pos": "FW"},
    {"n": "Lautaro Martínez", "c": "Argentina", "pos": "FW"},
    {"n": "Enzo Fernández", "c": "Argentina", "pos": "MF"},
    {"n": "Emiliano Martínez", "c": "Argentina", "pos": "GK"},
    {"n": "Cristian Romero", "c": "Argentina", "pos": "DF"},
    {"n": "Gabriel Magalhães", "c": "Brazil", "pos": "DF"},
    {"n": "Gabriel Martinelli", "c": "Brazil", "pos": "FW"},
    {"n": "Bruno Guimarães", "c": "Brazil", "pos": "MF"},
    {"n": "Lucas Paquetá", "c": "Brazil", "pos": "MF"},
    {"n": "Richarlison", "c": "Brazil", "pos": "FW"},
    {"n": "Alisson Becker", "c": "Brazil", "pos": "GK"},
    {"n": "Ederson", "c": "Brazil", "pos": "GK"},
    {"n": "Luis Díaz", "c": "Colombia", "pos": "FW"},
    {"n": "Moises Caicedo", "c": "Ecuador", "pos": "MF"},
    {"n": "Piero Hincapié", "c": "Ecuador", "pos": "DF"},
    {"n": "Son Heung-min", "c": "South Korea", "pos": "FW"},
    {"n": "Kaoru Mitoma", "c": "Japan", "pos": "FW"},
    {"n": "Takehiro Tomiyasu", "c": "Japan", "pos": "DF"},
    {"n": "Wataru Endo", "c": "Japan", "pos": "MF"},
    {"n": "Kim Min-jae", "c": "South Korea", "pos": "DF"},
    {"n": "Victor Osimhen", "c": "Nigeria", "pos": "FW"},
    {"n": "Mohamed Salah", "c": "Egypt", "pos": "FW"},
    {"n": "Achraf Hakimi", "c": "Morocco", "pos": "DF"},
    {"n": "Alphonso Davies", "c": "Canada", "pos": "DF"}
]
