print ("Välkommen till Lars och Olofs mobilabbonemang")
uppskattade_minuter = int(input("Hur många minuter uppskattar du att du ringer per månad?"))

if uppskattade_minuter < 33:
  print("Vi Recomenderar kontantabonemang")
elif uppskattade_minuter < 66:
  print("Vi Recomenderar det normala abonemanget")
else:
  print("Vi Recomenderar ett plusabonemang")