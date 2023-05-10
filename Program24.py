from pokemon.master import * # Import all functions and classes from the 'pokemon.master' module
import time # Import the 'time' module for time-related functions


poke_data = catch_em_all() # Fetch all available Pokemon data using the 'catch_em_all' function from the 'pokemon.master' module

i = 1 # Initialize a counter variable 'i' to 1
my_poke = {} # Create an empty dictionary 'my_poke' to store Pokemon names and their ASCII art representations
for key,value in poke_data.items(): # Iterate through each key-value pair in the 'poke_data' dictionary
    my_poke[value["name"].lower()] = value["ascii"] 
    i += 1
    if(i > 386): # If the counter variable 'i' is greater than 386, break the loop
        break

print(my_poke["pikachu"])  # Print the ASCII art of Charizard stored in the 'my_poke' dictionary, using the key "charizard"