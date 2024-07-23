import flet as ft
from flet_route import Routing, path
from views.home import home_view
from views.read_all_fruits import read_all_fruits_view
from views.create_fruit import create_fruit_view
from views.update_fruit import update_fruit_view
from views.delete_fruit import delete_fruit_view

def main(page: ft.Page):

    app_routes = [
        path(url="/", clear=True, view=home_view),
        path(url="/read_all_fruits", clear=False, view=read_all_fruits_view),
        path(url='/create_fruit', clear=False, view=create_fruit_view),
        path(url='/update_fruit', clear=False, view=update_fruit_view),
        path(url='/delete_fruit', clear=False, view=delete_fruit_view)
    ]

    Routing(
        page=page, 
        app_routes=app_routes, 
        )
    page.go(page.route)

ft.app(target=main, name='App', host='127.0.0.1', port=6000, view=ft.AppView.WEB_BROWSER)