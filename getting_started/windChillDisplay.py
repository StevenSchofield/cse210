# This program asks for an input of temperature and clarification on if that temp is F or C,
#   and returns the wind chill based on various wind speeds

# Function to find the wind chill (F) based on temp (F) and the wind speed
def windChill(temp, windSpeed):
    return 35.74 + (0.6215*temp) - 35.75*(pow(windSpeed, 0.16)) + 0.4275*temp*(pow(windSpeed, 0.16))

# Conversion function for temperature
def Cel_To_F(degrees):
    return degrees * (9/5) + 32

# Display a single line of data. Not a necessary function, but I feel it makes the code look nicer
def displayData(temp, windSpeed, windChill):
    print("At temperature " + str(temp) + \
        "F, and wind speed " + str(windSpeed) + \
        " mph, the windchill is: " + str(round(windChill, 2)) + "F")


## START OF PROGRAM ##

# I didn't put any checks at this point as the device will naturally throw an error on an incorrect input type
Temp = float(input("Please input the temperature: "))

# As there are clear breaks in the code, I felt that using an eternal loop would work ok here to check F/C input
while True:
    TempType = input("Fahrenheit or Celsius (F/C)? ")

    if TempType == "F" or TempType == "C":
        if TempType == "F":
            print("\nFahrenheit selected.\n")
            break
        else: 
            print("\nCelsius selected.\n")
            break
    # I got lazy, so only capitalaized letters will be accepted
    elif TempType == "f" or TempType == "c":
        print("Please capitalize the letter for convenience sake.\n")
    else:
        print("Sorry, that input is not valid. Please try again.\n")

# Convert input to Fahrenheit (if needed)
if TempType == "C":
    Temp = Cel_To_F(Temp)

for wind in range(5, 61, 5):
    displayData(Temp, wind, windChill(Temp, wind))

## END OF LINE ##