import os.path
import json
from models.People import People


def parse(request_id):
    path_to_file = os.path.abspath("json_requests/people_{0}.json".format(request_id))

    if not os.path.exists(path_to_file):
        print("Такой файл не найден")

    with open(path_to_file) as data_file:
        data = json.load(data_file)

    result = People()

    result.set_name(data["name"])
    result.set_birth_year(data["birth_year"])
    result.set_eye_color(data["eye_color"])
    result.set_gender(data["gender"])
    result.set_hair_color(data["hair_color"])
    result.set_height(data["height"])
    result.set_mass(data["mass"])
    result.set_skin_color(data["skin_color"])
    result.set_homeworld(data["homeworld"])
    result.set_films(data["films"])
    result.set_species(data["species"])
    result.set_starships(data["starships"])
    result.set_vehicles(data["vehicles"])
    result.set_url(data["url"])
    result.set_created_date(data["created"])
    result.set_edited_date(data["edited"])

    return result
