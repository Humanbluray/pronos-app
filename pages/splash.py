import flet as ft


class Splash(ft.UserControl):
    def __init__(self, page):
        super(Splash, self).__init__()
        self.page = page
        self.logo = ft.Image(src="logos/splash.png", fit="cover")

    def build(self):
        return ft.Container(
            width=self.page.window_width,
            height=self.page.window_height,
            content=self.logo
        )
