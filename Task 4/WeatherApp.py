import tkinter as tk
import requests
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "5726f0c7e9a36e67abc5d48d6ba896ad"  # Replace with your OpenWeatherMap API key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            params = {"q": city, "appid": self.api_key, "units": "metric"}
            response = requests.get(self.url, params=params)
            data = response.json()

            if response.status_code == 200:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                weather_info = f"Temperature: {temperature}°C\nDescription: {description}"
                self.weather_label.config(text=weather_info)
            else:
                messagebox.showerror("Error", "City not found. Please check the city name.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    weather_app = WeatherApp(root)
    root.mainloop()
