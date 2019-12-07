# Import the request module from the url library
import requests
from PIL import Image
import docx
taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
taco_recipe = requests.get(taco_url).json()
print(taco_recipe)