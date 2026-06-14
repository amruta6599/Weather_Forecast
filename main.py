import os
import time

from weather_service import (
    fetch_weather_data,
    get_weather_theme
)

# =========================
# COLORS
# =========================

CLR_HEADER = '\033[95m'
CLR_SUNNY = '\033[93m'
CLR_RAINY = '\033[94m'
CLR_SNOWY = '\033[96m'
CLR_CLOUDY = '\033[90m'
CLR_RESET = '\033[0m'
CLR_SUCCESS = '\033[92m'
CLR_ERROR = '\033[91m'
CLR_BORDER = '\033[37m'


# =========================
# FUNCTIONS
# =========================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_main_menu():

    clear_screen()

    print(f"{CLR_HEADER}{'=' * 50}{CLR_RESET}")
    print(f"{CLR_SUNNY}      ✨ WEATHER FORECAST CLI APP ✨{CLR_RESET}")
    print(f"{CLR_HEADER}{'=' * 50}{CLR_RESET}")

    print(f"\n{CLR_SUCCESS}[1]{CLR_RESET} Search Weather")
    print(f"{CLR_ERROR}[2]{CLR_RESET} Exit")

    print(f"\n{CLR_HEADER}{'-' * 50}{CLR_RESET}")


def display_weather_card(data):

    clear_screen()

    city = data["name"]
    country = data["sys"]["country"]

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    wind_speed = data["wind"]["speed"]

    weather = data["weather"][0]
    condition_id = weather["id"]
    description = weather["description"].title()

    theme_color, emoji, status_text = get_weather_theme(condition_id)

    print(f"{CLR_BORDER}┌──────────────────────────────────────────────┐{CLR_RESET}")
    print(f"{CLR_BORDER}│{CLR_RESET} 📍 {city}, {country}")
    print(f"{CLR_BORDER}├──────────────────────────────────────────────┤{CLR_RESET}")

    print(
        f"{CLR_BORDER}│{CLR_RESET} Condition   : "
        f"{theme_color}{emoji} {description}{CLR_RESET}"
    )

    print(
        f"{CLR_BORDER}│{CLR_RESET} Temperature : "
        f"{theme_color}{temp}°C{CLR_RESET}"
    )

    print(
        f"{CLR_BORDER}│{CLR_RESET} Feels Like  : "
        f"{feels_like}°C"
    )

    print(
        f"{CLR_BORDER}│{CLR_RESET} Humidity    : "
        f"💧 {humidity}%"
    )

    print(
        f"{CLR_BORDER}│{CLR_RESET} Wind Speed  : "
        f"💨 {wind_speed} m/s"
    )

    print(
        f"{CLR_BORDER}│{CLR_RESET} Pressure    : "
        f"🌡️ {pressure} hPa"
    )

    print(f"{CLR_BORDER}└──────────────────────────────────────────────┘{CLR_RESET}")

    print(
        f"\n📊 Theme Status: "
        f"{theme_color}[{status_text}]{CLR_RESET}"
    )


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        show_main_menu()

        choice = input(
            "\n👉 Select an option (1-2): "
        ).strip()

        if choice == "1":

            clear_screen()

            print(
                f"{CLR_HEADER}🔍 WEATHER SEARCH {CLR_RESET}"
            )

            city_name = input(
                "\nEnter city name: "
            ).strip()

            if not city_name:

                print(
                    f"\n{CLR_ERROR}❌ City name cannot be empty!{CLR_RESET}"
                )

                time.sleep(2)
                continue

            print("\n⚡ Fetching weather data...")

            data, error = fetch_weather_data(city_name)

            if error:

                print(
                    f"\n{CLR_ERROR}❌ {error}{CLR_RESET}"
                )

            else:

                display_weather_card(data)

            input(
                f"\nPress {CLR_SUNNY}[Enter]{CLR_RESET} to continue..."
            )

        elif choice == "2":

            clear_screen()

            print(
                f"\n{CLR_SUNNY}☀️ Thank you for using Weather Forecast CLI!{CLR_RESET}"
            )

            break

        else:

            print(
                f"\n{CLR_ERROR}❌ Invalid option!{CLR_RESET}"
            )

            time.sleep(1.5)


if __name__ == "__main__":
    main()