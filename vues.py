import flet as ft
from pages.classement import PlayerView, CLassementGeneral
from pages.liste_en_cours import ListeEnCoursPage
from pages.connexion import LoginPage
from pages.signup import SignUpPage
from pages.splash import Splash


def view_handler(page):
    return {
        '/': ft.View(
            route='/',
            controls=[
                Splash(page)
            ]
        ),

        '/connexion': ft.View(
            route='/connexion',
            controls=[
                LoginPage(page)
            ]
        ),

        '/signup': ft.View(
            route="/signup",
            controls=[
                SignUpPage(page)
            ]
        ),

        '/sign in first': ft.View(
            route="/sign in first",
            controls=[
                FirstLogin(page)
            ]
        ),

        '/playerview': ft.View(
            route='/playerview',
            controls=[
                PlayerView(page)
            ]
        ),

        '/liste en cours': ft.View(
            route='/liste en cours',
            controls=[
                ListeEnCoursPage(page)
            ]
        ),

        '/classement general': ft.View(
            route='/classement general',
            controls=[
                CLassementGeneral(page)
            ]
        )
    }
