# Import the request module Use
import requests
# The url of the API server with taco recipes
taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
# Make request to Api server, convert the json() response into a python dictionary
response = requests.get(taco_url).json()
# Print the request from the dictionary
print(response)
base_layer = response['base_layer']
