import sys

import pyowm


if __name__ == "__main__":

    observation = pyowm.OWM('4cb6c20a5fd231b32a334f0f6245cacb').weather_manager()
    w = observation.weather_at_place("London")

    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Your arguments: {sys.argv}")

    print("Weather in London: \n")
    if "temperature" in sys.argv:
        print(f"Temperature: {w.weather.temp}")
    if "clouds" in sys.argv:
        print(f"Clouds {w.weather.clouds}")
