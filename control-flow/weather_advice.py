weather = ["sunny", "rainy", "cold"]

askWeather = str(input("What's the weather like today? (sunny/rainy/cold):")).lower()
for ask in weather:
    if askWeather == weather[0]:
        print("Wear a t-shirt and sunglasses.")
        break
    elif askWeather == weather[1]:
        print("Don't forget your umbrella and a raincoat.")
        break
    elif askWeather == weather[2]:
        print("Make sure to wear a warm coat and a scarf.")
        break
    else: print("Sorry, I don't have recommendations for this weather.")
    break