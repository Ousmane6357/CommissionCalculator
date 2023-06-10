mi_set = set([1,2,3,4,5,6,7])
print(type(mi_set))
print(mi_set)


s1 = {1,2,3}
s2 = {4,5,6}

s3 = s1.union(s2)

print(s3)



t1 = {1,2,3}
s1.add(4)
print(s1)


m1 = {1,2,3}
m1.remove(2)
print(m1)

t1 = {1,2,3}
s1.discard(2)
print(s1)

t1 = {1,2,3}
t1.clear()
print(t1)


mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)




sorteo1 = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

resultado = sorteo1.pop()

print(resultado)


sorteo2 = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

agrego = sorteo2.add("Damián")

print(sorteo2)