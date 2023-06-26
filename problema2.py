print("ingrese su peso en kilogramos")
peso= float(input())
print("Ingrese su estatura en metros")
estatura=float(input())
i=estatura*estatura
IMC=peso/i
IMC=round(IMC,2)
print(F"Tu indice de masa corporal es {IMC}")

