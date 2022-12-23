import openai
import urllib.request
import argparse
import os
import sys


# Define the command-line arguments
parser = argparse.ArgumentParser(description="Enter two arguments: prompt and name")
parser.add_argument("-p", "--prompt", required=True, help="the prompt string for AI")
parser.add_argument("-n", "--name", required=True, help="the name of the file generated")


# Parse the command-line arguments
args = parser.parse_args()




# Set the API key for OpenAI
openai.api_key = "<insert-api-key>"

promptAI = args.prompt
imageName = args.name

# Generate an image using OpenAI
generated_image = openai.Image.create(
    model="image-alpha-001",
    prompt=promptAI
)

if generated_image is not None:
    # Save the generated image to a file
    # Use double quotes or concatenation to interpolate the promptAI variable
    image_url = generated_image['data'][0]['url']
    urllib.request.urlretrieve(image_url, "" + imageName + ".png")
else:
    "Could not create image."