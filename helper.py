import requests
import json
import os


def get_image(promt):

    url = "https://backend.tome.app/"

    data_dict = {
    "operationName": "GENERATE_IMAGES_MUTATION",
    "variables": {
        "prompt": promt,
        "tileId": "clcpit8xq1rz53a81cw2a77fy",
        "tomeId": "clcpissn208pf813av9ffc6mq"
    },
    "query": "mutation GENERATE_IMAGES_MUTATION($prompt: String!, $tileId: String!, $tomeId: String!) {\n  generateImages(prompt: $prompt, tileId: $tileId, tomeId: $tomeId) {\n    id\n    images {\n      imagePath\n      imageUrlTile\n      imageUrlPreview\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    payload = json.dumps(data_dict)

    headers = {
    'Host': 'backend.tome.app',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://tome.app',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://tome.app/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': os.environ.get("TOME_COOKIE")
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    imagedata = (response.json()["data"]["generateImages"]["images"])

    images = []

    for i in imagedata:
        images.append(i["imageUrlTile"])

    tile_images = [x.replace("1024", "300") for x in images]

    raw_images = [x[:x.index('?')] for x in images]


    return images, tile_images, raw_images

