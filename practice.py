# Import the request module from the url library
import requests
from PIL import Image, ImageFont, ImageDraw
import docx
taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
taco_recipe = requests.get(taco_url).json()
print(taco_recipe)
taco = Image.open('taco_img_unsplash.jpg')
width = taco.width
height = taco.height
smaller_taco = taco.resize((800,800))
smaller_taco_draw =ImageDraw.Draw(smaller_taco)
# The list of points are the coordinates of the top left corner X, and Y,
# and the bottom right corner X and Y.
font = ImageFont.truetype('arial.ttf', 60)
smaller_taco_draw.text([80,150], 'Random Taco Cookbook', fill='Fuchsia', font=font)
smaller_taco.save('Random_Taco_Cookbook.jpg')