import flet as ft
from flet import *
from controls import add_control_reference, return_control_reference
from form import Form


control_map = return_control_reference()


def append_data(e):
    # Добавление cont_input|TextField|value в list_notes|DataTable|rows=[]
    for key, value in control_map.items():
        if key == "AppList":
            data = DataRow(cells=[])
            for user_input in value.controls[:]:
                data.cells.append(Form(user_input.content.controls[1].value))
        if key == "AppInput":
            value.controls[0].rows.append(data)
            value.controls[0].update()


def button_enter():  # Кнопка Сохранить
    return Container(
        alignment=alignment.center,
        content=ft.IconButton(
            ft.icons.INPUT,
            tooltip="Сохранить",
            on_click=lambda e: append_data(e),
        ),
    )


class AppInput(UserControl):
    def __init__(self):
        super().__init__()

    def app_input_instance(self):
        add_control_reference("AppInput", self)

    def cont_input(self):  # Поле для ввода заметок
        return Container(
            ft.TextField(
                hint_text="Введите, для добавления в заметки...",
                width=550,
                multiline=True,
                max_lines=4,
                autofocus=True,
                bgcolor="white30",
                border_color="white",
                cursor_color="black",
            )
        )

    def build(self):
        self.app_input_instance()
        return Container(
            bgcolor=ft.colors.SURFACE_VARIANT,
            expand=True,
            height=110,
            border_radius=border_radius.only(bottom_left=15, bottom_right=15),
            padding=15,
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[self.cont_input(), button_enter()],
            ),
        )
