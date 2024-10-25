import os

import sentencex

# from sentencex import segment

home_dir = os.path.expanduser("~")
subtitles_dir = os.path.join(home_dir, "subtitles")
input_file = os.path.join(subtitles_dir, "iss.txt")
# text = """
# The James Webb Space Telescope (JWST) is a space telescope specifically designed to conduct infrared astronomy. The U.S. National Aeronautics and Space Administration (NASA) led Webb's design and development")
# """
# print(list(segment("en", text)))

# # Define the path to the input and output files
# home_dir = os.path.expanduser("~")
# subtitles_dir = os.path.join(home_dir, "subtitles")
# input_file = os.path.join(subtitles_dir, "iss.txt")
# output_file = os.path.join(subtitles_dir, "segmented.txt")
# 
# # Read the content from the input file
# try:
#     with open(input_file, 'r', encoding='utf-8') as f:
#         content = f.read()
#         segmented_list = list(segment("en", content))
#         for i in segmented_list:
#             with open(output_file, 'a', encoding='utf-8') as fb:
#                 fb.write(i)
# 
# 
#     print(f"Content from '{input_file}' has been successfully written to '{output_file}'.")
# except FileNotFoundError:
#     print(f"Error: The file '{input_file}' was not found.")
# except IOError as e:
#     print(f"An error occurred while processing the files: {str(e)}")



# Read the content from the input file
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(list(sentencex.segment("en", content)))

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except IOError as e:
    print(f"An error occurred while processing the files: {str(e)}")
