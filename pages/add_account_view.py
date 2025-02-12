import flet as ft
import utils.shared as shared
from storage.config import themes,theme,font_size
from utils.BusinessLogic import convert_data_format,save_data
import threading


theme_app = themes[theme]


def colm2_container1_colm(page):
    def show_banner():
        banner.open = True
        page.update()
        threading.Timer(1.5, close_banner).start()
    def close_banner():
        banner.open = False
        page.update()
    banner = ft.Banner(
            bgcolor=ft.Colors.GREEN_100, 
            leading=ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=40),
            content=ft.Text("تمت العملية بنجاح!", color=ft.Colors.BLACK),
            actions=[ft.TextButton("", disabled=True)], 
            force_actions_below=True,
    )
    page.overlay.clear()
    page.overlay.append(banner)
    
    ''' def threadingerue():
        while True:
            time.sleep(1)
            print(shared.data_account)
            print(shared.name_account)
            
    threading.Thread(target=threadingerue, args=()).start()'''
    
    if shared.data_account:
        data_account = shared.data_account[:]
        print(data_account)

        if not data_account or len(data_account) < 2:
            data_account = ["", []]
        print(data_account)

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
                shared.tlist[old_key][shared.tlist[old_key].index(data_account[1])] = new_value
            else:
                if new_key in shared.tlist:
                    shared.tlist[new_key].append(new_value)
                else:
                    shared.tlist[new_key] = [new_value]

            save_data("storage/data/data", convert_data_format(shared.tlist))

            show_banner()

            text_input_data.value = ""
            text_input_name.value = ""
            text_input_data.update()
            text_input_name.update()
            page.update()

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
                            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                            text_style=ft.TextStyle(size=font_size["button"])),
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

    elif shared.name_account:
        account_name = shared.name_account  # حفظ القيمة في متغير محلي
        print(account_name)

        def toggle_save_button(e):
            save_button.disabled = not bool(e.control.value.strip())  # تمكين أو تعطيل الزر بناءً على الإدخال
            save_button.update()  # تحديث الزر

        text_input = ft.TextField(
            label="معلومات",
            multiline=True,
            min_lines=2,
            max_lines=6,
            text_size=font_size["input"],
            border_radius=10,
            on_change=toggle_save_button  # استدعاء الدالة عند التغيير
        )

        save_button = ft.ElevatedButton(
            text="حفظ المعلومات",
            on_click=lambda e: add_account(account_name, text_input.value.split("\n"), page),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.padding.all(10),
                bgcolor=theme_app["button_bg_color"],
                color=theme_app["button_text_color"],
                overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                text_style=ft.TextStyle(size=font_size["button"])),
            width=200,
            height=50,
            disabled=True  # يكون معطلاً في البداية
        )

        def add_account(name_account, data, page):
            try:
                if not name_account:
                    print("Error: name_account is empty!")
                    return  

                if name_account not in shared.tlist:
                    print(f"Error: Account '{name_account}' not found in tlist! Creating a new entry.")
                    shared.tlist[name_account] = [] 

                if not data or all(line.strip() == "" for line in data):  # تجنب إضافة بيانات فارغة
                    print("Warning: Empty data provided, nothing to add.")
                    return 

                shared.tlist[name_account].append(data)
                save_data("storage/data/data", convert_data_format(shared.tlist))

                show_banner()
                text_input.value = ""
                text_input.update()  # تحديث الإدخال
                save_button.disabled = True  # تعطيل الزر بعد الإضافة
                page.update() 

            except Exception as ex:
                print(f"Exception: {ex}")

        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(f"إضافة حساب {account_name}",
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
                    content=save_button,
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
            shared.tlist.update({name:[]})
            save_data("storage/data/data",convert_data_format(shared.tlist))
            show_banner()
            text_input.value = ""
            page.update()
        
        
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(f"إضافة حساب {shared.name_account}", size=font_size["title"], weight=ft.FontWeight.BOLD,rtl=True),
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
                            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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

def create_icon_button(icon, tooltip, click): 
    btn = ft.IconButton(
        icon=icon,
        tooltip=tooltip,
        icon_size=50,
        width=70,
        height=70,
        on_click=click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=theme_app["button_border_radius"]),
            bgcolor=theme_app["button_bg_color"],
            padding=0,
            overlay_color=theme_app["button_overlay_color"],
        ),
    )

    container = ft.Container(
        content=btn,
        scale=1,
        animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        on_hover=lambda e: (setattr(e.control, "scale", 1.2 if e.data == "true" else 1), e.control.update()),
    )

    return container

def add_account_view(page):    
    buttons = [
        create_icon_button(ft.Icons.HOME, "الصفحة الرئيسية",lambda _:page.go("/")),
        create_icon_button(ft.Icons.ADD_CIRCLE, "صفحة الإنشاء",lambda _:None),
        create_icon_button(ft.Icons.SETTINGS, "الإعدادات",lambda _:page.go("/settings")),
        create_icon_button(ft.Icons.LOGOUT, "تسجيل الخروج",lambda _:page.go("/login")),
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
  
    shared.data_account.clear()
    shared.name_account = ""
    
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
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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
