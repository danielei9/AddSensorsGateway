gateway = ""
print(" Seleccione un modo de uso \n 1. Agregar sensores mediante excel... (Configuracion del excel 1º columna componentName y 3º Deveui)\n 2. Manualamente 1by1 () ")
mode = input()
print(" Introduzca la mac gateway... ejemplo b827eb18ad132")
gateway = input()
SJEVO = 0
BMETER = 0
print("Seleccione 1 para SJEVO y 2 para Bmeter")
typelogy = input()
if(typelogy == "1"):
    SJEVO = 1
if(typelogy == "2"):
    BMETER = 1
if(mode == "1"):
    print("Incluya el path del excel: (ejemplo: C:/Users/dbs99/Desktop/InstalacionAras.xlsx)")
    path = input()
