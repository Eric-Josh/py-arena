class Pet:
    
    # constructor
    def __init__(self, species, breed, name, birthYear ):
        self.species = species
        self.breed = breed
        self.name = name
        self.birthYear = birthYear
        
    # declear setters
    def setSpecies(self, species):
        self.species = species
    def setBreed(self, breed):
        self.breed = breed
    def setName(self, name):
        self.name = name
    def setBirthYear(staff, birthYear):
        self.birthYear = birthYear
        
    # declear getters
    def getSpecies(self):
        return self.species
    def getBreed(self):
        return self.breed
    def getName(self):
        return self.name
    def getBirthYear(self):
        if self.birthYear <= 2020 :
            birthYear = self.birthYear
        else:
            birthYear = 'You have entered future year. So not updated.'
            
        return birthYear
    
    # vocalization
    def getVocalization(self):
        if self.species == 'cat' :
            print('Vocaliation is maiaow')
        elif self.species == 'bird' and self.breed == 'nightingale' :
            print('Vocaliation is singsong')
        elif self.species == 'bird' and self.breed == 'cockatoo' :
            print('Vocaliation is hello!')
        elif self.species == 'bird' and self.breed != 'nightingale' or self.breed != 'cockatoo':
            print('Vocaliation is tweet')
        else:
            print('Vocalization is not found')
            

def displayInfomation():
    species = input("Enter species: ")
    breed = input("Enter breed: ")
    name = input("Enter name: ")
    birthYear = int(input("Enter birth year: "))
    
    petInfo = Pet(species, breed, name, birthYear)
    
    print("=" * 30)
    print("Species: " + petInfo.getSpecies())
    print("Breed: " + petInfo.getBreed())
    print("Pet Name: ", petInfo.getName())
    print("Birth Year: ", petInfo.getBirthYear())
    petInfo.getVocalization()
    
displayInfomation()
            