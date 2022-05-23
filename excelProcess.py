# coding: utf-8
import openpyxl
import addSensorToGateway
path = ""
from datetime import datetime
import time
gateway = ""

print(" Seleccione un modo de uso \n 1. Agregar sensores mediante excel... (Configuracion del excel 1º columna componentName y 3º Deveui)\n 2. Manualamente 1by1 () ")
mode = input()
print(" Introduzca la mac gateway... ejemplo b827eb18ad132")
gateway = input()

if(mode == "1"):
    print("Incluya el path del excel: (ejemplo: C:/Users/dbs99/Desktop/InstalacionAras.xlsx)")
    path = input()
    # workbook object is created
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    m_row = sheet_obj.max_row
    loraAddress = []
    componentName = []
    SJEVO = 0
    BMETER = 0
    print("Seleccione 1 para SJEVO y 2 para Bmeter")
    typelogy = input()
    if(typelogy == "1"):
        SJEVO = 1
    if(typelogy == "2"):
        BMETER = 1
    for i in range(1, m_row + 1):
        cell_obj = sheet_obj.cell(row = i, column = 1)
        componentName.append(cell_obj.value)
    #  print(cell_obj.value)

    for i in range(1, m_row + 1):
        cell_obj = sheet_obj.cell(row = i, column = 3)
        loraAddress.append(cell_obj.value)
    # print(cell_obj.value)

    for x in range(0,len(loraAddress)):
        print( str(loraAddress[x]) + " " + str(componentName[x]) )
        if (SJEVO):
            messageToSend = """{
                "path" : "/oemsensors",
                "method" : "POST",
                
                "body" : "{\\"sensorModelName\\":\\"SJEvoSJEvo\\",\\"applicationName\\":\\"app\\",\\"loraAddress\\":\\\"""" + loraAddress[x] + """\\",\\"componentName\\":\\\"""" + componentName[x] + """\\",\\"sensorNames\\":{\\"volume\\":\\"S01\\"},\\"serverIds\\":[2]}",
                "port" : 4999,
                "timestamp" : "2019-12-08T16:00:02.2805625Z",
                "requestId" : "123456790",
                "authentication" :true
            }"""
        if (BMETER):
            messageToSend = """{
                "path" : "/oemsensors",
                "method" : "POST",
                
                "body" : "{\\"sensorModelName\\":\\"BmetersBmeters\\",\\"applicationName\\":\\"app\\",\\"loraAddress\\":\\\"""" + loraAddress[x] + """\\",\\"componentName\\":\\\"""" + componentName[x] + """\\",\\"sensorNames\\":{\\"volume\\":\\"S01\\"},\\"serverIds\\":[2]}",
                "port" : 4999,
                "timestamp" : "2019-12-08T16:00:02.2805625Z",
                "requestId" : "123456790",
                "authentication" :true
            }"""
        addSensorToGateway.send(gateway,messageToSend)
        time.sleep(0.5)
if(mode == "2"):
    print("Lora Address DEVEUI: ")
    loraAddressStr = input()
    print("Component Name: ")
    componentNameStr = input()

    messageToSend = """{
                "path" : "/oemsensors",
                "method" : "POST",
                
                "body" : "{\\"sensorModelName\\":\\"SJEvoSJEvo\\",\\"applicationName\\":\\"app\\",\\"loraAddress\\":\\\"""" + loraAddressStr + """\\",\\"componentName\\":\\\"""" + componentNameStr + """\\",\\"sensorNames\\":{\\"volume\\":\\"S01\\"},\\"serverIds\\":[2]}",
                "port" : 4999,
                "timestamp" : "2019-12-08T16:00:02.2805625Z",
                "requestId" : "123456790",
                "authentication" :true
            }"""
    addSensorToGateway.send(gateway,messageToSend)
    time.sleep(0.5)