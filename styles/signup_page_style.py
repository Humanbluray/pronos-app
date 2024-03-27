import flet as ft

login_style: dict = dict(
            height=50, width=250,
            dense=True, content_padding=12,
            cursor_height=20,
            prefix_icon=ft.icons.MAIL_OUTLINE,
            label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            label="email", text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            focused_border_color="#1a3da1",
            bgcolor="white",
            border_radius=3
)
passwd_style: dict = dict(
            height=50, width=250,
            dense=True, content_padding=12,
            cursor_height=20,
            prefix_icon=ft.icons.LOCK_OUTLINE,
            label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            label="password", text_style=ft.TextStyle(size=13, font_family="Poppins Medium"),
            focused_border_color="#1a3da1",
            bgcolor="white",
            border_radius=3,
            password=True, can_reveal_password=True,
            tooltip="au moins 6 caractères"
)
name_style: dict = dict(
            height=50, width=250,
            dense=True, content_padding=12,
            cursor_height=20,
            prefix_icon=ft.icons.MAIL_OUTLINE,
            label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            label="Votre nom de joueur", text_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            focused_border_color="#1a3da1",
            bgcolor="white",
            border_radius=3
)
confirm_pass_style: dict = dict(
            height=50, width=250,
            dense=True, content_padding=12,
            cursor_height=20,
            prefix_icon=ft.icons.LOCK_OUTLINE,
            label_style=ft.TextStyle(size=12, font_family="Poppins Medium"),
            label="Confirm password", text_style=ft.TextStyle(size=13, font_family="Poppins Medium"),
            focused_border_color="#1a3da1",
            bgcolor="white",
            border_radius=3,
            password=True, can_reveal_password=True
)
connect_button_style: dict = dict(
    height=50, width=250, bgcolor="#1a3da1",
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
    content=ft.Text("inscription", size=12, font_family="Poppins Regular",
                    color="white"),
    elevation=5,
)
facebook_button_style: dict = dict(
    height=50, width=250, bgcolor="#1a3da1",
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
    content=ft.Row(
        [
            ft.Icon(ft.icons.FACEBOOK_ROUNDED, color=ft.colors.WHITE, size=30),
            ft.Text("with facebook", size=14, font_family="Poppins Regular",
                    color="white"),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=5
    ),
    elevation=5,
)
