def hotelnights(nights):
   return 140*nights
def airplanecost(city):
    if  "new york"==city:
        return 184
    elif  "moscouw"==city:
        return 234
    elif  "tokyo"==city:
        return 378
    elif  "amsterdam"==city:
        return 50
def rentalcarcost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rentalcarcost(days) + hotelnights(days) + airplanecost(city) + spending_money
	
print("Cost of car rental: ",rentalcarcost(5))

print("Cost of plane ride: ",airplanecost("moscouw"))

print("Cost of hotel room: ", hotelnights(7))

print("Total cost of the trip:",trip_cost("new york",7,500))

print(trip_cost("tokyo",6,500))
    
    
    
    

    