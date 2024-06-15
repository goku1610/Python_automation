import os
import google.generativeai as genai
import instructor
from pydantic import BaseModel

class StepModel(BaseModel):
    steps: list[str]

base_prompt = f"Whenever an SQL query returns a blank result, send an email via Gmail based on certain parameters. Whenever the user replies to the email, trigger a webhook to parse and insert gmail response data into the SQL table again now give me the automation steps to be feeded into trigger.dev"

def model_to_json(model_instance):
    """
       Converts a Pydantic model instance to a JSON string.
       Args:
           model_instance (YourModel): An instance of your Pydantic model.
       Returns:
           str: A JSON string representation of the model.
       """
    return model_instance.model_dump_json()

json_model = model_to_json(StepModel(steps=['step1','step2']))

optimized_prompt = base_prompt + f'.Please provide a response in a structured JSON format that matches the following model: {json_model}, do not give me explanation and use number bullets '
def gemini(a):

    genai.configure(api_key="AIzaSyBAOzHFjPoXhIo5HXR3KWMqE4K8KY8xrmQ")

    model = genai.GenerativeModel('gemini-1.5-pro')

    response = model.generate_content(a)

    return response.text

if __name__ == '__main__':
    automated_json = gemini(optimized_prompt)
    print(automated_json)

splitted = automated_json.split('```json')
list = []
final_splitted = splitted[1].split("```")
hello = final_splitted[0].replace("\n","")
list.append(hello.split("[")[1].split("]")[0])

list_FINAL = []
g = ""
for i in range(len(list[0].replace("    ",""))-1):
    g = g + list[0].replace("    ","")[i]
if __name__ == '__main__':
    automated_json = gemini(f"{list[0]} give me the python program for each numbered step independently")
    print(automated_json)
