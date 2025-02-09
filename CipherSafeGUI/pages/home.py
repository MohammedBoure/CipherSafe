import flet as ft
from utils.BusinessLogic import DataPreparationTuple, get_best_match,convert_data_format
from storage.config import themes,theme,font_size



data = """:battlenet
u9kfazeaezaeazeazezaesqddsdsqdqsdazeazezaedqsdsqdsqdaeazeazdsqdqsdqdaazeazeawcxche3m@yahoo.com Ehy92MRxPe o o z z i aze azeaze azeaeze zaea
:epic
n69kp0wz@yahoo.com ilXZmLbwWd p t 
:battlenet
8nzg2nyi@gmail.com q1djSuhNhk iazeaezaezae jazeazeazezaea lazeazezaezaezaezaezaezaezaezae iazazeazeazezae iaezaezaezaeaz
l470djdc@outlook.com izwlfog4i2 v h b n l
d0uje6j3@outlook.com s6udIFu0aO j o
3ihjsjx9@gmail.com Bkrz1TRit5 o 
deig9fyz@yahoo.com zBzG7dEElP t h b o g
:uplay
7iacznna@outlook.com ap2MbyqIcO u d p p a
q4sfx3ov@gmail.com uGeEeVczYm t p y x f
lfqvp6ei@yahoo.com abkzE5RboB e 
gk8im8t3@yahoo.com fFBzl8nXA9 a t w c j
6qj2b0e0@yahoo.com 53Z6jLhJcN k 
:steam
2tzfjtyc@gmail.com CCEZIuVrXa y n v j w
:origin
loy6po7y@yahoo.com 1KuJTnwuKB r n q m m
rg2t6jke@yahoo.com PCtzYhSEMn b r l i g
:gog
hjesxsjd@gmail.com zDJHpFFpAw d i y k l
0deusfzm@gmail.com qdbI6LnF8p o j g s n
ye0ak369@yahoo.com fVlfVFLjgU v p q c p
:steam
8ezfjukv@gmail.com 5bin6QCImS k l g a c
s7oc32x7@gmail.com iR3fcNBciV u c o o g
t586925h@outlook.com wW0jYWZlDe y m a h u
x1spqcq7@yahoo.com Pz0L6Ab4Ta h z x z u
v2uxd27p@outlook.com X1qkfy7JFD c v c m g
:uplay
45rgrj37@gmail.com CMxWL6y52K w o y s h
p0c7xwps@yahoo.com fOdr3q58Wy s c f e h
pvu2kv8q@gmail.com TmUQrPVkCZ p n o s c
4gs30mjl@outlook.com zXUNDvraxA e z e k d
d0xo8qnm@yahoo.com pMcFLOvzW8 n v o a c
:battlenet
nx4aad3q@outlook.com Dd5cthdvd3 z z m n r
fo0lejw5@gmail.com 6yHp44X39p q z m e k
:origin
jhse4ik8@gmail.com s7414mwXu9 r i b d j
vlyjjum5@outlook.com CWoR5Rr2Jh s c s e s
zjaaqbc4@outlook.com k3MsCvXtqV r p f l c
fz65s9z5@yahoo.com p942GtTkzy m e u v k
"""
tlist = DataPreparationTuple(data)
theme_app = themes[theme]

data_account = []
name_account = ""

def Pass(e):
    pass

def create_icon_button(icon, tooltip, click): 
    
    return ft.IconButton(
        icon=icon,
        tooltip=tooltip,
        icon_size=50,
        width=80,
        height=80,
        on_click=click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=theme_app["button_border_radius"]),
            bgcolor=theme_app["button_bg_color"],
            padding=10,
            overlay_color=theme_app["button_overlay_color"],
        )
    )
  

def home_view(page):
    
    def on_text_change(e):
        try:
            query = e.control.value.lower()
        except Exception:
            query = ""
        list_data = get_best_match(tlist, query)
        
        colm2_container1.content.controls.clear()
        colm2_container1.content.controls = [list_panels(list_data, page)]
        
        colm2_container1.update()  


    text_field = ft.TextField(
        label="البحث",
        text_size=font_size["input"],
        border=ft.InputBorder.UNDERLINE,
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
        on_change=on_text_change  
    )
    
    buttons = [
        create_icon_button(ft.icons.HOME, "الصفحة الرئيسية", lambda _:print(1)),
        create_icon_button(ft.icons.ADD_CIRCLE, "صفحة الإنشاء", lambda _: page.go("/add_account")),
        create_icon_button(ft.icons.BUILD, "صفحة التجهيز", Pass),
        create_icon_button(ft.icons.SETTINGS, "الإعدادات", Pass),
        create_icon_button(ft.icons.LOGOUT, "تسجيل الخروج", Pass),
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
        expand=4,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1]
    )

    colm1_container2 = ft.Container(
        content=ft.Stack(
            controls=[
                ft.Image(
                    src="https://media2.giphy.com/media/M4VVhrbRI5vGsu4CGT/giphy.gif",
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
        expand=7,
        padding=5,
        alignment=ft.alignment.center,
        bgcolor=theme_app["container_bg_colors"][1]
    )


    def on_click_edit_btn(name,index,page):
        data_account.clear()
        data_account.append(name)
        data_account.append(tlist[name][index])
        page.go("/add_account")

    def on_click_add_btn(name,page):
        global name_account
        name_account = ""
        name_account = name
        page.go("/add_account")

    def Panel_card(name, index, page):
        controls_list = []
        i = 0
        max_width = 0 
        
        controls_list.append(ft.Row(
            controls=[
                ft.Text(""),
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color=theme_app["expansion_panel_icon"],
                    icon_size=20,
                    tooltip="تعديل",
                    on_click=lambda _: on_click_edit_btn(name, index, page)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN  
        )
        )
        
        for item in tlist[name][index]:
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
                            icon=ft.icons.COPY,
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
            height=i * 40 + 50,  
            bgcolor=theme_app["panel_card_bg"],
            border_radius=5,
            padding=10,
            margin=5,
            content=ft.Column(controls=controls_list, spacing=0.1)
        )


    def Panel(name, page):
        control_list = []
        for i in range(len(tlist[name])):
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
                            on_click=lambda _:on_click_add_btn(name,page)
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

    colm2_container1 = ft.Container(
        content=ft.Column(
            controls=[list_panels(tlist, page)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll="auto"
        ),
        border=ft.border.all(2, theme_app["border_color"]),
        border_radius=15,
        expand=True,
        bgcolor=theme_app["container_bg_colors"][0],
        padding=10
    )

    colm1 = ft.Column(controls=[colm1_container1, colm1_container2], expand=3)
    colm2 = ft.Column(controls=[colm2_container1], expand=7)

    
    
    return ft.View(
        route="/",
        bgcolor=theme_app["background_colors"][0],
        controls=[colm1, colm2]
    )

