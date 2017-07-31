
class People:

    def __init__(self):
        self.__name = ""

        self.__birth_year = ""
        self.__eye_color = ""
        self.__gender = ""
        self.__hair_color = ""
        self.__height = ""
        self.__mass = ""
        self.__skin_color = ""

        self.__homeworld = ""

        self.__films = []
        self.__species = []
        self.__starships = []
        self.__vehicles = []

        self.__url = ""
        self.__created = ""
        self.__edited = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_birth_year(self, birth_year):
        self.__birth_year = birth_year

    def get_birth_year(self):
        return self.__birth_year

    def set_eye_color(self, eye_color):
        self.__eye_color = eye_color

    def get_eye_color(self):
        return self.__eye_color

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_hair_color(self, hair_color):
        self.__hair_color = hair_color

    def get_hair_color(self):
        return self.__hair_color

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_mass(self, mass):
        self.__mass = mass

    def get_mass(self):
        return self.__mass

    def set_skin_color(self, skin_color):
        self.__skin_color = skin_color

    def get_skin_color(self):
        return self.__skin_color

    def set_homeworld(self, homeworld):
        self.__homeworld = homeworld

    def get_homeworld(self):
        return self.__homeworld

    def set_films(self, films):
        self.__films.extend(films)

    def get_films(self):
        return self.__films

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
        return "Name : {0}\n".format(self.get_name())
