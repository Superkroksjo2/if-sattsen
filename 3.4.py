t = float(input('Temp?'))
if t < 18:
  print('Det är kallt')
  print('Sätt på värmen')
  if t < 12:
    print('Sätt på jackan!!!!!!')
  if t < 0:
    print('Vill du förfrysa eller?')
else:
  print('Det är varmt')
  if t > 22:
    print('Stäng av värmen!')
  if t > 30:
    print('Du kommer få värmeslag, gå in i skuggan')


print(f'"Det är {t:.1f} grader"')