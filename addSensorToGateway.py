# encoding: utf-8
import time
import paho.mqtt.client as paho
import os
from datetime import datetime

port = 8882
broker = "gesinen.es"
print("ADD sensors terminal: ")
print("conectando al broker", broker)
try:
    clt=paho.Client("client-addSensors")
    clt.tls_set()
    clt.username_pw_set(username="gesinen", password="gesinen2110")
    print(clt.connect(broker,8882))
except:
    print("connection failed")
    exit(1) #Should quit or raise flag to quit or retry

#print("¿ Nombre del Modelo de Sensor? Ej: ItronCyble4IoT")
#sensorModelName = input()

#print("¿ LoraAddress ? Ej: 90dffb8153211f25")
#loraAddress = str(input())

#print("¿ componentName ? Ej: DCSWAGWS0000000000")
#componentName = str(input())

#print("¿ Direccion gateway ? Ej: b827ebfb2d40")
#gateway = input()

def on_message(clt, usrdata, mess):
    time.sleep(1)
    incomingStr = str(mess.payload.decode("utf-8"))
    print(incomingStr)
    
def createLoopMqttRecive(clt):
    #Damos callback a usar cuando hay un msg
    clt.on_message = on_message
    print("conectando al broker", broker)
    try:
        clt.tls_set()
        clt.username_pw_set(username="gesinen", password="gesinen2110")
        print(clt.connect(broker,8882))
    except:
        print("connection failed")
        exit(1) #Should quit or raise flag to quit or retry
    try:
        clt.loop_start() # Inicia el bucle esperando a un msg
        print("subscribiendo...")
        clt.subscribe(topic)
        print("publicación:")
    except:
        print("subscribe Failed")

def send(gateway,messageToSend):
    topic = str(gateway)+ "/gateway_requests/request"
    # Nombre al cliente
    try:
        #createLoopMqttRecive(clt)
    #    time.sleep(3)
        clt.publish(topic ,messageToSend )
        print(messageToSend)

    except:
        pass
        print("Error ocurred")