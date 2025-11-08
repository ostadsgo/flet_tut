from time import sleep
import flet as ft



def insert_text(text, eq):
    print(text)
    print(eq)
    print(dir(eq))



def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 300
    page.window.height = 450
    page.window.left = 1000
    page.window.top = 50

    # Controls -- Widgets
    equation = ft.TextField()
    row_1 = [ft.ElevatedButton(text=s) for s in ("C", "CC", "**", "/")]
    row_2 = [ft.ElevatedButton(text=s) for s in ("9", "8", "7", "*")]
    row_3 = [ft.ElevatedButton(text=s) for s in ("6", "5", "4", "-")]
    row_4 = [ft.ElevatedButton(text=s) for s in ("3", "2", "1", "+")]
    row_5 = [ft.ElevatedButton(text=s) for s in ("0", ".", "=")]

    # Display controls
    page.add(ft.Row([equation]))
    page.add(ft.Row(row_1))
    page.add(ft.Row(row_2))
    page.add(ft.Row(row_3))
    page.add(ft.Row(row_4))
    page.add(ft.Row(row_5))

    def on_equal(e):
        equation.value = str(eval(equation.value))
        page.update()

    def backspace(e):
        equation.focus()
        equation.value = equation.value[:-1]
        page.update()

    def clear_all(e):
        equation.focus()
        equation.value = ""
        page.update()

    def append_text(e):
        equation.focus()
        equation.value += e.control.text
        page.update()

    # events
    row_1[0].on_click = backspace
    row_1[1].on_click = clear_all

    # add text to equation text
    for b in row_2 + row_3 + row_4:
        b.on_click = append_text

    row_5[2].on_click = on_equal
    

    equation.focus()
    # page update
    page.update()



if __name__ == "__main__":
    ft.app(main)
