### Importing Libraries

from flask import Flask, request, jsonify
from flask_cors import CORS

import openai

openai.api_type = "azure"
openai.api_base = "https://genai23-01.openai.azure.com/"
openai.api_key = "524e5269ea524937afde1488f7f9a769"
openai.api_version = "2023-05-15"

# Initializing flask app
app = Flask(__name__)
CORS(app)

def get_completion(prompt, model="gpt-model-03", temperature=0, max_tokens=500):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-model-03", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


@app.route('/questions', methods=['POST'])
def add_question():
    print("triggered!!!!!!!")
    data = request.get_json()
    question = data.get('question')
    print("Yes question arrived!!!", question)
    
    messages =  [
    {'role':'system', 'content':'you have only the knowledge of Stanford Encyclopedia of Philosophy.'},
    {'role':'assistant', 'content':question},
    {'role':'user', 'content':'I don\'t know'}  ]

    response = get_completion_from_messages(messages, temperature=0.3)
    print(response)

    # Here, you can process the question as needed
    response = {'answer': f'Answer: {response}'}
    return jsonify(response)


# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
