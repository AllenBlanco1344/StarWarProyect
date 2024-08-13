from services.api_service import ApiService

class SpeciesController:
    def __init__(self):
        self.api_service = ApiService()

    def list_species(self):
        species = self.api_service.get_all_species()
        for specie in species:
            print(f"Name: {specie.name}, Height: {specie.average_height}, Classification: {specie.classification}")
            print(f"Homeworld: {specie.homeworld}, Language: {specie.language}")
            print(f"Characters: {', '.join(specie.characters)}")
            print(f"Episodes: {', '.join(specie.films)}\n")
