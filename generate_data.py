import numpy as np
import pandas as pd
import random
from determine_job import DetermineJob

job_determine = DetermineJob()

stat_ranges = {
    "HP": (1, 255),
    "Attack": (5, 190),
    "Defense": (5, 230),
    "Special-Attack": (10, 194),
    "Special-Defense": (20, 230),
    "Speed": (5, 200),
}

def generate_random_pokemon(amount):
    pokemon_data = []
    
    for _ in range(amount):
        stats = {stat: np.random.randint(low, high + 1) for stat, (low, high) in stat_ranges.items()}

        stats_values = [stats[key] for key in [keys for keys in stats]]
        jobs = job_determine.get_jobs_primary(stats_values)

        pokemon = {
            "HP": stats["HP"],
            "Attack": stats["Attack"],
            "Defense": stats["Defense"],
            "Special-Attack": stats["Special-Attack"],
            "Special-Defense": stats["Special-Defense"],
            "Speed": stats["Speed"],
            "Job": jobs
        }
        
        pokemon_data.append(pokemon)
        
    return pd.DataFrame(pokemon_data)
