import json
import requests

def parse_json(url, isInfo):
    response = requests.get(url)
    content = response.json()
    
    if isInfo:
        name = content['name']
        moveset = ', '.join([move['move']['name'] for move in content['moves']])
        types = ', '.join([p_type['type']['name'] for p_type in content['types']])
        stats = [stat['base_stat'] for stat in content['stats']]
        
        poke_info = {'NAME': name , 'TYPE': types, 'HP': stats[0], 'ATTACK': stats[1], 'DEFENSE': stats[2], 
                                    'SPECIAL-ATTACK': stats[3], 'SPECIAL-DEFENSE': stats[4], 'SPEED': stats[5], 
                                    'TOTAL': sum(stats), 'MOVESET': moveset}
    else:
        p_type_name = content['name']
        poke_info = {p_type_name: {relation: [name['name'] for name in content['damage_relations'][relation]] 
                                   for relation in content['damage_relations']}}
        
    return poke_info

def main():
    print(parse_json('https://pokeapi.co/api/v2/pokemon/1/'))
    
main()