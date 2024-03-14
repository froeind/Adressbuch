import random

# Beispiellisten von Ländern, Vornamen und Nachnamen
beispiel_vornamen = ["Max", "Anna", "Paul", "Maria", "Felix", "Sophie", "Tim", "Lena", "Moritz", "Laura", "Julian", "Emma", "Jonas", "Lisa", "Leon", "Sarah", "Luca", "Hannah", "Finn", "Lea", "Elias", "Mia", "Nico", "Jana", "Jan", "Clara", "David", "Lara", "Lukas", "Elena"]
beispiel_nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Krüger", "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier"]
beispiel_strassen = ["Unter den Linden", "Champs-Élysées", "Kurfürstendamm", "Broadway", "Fifth Avenue", "Karl-Marx-Allee", "Oxford Street", "Rodeo Drive", "Abbey Road", "Sunset Boulevard", "Wall Street", "Savile Row", "Via Condotti", "Friedrichstraße", "Nevsky Prospekt", "Ginza", "Rue du Faubourg Saint-Honoré", "Park Avenue", "Mulholland Drive", "Potsdamer Platz", "La Rambla", "Rue de Rivoli", "Changan Avenue", "Via Monte Napoleone", "Michigan Avenue", "Las Ramblas", "Hollywood Boulevard", "Passeig de Gràcia", "Madison Avenue", "The Mall"]
beispiel_hausnummern = ["1", "12a", "45", "7b", "23", "102", "8", "55a", "19b", "3", "67", "34", "9", "22", "111", "76", "13c", "28", "4a", "61", "17", "85", "6b", "31", "14", "98", "2", "40a", "57", "10", "25"]
beispiel_postleitzahlen = ["10115", "10785", "12345", "13086", "20095", "20146", "30159", "40210", "50667", "60311", "70173", "80331", "90001", "1000", "2000", "3000", "4000", "5000", "6000", "7000", "8000", "9000", "10000", "20000", "30000", "40000", "50000", "60000", "70000", "80000"]
beispiel_staedte = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt am Main", "Stuttgart", "Dresden", "Leipzig", "Wien", "Zürich", "Paris", "London", "Rom", "Madrid", "Moskau", "Peking", "Tokio", "New York", "Los Angeles", "Toronto", "Sydney", "Rio de Janeiro", "Kairo", "Istanbul", "Delhi", "Bangkok", "Dubai", "Singapur", "Stockholm", "Oslo"]
beispiel_laender = ["Deutschland", "Frankreich", "Italien", "Spanien", "USA", "Kanada", "Japan", "China", "Indien", "Brasilien", "Russland", "Schweiz", "Österreich", "Niederlande", "Belgien", "Portugal", "Australien", "Neuseeland", "Südafrika", "Ägypten", "Griechenland", "Türkei", "Mexiko", "Argentinien", "Kolumbien", "Chile", "Peru", "Thailand", "Vietnam", "Südkorea"]

def generate_random_data():
    """Generiert einen neuen Beispieldatensatz."""
    vorname = random.choice(beispiel_vornamen)
    nachname = random.choice(beispiel_nachnamen)
    strasse = random.choice(beispiel_strassen)
    hausnummer = random.choice(beispiel_hausnummern)
    postleitzahl = random.choice(beispiel_postleitzahlen)
    stadt = random.choice(beispiel_staedte)
    land = random.choice(beispiel_laender)
    telefonnr = ("+" + str(random.randint(10, 99)) + " " + str(random.randint(1000000000, 9999999999)))
    return (vorname, nachname, strasse, hausnummer, postleitzahl, stadt, land, telefonnr)

def generate_multiple_random_data():
    addresses = []
    for anz in range(1,random.randint(5,10)):
        addresses.append(generate_random_data())
    return addresses
