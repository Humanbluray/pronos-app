from dotenv import load_dotenv
import os
from supabase import create_client
from styles.login_page_style import *
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

USER_EMAIL: str = ""


class LoginPage(ft.UserControl):
    def __init__(self, page):
        super(LoginPage, self).__init__()
        self.page = page
        self.logo = ft.Image(src="logos/logo.png", height=100, width=100)

        # widgets
        self.entete = ft.Text("Login", size=36, font_family="Poppins Bold")
        self.login = ft.TextField(
            **login_style
        )
        self.passwd = ft.TextField(
            **passwd_style
        )
        self.connect_button = ft.ElevatedButton(**connect_button_style, on_click=self.get_login)
        self.error_window = ft.AlertDialog(
            title=ft.Text("Erreur", size=18, font_family="Poppins SemiBold"),
            content=ft.Text(
                f"Identifants incorrects \nSi vous n'avez pas encore de compte cliquez plus bas",
                size=14, font_family="Poppins Medium"
                ),
            actions=[
                ft.TextButton(
                    content=ft.Text("Fermer", size=16, font_family="Poppins Regular", color="#1a3da1"),
                    height=50,
                    on_click=self.close_error_window)
            ]
        )

    def close_error_window(self, e):
        self.error_window.open = False
        self.error_window.update()

    def get_login(self, e):
        user_email = self.login.value
        user_password = self.passwd.value
        error = ""
        try:
            session = supabase.auth.sign_in_with_password({"email": user_email, "password": user_password})
            print(session.user.email)
        except Exception as ex:
            error = str(ex)

        if error != "":
            self.error_window.open = True
            self.error_window.update()
        else:
            self.page.go('/classement general')

    def build(self):
        return ft.Container(
            padding=ft.padding.only(top=100),
            content=ft.Column(
                [
                    ft.Divider(height=10, color="transparent"),
                    self.entete,
                    ft.Divider(height=10, color="transparent"),
                    ft.Container(
                        padding=ft.padding.only(left=45),
                        content=ft.Row(
                            [
                                ft.Text("USER ACCOUNT", size=11, font_family="Poppins Medium", color=ft.colors.GREY_500)
                            ], alignment=ft.MainAxisAlignment.START
                        )
                    ),
                    ft.Container(
                        border=ft.border.all(1, "#ebebeb"),
                        border_radius=10,
                        padding=15,
                        content=ft.Column(
                            [self.login, self.passwd, self.connect_button],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=32),
                        content=ft.Row(
                            [
                                ft.TextButton(
                                    on_click=lambda e: self.page.go('/signup'),
                                    content=ft.Text(
                                        "Doesn't have an account?", size=12,
                                        font_family="Poppins medium",
                                        color="#1a3da1"
                                    )
                                )
                            ], alignment="start",
                        )
                    ),
                    self.error_window
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

