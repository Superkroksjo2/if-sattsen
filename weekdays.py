weekday = input("vad är det för dag i dag")
weekday = str(weekday)

if weekday ==  "Måndag":
    print("På skolan till 13:30")
elif (weekday == "Tisdag") | (weekday == "Torsdag"):
    print("Gammlings dags")
elif weekday == "Onsdag":
    print("fan ochså inte Fredag")
else:
    print("Hälgdags")