import sqlite3

con = sqlite3.connect('data.sqlite', isolation_level=None)

def init_sql():
  con.execute('''CREATE TABLE IF NOT EXISTS data (
      realm_id         integer not null
    , realm_name       text    null
    , level            integer null
    , creature_id      integer not null
    , creature_name    text    null
    , creature_class   text    null
    , primary key      (realm_id, creature_id)
  )''')

def close_sql():
  con.close()

def sql_writer(list):
  con.executemany('''REPLACE INTO data (
      realm_id
    , realm_name
    , level
    , creature_id
    , creature_name
    , creature_class
  )
  VALUES (
      ?
    , ?
    , ?
    , ?
    , ?
    , ?
  )''', list)