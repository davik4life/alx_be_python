askWeather = str(input("What's the weather like today? (sunny/rainy/cold):")).lower()

if "sunny" == askWeather:
    print("Wear a t-shirt and sunglasses.")
elif "rainy" == askWeather:
    print("Don't forget your umbrella and a raincoat.")
elif "cold" == askWeather:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")