import flet as ft

matches = ["juventus - inter", "real madrid - barcelone", "liverppol chelsea", "lyon - psg", "nantes - rennes"]


class MatchContainer(ft.Container):
    def __init__(self, match: str):
        super().__init__(
            width=400, height=50,
            border=ft.border.all(1, '#ebebeb'),
            border_radius=10,
            padding=ft.padding.only(left=10, right=10, top=3, bottom=3)
        )
        self.match = match
        self.match_name = ft.Text(self.match)
        self.check = ft.Checkbox(value=False, on_change=self.val_ceck)
        self.score_home = ft.TextField(
            height=30, width=50, dense=True, text_style=ft.TextStyle(size=12, color="black"),
            input_filter=ft.NumbersOnlyInputFilter(),
            content_padding=10, cursor_height=20
        )
        self.score_away = ft.TextField(
            height=30, width=50, dense=True, text_style=ft.TextStyle(size=12, color="black"),
            input_filter=ft.NumbersOnlyInputFilter(),
            content_padding=10, cursor_height=20
        )
        self.content = ft.Container(
            border=ft.border.only(left=ft.BorderSide(width=5, color="blue")),
            content=ft.Row(
                [
                    ft.VerticalDivider(width=10, color="transparent"),
                    self.check,
                    self.match_name,
                    ft.Row(
                        [
                            self.score_home,
                            ft.Text("-"),
                            self.score_away
                        ]
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

        )

    def val_ceck(self, e):
        self.score_away.disabled = True if self.check.value else False
        self.score_home.disabled = True if self.check.value else False
        self.score_away.update()
        self.score_home.update()


class ListeEnCoursPage(ft.UserControl):
    def __init__(self, page):
        super(ListeEnCoursPage, self).__init__()
        self.page = page
        self.ct = ft.Column(
            controls=[],
            spacing=2
        )
        self.remplir()
        self.button = ft.ElevatedButton("valider", color="white", bgcolor="blue", on_click=self.cliquer)

    def remplir(self):
        for match in matches:
            self.ct.controls.append(
                MatchContainer(match)
            )

    def cliquer(self, e):
        scores = []
        for widget in self.ct.controls[:]:
            match = widget.match_name.value
            home = widget.score_home.value
            away = widget.score_away.value
            dico = {
                "match": match,
                "home": home,
                "away": away
            }
            scores.append(dico)
        print(scores)

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    self.ct,
                    self.button
                ]
            )
        )


def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 850
    demo = DemoApp()
    page.add(demo)


if __name__ == '__main__':
    ft.app(target=main)
