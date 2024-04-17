import gradio as gr
import random
from gradio_client import Client
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

#demo.launch()


def random_response():
    return gr.ChatInterface( random.choice(["Yes", "No"])).launch()


import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# })









