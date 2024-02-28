import flet as ft
from flet import *
from controls import add_control_reference, return_control_reference

control_map = return_control_reference()


class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_instance(self):
        add_control_reference("AppHeader", self)

    def app_header_logo(self):  # Логотип
        return Container(
            padding=padding.only(left=15),
            content=Icon(ft.icons.NOTES)
        )

    def app_header_name(self): # Имя окна
        return Container(
            padding=padding.only(left=15, right=15),
            content=Text("Заметки", color="white", size=20))

    def app_header_search(self): # Поиск
        return Container(
            padding=padding.only(left=15),
            width=320,
            bgcolor="white10",
            border_radius=6,
            animate_opacity=320,
            opacity=0.5,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(ft.icons.SEARCH_ROUNDED, opacity=0.85),
                    TextField(
                        hint_text="Найти",
                        border_color="transparent",
                        height=40,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white"
                    )
                ]
            )
        )

    # def app_header_button_theme(self): # Кнопка смены темы
    #     def change_theme(e):  # смена цветовой темы светлая/темная
    #       if e.theme_mode == ft.ThemeMode.DARK:
    #           e.theme_mode = ft.ThemeMode.LIGHT
    #       elif e.theme_mode == ft.ThemeMode.LIGHT:
    #           e.theme_mode = ft.ThemeMode.DARK
    #       else:
    #           e.theme_mode = ft.ThemeMode.LIGHT
    #       e.update()
    #     return Container(
    #         padding=padding.only(left=15),
    #         content=IconButton(ft.icons.WB_SUNNY_OUTLINED, tooltip="Сменить тему", on_click=change_theme)
    # )

    def app_header_button_avatar(self): # Авторизация
        return Container(content=IconButton(ft.icons.PERSON, tooltip="Авторизация"))

    def app_header_button_appbar(self): # Меню
        return Container(
            content=ft.PopupMenuButton(
                tooltip="Меню",
                items=[
                    ft.PopupMenuItem(text="Калькулятор(в разработке)"),
                    ft.PopupMenuItem(text="Календарь(в разработке)")
                ],
            ),
        )

    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[2].opacity = 1
            self.controls[0].content.controls[2].update()
        else:
            self.controls[0].content.controls[2].content.controls[1].value = ""
            self.controls[0].content.controls[2].opacity = 0.5
            self.controls[0].content.controls[2].update()

    def build(self):
        self.app_header_instance()

        return Container(
            expand=True,
            on_hover=lambda e: self.show_search_bar(e),
            height=60,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=border_radius.only(top_left=15, top_right=15),
            padding=padding.only(left=15, right=15),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_logo(),
                    self.app_header_name(),
                    self.app_header_search(),
                    # self.app_header_button_theme(),
                    self.app_header_button_avatar(),
                    self.app_header_button_appbar(),
                ],
            ),
        )
