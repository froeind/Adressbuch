
import tkinter as tk

# https://www.youtube.com/watch?v=MaqVvXv6zrU

# laut Bard=Gemini soll das das "Kein-Button-gedrückt"-Problem lösen - JA
def on_closing():
    # das muss natürlich hier rein, solange es tkinter noch gibt
    # und das lagere ich nicht in project_func aus
    newedit_window.destroy()
    '''
    frame_password.writeconf()
    frame_plot.writeconf()
    frame_ki.resetlist()
    frame_ki.writelist()
    frame_ki.writeconf()
    # und das ist 'natürlich' drin
    '''
    root.destroy()
    root.quit()
# laut Bard=Gemini soll das das "Kein-Button-gedrückt"-Problem lösen - JA

# GUI-Einrichtung
root = tk.Tk()
# laut Bard=Gemini soll das das "Kein-Button-gedrückt"-Problem lösen - JA
root.protocol("WM_DELETE_WINDOW", on_closing)
# laut Bard=Gemini soll das das "Kein-Button-gedrückt"-Problem lösen - JA
tkBreite = 780; tkHoehe = 800; tkX = 2800; tkY = 100
root.geometry("%dx%d+%d+%d"%(tkBreite, tkHoehe, tkX, tkY))
#root.minsize(750, 800)
#root.maxsize(1000, 800)
root.title("Kontaktdatenbank")

gray22 = "gray22"
gray23 = "gray23"
gray13 = "gray13"
gray76 = "gray76"
fontH12b = ("Helvetica", 12, "bold")
fontC10n = ("Courier", 10, "normal")
lavender = "lavender"
lightblue3 = "LightBlue3"

root.configure(bg=gray23)

# Adjust column width
#root.columnconfigure(1, minsize=200)

# tkinter-Variablen vor den Funktionen

strentry_datei = tk.StringVar(value="")

entry_name = tk.Entry()
strentry_name = tk.StringVar(value="")
entry_surname = tk.Entry()
strentry_surname = tk.StringVar(value="")
entry_street = tk.Entry()
strentry_street = tk.StringVar(value="")
entry_house_number = tk.Entry()
strentry_house_number = tk.StringVar(value="")
entry_postal_code = tk.Entry()
strentry_postal_code = tk.StringVar(value="")
entry_city = tk.Entry()
strentry_city = tk.StringVar(value="")
entry_country = tk.Entry()
strentry_country = tk.StringVar(value="")
entry_phone = tk.Entry()
strentry_phone = tk.StringVar(value="")

entry_search = tk.Entry()
strselected_filter = tk.StringVar(value="")
strselected_sort = tk.StringVar(value="")
lillybox = tk.Listbox()

lstAddresses = []
intListPointer = [-1]

import project_func

