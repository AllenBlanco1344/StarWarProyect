from services.api_service import ApiService

class PlanetController:
    def __init__(self):
        self.api_service = ApiService()

    def list_planets(self):
        planets = self.api_service.get_all_planets()
        for planet in planets:
            print(f"Name: {planet.name}, Orbital Period: {planet.orbital_period}, Rotation Period: {planet.rotation_period}")
            print(f"Population: {planet.population}, Climate: {planet.climate}")
            print(f"Residents: {', '.join(planet.residents)}")
            print(f"Episodes: {', '.join(planet.films)}\n")
