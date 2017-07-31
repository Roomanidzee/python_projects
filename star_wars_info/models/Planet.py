
class Planet:

    def __init__(self):
        self.__name = ""

        self.__diameter = ""
        self.__rotation_period = ""
        self.__orbital_period = ""
        self.__gravity = ""
        self.__population = ""
        self.__climate = ""
        self.__terrain = ""
        self.__surface_water = ""

        self.__residents = []
        self.__films = []

        self.__url = ""
        self.__created = ""
        self.__edited = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_diameter(self, diameter):
        self.__diameter = diameter

    def get_diameter(self):
        return self.__diameter

    def set_rotation_period(self, rotation_period):
        self.__rotation_period = rotation_period

    def get_rotation_period(self):
        return self.__rotation_period

    def set_orbital_period(self, orbital_period):
        self.__orbital_period = orbital_period

    def get_orbital_period(self):
        return self.__orbital_period

    def set_gravity(self, gravity):
        self.__gravity = gravity

    def get_gravity(self):
        return self.__gravity

    def set_population(self, population):
        self.__population = population

    def get_population(self):
        return self.__population

    def set_climate(self, climate):
        self.__climate = climate

    def get_climate(self):
        return self.__climate

    def set_terrain(self, terrain):
        self.__terrain = terrain

    def get_terrain(self):
        return self.__terrain

    def set_surface_water(self, surface_water):
        self.__surface_water = surface_water

    def get_surface_water(self):
        return self.__surface_water

    def set_residents(self, residents):
        self.__residents.extend(residents)

    def get_residents(self):
        return self.__residents

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
