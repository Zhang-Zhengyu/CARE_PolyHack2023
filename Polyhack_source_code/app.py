from flask import Flask, render_template, request, redirect, url_for
import os
import openai
import webbrowser
import threading

app = Flask(__name__)

def open_browser():
    webbrowser.open('http://localhost:5000/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a psychological counsellor and you are doing research on social media violence."},
            {"role": "system", "content": "The messages sent to you are the words of users in social media."},
            {"role": "system", "content": "You will need to recognise the language of these texts first and reply in the recognised language.）"},
            {"role": "system", "content": "Your response should contain two elements."},
            {"role": "system", "content": "The first element: whether the language contains elements of social media violence.The answer can only be one of YES/NO."},
            {"role": "system", "content": "The second element: If an element of social media violence is included, give suggestions to help the victim improve his or her psychological state."},
            {"role": "system", "content": "The format of your answer should be '[content of element one]: content of element two'. You need to answer in the language you recognise."},
            {"role": "system", "content": "You will need to recognise the language of these texts first and reply in the recognised language.）"},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content
    

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/output')
def output():
    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'r', encoding='utf-8') as f:
        output_text = f.read()
    return render_template('output.html', output_text=output_text)

if __name__ == '__main__':
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxx" # Please make sure you have obtained your OpenAI API Key and fill it in here.
    threading.Timer(1, open_browser).start()
    app.run(debug=True)