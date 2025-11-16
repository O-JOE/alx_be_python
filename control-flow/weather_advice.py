# weather_advice.py
def get_recommendation(weather_input: str) -> str:
    """
    Return clothing recommendation based on the weather input.
    """
    if not weather_input:
        return "Sorry, I don't have recommendations for this weather."

    # Normalize input: remove extra spaces and make lower-case
    weather = weather_input.strip().lower()

    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
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