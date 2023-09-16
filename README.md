# TOME-API

This is a basic backend Flask API that allows users to easily retrieve DALL-E generated images. 

It allows user to make a GET request to the endpoint with their desired prompt, which sends the prompt to the "TOME" backend API along with additional details like headers, data, cookies(user-auth). 
The API processes the response, filters the required data, and returns the links in JSON format.

User does not need to make account on TOME and there is no need for buying additional credits. This process is automated for a particaular account for tessting purposes.

Potential use case is to make a dataset for fake/real image detection model training.

Currently deployed at : https://imggen.adhiraj.live

# Interaction

Pass in your image generation prompt as 'prompt' argument in GET request to /genimg endpoint.

# Example 

Request :

![image](https://user-images.githubusercontent.com/87516052/211926141-5bec72ee-1e45-43ef-bf6c-b77ffd866db4.png)

Result :

![image](https://user-images.githubusercontent.com/87516052/211926494-8642142b-5331-4467-bf7c-4359eadebf0f.png)

Actual Generated Image for example Prompt :

![image](https://user-images.githubusercontent.com/87516052/211926589-46327cda-5361-4c47-9e81-d63c91503653.png)


