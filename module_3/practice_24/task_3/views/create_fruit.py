import flet as ft
from flet_route import Params,Basket
import requests

def create_fruit_view(page:ft.Page,params:Params,basket:Basket):
    name = ft.TextField(label='Name of fruit')
    price = ft.TextField(label='Price of fruit')
    
    def create_fruit(e):
        resp = requests.post(url='http://127.0.0.1:5000/create_fruit', json={'name': name.value, 'price': int(price.value)})
    
    submit = ft.ElevatedButton(text='Submit', on_click=create_fruit)
    return ft.View(
        "/create_fruit",
        controls=[
            name,
            price,
            ft.Row([
                submit,
                ft.ElevatedButton("Go back", on_click=lambda _: page.go("/"))
            ])
        ]
    )