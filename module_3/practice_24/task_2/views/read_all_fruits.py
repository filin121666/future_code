import flet as ft
from flet_route import Params, Basket

def read_all_fruits_view(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/read_all_fruits",
        controls=[
            ft.ElevatedButton("Go back", on_click=lambda _: page.go("/")),
        ]
    )