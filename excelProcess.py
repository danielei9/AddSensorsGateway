# coding: utf-8
import openpyxl
import addSensorToGateway
path = "C:/Users/dbs99/Desktop/c.xlsx"
from datetime import datetime
import time
gateway = "b827eb4b07fe"

# workbook object is created
wb_obj = openpyxl.load_workbook(path)
 
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
loraAddress = []
componentName = []


# Loop will print all values
# of first column

for i in range(1, m_row + 1):
    cell_obj = sheet_obj.cell(row = i, column = 1)
    componentName.append(cell_obj.value)
  #  print(cell_obj.value)

for i in range(1, m_row + 1):
    cell_obj = sheet_obj.cell(row = i, column = 3)
    loraAddress.append(cell_obj.value)
   # print(cell_obj.value)

for x in range(300,len(loraAddress)):
    print( str(loraAddress[x]) + " " + str(componentName[x]) )
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
