import openai
import json
from base64 import b64decode

prompt = input("The promt: ")
openai.api_key = "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"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256',
    response_format='b64_json'
)

with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(prompt.split(' '))

with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)
