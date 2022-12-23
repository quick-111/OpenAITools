import openai
import urllib.request
import argparse
from PIL import Image

# Define the command-line arguments
parser = argparse.ArgumentParser(description="Check the size of two images")
parser.add_argument("-i", "--image1", required=True, help="the first image")
parser.add_argument("-n", "--name", required=True, help="the name of the file generated")


# Parse the command-line arguments
args = parser.parse_args()

# Set the API key for OpenAI
openai.api_key = "<insert-api-key>"

image1 = args.image1
imageName = args.name

print(image1)

generated_image = openai.Image.create_variation(
    image = open(image1, "rb"),
    n = 1,
    size = "1024x1024"
)

if generated_image is not None:
    # Save the generated image to a file
    # Use double quotes or concatenation to interpolate the promptAI variable
    image_url = generated_image['data'][0]['url']
    urllib.request.urlretrieve(image_url, imageName+".png")
else:
    "Could not create image."
