
class Film:

    def __init__(self):
        self.__title = ""

        self.__episode_id = 0
        self.__opening_crawl = ""
        self.__director = ""
        self.__producer = ""
        self.__release_date = ""

        self.__species = []
        self.__starships = []
        self.__vehicles = []
        self.__characters = []
        self.__planets = []

        self.__url = ""
        self.__created = ""
        self.__edited = ""

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_episode_id(self, episode_id):
        self.__episode_id = episode_id

    def set_opening_crawl(self, opening_crawl):
        self.__opening_crawl = opening_crawl

    def get_opening_crawl(self):
        return self.__opening_crawl

    def set_director(self, director):
        self.__director = director

    def get_director(self):
        return self.__director

    def set_producer(self, producer):
        self.__producer = producer

    def get_producer(self):
        return self.__producer

    def set_release_date(self, release_date):
        self.__release_date = release_date

    def get_release_date(self):
        return self.__release_date

    def set_species(self, species):
        self.__species.extend(species)

    def get_species(self):
        return self.__species

    def set_starships(self, starships):
        self.__starships.extend(starships)

    def get_starships(self):
        return self.__starships

    def set_vehicles(self, vehicles):
        self.__vehicles.extend(vehicles)

    def get_vehicles(self):
        return self.__vehicles

    def set_characters(self, characters):
        self.__characters.extend(characters)

    def get_characters(self):
        return self.__characters

    def set_planets(self, planets):
        self.__planets.extend(planets)

    def get_planets(self):
        return self.__planets

    def set_url(self, url):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_created_date(self, created_date):
        self.__created = created_date

    def get_created_date(self):
        return self.__created

    def set_edited_date(self, edited_date):
        self.__edited = edited_date

    def get_edited_date(self):
        return self.__edited

    def __repr__(self):
        return "Film : {0}".format(self.get_title())