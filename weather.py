"""
Simple weather data experiment.

This is a small test project for experimenting with
Python, dictionaries and basic calculations.
"""

weather_data = {
    "location": "Aalesund",
    "temperature": 14,
    "humidity": 72,
    "wind_speed": 5.4,
    "condition": "Cloudy"
}


def show_weather(data):
    print("Weather information")
    print("-------------------")
    print(f"Location: {data['location']}")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind speed: {data['wind_speed']} m/s")
    print(f"Condition: {data['condition']}")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    show_weather(weather_data)

    fahrenheit = celsius_to_fahrenheit(
        weather_data["temperature"]
    )

    print()
    print(f"Temperature in Fahrenheit: {fahrenheit:.1f}°F")


if __name__ == "__main__":
    main()
