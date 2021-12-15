import math

colours = ['Phoenix Yellow', 'Tomato Red', 'Sky Blue', 'Grass Green', 'Blood Red', 'Flame Orange', 'Royal Blue', 'Eggshell White', 'Midnight Black']
makes = ['Alfa Romeo', 'Aston Martin', 'Audi', 'BMW', 'Bentley', 'Bugatti', 'Chevrolet', 'Citroen', 'Dacia', 'Ferrari', 'Fiat', 'Ford', ' Honda' , 'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Lamborghini', 'Land Rover', 'Lexus', 'Lotus', 'MG', 'Mini', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Peugot', 'Porshe', 'Renault', 'Rolls-Royce', 'SKODA', 'Smart', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Vauxhall', 'Volkswagen', 'Volvo']

# LIST CAR MAKES
def displayMakes():
    count = 0
    for type in makes:
        print(f'[{count}] {type}')
        count += 1

# LIST CAR COLOURS
def displayColours():
    count = 0
    for c in colours:
        print(f'[{count}] {c}')
        count += 1

def createCar():

    displayMakes()
    make_selected = 0
    # SELECT CAR MAKE
    while make_selected == 0:
        num = input('Please select a make: ')
        if int(num) <= len(makes) and int(num) >= 0:
            car_make = makes[int(num)]
            make_selected = 1
        else:
            print('Invalid selection')
    
    # INPUT CAR MODEL
    car_model = input('Please enter the car make: ')
    displayColours()
    colour_selecter = 0

    # SELECT CAR COLOUR
    while colour_selecter == 0:
        num = input('Select a Colour: ')
        if int(num) <= len(colours) and int(num) >= 0:
                car_colour = colours[int(num)]
                colour_selecter = 1
        else:
            print('Invalid Selection')
    
    # INPUT CAR AGE
    car_age = input('Please enter the age of this car: ')

    # PRINT CAR DETAILS
    print(f'{car_make} {car_model} in {car_colour}')
    return Car(car_make, car_model, car_age, car_colour)

# DEFINE CAR CLASS + MIX FUNCTION
class Car:
    def __init__(self, make, model, age, colour):
        self.make = make
        self.model = model
        self.age = age
        self.colour = colour
    
    def mix(self, car2):
        new_make = self.make[:math.ceil(len(self.make)/2)] + car2.make[math.ceil(len(car2.make)/2):]
        new_model = self.model[:math.ceil(len(self.model)/2)] + car2.model[math.ceil(len(car2.model)/2):]
        old_colour = self.colour.split(' ')
        old_colour_mix = car2.colour.split(' ')
        new_colour = old_colour[0] + ' ' + old_colour_mix[1]

        new_age = (int(self.age) + int(car2.age)) / 2
        return {'make':new_make, 'model': new_model, 'age': new_age, 'colour': new_colour}    


car1 = createCar()
car2 = createCar()
car_mix = car1.mix(car2)
print(car_mix)
