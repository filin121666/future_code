import flet as ft
from flet_route import Params,Basket

def create_fruit_view(page:ft.Page,params:Params,basket:Basket):
    name = ft.TextField(label='Name of fruit')
    price = ft.TextField(label='Price of fruit')
    submit = ft.ElevatedButton(text='Submit')
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