temp = int(input("What is the temperature today:"))

if temp >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 < temp < 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 < temp <19:
    print("It's a cool day. Wear a jacket!")
elif temp <= 10:
    print("It's a cold day. Stay warm!")