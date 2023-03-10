from flask import Flask, request, jsonify
from helper import get_image

app = Flask(__name__)

@app.route('/')
def index():
    return (f'Hi, This is the index page of the DALL-E UNOFFICIAL TOME API. Use the /<YOUR_QUERY> endpoint to get the result.')

@app.route('/<promt>')
def hello(promt):
    images, tile_images, raw_images = get_image(promt)
    return jsonify(images = images, tile_images = tile_images, raw_images = raw_images)


if __name__ == '__main__':
    app.run()
