import numpy as np
import pandas as pd
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
    stats_array = np.column_stack([np.random.randint(low, high + 1, size=amount) for _, (low, high) in stat_ranges.items()])

    jobs = [job_determine.get_jobs_primary(stats) for stats in stats_array]

    pokemon_data = pd.DataFrame(stats_array, columns=stat_ranges.keys())
    pokemon_data['Job'] = jobs

    return pokemon_data

