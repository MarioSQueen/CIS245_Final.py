# Mario S. Queen
# CIS 245
# July 2022
# Final Project: Using User Input to Obtain Weather Information from a Web Service

# Define as "main" to be able to loop the program later.
def main():
    
    import json
    import requests

# Create variables for all parts of the web address that will be requested.
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "2c6a40c825fc300c2e2d0b293fe03f58"

# Use input() funcion to allow user to enter a location 
    city = input("\nPlease Enter the City or Zip Code Where You Would Like the Temperture: ")

# use title() function to capitalize the first letter in user entry.
    city = city.title()

#Create a variable that incorportates the website, personal appid, and location the user inputted.
    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    print(url)
    print()

# Use requests.get() function to have Python requests information from web
    response = requests.get(url)
    unformated_data = response.json()
    
# Use try block to return valid responses from web   
    try:
        temp = unformated_data["main"]["temp"]
        print(f"\nThe current temp is: {temp} degrees in {city}...")

# Use except block to print an error and loop the program back to the beginning
    except Exception as e:
        print(e)
        print("\nInvalid Entry! ")
        main()

# Create variable and use input() function to allow user to request to enter another selection or to end the program.
    restart = input("\nWould You Like to Check the Temp for a Different Location, Type: Y for Yes; Q to Quit: ")

    restart = restart.title()

# Using 'if' block to either restart the program or end it.
    if restart == "Y":
        main()
        
    elif restart == "Q":
        print("\nThank You and Have a Nice Day!")
        exit()

main()