n = int(input()) 
if n < 0 or n > 80 : 
  print("Error : Out of range") 
else: 
  out = "" 
  if n % 3 == 1 : 
    out = "1" + out
  elif n % 3 == 2:
    out = "2"+ out 
  else: 
    out = "0" + out 
  n //= 3 
  if n % 3 == 1 : 
    out = "1" + out
  elif n % 3 == 2:
    out = "2"+ out 
  else: 
    out = "0" + out 
  n //= 3
  if n % 3 == 1 : 
    out = "1" + out
  elif n % 3 == 2:
    out = "2"+ out 
  else: 
    out = "0" + out 
  n //= 3
  if n % 3 == 1 : 
    out = "1" + out
  elif n % 3 == 2:
    out = "2"+ out 
  else: 
    out = "0" + out 
  print(out)
