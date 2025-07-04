import adafruit_dht
import board
import time

dht = adafruit_dht.DHT11(board.D17, use_pulseio=False)  # GPIO17

for _ in range(3):  # Try 3 times
    try:
        temp = dht.temperature
        humidity = dht.humidity
        print(f"Temp: {temp}°C, Humidity: {humidity}%")
        break
    except RuntimeError as e:
        print("Retrying...", e)
        time.sleep(2)
else:
    print("Failed after 3 attempts. Check wiring!")
