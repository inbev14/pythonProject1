x = ('apple', 'banana', 'cherry')
z = ['11', '22', '33']
z.sort()
y = enumerate(x)
dictor = {}
for el, val in y:
	dictor[el] = val
print(dictor)