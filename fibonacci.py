def fun(x):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fun(x-2) + fun(x-1)

print(fun(0), fun(1), fun(2))