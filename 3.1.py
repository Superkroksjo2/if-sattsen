kostnad = input("Hur mycket kostar en minut (I kronor)")
kostnad = float(kostnad)
minuter = input("Hur mycket ringer du per månad (I minuter)")
minuter = float(minuter)
pris = minuter * kostnad

if pris > 299:
  pris = pris * 0.9

print(f"Priset är {pris:.1f} :-")