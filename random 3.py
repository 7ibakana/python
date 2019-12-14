# Import the request module Use
import requests
# The url of the API server with taco recipes
taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
# Make request to Api server, convert the json() response into a python dictionary
taco_recipe = requests.get(taco_url).json()
# Print the request from the dictionary
print(taco_recipe)
