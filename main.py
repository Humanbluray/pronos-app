import flet as ft
from vues import view_handler
import time


def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 850
    page.fonts = {
        "Poppins Medium": "fonts/Poppins-Medium.ttf",
        "Poppins Regular": "fonts/Poppins-Regular.ttf",
        "Poppins Bold": "fonts/Poppins-Bold.ttf",
        "Poppins ExtraBold": "fonts/Poppins-ExtraBold.ttf",
        "Poppins Itlaic": "fonts/Poppins-Italic.ttf",
        "Poppins Light": "fonts/Poppins-Light.ttf",
        "Poppins SemiBold": "fonts/Poppins-SemiBold.ttf"
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            view_handler(page)[page.route]
        )

    page.on_route_change = route_change

    def launch():
        page.go('/')
        time.sleep(3)
        page.go('/connexion')

    launch()


if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
