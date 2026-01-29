import random
import time
import matplotlib.pyplot as plt

# Lists to store data
temps = []
humidity = []
time_stamps = []

for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    hum = 60 + random.uniform(-5, 5)

    temps.append(temp)
    humidity.append(hum)
    time_stamps.append(t)

    try:
        with open("sensor_data.csv", "a") as csv_file:
            csv_file.write(f"{t},{temp:.2f},{hum:.2f}\n")

        with open("sensor_data.txt", "a") as txt_file:
            txt_file.write(
                f"Time: {t}s | Temperature: {temp:.2f} C | Humidity: {hum:.2f}%\n"
            )
    except IOError as e:
        print("File error:", e)

    time.sleep(0.5)

# Plot the data
plt.plot(time_stamps, temps, label="Temperature (C)")
plt.plot(time_stamps, humidity, label="Humidity (%)")
plt.xlabel("Time (s)")
plt.ylabel("Values")
plt.title("Temperature and Humidity Log")
plt.legend()
plt.show() 
