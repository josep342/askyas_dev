import sqlite3

ccon=sqlite3.connect('kenamelBD.db')

cursorr=ccon.cursor()

etat0=cursorr.execute('''  CREATE TABLE IF NOT EXISTS actualite(id INTEGER PRIMARY KEY AUTOINCREMENT,titre TEXT,soustitre TEXT,detail TEXT,photo TEXT,ddate DATE)''')
etat1=cursorr.execute('''  CREATE TABLE IF NOT EXISTS service(id INTEGER PRIMARY KEY AUTOINCREMENT,titre TEXT,soustitre TEXT,detail TEXT,photo TEXT,type TEXT,ddate DATE)  ''')  
etat2=cursorr.execute('''  CREATE TABLE IF NOT EXISTS annonce(id INTEGER PRIMARY KEY AUTOINCREMENT,titre TEXT,soustitre TEXT,detail TEXT,photo TEXT,type TEXT,ddate DATE)  ''')  


if etat1 and etat0 and etat2:

    print("calem")