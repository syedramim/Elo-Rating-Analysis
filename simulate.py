import random
import pandas as pd

def simulate_round(pokemon_1, pokemon_2, move_adv_df):
    wins = 0
    stats1 = pokemon_1['stats']
    stats2 = pokemon_2['stats']
    
    #if speed higher it has higher mlpt because faster otherwise lower mlpt
    multiplier = 1.2 if stats1[len(stats1)-1] < stats2[len(stats2)-1] else 0.8
    
    multiplier *= handle_type_advantages(pokemon_1['type'], pokemon_2['type'], move_adv_df)
    
    elo1 = pokemon_1['Primary ELO'] * multiplier
    elo2 = pokemon_1['Primary ELO']
    
    chance_win_p1 = elo1 / (elo1+elo2)
    
    for i in range(100):
        if coin_toss(chance_win_p1): 
            wins += 1
        
    new_ratings = update_elo((elo1/multiplier), elo2, 1) if wins >= 50 else update_elo((elo1/multiplier), elo2, 0)

    return new_ratings
    

def handle_type_advantages(p_type1, p_type2, move_adv_df):
    multiplier = 1

    filtered_p_type1 = [t1.lower() for t1 in p_type1 if t1]
    filtered_p_type2 = [t2.lower() for t2 in p_type2 if t2]

    for pt1 in filtered_p_type1:
        for pt2 in filtered_p_type2:
            if pt2 in move_adv_df[pt1][0]:
                multiplier *= 0.8
            elif pt2 in move_adv_df[pt1][1]:
                multiplier *= 1.2

    return multiplier

def coin_toss(chance):
    return (random.random() + rng_factor()) < (chance + rng_factor())

def rng_factor():
    variance = random.uniform(0.00, 0.05)
    rng_factor = random.uniform(0.0001, 0.1)
    
    return variance + rng_factor

def calc_win_chance(elo1, elo2):
    return 1 / (1 + 10 ** ((elo2 - elo1) / 400))

def update_elo(elo1, elo2, result, k_factor=10):
    chance_p1_win = calc_win_chance(elo1, elo2)
    chance_p2_win = calc_win_chance(elo2, elo1)

    new_elo1 = elo1 + k_factor * (result - chance_p1_win)
    new_elo2 = elo2 + k_factor * ((1 - result) - chance_p2_win)

    return max(new_elo1, 100), max(new_elo2,100)
    
