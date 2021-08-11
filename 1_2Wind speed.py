print(" *** Wind classification ***")
windSpeed = float((input("Enter wind speed (km/h) : ")))
if windSpeed >= 0 and windSpeed <= 51.99 :
    print("Wind classification is Breeze.")
elif windSpeed >= 52.00 and windSpeed <= 55.99 :
    print("Wind classification is Depression.")
elif windSpeed >= 56.00 and windSpeed <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif windSpeed >= 102.00 and windSpeed <= 208.99 :
    print("Wind classification is Typhoon.")
elif windSpeed >= 209 :
    print("Wind classification is Super Typhoon.")
else:
    print("Error")