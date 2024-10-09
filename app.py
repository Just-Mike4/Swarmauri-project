from flask import Flask, jsonify
import gradio as gr
from Swarmauri import demo

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify(message='Gradio app is running at /gradio'), 200

app = gr.mount_gradio_app(app, demo, path='/gradio')