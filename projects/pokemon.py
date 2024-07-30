# import requests
# import json

# def getPokemon(id: int):
#     url = f'https://fakestoreapi.com/products/{id}/'
#     api_call = requests.get(url)
#     response = api_call.json()
#     title = response['title']
#     return title


# # getPokemon('20')

# def allProducts():
#     api_url = f'https://fakestoreapi.com/products/'
#     api_call = requests.get(api_url)
#     api_response = api_call.json()
#     return api_response

# all_in = allProducts()
# print(all_in)