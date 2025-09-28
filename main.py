
class Car():
    license_plate = ""
    horsepower = ""
    color = ""
    model = ""
    brand = ""

    def _init_(car):
        print("Making a new car")
    def change_details(car):
        print("Please enter the brand of your car: ")
        car.brand = input()
        print("Please enter the horsepower of your car: ")
        car.horsepower = input()
        print("Please enter the model of car you own")
        car.model = input()
        print("Please enter the color of the car")
        car.color = input()
        print("Please enter your license plate: ")
        car.license_plate = input()
    def show_Details(car):
        print("The details of the car is: ")
        print(car.color)
        print(car.brand)
        print(car.model)
        print(car.license_plate)
        print(car.horsepower)

Toyota = Car()
Toyota.change_details()
Toyota.show_Details()


