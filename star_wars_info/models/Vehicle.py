
class Vehicle:

    def __init__(self):
        self.__name = ""

        self.__model = ""

        self.__vehicle_class = ""
        self.__manufacturer = ""
        self.__cost_in_credits = ""
        self.__length = ""
        self.__crew = ""
        self.__passengers = ""
        self.__max_atmosphering_speed = ""
        self.__cargo_capacity = ""
        self.__consumables = ""

        self.__films = []
        self.__pilots = []

        self.__url = ""
        self.__created = ""
        self.__edited = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_vehicle_class(self, vehicle_class):
        self.__vehicle_class = vehicle_class

    def get_vehicle_class(self):
        return self.__vehicle_class

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_manufacturer(self):
        return self.__manufacturer

    def set_cost_in_credits(self, cost_in_credits):
        self.__cost_in_credits = cost_in_credits

    def get_cost_in_credits(self):
        return self.__cost_in_credits

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_crew(self, crew):
        self.__crew = crew

    def get_crew(self):
        return self.__crew

    def set_passengers(self, passengers):
        self.__passengers = passengers

    def get_passengers(self):
        return self.__passengers

    def set_max_atmosphering_speed(self, max_atmosphering_speed):
        self.__max_atmosphering_speed = max_atmosphering_speed

    def get_max_atmosphering_speed(self):
        return self.__max_atmosphering_speed

    def set_cargo_capacity(self, cargo_capacity):
        self.__cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        return self.__cargo_capacity

    def set_consumables(self, consumables):
        self.__consumables = consumables

    def get_consumables(self):
        return self.__consumables

    def set_films(self, films):
        self.__films.extend(films)

    def get_films(self):
        return self.__films

    def set_pilots(self, pilots):
        self.__pilots.extend(pilots)

    def get_pilots(self):
        return self.__pilots

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
        return "Name: {0}, \n Model: {1}".format(self.get_name(), self.get_model())
