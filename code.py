'''Currency converter
   Sophie Buckley, 9/7/13
 
   This is a simple program that will convert one currency to another.
   The currencies currently supported are pound sterling, the euro and usd.
'''
import requests
from datetime import datetime
 
def currencyConvert():
    #Store what the user wants to convert as a variable.
    userChoice = raw_input ('What currency do you want to be converted? \n Type 1 for pound sterling. \n Type 2 for euro. \n Type 3 for usd. \n')
    print
    #If the user has typed 1...
    if userChoice == '1':
        #...then poundConversion is called. This will prompt the user further and carry out the actual conversion.
        poundConversion()
 
    #If the user has typed 2...
    elif userChoice == '2':
        #...then euroConversion is called. This will prompt the user further and carry out the actual conversion.
        euroConversion()
 
    #If the user has typed 3...
    elif userChoice == '3':
        #...then usdConversion is called. This will prompt the user further and carry out the actual conversion.
        usdConversion()
 
    else:
        #An error message is displayed and they're prompted again.
        print('Error: you have entered invalid information - please try again.')
        currencyConvert()
 
def poundConversion():
    userSecondChoice = raw_input('What would you like to convert to? \n Type 1 for euro. \n Type 2 for usd. \n')
    if userSecondChoice == '1':
        #Prompt for the amount of pound sterling that they want to be converted.
        #Store the amount as a variable.
        userPound = input ("Enter the amount in pounds that you would like to convert.\n")
 
        EurofromPound = userPound * getRate('GBP', 'EUR')
        #Output the amount to the user.
        print
        print "%0.2f" %userPound, "pounds = %0.2f" %EurofromPound, "euro."
        print
        useAgain()
 
    elif userSecondChoice == '2':
        #Prompt for the amount of pound sterling that they want to be converted.
        #Store the amount as a variable.
        userPound = input ("Enter the amount in pounds that you would like to convert.\n")
 
        USDfromPound = userPound * getRate('GBP', 'USD')
        #Output the amount to the user.
        print
        print "%0.2f" %userPound, "pounds = %0.2f" %USDfromPound, "dollars."
        print
        useAgain()
 
    #If the user doesn't enter 1 or 2 for a currency to convert to...
    else:
        #An error message is displayed and they're prompted again.
        print('Error: you have entered invalid information - please try again.')
        poundConversion()
 
def euroConversion():
    userSecondChoice = raw_input('What would you like to convert to? \n Type 1 for pounds. \n Type 2 for usd. \n')
    if userSecondChoice == '1':
        #Prompt for the amount of euros that they want to be converted.
        #Store the amount as a variable.
        userEuro = input ("Enter the amount in euros that you would like to convert.\n")
 
        PoundfromEuro = userEuro * getRate('EUR', 'GBP')
        #Output the amount to the user.
        print
        print "%0.2f" %userEuro, "euro = %0.2f" %PoundfromEuro, "pounds."
        print
        useAgain()
 
    elif userSecondChoice == '2':
        #Prompt for the amount of euros that they want to be converted.
        #Store the amount as a variable.
        userEuro = input ("Enter the amount in euros that you would like to convert.\n")
 
        USDfromEuro = userEuro * getRate('EUR', 'USD')
        #Output the amount to the user.
        print
        print "%0.2f" %userEuro, "euro = %0.2f" %USDfromEuro, "dollars."
        print
        useAgain()
    #If the user doesn't enter 1 or 2 for a currency to convert to...
    else:
        #An error message is displayed and they're prompted again.
        print('Error: you have entered invalid information - please try again.')
        euroConversion()
 
def usdConversion():
    userSecondChoice = raw_input('What would you like to convert to? \n Type 1 for pounds. \n Type 2 for euro. \n')
    if userSecondChoice == '1':
        #Prompt for the amount of dollars that they want to be converted.
        #Store the amount as a variable.
        userUSD = input ("Enter the amount in dollars that you would like to convert.\n")
 
        PoundfromUSD = userUSD * getRate('USD', 'GBP')
        #Output the amount to the user.
        print
        print "%0.2f" %userUSD, "dollars = %0.2f" %PoundfromUSD, "pounds."
        print
        useAgain()
 
    elif userSecondChoice == '2':
        #Prompt for the amount of euros that they want to be converted.
        #Store the amount as a variable.
        userUSD = input ("Enter the amount in dollars that you would like to convert.\n")
 
        EurofromUSD = userUSD * getRate('USD', 'EUR')
        #Output the amount to the user.
        print
        print "%0.2f" %userUSD, "dollars = %0.2f" %EurofromUSD, "euro."
        print
        useAgain()
    #If the user doesn't enter 1 or 2 for a currency to convert to...
    else:
        #An error message is displayed and they're prompted again.
        print('Error: you have entered invalid information - please try again.')
        usdConversion()
 
 
 
 
def getRate(fromCny, toCny):
    #Gets the html from the webpage. 
    html = requests.get('http://www.google.co.uk/finance/converter?a=1&from=%s&to=%s' % (fromCny, toCny)).content
    #Finds the position of <span class... etc (the line with the converted number on).
    position = html.find('<span class=')
    #Finds the end + 1 of the value being scraped.
    position2 = html.find(toCny, position)
    #returns the exchange rate as a float (rather than the string that it originally was).
    return float(html[position + 16:position2 - 1:])
 
 
 
 
 
def useAgain():
    #Ask the user whether they want to use the program again. 
    userAgain = raw_input ('Would you like to convert something else? \n Yes \n No \n') 
    #If they say yes, then the program runs again.
    if userAgain.lower() == 'yes':
        currencyConvert()
    #If they say no, then the program is terminated.
    elif userAgain.lower() == 'no':
        #The variable hour gets the current date and time from the computer.
        hour = datetime.now().time().hour
        #If it is between 6am and 12pm then the user gets this message.
        if 6 <= hour < 12:
            timeEnding = 'have a nice morning!'
        #If it is between 12pm and 5pm then the user gets this message.
        elif 12 <= hour < 17:
            timeEnding = 'have a pleasant afternoon!'
        #If it is between any other time...
        else:
            timeEnding = 'have a lovely evening!'
        print('Thank you for using this program - ' + timeEnding)
        quit()
    #If they say anything else then they are prompted again.
    else:
        print('Error: you have entered invalid information - please try again.')
        useAgain()
 
 
currencyConvert()
