import flet as ft
from flet_route import Params, Basket
import requests


def update_fruit_view(page: ft.Page, params: Params, basket: Basket):
    id = ft.TextField(label='Fruit id')
    name = ft.TextField(label='New name for fruit')
    price = ft.TextField(label='New price for fruit')

    def update_fruit(e):
        resp = requests.post(url='http://127.0.0.1:5000/update_fruit',
                             json={'_id': id.value, 'name': name.value, 'price': price.value})
        
    submit = ft.ElevatedButton(text='Submit', on_click=update_fruit)
    return ft.View(
        "/update_fruit",
        controls=[
            id,
            name,
            price,
            ft.Row([
                submit,
                ft.ElevatedButton("Go back", on_click=lambda _: page.go("/")),
            ])
        ]
    )
