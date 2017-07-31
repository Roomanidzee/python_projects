
class Species:

    def __init__(self):
        self.__name = ""

        self.__classification = ""
        self.__designation = ""
        self.__average_height = ""
        self.__average_lifespan = ""
        self.__eye_colors = ""
        self.__hair_colors = ""
        self.__skin_colors = ""
        self.__language = ""
        self.__homeworld = ""

        self.__people = []
        self.__films = []

        self.__url = ""
        self.__created = ""
        self.__edited = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_classification(self, classification):
        self.__classification = classification

    def get_classification(self):
        return self.__classification

    def set_designation(self, designation):
        self.__designation = designation

    def get_designation(self):
        return self.__designation

    def set_average_height(self, average_height):
        self.__average_height = average_height

    def get_average_height(self):
        return self.__average_height

    def set_average_lifespan(self, average_lifespan):
        self.__average_lifespan = average_lifespan

    def get_average_lifespan(self):
        return self.__average_lifespan

    def set_eye_colors(self, eye_colors):
        self.__eye_colors = eye_colors

    def get_eye_colors(self):
        return self.__eye_colors

    def set_hair_colors(self, hair_colors):
        self.__hair_colors = hair_colors

    def get_hair_colors(self):
        return self.__hair_colors

    def set_skin_colors(self, skin_colors):
        self.__skin_colors = skin_colors

    def get_skin_colors(self):
        return self.__skin_colors

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language

    def set_homeworld(self, homeworld):
        self.__homeworld = homeworld

    def get_homeworld(self):
        return self.__homeworld

    def set_people(self, people):
        self.__people.extend(people)

    def get_people(self):
        return self.__people

    def set_films(self, films):
        self.__films.extend(films)

    def get_films(self):
        return self.__films

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
