
import flet as ft



def main(page: ft.Page):
    page.title = "Calculator"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    equation = ft.TextField() 


    page.add(ft.Row([equation]))


ft.app(main)
