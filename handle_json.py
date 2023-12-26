import json
import requests

def parse_json(url):
    response = requests.get(url)
    content = response.json()
    
    name = content['name']
    moveset = ', '.join([move['move']['name'] for move in content['moves']])
    types = ', '.join([p_type['type']['name'] for p_type in content['types']])
    stats = [stat['base_stat'] for stat in content['stats']]
    
    poke_info = {'NAME': name , 'TYPE': types, 'HP': stats[0], 'ATTACK': stats[1], 'DEFENSE': stats[2], 
                                'SPECIAL-ATTACK': stats[3], 'SPECIAL-DEFENSE': stats[4], 'SPEED': stats[5], 
                                'TOTAL': sum(stats), 'MOVESET': moveset}
    
    return poke_info

def main():
    print(parse_json('https://pokeapi.co/api/v2/pokemon/1/'))
    
main()