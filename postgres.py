import psycopg2

con = psycopg2.connect(
    database = 'Mydb',
    host = 'localhost',
    user = 'postgres',
    password = 'root',
    port = 5454
)

cur = con.cursor();

cur.execute('SELECT * FROM students WHERE "Name" = \'Huzaifa-Amjad\'')

data = cur.fetchall()

print("Index\t\tName\t\t\tBonafide")
for d in data:
    print(f"{d[0]}\t\t{d[1]}\t\t{d[2]}")