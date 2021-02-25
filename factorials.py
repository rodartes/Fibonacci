def fact(x):
  if x == 1 or x == 0:
    return 1;
  elif x < 0:
    return "error"
  else:
    return x * fact(x-1)
