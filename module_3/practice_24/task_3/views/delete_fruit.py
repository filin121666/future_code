import flet as ft
from flet_route import Params,Basket
import requests

def delete_fruit_view(page:ft.Page,params:Params,basket:Basket):
    id = ft.TextField(label='Fruit id')
    
    def delete_fruit(e):
        resp = requests.post(url='http://127.0.0.1:5000/delete_fruit', json={'_id': id.value})
    
    submit = ft.ElevatedButton(text='Submit', on_click=delete_fruit)
    return ft.View(
        "/delete_fruit",
        controls=[
            id,
            ft.Row([
                submit,
                ft.ElevatedButton("Go back", on_click=lambda _: page.go("/")),
            ])
        ]
    )