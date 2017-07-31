import os.path
import json
from models.Planet import Planet


def parse(request_id):
    path_to_file = os.path.abspath("json_requests/planets_{0}.json".format(request_id))

    if not os.path.exists(path_to_file):
        print("Такой файл не найден")

    with open(path_to_file) as data_file:
        data = json.load(data_file)

    result = Planet()

    result.set_name(data["name"])
    result.set_diameter(data["diameter"])
    result.set_rotation_period(data["rotation_period"])
    result.set_orbital_period(data["orbital_period"])
    result.set_gravity(data["gravity"])
    result.set_population(data["population"])
    result.set_climate(data["climate"])
    result.set_terrain(data["terrain"])
    result.set_surface_water(data["surface_water"])
    result.set_residents(data["residents"])
    result.set_films(data["films"])
    result.set_url(data["url"])
    result.set_created_date(data["created"])
    result.set_edited_date(data["edited"])

    return result