intRow = 0
#Überschrift Datei öffnen
datei_label = tk.Label(root, text="Daten hinzufügen", bg=gray23, fg=gray76, font=fontH12b)
datei_label.grid(row=intRow, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

intRow += 1
browse_button = tk.Button(root, text="Datei öffnen", bg=gray22, fg=gray76, activebackground=lightblue3, width=20, command=lambda: project_func.command_browse_file(lillybox, lstAddresses, intListPointer, strentry_datei))
browse_button.grid(row=intRow, column=1, padx=10, pady=5, sticky="w")

random_button = tk.Button(root, text="Zufällige erzeugen", bg=gray22, fg=gray76, activebackground=lightblue3, width=20, command=lambda: project_func.command_random(lillybox, lstAddresses, intListPointer))
random_button.grid(row=intRow, column=3, padx=10, pady=5, sticky="e")

intRow += 1
label_datei = tk.Label(root, text="Geöffnete Datei:", bg=gray23, fg=gray76)
label_datei.grid(row=intRow, column=0, sticky="e", padx=10, pady=5)
entry_datei = tk.Entry(root, textvariable=strentry_datei, bg=lavender, fg=gray13, width=100)
entry_datei.grid(row=intRow, column=1, columnspan=3, padx=10, pady=5, sticky="w")

# Leere Zeile als Platzhalter #####################
intRow += 1
empty_label = tk.Label(root, text="", bg=gray23)
empty_label.grid(row=intRow, column=0)
###################################################

###################################################

# Edit- und Neu-Anlage-Fenster

def on_closing_newedit():
    # und das lagere ich auch nicht in project_func aus
    newedit_window.withdraw()

newedit_window = tk.Toplevel()

tkBreite = 400; tkHoehe = 400; tkX = 2500; tkY = 100
newedit_window.geometry("%dx%d+%d+%d"%(tkBreite, tkHoehe, tkX, tkY))
#newedit_window.minsize(450, 300)
#newedit_window.maxsize(1000, 800)
newedit_window.configure(bg=gray23)
newedit_window.protocol("WM_DELETE_WINDOW", on_closing_newedit)
newedit_window.withdraw()

# Labels und Eingabefelder
intEditRow = 0
tk.Label(newedit_window, text="Vorname:", bg=gray23, fg=gray76).grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(newedit_window, textvariable=strentry_name, width=40, bg=lavender, fg=gray13)
entry_name.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Nachname:", bg=gray23, fg=gray76).grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_surname = tk.Entry(newedit_window, textvariable=strentry_surname, width=40, bg=lavender, fg=gray13)
entry_surname.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Straße:", bg=gray23, fg=gray76).grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_street = tk.Entry(newedit_window, textvariable=strentry_street, width=40, bg=lavender, fg=gray13)
entry_street.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Hausnummer:", bg=gray23, fg=gray76).grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_house_number = tk.Entry(newedit_window, textvariable=strentry_house_number, width=40, bg=lavender, fg=gray13)
entry_house_number.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Postleitzahl:", bg=gray23, fg=gray76).grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_postal_code = tk.Entry(newedit_window, textvariable=strentry_postal_code, width=40, bg=lavender, fg=gray13)
entry_postal_code.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Stadt:", bg=gray23, fg=gray76).grid(row=5, column=0, sticky="e", padx=10, pady=5)
entry_city = tk.Entry(newedit_window, textvariable=strentry_city, width=40, bg=lavender, fg=gray13)
entry_city.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Land:", bg=gray23, fg=gray76).grid(row=6, column=0, sticky="e", padx=10, pady=5)
entry_country = tk.Entry(newedit_window, textvariable=strentry_country, width=40, bg=lavender, fg=gray13)
entry_country.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Label(newedit_window, text="Telefonnummer:", bg=gray23, fg=gray76).grid(row=7, column=0, sticky="e", padx=10, pady=5)
entry_phone = tk.Entry(newedit_window, textvariable=strentry_phone, width=40, bg=lavender, fg=gray13)
entry_phone.grid(row=intEditRow, column=1, padx=10, pady=5)

intEditRow += 1
tk.Button(newedit_window, text="Abbrechen", bg=gray22, fg=gray76, activebackground=lightblue3, command=lambda: project_func.command_newedit_window_cancel(newedit_window)).grid(row=intEditRow, column=0, padx=10, pady=10, sticky="ew")
tk.Button(newedit_window, text="Speichern", bg=gray22, fg=gray76, activebackground=lightblue3, command=lambda: project_func.command_newedit_window_save(lillybox, lstAddresses, intListPointer, newedit_window, [strentry_name, strentry_surname, strentry_street, strentry_house_number, strentry_postal_code, strentry_city, strentry_country, strentry_phone])).grid(row=intEditRow, column=1, padx=10, pady=10, sticky="ew")

###################################################

# Überschrift Kontaktbuch anzeigen
intRow += 1
kontakte_label = tk.Label(root, text="Meine Daten", bg="gray23", fg=gray76, font=fontH12b)
kontakte_label.grid(row=intRow, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

# Labels, Eingabefeld und Button zum Suchen 
intRow += 1
label_search = tk.Label(root, text="Suche:", bg=gray23, fg=gray76)
label_search.grid(row=intRow, column=0, sticky="e", padx=10, pady=5)
entry_search = tk.Entry(root, bg=lavender, fg=gray13, width=75)
entry_search.grid(row=intRow, column=1, columnspan=3, padx=10, pady=5, sticky="w")
search_button = tk.Button(root, text="Suche", bg=gray22, fg=gray76, activebackground=lightblue3, command=project_func.command_search, width=15)
search_button.grid(row=intRow, column=3, padx=10, pady=5, sticky="e")

# Label für das Dropdown-Menü
intRow += 1
filter_label = tk.Label(root, text="Filtern nach:", bg=gray23, fg=gray76)
filter_label.grid(row=intRow, column=0, sticky="e", padx=10, pady=5)

# Liste der Filteroptionen erstellen
filter_options = ["Vorname", "Nachname", "Straße", "Stadt", "Telefonnummer"]

# StringVar zum Speichern des ausgewählten Filters erstellen
strselected_filter.set(filter_options[0])  # Standardfilteroption setzen
strselected_filter.get()

# Dropdown-Menü erstellen
filter_menu = tk.OptionMenu(root, strselected_filter, *filter_options, command=project_func.command_filter_selected)
filter_menu.config(bg=gray22, fg=gray76, bd=0, highlightthickness=1, highlightbackground="gray", activebackground=lightblue3, width=30 )
filter_menu.grid(row=intRow, column=1, padx=10, pady=5, sticky="w")

#Sortieren Label für das Dropdown-Menü
sort_label = tk.Label(root, text="Sortieren:", bg=gray23, fg=gray76)
sort_label.grid(row=intRow, column=2, sticky="e", padx=10, pady=5)

# Liste der Filteroptionen "Sortieren" erstellen
sort_options = ["Aufsteigend", "Absteigend"]

# StringVar zum Speichern des ausgewählten Filters erstellen
strselected_sort.set(sort_options[0])  # Standardfilteroption setzen

# Dropdown-Menü erstellen Sortieren
sort_menu = tk.OptionMenu(root, strselected_sort, *sort_options, command=project_func.command_sort_selected)
sort_menu.config(bg=gray22, fg=gray76, bd=0, highlightthickness=1, highlightbackground="gray", activebackground=lightblue3, width=30 )
sort_menu.grid(row=intRow, column=3, padx=10, pady=5, sticky="w")

# Button zum Anzeigen aller Kontakte
intRow += 1
display_all_button = tk.Button(root, text="Alle anzeigen", bg=gray22, fg=gray76, activebackground=lightblue3, command=project_func.command_display_all_contacts, width=15)
display_all_button.grid(row=intRow, column=3, sticky="e", padx=10, pady=10)

# Kontakte hinzufügen
intRow += 1
newadd_button = tk.Button(root, text="Neu", bg=gray22, fg=gray76, activebackground=lightblue3, command=lambda type="n": project_func.command_newadd_contact(type, lstAddresses, intListPointer, newedit_window, [strentry_name, strentry_surname, strentry_street, strentry_house_number, strentry_postal_code, strentry_city, strentry_country, strentry_phone]), width=15)
newadd_button.grid(row=intRow, column=0, padx=10, pady=5, sticky="we") 

# Button zum Bearbeiten des ausgewählten Kontakts
edit_contact_button = tk.Button(root, text="Bearbeiten", bg=gray22, fg=gray76, activebackground=lightblue3, command=lambda type="e": project_func.command_newadd_contact(type, lstAddresses, intListPointer, newedit_window, [strentry_name, strentry_surname, strentry_street, strentry_house_number, strentry_postal_code, strentry_city, strentry_country, strentry_phone]), width=15)
edit_contact_button.grid(row=intRow, column=1, sticky="we", padx=10, pady=10)

# Button zum Löschen des ausgewählten Kontakts
delete_button = tk.Button(root, text="Löschen", bg=gray22, fg=gray76, activebackground="indian red", command=project_func.command_delete_contact, width=15)
delete_button.grid(row=intRow, column=2, sticky="we", padx=10, pady=10)

# Button zum Speichern des ausgewählten Kontakts
save_button = tk.Button(root, text="Speichern", bg=gray22, fg=gray76, activebackground=lightblue3, command=project_func.command_save_contact, width=15)
save_button.grid(row=intRow, column=3, sticky="we", padx=10, pady=10)

# Widget zum Anzeigen aller Kontakte
intRow += 1
lillybox = tk.Listbox(root, background=lavender, foreground=gray13, font=fontC10n, height=25)
lillybox.grid(row=intRow, column=0, columnspan=4, padx=10, pady=10, sticky="nwse")
lillybox.configure(exportselection=False)
lillybox.bind('<<ListboxSelect>>', lambda event: project_func.command_listbox_select(event, lillybox, intListPointer))

intListPointer = project_func.showlist_initial_from_db(lstAddresses, lillybox, intListPointer, 0)

root.mainloop()
