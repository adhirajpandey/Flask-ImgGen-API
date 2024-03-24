# TOME-API

This is a basic backend Flask API that allows users to easily retrieve DALL-E generated images. 

It allows user to make a GET request to the endpoint with their desired prompt, which sends the prompt to the "TOME" backend API along with additional details like headers, data, cookies(user-auth). 
The API processes the response, filters the required data, and returns the links in JSON format.

User does not need to make account on TOME and there is no need for buying additional credits. This process is automated for a particaular demo account for testing purposes.

Potential use case is to make a dataset for fake/real image detection model training.

Currently deployed at : https://imggen.adhirajpandey.me/

# Interaction

Pass in your image generation prompt as 'prompt' argument in GET request to /genimg endpoint.

# Example 

Request :

![request](https://github.com/adhirajpandey/Flask-ImgGen-API/assets/87516052/6b289b4b-319b-45af-9190-4b23b1ab05bc)


Result :

![response](https://github.com/adhirajpandey/Flask-ImgGen-API/assets/87516052/b9d6bfee-a43c-4e90-96cf-080b70bb41ab)


Actual Generated Image for example Prompt :

![image](https://github.com/adhirajpandey/Flask-ImgGen-API/assets/87516052/05467ac8-2920-4fd5-9a86-8565fdd94637)



## Disclaimer
This project is not affiliated with Tome or its services. It's an independent tool created for educational and personal use.
