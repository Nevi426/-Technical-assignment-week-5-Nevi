#ke2
import numpy as np
import matplotlib.pyplot as plt
import Adafruit_DHT
from threading import Timer


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def ambil():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            #print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
            
            #ambil() mengembalikan suhu dalam Derajat Celcius
            return float("{0:0.1f}".format(temperature))
              
        else:
            print("Gagal mengambil data dari sensor suhu(DHT11)")

ambil ()