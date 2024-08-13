import requests 
import matplotlib.pyplot as plt 
import pandas as pd

# Clase para interactuar con la API SWAPI
class SWAPIClient:
    BASE_URL = "https://www.swapi.tech/api"

    def get_data(self, endpoint):
        response = requests.get(f"{self.BASE_URL}/{endpoint}")
        return response.json()['result'] if response.status_code == 200 else None

    def get_films(self):
        return self.get_data("films")

    def get_species(self):
        return self.get_data("species")

    def get_planets(self):
        return self.get_data("planets")

    def search_character(self, query):
        return self.get_data(f"people/?name={query}")

# Clases del Modelo
class Pelicula:
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

class Especie:
    def __init__(self, name, height, classification, homeworld, language, characters, films):
        self.name = name
        self.height = height
        self.classification = classification
        self.homeworld = homeworld
        self.language = language
        self.characters = characters
        self.films = films

class Planeta:
    def __init__(self, name, orbital_period, rotation_period, population, climate, films, residents):
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.population = population
        self.climate = climate
        self.films = films
        self.residents = residents

class Personaje:
    def __init__(self, name, homeworld, films, gender, species, starships, vehicles):
        self.name = name
        self.homeworld = homeworld
        self.films = films
        self.gender = gender
        self.species = species
        self.starships = starships
        self.vehicles = vehicles

# Funciones para mostrar datos
def mostrar_peliculas(peliculas):
    for pelicula in peliculas:
        print(f"Título: {pelicula.title}")
        print(f"Episodio: {pelicula.episode_id}")
        print(f"Fecha de lanzamiento: {pelicula.release_date}")
        print(f"Opening Crawl: {pelicula.opening_crawl}")
        print(f"Director: {pelicula.director}")
        print("-" * 40)

def mostrar_especies(especies):
    for especie in especies:
        print(f"Nombre: {especie.name}")
        print(f"Altura: {especie.height}")
        print(f"Clasificación: {especie.classification}")
        print(f"Planeta de origen: {especie.homeworld}")
        print(f"Lengua: {especie.language}")
        print(f"Personajes: {', '.join(especie.characters)}")
        print(f"Episodios: {', '.join(especie.films)}")
        print("-" * 40)

def mostrar_planetas(planetas):
    for planeta in planetas:
        print(f"Nombre: {planeta.name}")
        print(f"Período de órbita: {planeta.orbital_period}")
        print(f"Período de rotación: {planeta.rotation_period}")
        print(f"Población: {planeta.population}")
        print(f"Clima: {planeta.climate}")
        print(f"Episodios: {', '.join(planeta.films)}")
        print(f"Residentes: {', '.join(planeta.residents)}")
        print("-" * 40)

# Ejemplo de uso
if __name__ == "__main__":
    client = SWAPIClient()

    # Obtener y mostrar películas
    peliculas_data = client.get_films()
    peliculas = [Pelicula(f['properties']['title'], 
                          f['properties']['episode_id'], 
                          f['properties']['release_date'], 
                          f['properties']['opening_crawl'], 
                          f['properties']['director']) 
                 for f in peliculas_data]
    mostrar_peliculas(peliculas)

    # Obtener y mostrar especies
    especies_data = client.get_species()
    especies = [Especie(e['properties']['name'], 
                        e['properties']['average_height'], 
                        e['properties']['classification'], 
                        e['properties']['homeworld'], 
                        e['properties']['language'], 
                        e['properties']['people'], 
                        e['properties']['films']) 
                for e in especies_data]
    mostrar_especies(especies)

    # Obtener y mostrar planetas
    planetas_data = client.get_planets()
    planetas = [Planeta(p['properties']['name'], 
                        p['properties']['orbital_period'], 
                        p['properties']['rotation_period'], 
                        p['properties']['population'], 
                        p['properties']['climate'], 
                        p['properties']['films'], 
                        p['properties']['residents']) 
                for p in planetas_data]
    mostrar_planetas(planetas)

    # Buscar y mostrar personaje
    query = input("Introduce el nombre del personaje a buscar: ")
    personaje_data = client.search_character(query)
    if personaje_data:
        for p in personaje_data:
            print(f"Nombre: {p['properties']['name']}")
            print(f"Planeta de origen: {p['properties']['homeworld']}")
            print(f"Episodios: {', '.join(p['properties']['films'])}")
            print(f"Género: {p['properties']['gender']}")
            print(f"Especie: {p['properties']['species']}")
            print(f"Naves: {', '.join(p['properties']['starships'])}")
            print(f"Vehículos: {', '.join(p['properties']['vehicles'])}")
            print("-" * 40)

    # Ejemplo de gráfico usando datos CSV
    # Se asume que los datos ya han sido exportados a CSV previamente

    # Leer datos desde CSV y generar gráficos
    df = pd.read_csv('naves.csv')

    # Gráfico de Longitud de Naves
    plt.figure(figsize=(10, 6))
    df['longitud'].plot(kind='bar')
    plt.title('Comparación de la Longitud de Naves')
    plt.xlabel('Naves')
    plt.ylabel('Longitud')
    plt.show()

    # Estadísticas sobre naves
    print(df.describe())

    # Se puede seguir implementando la lógica para gestión de misiones, etc.
