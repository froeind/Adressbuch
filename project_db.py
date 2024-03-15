import sqlite3

# Name der SQLite-Datenbank
db_name = "telefonbuch.db"

def connect_to_database():
    """Verbindung zur SQLite-Datenbank herstellen."""
    conn = sqlite3.connect(db_name)
    return conn

def create_table():
    """Tabelle erstellen, wenn sie nicht existiert."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_personen (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Vorname TEXT,
                        Nachname TEXT,
                        Strasse TEXT,
                        Hausnummer TEXT,
                        Postleitzahl TEXT,
                        Stadt TEXT,
                        Land TEXT,
                        TelefonNr TEXT
                    )''')
    conn.commit()
    conn.close()

def insert_data(lstPersonen):
    """Daten in die Tabelle einfügen."""
    conn = connect_to_database()
    cursor = conn.cursor()
    for person in lstPersonen:
        if NoRecord(person):
            cursor.execute('''INSERT INTO tbl_personen (
                            Vorname, 
                            Nachname, 
                            Strasse, 
                            Hausnummer, 
                            Postleitzahl, 
                            Stadt, 
                            Land, 
                            TelefonNr) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', person)
    conn.commit()
    conn.close()

def read_data():
    """Daten aus der Tabelle lesen und zurückgeben."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_personen')
    data = cursor.fetchall()
    conn.close()
    return data

def delete_record(record_id):
    """Datensatz löschen."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tbl_personen WHERE Id=?', (record_id))
    conn.commit()
    conn.close()

def update_record(record):
    """Datensatz aktualisieren."""
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = """
    UPDATE tbl_personen
    SET Vorname = ?, 
    Nachname = ?, 
    Strasse = ?, 
    Hausnummer = ?, 
    Postleitzahl = ?, 
    Stadt = ?, 
    Land = ?, 
    TelefonNr = ?
    WHERE Id = ?
    """
    cursor.execute(sql, (record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[0]))
    conn.commit()
    conn.close()

def CheckDB():
    conn = connect_to_database()
    res = conn.execute("SELECT name FROM sqlite_master")
    print(res.fetchall())
    cursor = conn.cursor()
    print(list(cursor.execute("PRAGMA database_list")))

def NoRecord(person):
    """Daten in der Tabelle suchen und Ergebnis zurückgeben."""
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = """
    SELECT Id
    FROM tbl_personen
    WHERE Vorname = ?
    AND Nachname = ?
    AND Strasse = ?
    AND Hausnummer = ?
    AND Postleitzahl = ?
    AND Stadt = ?
    AND Land = ?
    AND TelefonNr = ?
    """
    cursor.execute(sql, (person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]))
    data = cursor.fetchone()
    conn.close()
    return data == None


