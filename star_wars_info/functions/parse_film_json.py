import os.path
import json
from models.Film import Film


def parse(request_id):
    path_to_file = os.path.abspath("json_requests/films_{0}.json".format(request_id))

    if not os.path.exists(path_to_file):
        print("Такой файл не найден")

    with open(path_to_file) as data_file:
        data = json.load(data_file)

    result = Film()

    result.set_title(data["title"])
    result.set_episode_id(data["episode_id"])
    result.set_opening_crawl(data["opening_crawl"])
    result.set_director(data["director"])
    result.set_producer(data["producer"])
    result.set_release_date(data["release_date"])
    result.set_species(data["species"])
    result.set_starships(data["starships"])
    result.set_vehicles(data["vehicles"])
    result.set_characters(data["characters"])
    result.set_planets(data["planets"])
    result.set_url(data["url"])
    result.set_created_date(data["created"])
    result.set_edited_date(data["edited"])

    return result
