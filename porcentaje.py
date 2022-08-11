print("""--------------------------
CALCULADORA DE PORCENTAJE
--------------------------""")

print("""Para poder calcular el precio final después del impuesto 
solamente ingresa el precio final deseado y el porcentaje de impuesto que se te cobrara""")

precio_final = float(input("""
Inserte el precio deseado: """))
impuesto_cobrado = float(input ("Ingrese el impuesto cobrado: "))
impuesto_cobrado = impuesto_cobrado * 0.01

contador = float(0)
incremento = precio_final
while contador < precio_final:
    contador = incremento - (incremento*impuesto_cobrado)
    incremento = incremento + 1

print("El precio final debe después de impuesto debe ser: ",incremento)
print("Gracias por usar este programa")
print("...")