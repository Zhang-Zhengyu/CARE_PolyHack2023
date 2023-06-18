import subprocess
import os

print("Welcome")
print("© Forward Roll in Polyhack 2023")
print("A python required environment check is in progress.")
os.system(f'pip install {"flask"}')
os.system(f'pip install {"openai"}')
os.system(f'pip install {"pdfplumber"}')
os.system(f'pip install {"re"}')
os.system(f'pip install {"webbrowser"}')
os.system(f'pip install {"threading"}')
os.system(f'pip install {"webdriver"}')
os.system(f'pip install {"selenium"}')
print("The environment has been successfully initialised and is about to start running.")

subprocess.Popen(['python', 'app.py'])