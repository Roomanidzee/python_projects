import os
import os.path
import json

import requests

from models.RootLinks import RootLinks

__links = RootLinks()

__links_type = {

    'films': __links.get_films_link(),
    'people': __links.get_people_link(),
    'planets': __links.get_planets_link(),
    'species': __links.get_species_link(),
    'starships': __links.get_starships_link(),
    'vehicles': __links.get_vehicles_link()

}


def make_request(request_type, request_id):
    request_string = "{0}/{1}".format(__links_type.get(request_type), request_id)

    header = requests.utils.default_headers()

    response = requests.get(request_string, headers=header)

    path_to_dir = os.path.abspath('json_requests')

    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)

    data = response.json()
    file_name = "{0}_{1}.json".format(request_type, request_id)

    path_to_file = os.path.join(path_to_dir, file_name)

    with open(path_to_file, 'w+') as f:
        json.dump(data, f)
"""
request_string = "{0}/{1}".format(__links_type.get('films'), 3)

header = requests.utils.default_headers()

response = requests.get(request_string,  headers=header)

print(response.content)
"""