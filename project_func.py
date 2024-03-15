
import project_db
import project_random
import project_csv

def command_newadd_contact(type, lstAddresses, intListPointer, newedit_window,*strentries):
    # in diesem Tupel muss ich, warum auch immer, das erste Element nehmen, das ist die Liste
    strentries = strentries[0]
    #print("command_newadd_contact", intListPointer[0])
    if type == "e":
        if intListPointer[0] == -1: return
        # vorbelegen
        #print(lstAddresses)
        data = lstAddresses[intListPointer[0]]
        #print(data)
        # ich starte bei 1, weil ich die Id nicht brauche
        i = 1
        # und das geht auch nicht
        #for i, entry in enumerate(strentries):
        for entry in strentries:
            entry.set(data[i])
            i += 1
        newedit_window.title("Kontakt bearbeiten")
    else:
        # leeren
        # der Testdruck geht
        #print(strentries)
        for entry in strentries:
            # der auch
            #print(entry)
            # aber der nicht, warum auch immer wieder - ist das nervig
            #print(type(entry))
            entry.set("")
        newedit_window.title("Neuer Kontakt")
    newedit_window.deiconify()

def command_newedit_window_cancel(newedit_window):
    newedit_window.withdraw()

def command_newedit_window_save(listbox, lstAddresses, intListPointer, newedit_window, *strentries):
    # sowohl bei Neu als auch bei Edit sollte ich auf leere Felder checken
    # dann muss ich erkennen, dass es Neu oder Edit ist
    # ich positioniere jetzt noch nicht auf die eingefügte Adresse
    # (dann auch bei random)
    blnNew = newedit_window.title() == "Neuer Kontakt"
    neweditedentry = []
    strentries = strentries[0]
    for entry in strentries:
        neweditedentry.append(entry.get())
    if blnNew:
        neweditedentry= [tuple(neweditedentry)]
        project_db.insert_data(neweditedentry)
        intListPointer = showlist_initial_from_db(lstAddresses, listbox, intListPointer, len(lstAddresses))
    else:
        neweditedentry = [lstAddresses[intListPointer[0]][0]] + neweditedentry
        project_db.update_record(neweditedentry)
        intListPointer = showlist_initial_from_db(lstAddresses, listbox, intListPointer, intListPointer[0])
    newedit_window.withdraw()

def command_search():
    pass

def command_filter_selected():
    pass

def command_sort_selected():
    pass

def command_display_all_contacts():
    pass

def command_delete_contact():
    pass

def command_save_contact():
    pass

import tkinter as tk

def showlist(listbox_all, liste):
    data_format = "{:<10}{sp1}{:<11}{sp2}{:<20}{sp3}{:<6}{sp4}{:<13}{sp5}{:<13}{sp6}{:<15}"
    listbox_all.delete(0, tk.END)
    #print(len(liste[0]))
    littlelilly = [(elem[1], elem[2], elem[3]+" "+elem[4], elem[5], elem[6], elem[7], elem[8]) for elem in liste]
    #print(len(littlelilly[0]))
    for row in littlelilly:
        listbox_all.insert(tk.END, data_format.format(*row, sp1=" "*0, sp2=" "*0, sp3=" "*0, sp4=" "*0, sp5=" "*0, sp6=" "*0))

from tkinter import filedialog as fd

def OpenTKinterDialog():

    import tkinter as tk
    tkDialogFenster = tk.Tk()
    tkDialogFenster.wm_attributes("-topmost", 1)
    tkDialogFenster.withdraw()

def GetFilepath():
    OpenTKinterDialog()
    dicParameter = dict(defaultextension = ".txt",
                        #initialdir = "C:/Users/Input/Documents/karrieretutor/2 Python/a Programme/Volker Trenel/Python-Part_2/0102 - Dateifunktionen+/_Dateien",
                        initialfile = "Import_Text.txt",
                        filetypes = [("Textdatei", "*.txt"),
                                    ("CSV-Datei", "*.csv"),
                                    ("Alle Dateien", "*.*")],
                        title = "Bitte wählen Sie eine Importliste aus.")
    return fd.askopenfilename(**dicParameter)

import csv

def ReadCSV(strFilename, strDelimiter = ';'):
    '''
    wenn der Delimiter stimmt stehen die Titel bzw. die erste Zeile als Liste in lstTitel[0]
    und die Daten bzw. alles ab Zeile zwei in lstData jede Zeile als Liste von Listen in lstData
    '''
    with open(strFilename, 'r') as objFile:
        return csv.reader(objFile, delimiter = strDelimiter)

