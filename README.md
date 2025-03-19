# ELO Rating

This project aims to provide an accurate way to measure how "good" a Pokemon is. It uses the pokeapi.co API to get data and then processes it using Pandas. The project utilizes Numpy along with Scikit-Learn to assign "jobs" for Pokemon to create a better rating system. It also uses a chess algorithm to rank each Pokemon.

## Overview

The project aims to predict which Pokemon are generally considered strong based on their stats, primary jobs, secondary jobs, and type advantages assigned using machine learning scikit-learn. The ELO rating system is used to achieve this.

## Features

- **Data Extraction and Cleaning**: Uses the pokeapi.co API.
- **Job Assignment**: Assigns jobs to Pokemon based on their stats.
- **ELO Rating System**: Rates Pokemon using a modified ELO rating algorithm.
- **Simulations**: Runs simulations to determine the best Pokemon.

## Files

- **poke_db.xlsx**: Contains parsed JSON data.
- **ratings.xlsx**: Contains ELO ratings of the Pokemon.
- **type_advantages.xlsx**: Information on type advantages.
- **determine_job.py**: Determines the best-suited jobs for the Pokemon.
- **generate_data.py**: Generates data for job prediction.
- **handle_json.py**: Handles API data parsing.
- **poke_jobs.py**: Enum for Pokemon jobs.
- **simulate.py**: Main simulation and rating script.
- **pokemon_rating.ipynb**: Main Jupyter Notebook for running the project.

## Running the Project

1. **Clone the Repository**:
    ```bash
   https://github.com/syedramim/Elo-Rating-Analysis.git
    ```
2. **Run the Jupyter Notebook**:
    - Open `pokemon_rating.ipynb` and run all cells.

## Optimizing ELO Ratings

- Modify `simulate.py` to adjust multipliers and weights.
- Create better simulation methods to mimic actual Pokemon battles.

