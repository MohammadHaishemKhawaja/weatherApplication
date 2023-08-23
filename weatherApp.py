import tkinter as tk
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# by Mohammad Khawaja

API_KEY = "2ba22dca89af6176243657beb0aad935"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"  # Fetch data in Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def update_weather_label():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            weather_label.config(text=f"Temperature: {temperature}°F\nHumidity: {humidity}%")

            # Clear the previous graph
            ax.clear()

            # Create and display a new bar graph
            ax.bar(["Temperature", "Humidity"], [temperature, humidity])
            ax.set_xlabel("Data Type")
            ax.set_ylabel("Value")
            ax.set_title("Temperature and Humidity")
            canvas.draw()
        else:
            weather_label.config(text="City not found")
    else:
        weather_label.config(text="Enter a city")

# GUI setup
root = tk.Tk()
root.title("Weather App")

# Customize the appearance of the GUI elements
root.geometry("400x600")  # Set the initial size of the window
root.configure(bg="#3498db")  # Set the background color

city_label = tk.Label(root, text="Enter city:", font=("Arial", 16), bg="#3498db", fg="white")
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), bg="#2ecc71", fg="white", command=update_weather_label)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300, bg="#3498db", fg="white", padx=20, pady=10)
weather_label.pack()

# Create a figure and axis for the graph
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()
