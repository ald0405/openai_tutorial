import os
import openai
import json 
os.environ['SECRET_KEY'] = 'YOUR KEY' # get your own key at https://beta.openai.com
openai.api_key = os.getenv("SECRET_KEY")

prompt = 'how to parse a nested json in python'
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


openai_object_json = json.dumps(response,indent=4)
openai_object_data = json.loads(openai_object_json)
formatted_text = openai_object_data['choices'][0]['text']

print(f'\nThe prompt was:\n {prompt}\n')
print("--" * 25)
print(f'\nThe formatted response is :\n {formatted_text}\n')




