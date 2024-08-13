from services.api_service import ApiService

class CharacterController:
    def __init__(self):
        self.api_service = ApiService()

    def search_characters(self, name_query):
        characters = self.api_service.get_characters_by_name(name_query)
        for character in characters:
            print(f"Name: {character.name}, Homeworld: {character.homeworld}, Gender: {character.gender}")
            print(f"Species: {character.species}, Starships: {', '.join(character.starships)}")
            print(f"Vehicles: {', '.join(character.vehicles)}")
            print(f"Episodes: {', '.join(character.films)}\n")
