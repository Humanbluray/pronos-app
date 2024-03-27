import flet as ft
import backend
from pages.connexion import USER_EMAIL

player = ""
points = 0
rang = 0


class CLassementGeneral(ft.UserControl):
    def __init__(self, page):
        super(CLassementGeneral, self).__init__()
        self.page = page
        self.classement_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("pos", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("evo", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("player", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("pts", size=13, font_family="Poppins Bold")),
            ],
            rows=[]
        )
        self.container_table = ft.Container(
            expand=True, height=750, width=400,
            content=ft.Column([self.classement_table], expand=True, height=750, scroll="always")
        )
        self.list_name = ft.Dropdown(
            dense=True, height=40, width=130,
            border="underline",
            text_style=ft.TextStyle(size=12, font_family="Poppins Medium", color="black"),
            content_padding=12,
            on_change=self.on_change_list
        )
        self.list_number = ft.Text(visible=False)
        self.all = ft.ElevatedButton(on_click=self.back)
        self.infos = ft.Text("", size=11, color="grey", font_family="Poppins Regular")
        self.fill_table()
        self.load_options()

    def load_options(self):
        for data in backend.nom_listes():
            self.list_name.options.append(
                ft.dropdown.Option(data.upper())
        )

    def on_change_list(self, e):
        self.list_number.value = backend.id_liste_by_name(self.list_name.value.lower())
        self.list_number.update()

        for row in self.classement_table.rows[:]:
            self.classement_table.rows.remove(row)

        number = int(self.list_number.value)
        self.infos.value = f"CLASSEMENT A L'ISSUE DE LA LISTE {number}"
        self.infos.update()

        datas = backend.claseement_general(number)
        for data in datas:
            if data["evolution"] == "up":
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.KEYBOARD_ARROW_UP, color=ft.colors.GREEN_500, size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )
            elif data["evolution"] == "down":
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.KEYBOARD_ARROW_DOWN, color="red", size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )
            else:
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.REMOVE, color=ft.colors.GREY_400, size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )
            self.classement_table.update()

    def back(self, e):
        self.list_number.value = ""
        self.list_name.value = ""
        self.list_name.update()
        self.list_number.update()
        self.infos.value = f"CLASSEMENT A L'ISSUE DE LA LISTE {backend.max_liste()}"
        self.infos.update()

        self.fill_table()
        self.classement_table.update()

    def fill_table(self):
        for row in self.classement_table.rows[:]:
            self.classement_table.rows.remove(row)

        self.infos.value = f"CLASSEMENT A L'ISSUE DE LA LISTE {backend.max_liste()}"
        # self.infos.update()

        datas = backend.claseement_general(backend.max_liste())
        for data in datas:
            if data["evolution"] == "up":
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.KEYBOARD_ARROW_UP, color=ft.colors.GREEN_500, size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )
            elif data["evolution"] == "down":
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.KEYBOARD_ARROW_DOWN, color="red", size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )
            else:
                self.classement_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data['rang'], size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Icon(ft.icons.REMOVE, color=ft.colors.GREY_400, size=24)),
                            ft.DataCell(ft.Text(data['player'].upper(), size=12, font_family="Poppins Medium")),
                            ft.DataCell(ft.Text(data['points'], size=12, font_family="Poppins Medium")),
                        ], on_select_changed=lambda e: self.select_player(e.control.cells[2].content.value,
                                                                          e.control.cells[3].content.value,
                                                                          e.control.cells[0].content.value)
                    )
                )

    def select_player(self, e, f, g):
        global player, points, rang
        player = e.lower()
        points = f
        rang = g
        self.page.go('/playerview')

    def build(self):
        return ft.Container(
            padding=ft.padding.only(left=5, right=5),
            expand=True, height=750,
            content=ft.Column(
                [
                    ft.Container(
                        padding=ft.padding.only(left=5, right=5, top=5, bottom=5),
                        content=ft.Row(
                            [
                                ft.Row(
                                    [
                                        # ft.Image(src="logos/logo.png", height=50, width=50),
                                        ft.Text("BETCLUB", size=26, font_family="Poppins Bold")
                                    ], spacing=0
                                ),
                                ft.Row(
                                    [
                                        ft.IconButton(ft.icons.PERSON_OUTLINED),
                                        ft.IconButton(ft.icons.ANALYTICS_OUTLINED),
                                        ft.IconButton(ft.icons.LOGOUT),
                                    ], spacing=0
                                )
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ),
                    ft.Divider(height=5),
                    ft.Text("CLASSEMENT GENERAL", size=16, font_family="Poppins Bold", color=ft.colors.GREY_600),
                    ft.Divider(height=5),
                    ft.Row([self.list_name, self.list_number, self.all], alignment="spaceBetween"),
                    ft.Divider(height=2, color="transparent"),
                    self.infos,
                    ft.Divider(height=1),
                    self.container_table
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )


class PlayerView(ft.UserControl):
    def __init__(self, page):
        super(PlayerView, self).__init__()
        global player
        self.page = page
        self.listes = ft.Text("LISTES JOUEES", size=10, font_family="Poppins Medium", color="black")
        self.rep_listes = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.goal_average = ft.Text("GOAL AVERAGE", size=10, font_family="Poppins Medium", color="black")
        self.rep_goal_average = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.moyenne_points_liste = ft.Text("MOYENNE POINTS PAR LISTE", size=10, font_family="Poppins Medium", color="black")
        self.rep_moy_pts_liste = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.rang_actuel = ft.Text("RANG ACTUEL", size=10, font_family="Poppins Medium", color="black")
        self.rep_rang_actuel = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.points_actuels = ft.Text("POINTS ACTUELS", size=10, font_family="Poppins Medium", color="black")
        self.rep_pts_actu = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.moyenne_gen_liste = ft.Text("MOYENNE POINTS GENERAL PAR LISTE", size=10, font_family="Poppins Medium", color="black")
        self.rep_moy_gen_liste = ft.Text("", size=28, font_family="Poppins ExtraBold", color=ft.colors.TEAL_700)
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("liste", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("points", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("rang", size=13, font_family="Poppins Bold")),
                ft.DataColumn(ft.Text("pts gen", size=13, font_family="Poppins Bold"))
            ],
            rows=[]
        )
        self.ct_table = ft.Container(
            height=200, width=400, expand=True,
            content=ft.Column([self.table], height=200, expand=True, scroll="always")
        )
        self.reponses()

    def reponses(self):
        global player, points, rang
        if player == "" or points == 0 or rang == 0:
            pass
        else:
            player_id = backend.id_by_player_name(player)
            self.rep_listes.value = backend.nb_listes_by_player_id(player_id)
            self.rep_pts_actu.value = points
            self.rep_goal_average.value = backend.goal_average_by_player_id(player_id)
            self.rep_moy_pts_liste.value = f"{backend.moyenne_points_liste_by_player_id(player_id):.2f}"
            self.rep_moy_gen_liste.value = f"{points/backend.nb_listes_by_player_id(player_id):.2f}"
            self.rep_rang_actuel.value = rang

    def build(self):
        global player, points
        return ft.Container(
            padding=ft.padding.only(left=5, right=5),
            expand=True, height=750,
            content=ft.Column(
                [
                    ft.Container(
                        bgcolor="teal",
                        padding=ft.padding.all(10),
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    ft.icons.KEYBOARD_ARROW_LEFT,
                                    icon_size=30, icon_color="white",
                                    on_click=lambda e: self.page.go('/')
                                ),
                                ft.Text("PLAYER STATS", size=22, font_family="Poppins Bold")
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ),
                    ft.Divider(height=2, color="transparent"),
                    ft.Text(f"{player.upper()}", size=28, font_family="Poppins Bold", color=ft.colors.BLACK),
                    ft.Divider(height=2),
                    ft.Column([self.listes, self.rep_listes], spacing=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Column([self.goal_average, self.rep_goal_average], spacing=1,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Column([self.moyenne_points_liste, self.rep_moy_pts_liste], spacing=1,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Column([self.moyenne_gen_liste, self.rep_moy_gen_liste], spacing=1,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Column([self.points_actuels, self.rep_pts_actu], spacing=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                    ft.Column([self.rang_actuel, self.rep_rang_actuel], spacing=1,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=1),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

