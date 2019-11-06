
# %%
os.chdir(os.path.realpath("/Users/user/Documents/GitHub/Lambda/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis"))


# %%

import os
print(os.getcwd())

# %%

import psycopg2
from creds import Elephant

# %%

dbname = Elephant.dbname #same as user
user = Elephant.user #same as dbname
password = Elephant.password #don't commit this to github!
host = Elephant.host #from SERVER type this in as string

# %%


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()



import sqlite3
sl_conn = sqlite3.connect('/Users/user/Documents/GitHub/Lambda/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
# sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()
# sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall()
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()
# print(sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())

create_character_table = """
  CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
"""

pg_curs.execute(create_character_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)

# print(pg_curs.fetchall())
# # print(str(characters[0][1:]))

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:])

# print(example_insert)

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  pg_curs.execute(insert_character)

# print(insert_character)

pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 20;')
print(pg_curs.fetchall())
pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

print(characters[0])
print(pg_characters[0])

for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

pg_curs.close()
pg_conn.commit()




