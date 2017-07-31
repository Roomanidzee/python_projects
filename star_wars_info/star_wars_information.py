from functions import (parse_film_json, parse_people_json, parse_planet_json, parse_species_json, parse_starship_json,
                       parse_vehicle_json, make_request_to_api)


def assemble(f, x):
    return f(x)

parse_types = {

    'films': parse_film_json.parse,
    'people': parse_people_json.parse,
    'planets': parse_planet_json.parse,
    'species': parse_species_json.parse,
    'starships': parse_starship_json.parse,
    'vehicles': parse_vehicle_json.parse

}

print("Привет, друг!")
print()

request_type = input("Введите тип запроса: ")
print()

request_id = input("Введите id нужной темы: ")
print()

make_request_to_api.make_request(request_type, str(request_id))

result = assemble(parse_types.get(request_type), str(request_id))

print(result)