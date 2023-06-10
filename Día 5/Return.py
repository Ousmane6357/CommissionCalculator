def multiplicar(numero1,numero2):
    return numero1 * numero2
resultado = multiplicar(200,40)
print(resultado)




def potencia(v1, v2):
    return v1 ** v2




def usd_a_eur(monto_usd):
    conversion = 0, 90
    monto_eur = monto_usd * conversion

    return monto_eur






dolares = 100
monto_euros = usd_a_eur(dolares)
print("El equivalente en euro es : ", monto_euros)






def invertir_palabra(dada):
    return dada[::-1]
palabra = input("Dame una palabra: ").upper()
palabra_invertida = invertir_palabra(palabra)
print("La palabra invertida es " , palabra_invertida)