def ReadText(strFilename, strDelimiter = ';'):
    '''
    wenn der Delimiter stimmt stehen die Titel bzw. die erste Zeile als Liste in lstTitel[0]
    und die Daten bzw. alles ab Zeile zwei in lstData jede Zeile als Liste von Listen in lstData
    '''
    lstData = []
    with open(strFilename) as objFile:
        varLine = objFile.readline()
        while varLine:
            lstData.append(varLine.split(strDelimiter))
            varLine = objFile.readline()
    return lstData

def DataImport():
    while True:
        strFilepath = GetFilepath()
        if strFilepath == "": return "", []
        else:
            lstFilepath = strFilepath.split("/")
            lstFilename = lstFilepath[-1].split(".")
            if lstFilename[-1] == "csv": return strFilepath, ReadCSV(strFilepath)
            elif lstFilename[-1] == "txt": return strFilepath, ReadText(strFilepath)
            else: print("Sie haben keine gültige Datei ausgewählt!")

def DataRefine(lstData):
    # 'KundenID', 'Firma', 'Land', 'Bundesland', 'Ort', 'Plz', 'Adresse', 'Name', 'Vorname', 'Position', 'Rufnummer', 'Fax', 'Umsatz', 'Kosten\n'
    # wird zu
    # 'Vorname', 'Name', 'Adresse Straße', 'Adresse Hausnummer', 'Plz', 'Ort', 'Land', 'Rufnummer'
    lstData = [(elem[8], elem[7], elem[6].split(" ")[0], elem[6].split(" ")[-1], elem[5], elem[4], elem[2], elem[10]) for elem in lstData]
    return lstData

def showlist_initial_from_db(lstAddresses, listbox, intListPointer, intSelectedPosition):
    lstAddresses.clear()
    lstAddresses.extend(project_db.read_data())
    #print(lstAddresses)
    # Anzeige in Listenfeld
    showlist(listbox, lstAddresses)
    # Positionierung auf erstem Datensatz
    # wenn was existiert
    # oder auf erstem neuen Eintrag
    if lstAddresses:
        if intSelectedPosition < len(lstAddresses):
            # es kam was dazu, durch Import, Zufall oder Neu
            # also nehme ich diese vorinitialisierte Position, den ersten neuen Wert
            # ansonsten habe ich was verändert und bleibe dort
            intListPointer[0] = intSelectedPosition
        else:
            intListPointer[0] = 0
        # und noch erste neue Zeile markieren
        listbox.select_set(intListPointer[0])
        listbox.see(intListPointer[0])
    else:
        intListPointer[0] = -1
    return intListPointer

def command_browse_file(listbox, lstAddresses, intListPointer, strentry_datei):
    strFilepath, lstImport = DataImport()
    if lstImport != []:
        strentry_datei.set(strFilepath)
        #print(lstImport)
        lstImport = DataRefine(lstImport)
        #print(); print()
        # lstTitle ist Tupel
        # lstData ist List of Tupel
        lstTitle = lstImport[0]
        lstData = lstImport[1:]
        #print(lstTitle); print(lstData)
        # Hinzufügen über Datenbank, weil ja der eindeutige Index vergeben werden muss/sollte
        # also müssen die eingelesenen Daten zuerst in die Datenbank und dann hole ich alles wieder raus
        # und ich merke mir die letzte Zeilennummer
        # sollte überhaupt was dazukommen, hebe ich das erste neue Datum hervor
        project_db.insert_data(lstData)
        #project_db.CheckDB()
        intListPointer = showlist_initial_from_db(lstAddresses, listbox, intListPointer, len(lstAddresses))

def command_random(listbox, lstAddresses, intListPointer):
    # hier wird Lars'/Berts? Zufallserzeugung eingebunden, oder auch nicht
    lstData = project_random.generate_multiple_random_data()
    project_db.insert_data(lstData)
    intListPointer = showlist_initial_from_db(lstAddresses, listbox, intListPointer, len(lstAddresses))

