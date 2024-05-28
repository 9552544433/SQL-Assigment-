import sqlite3


conn = sqlite3.connect('example.db')
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS Ages (
    name VARCHAR(128),
    age INTEGER
)
''')


cur.execute('DELETE FROM Ages')


cur.execute('INSERT INTO Ages (name, age) VALUES ("Mara", 28)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Otto", 33)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Fyn", 31)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Neshawn", 17)')


conn.commit()


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')


result = cur.fetchone()
if result:
    print(f"Answer ==> The first row in the resulting record set : {result[0]}")


conn.close()
