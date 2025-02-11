import flet as ft
import pages.home as home
from storage.config import font_size
from utils.BusinessLogic import convert_data_format,save_data
import threading


theme_app = home.theme_app



    
def add_account(name_account,data,page):
    home.tlist[name_account].append(data)
    save_data("storage/data/data",convert_data_format(home.tlist))
    text_input.content.value = ""
    page.update()

def colm2_container1_colm(page):
    def show_banner():
        banner.open = True
        page.update()
        threading.Timer(1.5, close_banner).start()
    def close_banner():
        banner.open = False
        page.update()
    banner = ft.Banner(
            bgcolor=ft.colors.GREEN_100, 
            leading=ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=40),
            content=ft.Text("تمت العملية بنجاح!", color=ft.colors.BLACK),
            actions=[ft.TextButton("", disabled=True)], 
            force_actions_below=True,
    )
    page.overlay.append(banner)
    
    if home.data_account:
        data_account = home.data_account[:] if home.data_account and len(home.data_account) > 0 else ["", []]

        text_input_name = ft.TextField(
            label="الحساب",
            value=data_account[0], 
            text_size=font_size["input"],
            border_radius=10,
        )
        text_input_data = ft.TextField(
            label="معلومات",
            multiline=True,
            min_lines=2,
            max_lines=6,
            value="\n".join(map(str, data_account[1])) if data_account[1] else "",
            text_size=font_size["input"],
            border_radius=10,
        )

        def add_account(data, page):
            if not data_account or len(data_account) < 1 or not data_account[0]:
                return

            old_key = data_account[0]
            new_key = data[0]
            new_value = data[1]

            if old_key == new_key:
                home.tlist[old_key][home.tlist[old_key].index(data_account[1])] = new_value
            else:
                if new_key in home.tlist:
                    home.tlist[new_key].append(new_value)
                else:
                    home.tlist[new_key]=[new_value]
                    

            save_data("storage/data/data", convert_data_format(home.tlist))

            show_banner()

            text_input_data.value = ""
            text_input_name.value = ""
            page.update()

        print(home.data_account)
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("التعديل على الحساب", size=font_size["title"], weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=15),
                ),
                ft.Container(
                    content=text_input_name,
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=text_input_data,
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="حفظ التعديلات",
                        on_click=lambda e: add_account((text_input_name.value, text_input_data.value.split("\n")), page),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=ft.padding.all(10),
                            bgcolor=theme_app["button_bg_color"],
                            color=theme_app["button_text_color"],
                            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                            text_style=ft.TextStyle(size=font_size["button"]),
                        ),
                        width=200,
                        height=50,
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
        name_account = home.name_account[:] if home.name_account and len(home.name_account) > 0 else ""
        text_input = ft.TextField(
                        label="معلومات",
                        multiline=True,
                        min_lines=2,
                        max_lines=6,
                        text_size=font_size["input"],
                        border_radius=10,
                    )
        def add_account(name_account,data,page):
            home.tlist[name_account].append(data)
            save_data("storage/data/data",convert_data_format(home.tlist))
            show_banner()
            text_input.value = ""
            page.update()
        
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(f"إضافة حساب {home.name_account}",
                                    size=font_size["title"],
                                    weight=ft.FontWeight.BOLD,
                                    rtl=True),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=15),
                ),
                ft.Container(
                    content=text_input,
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="حفظ المعلومات",
                        on_click=lambda e: add_account(name_account,text_input.value.split("\n"),page),
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
        text_input = ft.TextField(
                        label="معلومات",
                        multiline=True,
                        min_lines=2,
                        max_lines=6,
                        text_size=font_size["input"],
                        border_radius=10,
                    )
        def add_name_of_account(name,page):
            home.tlist.update({name:[]})
            save_data("storage/data/data",convert_data_format(home.tlist))
            show_banner()
            text_input.value = ""
            page.update()
        
        
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(f"إضافة حساب {home.name_account}", size=font_size["title"], weight=ft.FontWeight.BOLD,rtl=True),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=15),
                ),
                ft.Container(
                    content=text_input,
                    padding=ft.padding.symmetric(horizontal=20),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="حفظ المعلومات",
                        on_click=lambda e: add_name_of_account(text_input.value,page),
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
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1]
    )

    colm2_container1 = ft.Container(
        content=colm2_container1_colm(page),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        bgcolor=theme_app["container_bg_colors"][1],
        padding=10,

        height=600  
    )

    
    home.data_account.clear()
    home.name_account = ""
    
    colm2_container2 = colm2_container2 = ft.Container(
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
        padding=10,  
        bgcolor=theme_app["container_bg_colors"][1],
        alignment=ft.alignment.center,

        # ✅ ضبط العرض ليكون بكامل الشاشة
        width=float("inf"),  

        # ✅ ضبط الارتفاع ليكون 600 بكسل
        height=600  
    )


    
    colm1 = ft.Column(controls=[colm1_container1], expand=2)
    colm2 = ft.Column(controls=[colm2_container1, colm2_container2], expand=12,scroll="hidden")

    return ft.View(
        route="/add_account",
        bgcolor=theme_app["background_colors"][0],
        controls=[colm1, colm2]
    )


