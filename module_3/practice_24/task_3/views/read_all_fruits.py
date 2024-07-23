import flet as ft
from flet_route import Params, Basket
import requests

def read_all_fruits_view(page: ft.Page, params: Params, basket: Basket):
    resp = requests.get(url='http://127.0.0.1:5000/get_all_fruits')
    data = resp.json()
    table = ft.DataTable(columns=[
        ft.DataColumn(ft.Text('Id')),
        ft.DataColumn(ft.Text('Name')),
        ft.DataColumn(ft.Text('Price'), numeric=True),
        ft.DataColumn(ft.Text('Text id for copy'))
    ],
        width=1000
    )
    for i in data:
        row = ft.DataRow(cells=[
            ft.DataCell(ft.Text(i['_id'])),
            ft.DataCell(ft.Text(i['name'])),
            ft.DataCell(ft.Text(i['price'])),
            ft.DataCell(ft.TextField(value=i['_id']))
        ])
        table.rows.append(row)

    return ft.View(
        "/read_all_fruits",
        controls=[
            table,
            ft.ElevatedButton("Go back", on_click=lambda _: page.go("/")),
        ]
    )
