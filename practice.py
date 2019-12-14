# PIL to import Image, ImageFont, ImageDraw
from PIL import Image, ImageFont, ImageDraw
taco = Image.open('taco_img_unsplash.jpg') # Uses Pil to open the Image of the taco_img_unsplaish.jpg
''' Take the taco width,
the taco height,
and resize the into 800, by 800.'''
width = taco.width
height = taco.height
smaller_taco = taco.resize((800,800))
# Use the Draw from PIL to draw on the resized taco image
smaller_taco_draw =ImageDraw.Draw(smaller_taco)
''' The list of points are the coordinates of the top left corner X, and Y,
and the bottom right corner X and Y.'''
font = ImageFont.truetype('arial.ttf', 60)
# Draw text on the coordinates 80, 50 that says Random Taco Cookbook,
#Fill it with the color fuchsia, and the font type font.
smaller_taco_draw.text([80,150], 'Random Taco Cookbook', fill='Fuchsia', font=font)
smaller_taco.save('Random_Taco_Cookbook.jpg') # Save the new image as Random_Taco_Cookbook.jpg