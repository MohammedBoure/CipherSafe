import flet as ft
from pages.home import home_view 
from pages.add_account_view import  add_account_view
from pages.settings import  settings_view
from pages.login import login_view
from storage.config import theme



def main(page: ft.Page):
    page.title = "CaferSafe"
    page.window.width = 500
    page.window.height = 700
    
    page.theme_mode = ft.ThemeMode.LIGHT if theme == "light" else ft.ThemeMode.DARK


    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/add_account":
            page.views.append(add_account_view(page))
        elif page.route == "/settings":
            page.views.append(settings_view(page))
        elif page.route == "/login":
            page.views.append(login_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main,web_renderer="html")
