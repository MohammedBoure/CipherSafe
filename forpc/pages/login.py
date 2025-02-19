import flet as ft
from pages.home import theme_app
from utils.Encryption import simple_hash_256
import os

def login_view(page):
    top_image = ft.Image(src="assets/1.gif",
                         width=200, height=200)
    
    key_field = ft.TextField(
        hint_text="Enter your code",
        color=theme_app["text_color"],
        password=True,
        text_align=ft.TextAlign.CENTER,
        height=40,
        can_reveal_password=True,
        cursor_color=theme_app["input_cursor_color"],
        selection_color=theme_app["input_selection_color"],
        border_color=theme_app["input_border_color"],
        fill_color=theme_app["input_fill_color"],
        hover_color=theme_app["input_hover_color"]
    )

    key_field_container = ft.Container(
        content=key_field,
        width=280,
        padding=10,
        bgcolor=ft.Colors.TRANSPARENT,
        border_radius=8
    )

    toggle_password_button = ft.IconButton(
        icon=ft.Icons.VISIBILITY,
        icon_color=theme_app["text_color"],
        on_click=lambda e: key_field.update(password=not key_field.password)
    )

    key_field_row = ft.Row(
        controls=[key_field_container, toggle_password_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    def on_submit(e):
        password = key_field.value
        if password and os.path.exists("storage/key"):
            with open("storage/key",'rb') as file:
                key = file.read()
                
            if simple_hash_256(password) == key:
                page.go("/")
        elif password and not os.path.exists("storage/key"): 
            with open("storage/key", "wb") as file:
                file.write(simple_hash_256(password))
            page.go("/")
                    

    submit = ft.ElevatedButton(
        "Enter",
        height=50,
        width=280,
        on_click=lambda e: on_submit(e),
        bgcolor=theme_app["button_bg_color"],
        color=theme_app["button_text_color"],
        elevation=5,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=theme_app["button_border_radius"])
        )
    )
    
    
    if os.path.exists("storage/key"):
        text = ft.Text("أدخل رمز المرور",size=12,color="red",rtl=True)
    else:
        text = ft.Text("هدا الكود هو المسؤول عن عمليات التشفير\nيفضل وضعه بعناية",size=12,color="red",rtl=True)

    login_container = ft.Container(
        content=ft.Column(
            controls=[top_image, key_field_row, submit,text],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        width=320,
        height=500,
        padding=20,
        bgcolor=theme_app["container_bg_colors"][0],
        border_radius=theme_app["container_border_radius"],
        alignment=ft.alignment.center,
        border=ft.border.all(2, theme_app["border_color"])
    )

    return ft.View(
        route="/login",
        controls=[  
            ft.Container(
                content=login_container,
                expand=True,
                alignment=ft.alignment.center
            )
        ],
        bgcolor=theme_app["background_colors"][0]
    )
