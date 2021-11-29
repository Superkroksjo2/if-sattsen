# kontant < 33
# normal 33-66
# plus < 66

print ("Välkommen till Lars och Olofs mobilabbonemang")
uppskattade_minuter = int(input("Hur många minuter uppskattar du att du ringer per månad?"))

if uppskattade_minuter < 33:
  print("Du vill ha kontantabonemang")
elif uppskattade_minuter < 66:
  print("Du vill ha normalabonemang")
else:
  print("Du vill ha plusabonemang")