from models.film import Film
from models.species import Species
from models.planet import Planet
from models.character import Character
import requests

class ApiService:
    BASE_URL = "https://www.swapi.tech/api"

    def get_all_films(self):
        response = requests.get(f"{self.BASE_URL}/films/")
        data = response.json()["result"]
        films = [self._create_film_obj(film) for film in data]
        return films

    def get_all_species(self):
        response = requests.get(f"{self.BASE_URL}/species/")
        data = response.json()["result"]
        species = [self._create_species_obj(specie) for specie in data]
        return species

    def get_all_planets(self):
        response = requests.get(f"{self.BASE_URL}/planets/")
        data = response.json()["result"]
        planets = [self._create_planet_obj(planet) for planet in data]
        return planets

    def get_characters_by_name(self, name_query):
        response = requests.get(f"{self.BASE_URL}/people/?search={name_query}")
        data = response.json()["result"]
        characters = [self._create_character_obj(character) for character in data]
        return characters

    def _create_film_obj(self, film_data):
        return Film(
            title=film_data["properties"]["title"],
            episode_id=film_data["properties"]["episode_id"],
            release_date=film_data["properties"]["release_date"],
            opening_crawl=film_data["properties"]["opening_crawl"],
            director=film_data["properties"]["director"],
        )

    def _create_species_obj(self, species_data):
        return Species(
            name=species_data["properties"]["name"],
            average_height=species_data["properties"]["average_height"],
            classification=species_data["properties"]["classification"],
            homeworld=species_data["properties"]["homeworld"],
            language=species_data["properties"]["language"],
            characters=species_data["properties"]["people"],
            films=species_data["properties"]["films"],
        )

    def _create_planet_obj(self, planet_data):
        return Planet(
            name=planet_data["properties"]["name"],
            orbital_period=planet_data["properties"]["orbital_period"],
            rotation_period=planet_data["properties"]["rotation_period"],
            population=planet_data["properties"]["population"],
            climate=planet_data["properties"]["climate"],
            residents=planet_data["properties"]["residents"],
            films=planet_data["properties"]["films"],
        )

    def _create_character_obj(self, character_data):
        return Character(
            name=character_data["properties"]["name"],
            homeworld=character_data["properties"]["homeworld"],
            gender=character_data["properties"]["gender"],
            species=character_data["properties"]["species"],
            starships=character_data["properties"]["starships"],
            vehicles=character_data["properties"]["vehicles"],
            films=character_data["properties"]["films"],
        )
