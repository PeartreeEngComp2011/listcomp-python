#Sem list comprehension

x = [1,2,3,4,5]
y = []

for i in x:
	y.append(i**2)

print(x)
print(y)

#Com list comprehension

x = [1,2,3,4,5]
y = [i**2 for i in x]

print("Usando list comprehension")
print(x)
print(y)

#Imprindo números ímpares com list comprehension

x = [1,2,3,4,5,6,7,8,9,10]
z = [i for i in x if i%2==1]

print(z)
