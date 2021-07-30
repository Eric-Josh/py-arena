import datetime

class Pet:
    
    # constructor
    def __init__(self, species, breed, name, birthYear ):
        self.species = species
        self.breed = breed
        self.name = name
        self.birthYear = birthYear
        
    # define getters
    def getSpecies(self):
        return self.species
    def getBreed(self):
        return self.breed
    def getName(self):
        return self.name
    def getBirthYear(self):
        return self.birthYear
    
    # define setters
    def setSpecies(self, species):
        self.species = species
    def setBreed(self, breed):
        self.breed = breed
    def setName(self, name):
        self.name = name
    def setBirthYear(staff, birthYear):
        self.birthYear = birthYear
        
    # calculateAge method
    def calculateAge(self):
        now = datetime.datetime.now()
        if self.birthYear < now.year :
            age = now.year - self.birthYear
            print('Pets age is ',age)
        else:
            print('Birth year is a future year')
            
    def getLifeExpectancy(self):
        if self.species == 'Rabbit' :
            print('Life Span is 1 - 2 years')
        elif self.species == 'Cat' and self.breed == 'Persian' :
            print('Life Span is 10 - 17 years')
        elif self.species == 'Cat' and self.breed == 'Turkish Angora' :
            print('Life Span is 12 - 18 years')
        elif self.species == 'Cat' and self.breed == 'Egyptian Mau' :
            print('Life Span is 13 - 16 years')
        else:
            print('Life Expectancy is unknown')
            

def displayInfomation():
    species = input("Enter species: ")
    breed = input("Enter breed: ")
    name = input("Enter name: ")
    birthYear = int(input("Enter birth year: "))
    
    x = Pet(species, breed, name, birthYear)
    
    print("=" * 30)
    print("Species: " + x.getSpecies())
    print("Breed: " + x.getBreed())
    print("Pet Name: ", x.getName())
    print("Birth Year: ", x.getBirthYear())
    x.calculateAge()
    x.getLifeExpectancy()
    
displayInfomation()