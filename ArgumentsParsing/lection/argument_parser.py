import argparse
import sys
import pyowm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--clouds",
                        required=False,
                        dest="clouds",
                        help="Show clouds measurement: (0, 100)",
                        action='store_true',
                        )
    parser.add_argument("-nt", "--no-temperature", required=False, dest="temperature",
                        help="Exclude temperature from output",
                        action='store_false',
                        )
    parser.add_argument("--town", required=True, dest="town",
                        help="Location for which weather will be shown; Example: London, Lviv etc...")

    parser.add_argument("-w", "--wind", required=False, dest="wind",
                        help="Show wind measurement: (0, 100)",
                        action='store_true',)
    args = parser.parse_args()

    observation = pyowm.OWM('4cb6c20a5fd231b32a334f0f6245cacb').weather_manager()
    try:
        weather = observation.weather_at_place(args.town)
    except pyowm.commons.exceptions.NotFoundError as e:
        print("we can't find the city with this name")
        sys.exit()

    if args.clouds:
        print(f"Clouds {weather.weather.clouds}")
    if args.temperature:
        print(f"Temperature: {weather.weather.temp}")
    if args.wind:
        print(f'Wind power:{weather.weather.wind}')