class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in self.PET_TYPES:
            raise Exception
        
        Pet.all.append(self)

    

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # should return a list of pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        # should assign this owner to the pet if it's an instance of Pet
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
        
    def get_sorted_pets(self):
        # Should return a list of this pwner's pets sorted by their names
        return sorted(self.pets(), key = lambda pet: pet.name)

        