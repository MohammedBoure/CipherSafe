import flet as ft
from storage.config import write_json, read_json

themes = read_json("storage/themes.json")
font_sizes = read_json("storage/font_sizes.json")

def settings_view(page: ft.Page):
    theme_options = list(themes.keys())

    selected_theme = ft.Dropdown(
        label="Theme",
        options=[ft.dropdown.Option(key, key) for key in theme_options],
        value="dark",
    )

    color_fields = {}
    font_size_fields = {}

    def load_theme_fields(theme_name):
        nonlocal color_fields, font_size_fields
        theme_data = themes.get(theme_name, {})

        color_fields.clear()
        for key, value in theme_data.items():
            if isinstance(value, list):
                color_fields[key] = [ft.TextField(label=f"{key} {i+1}", value=color) for i, color in enumerate(value)]
            else:
                color_fields[key] = ft.TextField(label=key, value=value)

        font_size_fields.clear()
        font_size_fields.update({
            key: ft.TextField(label=f"{key} Font Size", value=str(value)) for key, value in font_sizes.items()
        })

        update_ui()

    def update_ui():
        if not page.views:
            return

        current_view = page.views[-1]
        current_view.controls.clear()

        current_view.controls.extend([
            ft.Text("Settings Page", size=30),
            selected_theme,
            *[field for fields in color_fields.values() for field in (fields if isinstance(fields, list) else [fields])],
            *font_size_fields.values(),
            ft.ElevatedButton("Save Settings", on_click=save_settings),
            ft.ElevatedButton("Back to Home", on_click=go_home),
        ])
        page.update()

    def save_settings(e):
        selected_theme_value = selected_theme.value

        for key, field in color_fields.items():
            if isinstance(field, list):
                themes[selected_theme_value][key] = [f.value for f in field]
            else:
                themes[selected_theme_value][key] = field.value

        for key, field in font_size_fields.items():
            font_sizes[key] = int(field.value)
            
        with open("storage/theme",'w') as file:
            file.write(selected_theme.value)

        write_json(themes, "storage/themes.json")
        write_json(font_sizes, "storage/font_sizes.json")

        page.snack_bar = ft.SnackBar(ft.Text("Settings Saved!"))
        page.snack_bar.open = True
        page.update()

    def go_home(e):
        page.go("/")

    selected_theme.on_change = lambda e: load_theme_fields(selected_theme.value)

    load_theme_fields(selected_theme.value)

    settings_page = ft.View(
        route="/settings",
        controls=[
            ft.Text("Settings Page", size=30),
            selected_theme,
            *[field for fields in color_fields.values() for field in (fields if isinstance(fields, list) else [fields])],
            *font_size_fields.values(),
            ft.ElevatedButton("Save Settings", on_click=save_settings),
            ft.ElevatedButton("Back to Home", on_click=go_home),
        ],
        scroll="auto"
    )

    return settings_page