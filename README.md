-This projects aims to provide an accurate way to measure how "good" a pokemon is
	-It uses the pokeapi.co API to get the data and then cleans it through pandas
	-The project utilizes Numpy alongisde scikit-learn to provide "jobs" for pokemons to create a better rating for them
	-The project also utilizes the chess algorithm to rate every single pokemon

	-poke_db.xlsx has the parsed json info
	-type_advantages.xlsx has the info on type advantages
	-determine_job.py determines the best suited jobs for the pokemons
	-generate data utilizes numpy to quickly generate data to be utilized by scikit-learn to predict jobs for actual pokemon
	-handle_json.py is the test file to figure out handling the api and parse it
	-poke_jobs.py is an enum to contain the poke jobs
	-simulate.py is where the magic of ratings happen, this part is highly biased in the sense that I determined what stats are most important based off research
	-pokemon_rating.ipynb is the main file, it utilizes all the methods to rate the pokemon

	==NOTE, the project is done in the sense that it rates them based solely off stats but I plan to make it much more complex==
 
