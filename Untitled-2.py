metodo = input("Ingresar metodo de pago: ").strip()
contador = 0

with open("SalesJan2009.csv", "r", encoding="utf-8") as f:

  for linea in f:
      dato = linea.strip().split(",") 
      print (dato)
      if dato[3].strip() == metodo:
          contador += 1

print(f"{metodo}: {contador}")