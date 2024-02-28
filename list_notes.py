import flet as ft 
from flet import *
from controls import add_control_reference
from container_input import button_enter


class AppList(UserControl):
    def __init__(self):
        super().__init__()

    def app_list_instance(self):
        add_control_reference("AppList", self)

    def app_list_field(self, name: str, expand: True):
        return Container(
            expand=expand,
            height=45,
            bgcolor="white",
            border_radius=6,
            padding=8,        
        )

    def build(self):
        self.app_list_instance()
        return Row(
                expand=True,
                controls=[
                    DataTable(
                        expand=True,
                        border_radius=6,
                        bgcolor="white",
                        rows=[]
                    ),                    
                ],                
            )
