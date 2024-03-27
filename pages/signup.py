from dotenv import load_dotenv
import os
from supabase import create_client
from styles.signup_page_style import *
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

USERNAME: str = ""
PLAYER_NAME: str = ""


class SignUpPage(ft.UserControl):
    def __init__(self, page):
        super(SignUpPage, self).__init__()
        self.page = page

        # widgets
        self.entete = ft.Text("Sign up", size=36, font_family="Poppins Bold")
        self.login = ft.TextField(
            **login_style
        )
        self.passwd = ft.TextField(**passwd_style, )
        self.confirm = ft.TextField(**confirm_pass_style, on_change=self.change_password)
        self.name = ft.TextField(**name_style)
        self.inscrip_button = ft.ElevatedButton(**connect_button_style, on_click=self.auth_with_password)
        self.facebook_button = ft.ElevatedButton(**facebook_button_style)

        self.title_alert = ft.Text("", size=18, font_family="Poppins SemiBold")
        self.text_alert = ft.Text("", size=12, font_family="Poppins Medium")

        self.alert_window = ft.AlertDialog(
            title=self.title_alert,
            content=self.text_alert,
            actions=[
                ft.TextButton(
                    content=ft.Text("Fermer", size=16, font_family="Poppins Regular", color="#1a3da1"),
                    height=50,
                    on_click=self.close_alert_window)
            ]
        )

    def close_alert_window(self, e):
        self.alert_window.open = False
        self.alert_window.update()

    def change_password(self, e):
        if self.confirm.value == self.passwd.value:
            self.passwd.border_color = "green"
            self.confirm.border_color = "green"
            self.passwd.update()
            self.confirm.update()
        else:
            self.passwd.border_color = ft.colors.BLACK45
            self.confirm.border_color = ft.colors.BLACK45
            self.passwd.update()
            self.confirm.update()

    def auth_with_password(self, e):
        global PLAYER_NAME
        email = self.login.value
        password = self.passwd.value
        if self.confirm.value == self.passwd.value:

            try:
                supabase.auth.sign_up({'email': email, 'password': password})
                self.text_alert.value = f"un email de confirmation a été envoyé\n à l'adresse {email}"
                self.title_alert.value = "Confirmation"
                self.text_alert.update()
                self.title_alert.update()
                self.alert_window.open = True
                self.alert_window.update()


            except Exception as ex:
                self.text_alert.value = f"{ex}"
                self.title_alert.value = "Erreur"
                self.text_alert.update()
                self.title_alert.update()
                self.alert_window.open = True
                self.alert_window.update()

        else:
            self.text_alert.value = "les mots de passe ne correspondent pas"
            self.title_alert.value = "erreur"
            self.text_alert.update()
            self.title_alert.update()
            self.alert_window.open = True
            self.alert_window.update()

    def build(self):
        return ft.Container(
            padding=ft.padding.only(top=100),
            content=ft.Column(
                [
                    ft.Divider(height=10, color="transparent"),
                    self.entete,
                    ft.Divider(height=10, color="transparent"),
                    ft.Container(
                        border=ft.border.all(1, "#ebebeb"),
                        border_radius=10,
                        padding=15,
                        content=ft.Column(
                            [
                                self.login,
                                self.passwd,
                                self.confirm,
                                self.name,
                                self.inscrip_button,
                                self.facebook_button

                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ),
                    ft.Container(
                        border_radius=10,
                        padding=ft.padding.only(left=32),
                        content=ft.Row(
                            [
                                ft.TextButton(
                                    on_click=lambda e: self.page.go('/connexion'),
                                    content=ft.Text(
                                        "Tu as déja un compte ?", size=12,
                                        font_family="Poppins medium",
                                        color="#1a3da1"
                                    )
                                )
                            ], alignment="start",
                        )
                    ),
                    self.alert_window
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
