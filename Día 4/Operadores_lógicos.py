mi_bool = (4>5) and (5 ==3+2)
print((mi_bool))
mi_bool1 =  1 ==40 or ('perro' == ('perro'))
print(mi_bool1)

texto = "La vida es loca"
mi_bool2 = ("vida" in texto) and ("java" in texto)
print(mi_bool2)


num1 = (36)
num2 = (72/2)
num3 = (48)
mi_bool3 = (num1 > num2) and (num1 < num3)
print(mi_bool3)



num1 = (36)
num2 = (72/2)
num3 = (48)
mi_bool4 = (num1 > num2) or (num1 < num3)
print(mi_bool4)


frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"



mi_bool5 =  (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool5)
