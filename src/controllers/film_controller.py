from services.api_service import ApiService

class FilmController:
    def __init__(self):
        self.api_service = ApiService()

    def list_films(self):
        films = self.api_service.get_all_films()
        for film in films:
            print(f"Title: {film.title}, Episode: {film.episode_id}, Release Date: {film.release_date}")
            print(f"Director: {film.director}")
            print(f"Opening Crawl:\n{film.opening_crawl}\n")
