class Film:
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

    def __str__(self):
        return f"Episode {self.episode_id}: {self.title} ({self.release_date})"
