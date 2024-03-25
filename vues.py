import flet as ft
from pronos import DemoApp, PlayerView


def view_handler(page):
    return {
        '/': ft.View(
            route="/",
            controls=[
                DemoApp(page)
            ]
        ),
        '/playerview': ft.View(
            route='/playerview',
            controls=[
                PlayerView(page)
            ]
        )
    }
