import flet as ft
from flet import *


class Form(UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()

    def build(self):
        return ft.TextField(
            value=self.user_input,
            border_color="black",
            height=50,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            color="black",
            read_only=True,
            # on_blur=lambda e: self.save_value(e)
        )
