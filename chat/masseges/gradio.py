import replicate
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

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# })
	
# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# })



from gradio_client import Client
def my_client(m):
    
    client = Client("https://a59785f42a47c8d0fe.gradio.live/")
    result = client.predict(input_text=m,api_name="/predict")

    print(result)
    
    return result
import os
os.environ["REPLICATE_API_TOKEN"] = "r8_aNF0YSKpHgcz35KKPccX3EId5mV8Mbp21VCGa"
def chatting(input:str):
    

    answer = replicate.run(
        "meta/llama-2-7b-chat",
        input={
            "top_p": 1,
            "prompt": input,
            "temperature": 0.2,
            "system_prompt":"""\
You are a helpful, respectful, and honest assistant designed to improve English language skills. Always provide accurate and helpful responses to language improvement tasks, while ensuring safety and ethical standards. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased, positive, and focused on enhancing language skills.

If a question does not make sense or is not factually coherent, explain why instead of answering something incorrect. If you don't know the answer to a question, please don't share false information.

Your role is to guide users through various language exercises and challenges, helping them to practice and improve their English skills in a fun and engaging way. Always encourage users to try different approaches and provide constructive feedback to help them progress.
answer in short sentences 
"""
            ,"max_new_tokens": 800,
            "repetition_penalty": 1
        },
    )

    output = ""
    for x in answer:
        output += x
        
    return output

# print(chatting(''))


