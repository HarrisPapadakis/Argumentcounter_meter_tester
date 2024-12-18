#This program uses "for" and "in" operator

cars = ["suzuki", "seat", "ford", "toyota", "bmw", "mercedes"] # create a list with given values

for car in cars:
    if car == "bmw":
        print(car.upper())  # Print in uppercase if the car is "bmw"
    else:
        print(car.title())  # Print in title case for other cars
