import os.path
import json
from models.Starship import Starship


def parse(request_id):
    path_to_file = os.path.abspath("json_requests/starships_{0}.json".format(request_id))

    if not os.path.exists(path_to_file):
        print("Такой файл не найден")

    with open(path_to_file) as data_file:
        data = json.load(data_file)

    result = Starship()

    result.set_name(data["name"])
    result.set_model(data["model"])
    result.set_starship_class(data["starship_class"])
    result.set_manufacturer(data["manufacturer"])
    result.set_cost_in_credits(data["cost_in_credits"])
    result.set_length(data["length"])
    result.set_crew(data["crew"])
    result.set_passengers(data["passengers"])
    result.set_max_atmosphering_speed(data["max_atmosphering_speed"])
    result.set_hyperdrive_rating(data["hyperdrive_rating"])
    result.set_mglt(data["MGLT"])
    result.set_cargo_capacity(data["cargo_capacity"])
    result.set_consumables(data["consumables"])
    result.set_films(data["films"])
    result.set_pilots(data["pilots"])
    result.set_url(data["url"])
    result.set_created_date(data["created"])
    result.set_edited_date(data["edited"])

    return result
