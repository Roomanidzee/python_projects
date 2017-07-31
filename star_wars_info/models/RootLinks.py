
class RootLinks:

    def __init__(self):
        self.__base_link = "https://swapi.co/api"

        self.__films_link = "{0}/films".format(self.__base_link)
        self.__people_link = "{0}/people".format(self.__base_link)
        self.__planets_link = "{0}/planets".format(self.__base_link)
        self.__species_link = "{0}/species".format(self.__base_link)
        self.__starships_link = "{0}/starships".format(self.__base_link)
        self.__vehicles_link = "{0}/vehicles".format(self.__base_link)

    def get_films_link(self):
        return self.__films_link

    def get_people_link(self):
        return self.__people_link

    def get_planets_link(self):
        return self.__planets_link

    def get_species_link(self):
        return self.__species_link

    def get_starships_link(self):
        return self.__starships_link

    def get_vehicles_link(self):
        return self.__vehicles_link

    def __repr__(self):
        return "Films link: {0},\n People link: {1},\n Planets link: {2}, \n Species link: {3}, \n Starships link: " \
               "{4},\n Vehicles link: {5}".format(self.get_films_link(), self.get_people_link(),self.get_planets_link(),
                                                  self.get_species_link(), self.get_starships_link(),
                                                  self.get_vehicles_link())
