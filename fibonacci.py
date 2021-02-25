#implementation - fibonacci sequence

def fun(x):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fun(x-2) + fun(x-1)

#implementation - factorials

def fact(x):
  if x == 1 or x == 0:
    return 1;
  elif x < 0:
    return "error"
  else:
    return x * fact(x-1)
