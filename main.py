from time import sleep
import flet as ft



def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 300
    page.window.height = 450
    page.window.left = 1000
    page.window.top = 50

    # Controls -- Widgets
    first_name = ft.Text("First name:")
    last_name = ft.Text("Lst name:")
    first_name_text = ft.TextField()
    last_name_text = ft.TextField()

    # Display controls
    page.add(ft.Row([first_name, first_name_text]))
    page.add(ft.Row([last_name, last_name_text]))
    page.add(ft.Row([ft.ElevatedButton(text="Login"), ft.ElevatedButton(text="Close")]))
    

    # page update
    page.update()



if __name__ == "__main__":
    ft.app(main)
