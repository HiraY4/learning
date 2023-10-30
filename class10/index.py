def generator1(rang):
  for i in range(rang):
    yield i       # yields the NEWLY GENERATED value as these are not stored beforehand

gen = generator1(5)

print(next(gen))
print(next(gen))
print(next(gen))