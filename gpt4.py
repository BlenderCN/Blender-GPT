import openai
import bpy

def get_api_key():
    preferences = bpy.context.preferences.addons[__name__.partition('.')[0]].preferences
    return preferences.api_key

def get_gpt4_response(prompt, max_tokens=250):
    openai.api_key = get_api_key()

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a Blender editor assistant.  You will respond to all requests by writing python code based on the user request.  Only respond with the raw python code and to not explain anything.  Do not include markdown formatting, do not include the word python at the start"},{"role": "user", "content": prompt}])
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
