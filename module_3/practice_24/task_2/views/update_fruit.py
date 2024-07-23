import flet as ft
from flet_route import Params,Basket

def update_fruit_view(page:ft.Page,params:Params,basket:Basket):
    id = ft.TextField(label='Fruit id')
    name = ft.TextField(label='New name for fruit')
    price = ft.TextField(label='New price for fruit')
    submit = ft.ElevatedButton(text='Submit')
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