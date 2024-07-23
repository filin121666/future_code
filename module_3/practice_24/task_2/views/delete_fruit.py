import flet as ft
from flet_route import Params,Basket

def delete_fruit_view(page:ft.Page,params:Params,basket:Basket):
    id = ft.TextField(label='Fruit id')
    submit = ft.ElevatedButton(text='Submit')
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