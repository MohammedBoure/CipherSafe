import flet as ft
from utils.BusinessLogic import DataPreparationTuple, get_best_match, convert_data_format, save_data
from storage.config import themes, theme, font_size
import utils.shared as shared

shared.tlist = DataPreparationTuple("storage/data/data")
theme_app = themes[theme]

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

def home_view(page):
    def on_text_change(e):
        try:
            query = e.control.value.lower()
        except Exception:
            query = ""
        list_data = get_best_match(shared.tlist, query)
        
        colm1_container1.content.controls.clear()
        colm1_container1.content.controls = [list_panels(list_data, page)]
        
        colm1_container1.update()  

    text_field = ft.TextField(
        label="🔍 البحث",
        text_size=font_size["input"],
        border=ft.InputBorder.OUTLINE,
        border_radius=8,
        text_align=ft.TextAlign.CENTER,
        filled=True,
        hint_text="إسم الحساب",
        width=400,
        color=theme_app["text_color"],
        border_color=theme_app["input_border_color"],
        fill_color=theme_app["input_fill_color"],
        hover_color=theme_app["input_hover_color"],
        cursor_color=theme_app["input_cursor_color"],
        selection_color=theme_app["input_selection_color"],
        focused_border_color=theme_app["primary_color"],
        on_change=on_text_change  
    )



    buttons = [
        create_icon_button(ft.icons.HOME, "الصفحة الرئيسية", lambda _: None),
        create_icon_button(ft.icons.ADD_CIRCLE, "صفحة الإنشاء", lambda _: page.go("/add_account")),
        create_icon_button(ft.icons.SETTINGS, "الإعدادات", lambda _: page.go("/settings")),
        create_icon_button(ft.icons.LOGOUT, "تسجيل الخروج", lambda _: page.go("/login")),
    ]

    colm2_container1 = ft.Container(
        content=ft.Row(
            controls=buttons,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll="hidden"
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=2,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1]
    )

    colm1_container2 = ft.Container(
        content=ft.Stack(
            controls=[
                ft.Image(
                    src="assets/2.gif",
                    width=200, height=200, top=-75
                ),
                ft.Container(
                    content=text_field,
                    alignment=ft.alignment.center,  
                    rtl=True,
                    top=70,
                    width=400
                )
            ],
            width=500,  
            height=180,  
            expand=True,
            alignment=ft.alignment.center,
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=4,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1],
        margin=ft.margin.only(top=30)
    )

    def close_dlg_accoun_name(e, bol):
        try:
            if not bol:
                dlg_modal_accoun_name.open = False
            else:
                if shared.name_of_account_delete in shared.tlist:
                    shared.tlist.pop(shared.name_of_account_delete)
                    save_data("storage/data/data", convert_data_format(shared.tlist))

                dlg_modal_accoun_name.open = False
                colm2_container1.content.controls = [list_panels(shared.tlist, e.control.page)]
                colm2_container1.update()

            dlg_modal_accoun_name.update()
            e.control.page.update()
        except Exception as ex:
            print(f"Exception: {ex}")

    dlg_modal_accoun_name = ft.AlertDialog(
        modal=True,
        title=ft.Text("التأكيد", rtl=True),
        content=ft.Text("هل أنت متأكد من حذف هذه الحسابات؟", rtl=True),
        actions=[
            ft.TextButton(
                "نعم",
                on_click=lambda _: close_dlg_accoun_name(_, True),
                style=ft.ButtonStyle(
                    bgcolor=theme_app["button_overlay_color"],
                    color=theme_app["button_text_color"],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    overlay_color=theme_app["button_bg_color"],
                    padding=ft.Padding(12, 8, 12, 8),
                )
            ),
            ft.TextButton(
                "لا",
                on_click=lambda _: close_dlg_accoun_name(_, False),
                style=ft.ButtonStyle(
                    bgcolor=theme_app["button_overlay_color"],
                    color=theme_app["button_text_color"],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    overlay_color=theme_app["button_bg_color"],
                    padding=ft.Padding(12, 8, 12, 8),
                )
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_accoun_name(e, name):
        try:
            shared.name_of_account_delete = name

            if dlg_modal_accoun_name not in e.control.page.overlay:
                e.control.page.overlay.append(dlg_modal_accoun_name)
                e.control.page.update()  

            dlg_modal_accoun_name.open = True
            e.control.page.update() 

        except Exception as ex:
            print(f"Exception: {ex}")

    def close_dlg_accoun(e, bol):
        try:
            print(shared.account_delete, "1111111111111")
            if not bol:
                dlg_modal_account.open = False
                e.control.page.update()
            else:
                shared.tlist[shared.account_delete[0]].pop(shared.account_delete[1])
                save_data("storage/data/data", convert_data_format(shared.tlist))  
                dlg_modal_account.open = False
                
                colm2_container1.content.controls.clear()
                colm2_container1.content.controls = [list_panels(shared.tlist, page)]
                
                e.control.page.update()   
                colm2_container1.update()  
        except Exception as ex:
            print(f"Exception : {ex}")           

    dlg_modal_account = ft.AlertDialog(
        modal=True,
        title=ft.Text("التأكيد", rtl=True),
        content=ft.Text("هل أنت متأكد من حدف هدا الحساب!", rtl=True),
        actions=[
            ft.TextButton(
                "نعم",
                on_click=lambda _: close_dlg_accoun(_, True),
                style=ft.ButtonStyle(
                    bgcolor=theme_app["button_overlay_color"],
                    color=theme_app["button_text_color"],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    overlay_color=theme_app["button_bg_color"],
                    padding=ft.Padding(12, 8, 12, 8),
                )
            ),
            ft.TextButton(
                "لا",
                on_click=lambda _: close_dlg_accoun(_, False),
                style=ft.ButtonStyle(
                    bgcolor=theme_app["button_overlay_color"],
                    color=theme_app["button_text_color"],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    overlay_color=theme_app["button_bg_color"],
                    padding=ft.Padding(12, 8, 12, 8),
                )
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_accoun(e, name, index):
        try:
            shared.account_delete = [name, index]

            if dlg_modal_account not in e.control.page.overlay:
                e.control.page.overlay.append(dlg_modal_account)
                e.control.page.update()  
                
            dlg_modal_account.open = True
            e.control.page.update()  

        except Exception as ex:
            print(f"Exception: {ex}")

    def on_click_edit_btn(name, index, page):
        try:
            if name not in shared.tlist:
                print(f"Error: Account '{name}' not found in tlist")
                return  
            if index < 0 or index >= len(shared.tlist[name]):
                print(f"Error: Invalid index {index} for account '{name}'")
                return  

            shared.data_account.clear()
            shared.data_account.append(name)
            shared.data_account.append(shared.tlist[name][index])

            page.update()
            page.go("/add_account")

        except Exception as ex:
            print(f"Exception: {ex}")

    def on_click_add_btn(name, page):
        try:
            shared.name_account = name
            page.go("/add_account")
        except Exception as ex:
            print(f"Exception : {ex}")

    def Panel_card(name, index, page):
        controls_list = []
        i = 0
        max_width = 0 
        
        controls_list.append(ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.EDIT,
                    icon_color=theme_app["expansion_panel_icon"],
                    icon_size=20,
                    tooltip="تعديل",
                    on_click=lambda _: on_click_edit_btn(name, index, page)
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=theme_app["expansion_panel_icon"],
                    icon_size=20,
                    tooltip="تعديل",
                    on_click=lambda _: open_dlg_accoun(_, name, index)
                )
                
            ],
            alignment=ft.MainAxisAlignment.CENTER  
        )
        )
        
        for item in shared.tlist[name][index]:
            i += 1
            text_width = len(item) * 10 
            max_width = max(max_width, text_width) 
            
            controls_list.append(
                ft.Row(
                    controls=[
                        ft.Text(item, width=text_width,
                                color=theme_app["panel_card_text_color"],
                                size=font_size["body"],
                                expand=True,
                                text_align=ft.TextAlign.LEFT
                                ),
                        ft.IconButton(
                            icon=ft.Icons.COPY,
                            icon_color=theme_app["expansion_panel_icon"],
                            on_click=lambda e, text=item: page.set_clipboard(text),
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
            
        return ft.Container(
            width=max_width + 100, 
            height=i * 45 + 50,  
            bgcolor=theme_app["panel_card_bg"],
            border_radius=5,
            padding=ft.padding.only(left=20, right=15),
            margin=5,
            content=ft.Column(controls=controls_list, spacing=0.1)
        )

    def Panel(name, page):
        control_list = []
        for i in range(len(shared.tlist[name])):
            control_list.append(Panel_card(name, i, page))
        return ft.ExpansionPanel(
            header=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            name,
                            color=theme_app["expansion_panel_text_color"],
                            font_family="Arial",
                            size=font_size["subtitle"],
                            text_align=ft.TextAlign.CENTER,
                            expand=True  
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ADD,
                            icon_color=theme_app["expansion_panel_icon"],
                            on_click=lambda _: on_click_add_btn(name, page)
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=theme_app["expansion_panel_icon"],
                            on_click=lambda _: open_dlg_accoun_name(_, name),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
                ),
                alignment=ft.alignment.center,
                padding=10,
                bgcolor=theme_app["expansion_panel_header_bg"]
            ),
            bgcolor=theme_app["container_bg_colors"][1],
            content=ft.Row(
                controls=control_list,
                wrap=True,
                spacing=5,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        )

    def list_panels(namelist, page):
        control_list = []
        for key in namelist.keys():
            control_list.append(Panel(key, page))
        return ft.ExpansionPanelList(
            expand_icon_color=theme_app["expansion_panel_icon"],
            elevation=3,
            divider_color=theme_app["expansion_panel_divider"],
            controls=control_list
        )

    colm1_container1 = ft.Container(
        content=ft.Column(
            controls=[list_panels(shared.tlist, page)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll="auto"
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=10,
        bgcolor=theme_app["container_bg_colors"][0],
        padding=10
    )

    colm1 = ft.Column(controls=[colm1_container2, colm1_container1], expand=8)
    colm2 = ft.Column(controls=[colm2_container1], expand=1)

    return ft.View(
        route="/",
        bgcolor=theme_app["background_colors"][0],
        controls=[colm1, colm2]
    )