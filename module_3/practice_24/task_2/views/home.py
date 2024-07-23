import flet as ft
from flet_route import Params, Basket

def home_view(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/",
        controls=[
            ft.ElevatedButton("Create fruit", on_click=lambda _: page.go("/create_fruit")),
            ft.ElevatedButton("Read all fruits", on_click=lambda _: page.go("/read_all_fruits")),
            ft.ElevatedButton("Update fruit", on_click=lambda _: page.go("/update_fruit")),
            ft.ElevatedButton("Delete fruit", on_click=lambda _: page.go("/delete_fruit"))
        ]
    )