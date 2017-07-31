import os.path
import json
from models.Species import Species


def parse(request_id):
    path_to_file = os.path.abspath("json_requests/species_{0}.json".format(request_id))

    if not os.path.exists(path_to_file):
        print("Такой файл не найден")

    with open(path_to_file) as data_file:
        data = json.load(data_file)

    result = Species()

    result.set_name(data["name"])
    result.set_classification(data["classification"])
    result.set_designation(data["designation"])
    result.set_average_height(data["average_height"])
    result.set_average_lifespan(data["average_lifespan"])
    result.set_eye_colors(data["eye_colors"])
    result.set_hair_colors(data["hair_colors"])
    result.set_skin_colors(data["skin_colors"])
    result.set_language(data["language"])
    result.set_homeworld(data["homeworld"])
    result.set_people(data["people"])
    result.set_films(data["films"])
    result.set_url(data["url"])
    result.set_created_date(data["created"])
    result.set_edited_date(data["edited"])

    return result
