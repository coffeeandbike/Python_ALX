import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='zawodnicy',
    user='postgres',
    password='xxxxx'

)

# SELECT

cur = conn.cursor()
cur.execute("select * from zawodnicy")

wyniki = cur.fetchall()

print(wyniki)

for zawodnik in wyniki:
    print(zawodnik[1])

print('='*30)

#######################################

# INSERT

cur = conn.cursor()


# Ten kawałek kodu jest podatny na atak SQL injection
# https://sekurak.pl/czym-jest-sql-injection/
# '); truncate kibice; --

# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# sql = f"insert into kibice (imie_k, nazwisko_k) values ('{imie}', '{nazwisko}')"
# print(sql)
# cur.execute(sql)
# conn.commit()

# INSERT, ale bezpieczny pod katem SQL Injection

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
sql = f"insert into kibice (imie_k, nazwisko_k) values (%s, %s)"
# sql = f"insert into kibice (imie_k, nazwisko_k) values ('Piotr', E'\'); truncate kibice; --')"
dane = (imie, nazwisko)
cur.execute(sql, dane)
conn.commit()

# update, delete - robimy tak samo jak insert