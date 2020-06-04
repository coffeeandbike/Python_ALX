# Obok imion i nazwisk skoczków wypisz ich daty urodzenia w formacie typowym dla języka polskiego, czyli np. “07.02.2006 r.”
sql_1 = f"select imie, nazwisko, TO_CHAR(data_ur, 'dd.mm.yyyy')  as urodziny from zawodnicy order by nazwisko"

# Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”.
sql_2 = f"select imie, nazwisko, kraj from zawodnicy order by kraj"

# FIS dba, aby skoczkowie narciarscy nie byli zbyt szczupli i wymaga, aby ich BMI wynosiło co najmniej 20.
# Wypisz listę zawodników wraz z informacją czy mają odpowiednią wagę w stosunku do swojego wzrostu
# (informacja powinna być osobnym polem o wartości typu boolean)
sql_3 = f"""select imie, nazwisko, waga/(wzrost/100.0)^2 as BMI,
        CAST(CASE when waga/(wzrost/100.0)^2 >= 20 THEN 1 ELSE 0 END as bool)
        from zawodnicy"""

# Obok imion i nazwisko skoczków wypisz ich BMI z dokładnością do 2 i 3 miejsc po przecinku
sql_4 = f"select imie, nazwisko, round(waga/(wzrost/100.0)^2, 2) as BMI_2, " \
        f"round(waga/(wzrost/100.0)^2, 3) as BMI_3 from zawodnicy"

# Wypisując imiona i nazwiska zamień wielkość liter w nazwiskach, tak by tylko pierwsza litera była wielka
sql_5 = f"select initcap(imie), initcap(nazwisko) from zawodnicy"

# Wypisz listę wszystkich polskich zawodników





