import flet as ft


def settings_view(page):
        return ft.View(
            route="/settings",
            controls=[
                ft.Text("Settings Page", size=30),
                ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/")),
            ],
        )