# AddSensorsGateway
Add sensors from excel table to python and then send mqtt to gateway for config and add sensors to port 4999
Se pueden añadir de forma manual o de forma automatica desde un excel siguiendo la estructura indicada.
Cada vez se creacrá un .log con el nombre del gateway fecha y request / response.

````
-  | Columna 1 -> componentName || Columna 3 -> componentName |
````
## Requisitos: 
    - Tener instalado Python3 y gestor pip3
    - pip3 install paho-mqtt 
    - pip3 install openpyxl 
    
## Ejecución: 

Modo de ejecución en la carpeta de este proyecto, se ejecutará el script simplemente escriba en la terminal el comando y siga instrucciones:
```bash
    python3 excelProcess.py 
````
