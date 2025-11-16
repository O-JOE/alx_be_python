def get_recommendation(weather_input):
    weather = weather_input.strip().lower()

    if weather == "sunny":
        return "Wear a T-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    user_input = input("What's the weather like today? (sunny/rainy/cold): ")
    recommendation = get_recommendation(user_input)
    print(recommendation)

if __name__ == "__main__":
    main()