# OpenAITools
In this repository are few tools using OpenAI's API to automate study-guides and generate images.

The file chat.py takes in a text file as input, reads the file line by line (excluding empty lines), and returns an output.txt file that has both the questions and answers with some formatting. It also uses multiThreading to speed up the process.

How to use:
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 65 `api_key = "<insert-api-key>"`*
  2. Run the file in your terminal `python chat.py path/to/input.txt`
 
 
 ## imageGenerator.py
 The file imageGenerator.py takes a prompt as an input and outputs an image generated based on the prompt.
 
 How to use:
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 21 `openai.api_key = "<insert-api-key>"`*
  2. Run the file in your terminal. `python imageGenerator.py -p "Type prompt here" -n "NameOfNewFile"`

## imageVariation.py
The file imageVariation.py takes a square image as an input and outputs a similar variation of the image.

How to use:
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 16 `openai.api_key = "<insert-api-key>"`*
  2. Run the file in your terminal. `python imageVariation.py -i "path/to/image.png" -n "NameOfNewFile"


Please refer to OpenAI documentation for further instructions on how to make these API calls. https://beta.openai.com/docs/api-reference/introduction
  
  
