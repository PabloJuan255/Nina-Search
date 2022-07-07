#coding: utf-8
import sqlite3

database = sqlite3.connect('localdb',check_same_thread=False)
database_cursor = database.cursor()

def safe(stri):
  stri = str(stri).lower()
  stri = stri.replace('-','').replace(';','')
  stri = stri.replace('<','&lt').replace('>','&gt')
  stri = ''.join(e for e in stri if e.isalnum())
  stri = stri.replace(',','').replace(' ','')
  return stri #idk if this is safe.line 10 = STACKOVERFLOW

def newtable(table):
  table = safe(table).replace('.','')
  return database_cursor.execute('''
  CREATE TABLE IF NOT EXISTS '''+table+'''(
    sitename TEXT
    )
  ''')

def insert(val,tab,vrf=False):
  if(vrf == True):
    val = safe(val)
  tab = safe(tab)
  database_cursor.execute("INSERT INTO "+tab+" VALUES('"+val+"')")

def collum(name,tab,null="NOT NULL"):
  name = safe(name)
  tab = safe(tab)
  database_cursor.execute('ALTER TABLE '+tab+' ADD '+name) ##not working

def select(tab):
  tab = safe(tab)
  x = database_cursor.execute('SELECT * FROM '+tab)
  return x.fetchall()

def commit():
  database.commit()