
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the Location class
loc1 = Location("Tomas", "Portugal")
loc1.myLocation()

# Three more instantiations and method calls for the Location class
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

loc2.myLocation()
loc3.myLocation()

your_loc = Location("Элнур", "Кыргызстан")
your_loc.myLocation()

