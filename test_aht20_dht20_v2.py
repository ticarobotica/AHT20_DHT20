from machine import Pin, SoftI2C
from time import sleep_ms
from ahtx0 import AHT20
from DHT20 import DHT20


i2c_aht20=SoftI2C(sda=Pin(6), scl=Pin(7), freq=100000)
senzor_aht20=AHT20(i2c_aht20)

i2c_dht20=SoftI2C(sda=Pin(8), scl=Pin(9), freq=100000)
senzor_dht20=DHT20(0x38, i2c_dht20)


while True:
    temp_aht20=senzor_aht20.temperature
    humi_aht20=senzor_aht20.relative_humidity
    
    temp_dht20=senzor_dht20.measurements['t']
    humi_dht20=senzor_dht20.measurements['rh']
    
    print("Temp AHT20 = ", round(temp_aht20,2)," ","Humi AHT20 = ", round(humi_aht20,2)," ","Temp DHT20 = ", round(temp_dht20,2)," ","Humi DHT20 = ", round(humi_dht20,2)," ", end="\r")
    sleep_ms(1000)
    
