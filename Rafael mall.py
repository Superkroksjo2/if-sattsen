klockan = input("Vad är klockan?")
klockan = float(klockan)
if klockan < 7.00 :
  print("Du kommer i tid")
elif (klockan > 7.00) & (klockan < 7.20) :
  print("Nu har du bråttom")
else:
  print("Nu är du sen")