class Pet:
    
    # constructor
    def __init__(self, species, breed, name, birthYear ):
        self.species = species
        self.breed = breed
        self.name = name
        self.birthYear = birthYear
        
    # getters
    def getSpecies(self):
        return self.species
    def getBreed(self):
        return self.breed
    def getName(self):
        return self.name
    def getBirthYear(self):
        return self.birthYear
    
    # setters
    def setSpecies(self, species):
        self.species = species
    def setBreed(self, breed):
        self.breed = breed
    def setName(self, name):
        self.name = name
    def setBirthYear(staff, birthYear):
        self.birthYear = birthYear
        
    # calculateAge
    def calculateAge(self):
        if self.birthYear <= 2020 :
            age = 2020 - self.birthYear
            print('Pet age:',age)
        else:
            print('Birth year is a future year. So cannot calculate age.')
            
    # vocalization
    def getVocalization(self):
        if self.species == 'dog' :
            print('Vocaliation is wool')
        elif self.species == 'bird' and self.breed == 'falcon' :
            print('Vocaliation is cry')
        elif self.species == 'bird' and self.breed == 'crow' :
            print('Vocaliation is caw')
        else:
            print('Vocalization is not found')
            

def displayInformation():
    species = input("Enter species: ")
    breed = input("Enter breed: ")
    name = input("Enter name: ")
    birthYear = int(input("Enter birth year: "))
    
    output = Pet(species, breed, name, birthYear)
    
    print("#" * 30)
    print("Species:"+output.getSpecies())
    print("Breed:"+output.getBreed())
    print("Pet Name:"+output.getName())
    print("Birth Year:",output.getBirthYear())
    output.calculateAge()
    output.getVocalization()
    
displayInformation()