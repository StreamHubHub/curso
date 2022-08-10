print("""--------------------------
CALCULADORA DE PORCENTAJE
--------------------------""")

print("""Para poder calcular el precio final después del impuesto 
solamente ingresa el precio final deseado y el porcentaje de impuesto que se te cobrara""")

precio_final = int(input("""
Inserte el precio float deseado: """))
impuesto_cobrado = float(input ("Ingrese el impuesto cobrado: "))

contador = float(0)
incremento = precio_final
while contador < precio_final:
    contador = incremento - (incremento*impuesto_cobrado)
    incremento = incremento + 1
