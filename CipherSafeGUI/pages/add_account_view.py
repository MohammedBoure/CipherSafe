import flet as ft
import pages.home as home
from storage.config import font_size

theme_app = home.theme_app

def colm2_container1_colm():
    if home.data_account:
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("التعديل على الحساب", size=font_size["title"], weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=15),
                ),
                ft.Container(
                    content=ft.TextField(
                        label="الحساب",
                        value=home.data_account[0],
                        text_size=font_size["input"],
                        border_radius=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.TextField(
                        label="معلومات",
                        multiline=True,
                        min_lines=2,
                        max_lines=6,
                        value="\n".join(map(str, home.data_account[1])),
                        text_size=font_size["input"],
                        border_radius=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="حفظ التعديلات",
                        on_click=lambda e: print("تم الحفظ"),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=ft.padding.all(10),
                            bgcolor=theme_app["button_bg_color"],
                            color=theme_app["button_text_color"],
                            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                            text_style=ft.TextStyle(size=font_size["button"]),
                        ),
                        width=200,
                        height=50
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
    elif home.name_account:
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(f"إضافة حساب {home.name_account}", size=font_size["title"], weight=ft.FontWeight.BOLD,rtl=True),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=15),
                ),
                ft.Container(
                    content=ft.TextField(
                        label="معلومات",
                        multiline=True,
                        min_lines=2,
                        max_lines=6,
                        text_size=font_size["input"],
                        border_radius=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="حفظ المعلومات",
                        on_click=lambda e: print("تم الحفظ"),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=ft.padding.all(10),
                            bgcolor=theme_app["button_bg_color"],
                            color=theme_app["button_text_color"],
                            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                            text_style=ft.TextStyle(size=font_size["button"]),
                        ),
                        width=200,
                        height=50
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    else:
        return ft.Container(
            content=ft.Text("لم يتم العثور على بيانات الحساب", size=font_size["subtitle"], color=ft.colors.RED),
            alignment=ft.alignment.center,
            padding=ft.padding.all(20)
        )



def add_account_view(page):    
    buttons = [
        home.create_icon_button(ft.icons.HOME, "الصفحة الرئيسية",lambda _:page.go("/")),
        home.create_icon_button(ft.icons.ADD_CIRCLE, "صفحة الإنشاء",home.Pass),
        home.create_icon_button(ft.icons.BUILD, "صفحة التجهيز",home.Pass),
        home.create_icon_button(ft.icons.SETTINGS, "الإعدادات",home.Pass),
        home.create_icon_button(ft.icons.LOGOUT, "تسجيل الخروج",home.Pass),
    ]
    
    colm1_container1 = ft.Container(
        content=ft.Row(
            controls=buttons,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll="hidden"
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=3,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1]
    )

    colm2_container1 = ft.Container(
        content=colm2_container1_colm(),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=5,
        bgcolor=theme_app["container_bg_colors"][1],
        padding=10
    )
    
    home.data_account.clear()
    home.name_account = ""
    colm2_container2 = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="حفظ الحسابات كملف",
                    on_click=lambda e: print("Save clicked"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.all(10),
                        bgcolor=theme_app["button_bg_color"],
                        color=theme_app["button_text_color"],
                        overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                        text_style=ft.TextStyle(size=font_size["button"]),
                    ),
                    width=200,
                    height=50
                ),
                ft.ElevatedButton(
                    text="إستيراد ملف حسابات",
                    on_click=lambda e: print("Import clicked"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.all(10),
                        bgcolor=theme_app["button_bg_color"],
                        color=theme_app["button_text_color"],
                        overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                        text_style=ft.TextStyle(size=font_size["button"]),
                    ),
                    width=200,
                    height=50
                ),
                ft.ElevatedButton(
                    text="حفظ ملف حسابات مشفر",
                    on_click=lambda e: print("Save with Encrypt clicked"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.all(10),
                        bgcolor=theme_app["button_bg_color"],
                        color=theme_app["button_text_color"],
                        overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                        text_style=ft.TextStyle(size=font_size["button"]),
                    ),
                    width=200,
                    height=50
                ),
                ft.ElevatedButton(
                    text="إستيراد ملف حسابات مشفر",
                    on_click=lambda e: print("Import with Encrypt clicked"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.all(10),
                        bgcolor=theme_app["button_bg_color"],
                        color=theme_app["button_text_color"],
                        overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                        text_style=ft.TextStyle(size=font_size["button"]),
                    ),
                    width=200,
                    height=50
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10 
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=5,
        padding=10,  
        bgcolor=theme_app["container_bg_colors"][1],
        alignment=ft.alignment.center
    )

    
    colm1 = ft.Column(controls=[colm1_container1], expand=2)
    row2 = ft.Row(controls=[colm2_container1, colm2_container2], expand=12)

    return ft.View(
        route="/add_account",
        bgcolor=theme_app["background_colors"][0],
        controls=[colm1, row2]
    )