def command_listbox_select(event, listbox, intListPointer):
    # Liste der Indizes der ausgewählten Zeilen
    try:
        selected_indices = listbox.curselection()
        #print(selected_indices)
        # Zeilennummer der angeklickten Zeile
        intListPointer[0] = selected_indices[0]
    except:
        intListPointer[0] = -1
    #print("command_listbox_select", intListPointer[0])











'''
from tkinter import *
import random
import string

def adresse_speichern():
# Übernahme der Daten
vorname = str(entry_vorname.get() or 0)
nachname = str(entry_nachname.get() or 0)
strasse = str(entry_strasse.get() or 0)
hausnummer = str(entry_nummer.get() or 0)
plz = str(entry_plz.get() or 0)
ort = str(entry_ort.get() or 0)
vorwahl = str(entry_vorwahl.get() or 0)
durchwahl = str(entry_durchwahl.get() or 0)
handy = str(entry_handy.get() or 0)
eingaben = vorname, nachname, strasse, hausnummer, plz, ort, vorwahl, durchwahl, handy
print(eingaben)
with open('adressbuch.txt', 'a', encoding="ISO-8859-1") as objDatei:
    objDatei.write(";".join(eingaben))
    objDatei.write("\n")
    objDatei.close()

# Fenster
tkFenster = Tk()
tkFenster.title('Adressbuch 1. Versuch')
tkFenster.geometry('500x390')
tkFenster.configure(bg='#6f116f')
# Label mit Aufschrift Vorname
label_vorname = Label(master=tkFenster, bg='#90EE90', text='Vorname:')
label_vorname.place(x=50, y=24, width=140, height=27)
# Entry für das Label Vorname
entry_vorname = Entry(master=tkFenster, bg='white', justify="left")
entry_vorname.place(x=200, y=24, width=250, height=27)
# Label mit Aufschrift Nachname
label_nachname = Label(master=tkFenster, bg='#90EE90', text='Nachname:')
label_nachname.place(x=50, y=64, width=140, height=27)
# Entry für das Label Nachname
entry_nachname = Entry(master=tkFenster, bg='white', justify="left")
entry_nachname.place(x=200, y=64, width=250, height=27)
# Label mit Aufschrift Strasse und Hausnummer
label_str_nr = Label(master=tkFenster, bg='#90EE90', text='Strasse Nr.:')
label_str_nr.place(x=50, y=104, width=140, height=27)
# Entry für die Strasse
entry_strasse = Entry(master=tkFenster, bg='white', justify="left")
entry_strasse.place(x=200, y=104, width=200, height=27)
# Entry für die Nr.
entry_nummer = Entry(master=tkFenster, bg='white', justify="left")
entry_nummer.place(x=410, y=104, width=40, height=27)
# Label mit Aufschrift PLZ und Ort
label_plz_ort = Label(master=tkFenster, bg='#90EE90', text='PLZ Ort:')
label_plz_ort.place(x=50, y=144, width=140, height=27)
# Entry für die PLZ
entry_plz = Entry(master=tkFenster, bg='white', justify="left")
entry_plz.place(x=200, y=144, width=40, height=27)
# Entry für den Ort
entry_ort = Entry(master=tkFenster, bg='white', justify="left")
entry_ort.place(x=250, y=144, width=200, height=27)
# Label mit Aufschrift Vorwahl und Durchwahl
label_telefon = Label(master=tkFenster, bg='#90EE90', text='Vor- und Durchwahl:')
label_telefon.place(x=50, y=184, width=140, height=27)
# Entry für die Vorwahl
entry_vorwahl = Entry(master=tkFenster, bg='white', justify="left")
entry_vorwahl.place(x=200, y=184, width=120, height=27)
# Entry für die Durchwahl
entry_durchwahl = Entry(master=tkFenster, bg='white', justify="left")
entry_durchwahl.place(x=330, y=184, width=120, height=27)
# Label mit Aufschrift Handy
label_handy = Label(master=tkFenster, bg='#90EE90', text='Handy:')
label_handy.place(x=50, y=224, width=140, height=27)
# Entry für die Handynummer
entry_handy = Entry(master=tkFenster, bg='white', justify="left")
entry_handy.place(x=200, y=224, width=250, height=27)
# Button zum Speichern
buttonBerechnen = Button(master=tkFenster, bg='#90EE90', fg="black", text='Eintrag speichern', command=adresse_speichern)
buttonBerechnen.place(x=310, y=300, width=140, height=40)

# Aktivierung des Fensters
tkFenster.mainloop()

'''