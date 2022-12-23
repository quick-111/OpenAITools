# OpenAITools
Created a few tools using OpenAI Api to automate study-guides and generate images

The file chat.py takes in a text file as input, reads the file line by line (excluding empty lines), and returns an output.txt file that has both the questions and answers with some formatting.
How to use chat.py:
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 65 `api_key = "<insert-api-key>"`*
  2. Run the file in your terminal `python chat.py path/to/input.txt`
 
 
 The file imageGenerator.py
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 21 `openai.api_key = "<insert-api-key>"`*
  2. Run the file in your terminal. `python imageGenerator.py -p "Type prompt here" -n "NameOfNewFile"`

The file imageVariation.py
  1. Insert your own Api Key from the OpenAi API. *This can be found on line 16 `openai.api_key = "<insert-api-key>"`*
  2. Run the file in your terminal. `python imageVariation.py -i "path/to/image.png" -n "NameOfNewFile"
  
  
