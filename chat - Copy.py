import sys
import time
from pathlib import Path
from _thread import *
import threading
import openai
import matplotlib.pyplot as plt


def check_text_file(filenames):
    if not filenames:
        print("Error: No filenames provided")
        return

    # Use the filter function to create a new list of filenames that only contains
    # filenames with a ".txt" suffix
    text_files = filter(lambda x: Path(x).suffix == ".txt", filenames)

    # Check if the new list is empty
    if not text_files:
        print("Error: No text files found in filenames")
        return

    # Iterate over the list of text files
    for filename in text_files:
        print(f"\nFound text file: {filename}\n")
        return

def generate_response(line):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=line,
        max_tokens=2048,
        n=1,
        temperature=0.5
    )
    return response["choices"][0]["text"].strip()

def handle_chat(answers, line, i):
    response = generate_response(line)
    answers[i] = response

def write_to_file(questions, answers, output_file):
    for i in range(len(questions)):
        question_number = i+1
        response = answers[i]
        question = questions[i]
        # Use string formatting to create the output string
        output_string = "Question {question_number}:\n{question}\n\nAnswer:\n{response}\n\n----------------------------------------\n"
        output_string = output_string.format(question_number=question_number, question=question, response=response)

        # Write the output string to the output file
        output_file.write(output_string)


if __name__ == "__main__":
    start_time = time.time()

    filenames = sys.argv[1:]
    check_text_file(filenames)

    print("Working on it...")

    filename = filenames[0]
    api_key = "<insert-api-key>"
    openai.api_key = api_key

    input_filename = Path(filename).stem
    output_filename = input_filename + "_output.txt"

    # Open the input and output files
    with open(filename, "r") as input_file, open(output_filename, "w") as output_file:
        questions = [line.strip() for line in input_file if line.strip()]

        num_of_questions = len(questions)
        answers = [0]*num_of_questions
        for i in range(num_of_questions):
            line = questions[i]
            if line:
                t = threading.Thread(target=handle_chat, args=(answers, line, i), daemon=False)
                t.start()
                t.join()
        
        write_to_file(questions, answers, output_file)


    elapsed_time = time.time() - start_time
    print(f"\nElapsed time: {elapsed_time:.3f} seconds\n")