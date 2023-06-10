def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave} es = {valor}')
suma(x=3,y=5,z=2)



#Para sumarlo
def suma(**kwargs):
    total  = 0
    for clave,valor in kwargs.items():
        print(f'{clave} es = {valor}')
        total += valor

    return total
print(suma(x=3,y=5,z=2))


#Tercera manera
def prueba( num1,num2,*args,**kwargs):
    print(f'el primer valor es el {num1}')
    print(f'el segundo valor es el {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} es = {valor}')

args= [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args,**kwargs)