import numpy as np
import pandas as pd

class EloAlgo():
    def simulate_round(self, pokemon_1, pokemon_2, move_adv_df, elo_col, p_elo1, p_elo2):
        wins = 0
        stats1 = pokemon_1['stats']
        stats2 = pokemon_2['stats']
        
        #if speed higher it has higher mlpt because faster otherwise lower mlpt
        #if advantage mlpt *1.2 and if disadvantage *0.8 and if nuetral *1
        multiplier = 1.3 if stats1[-1] > stats2[-1] else (1/1.3)
        print(multiplier)
        multiplier *= self.handle_type_advantages(pokemon_1['type'], pokemon_2['type'], move_adv_df)

        elo1 = round(pokemon_1[elo_col] * multiplier)
        elo2 = pokemon_2[elo_col]

        chance_win_p1 = self.calc_win_chance(elo1, elo2)  

        #adding a high random chance mlpt since there can be a major rng factor with critical hits
        rng_factor_1 = np.random.uniform(0, 0.05, 1000) + np.random.uniform(0.95, 1.05, 1000)
        rng_factor_2 = np.random.uniform(0, 0.05, 1000) + np.random.uniform(0.95, 1.05, 1000)
        
        wins = np.sum(np.random.rand(1000)*rng_factor_1 < chance_win_p1*rng_factor_2)
        print(wins, chance_win_p1)
        return self.update_elo(p_elo1, p_elo2, 1 if wins > 500 else 0)
    

    def handle_type_advantages(self, p_type1, p_type2, move_adv_df):
        type_combinations = [(t1.lower(), t2.lower()) for t1 in p_type1 for t2 in p_type2 if t1 and t2]
        multipliers = []
        adv_multiplier = 1.3
        
        #if weak to then 0.8 multiplier and if strong to then 1.2 otherwise base of 1
        for t1, t2 in type_combinations:
            if t2 in move_adv_df[t1].iloc[0]:  
                multipliers.append(1/adv_multiplier)
            elif t2 in move_adv_df[t1].iloc[1]:  
                multipliers.append(adv_multiplier)
            else:
                multipliers.append(1.0) 

        return np.prod(multipliers)

    def calc_win_chance(self, elo1, elo2):
        return 1 / (1 + 10 ** ((elo2 - elo1) / 400))

    def update_elo(self, elo1, elo2, result, k_factor=32):
        chance_p1_win = self.calc_win_chance(elo1, elo2)
        chance_p2_win = self.calc_win_chance(elo2, elo1)
 
        new_elo1 = elo1 + k_factor * (result - chance_p1_win)
        new_elo2 = elo2 + k_factor * ((1 - result) - chance_p2_win)

        return round(new_elo1), round(new_elo2)
    

def main():
    poke1 = {
            'index': 0,
            'name': 'bulba',
            'stats': [45,49,49,65,65,45],
            'type': ['poison', 'grass'],
            'ELO': 318
        }
    
    poke2 = {
            'index': 1,
            'name': 'charma',
            'stats': [39,52,43,60,50,65],
            'type': ['fire'],
            'ELO': 309
        }
    x = EloAlgo()
    df = pd.read_excel('excel_files/type_advantages.xlsx')
    
    new_elo1, new_elo2 = x.simulate_round(poke1, poke2, df, 'ELO', 1500, 1500)
    print(new_elo1, new_elo2)
    
        
if __name__ == "__main__":
    main()
