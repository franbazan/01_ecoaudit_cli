# EcoAudit CLI - Módulo Principal
# Autores: [Fran Bazán] & [José Miguel]

from calculadora import estimar_consumo_wh, calcular_huella_co2

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")
    
    entrada = input("\nSeleccione una opción (1-3): ").strip()
    

    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue
    
    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        proceso=input("Nombre del proceso o dispositivo: ").strip()
        potencia=float(input("Introduce la potencia en W: ").strip())
        horas=float(input("Introduce las horas de uso: ").strip())
        iteraciones = int(input("Introduce el número de iteraciones: ").strip())
        consumo= potencia * horas
        huella= calcular_huella_co2(consumo)
        consumo = potencia * horas
       # SIMULACIÓN ITERATIVA PASO A PASO (PARA INSPECCIÓN EN DEPURADOR)
        print("\nIniciando simulación ciclo a ciclo...")
        consumo_ciclo = estimar_consumo_wh(potencia, horas, 1) # Consumo de un solo ciclo
        consumo_acumulado = 0.0
        ciclo = 1

        while ciclo <= iteraciones:
         consumo_acumulado = consumo_acumulado + consumo_ciclo # <--- PONDRÉIS AQUÍ EL PUNTO ROJO
         print(f" [Ciclo {ciclo}] Consumo acumulado parcial: {consumo_acumulado:.2f} Wh")
         ciclo = ciclo + 1
      
        try:
            if iteraciones <= 0:
                print("⚠️ El valor debe ser mayor que cero.")
            else:
                print(f"✔️ Configurado con éxito para {iteraciones} iteraciones.")
                with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
                # Escribimos los datos separados por comas y terminamos con salto de línea (\n)
                    archivo.write(f"{proceso},{potencia},{horas},{iteraciones},{consumo:.2f},{huella:.4f}\n")
                    print("💾 Registro guardado con éxito en 'auditorias.csv'.")
        except ValueError:
                print("⚠️ Error de formato: debe introducir un número entero.")
        
    elif opcion == 2:
        try:
            with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:
                print("Historial de auditorías:")
                print(archivo.read())
        except FileNotFoundError:
           print("⚠️ No se encontró el archivo 'auditorias.csv'. Aún no se han realizado auditorías.")
       
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")

     