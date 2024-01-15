This project aims to provide an accurate way to measure how "good" a Pokemon is. It uses the pokeapi.co API to get the data and then clean it through pandas. The project utilizes Numpy along with scikit-learn to provide "jobs" for Pokemons to create a better rating for them. The project also utilizes the chess algorithm to rate every single Pokemon.

The Project, to a large extent, was quite accurate; of course, it wasn't perfect in predicting what is the best Pokemon, but in general, it predicts which Pokemon generally are considered to be very strong.

It should be noted that the way this program handles the ELO is primarily through the Pokemon's stats, primary jobs, and secondary jobs, alongside their type advantages. It does not, however, consider movesets or abilities.

To Run the Program:

    -Simply Git Clone the Program into a coding space
    -Go into pokemon_rating.ipynb and hit Run All, assuming you are in a Jupyter Notebooks space
    -Once the program has run, you can scroll to the bottom and see that it will look exactly like my notebook

To Create Your Own More Optimized Elo:

    -Go into simulate.py and chance the multipliers, giving more weight to what you consider to be more important, alongside what multiplier number you think best
    -Another way to optimize would be to create a better way to simulate a round, similar to an actual Pokemon battle. This code just runs 1000 iterations and sees who is most likely to win and calculates the ELO based off that. 


THE DESCRIPTION OF EACH FILE IS DOWN BELOW:

-poke_db.xlsx has the parsed JSON info

-ratings.xlsx contains all the elo ratings of the pokemons, the stats elo is based only on their stats, the primary job is off their primary job and the secondary job elo is off their secondary jobs and finally the ELO is calculated through this formula:

    -ELO = STAT_ELO + 0.5(PRIMARY_JOB_ELO) + 0.5(SECONDARY_JOB_ELO/N) where N is the amount of secondary jobs

-type_advantages.xlsx has the info on type advantages

-determine_job.py determines the best-suited jobs for the Pokemon

-generate data utilizes numpy to quickly generate data to be utilized by scikit-learn to predict jobs for actual Pokemon

-handle_json.py is the test file to figure out how to handle the api and parse it

-poke_jobs.py is an enum to contain the poke jobs

-simulate.py is where the magic of ratings happens. This part is highly biased in the sense that I determined what stats are most important based on research

-pokemon_rating.ipynb is the main file. It utilizes all the methods to rate the pokemon

 
