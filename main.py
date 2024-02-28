import flet as ft
from flet import *
from header import AppHeader
from list_notes import AppList
from container_input import AppInput


def main(page: Page):
    page.title = "Автоматизированный рабочий кабинет"
    page.window_always_on_top = True
    page.theme_mode = 'dark'
    page.window_width = 650
    page.window_height = 700
    page.window_resizable = False
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Column(
                    scroll="hidden",
                    expand=True,
                    controls=[
                        AppList(),
                    ]),
                
                AppInput()
            ]
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
