import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

readData = ""

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

# get all the *.d.ts files in the directory
for filename in os.listdir('./'):
    if filename.endswith(".d.ts"):
        with open(filename, 'r') as file:
            readData = file.read()
            file.close()
            prompt = prompt = f"update the questions with new questions in the beside data and give me the output in json format => {readData}"
            response = model.generate_content(prompt)
            print(response.text + "\n")
            continue
    else:
        continue
    
# with open("Anger.d.ts", "r") as f:
#     readData = f.read()

# prompt = prompt = f"update the questions with new questions in the beside data and give me the output in json format => {readData}"

# response = model.generate_content(prompt)

# print(response.text)