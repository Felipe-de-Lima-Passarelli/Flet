import flet as ft

def main(page: ft.Page):
    container = ft.Container(
        #height = 100,
        #width = 200,
        image_src = "https://flet.dev/img/docs/controls/container/container-diagram.png",
        expand = True,
        bgcolor = ft.Colors.WHITE,
        margin = ft.margin.all(10),
        #border = ft.border.all(width = 10, color = ft.Colors.RED),
        border = ft.border.only(
            top = ft.BorderSide(width = 15, color = ft.Colors.PINK),
            bottom = ft.BorderSide(width = 15, color = ft.Colors.BLUE),
            left = ft.BorderSide(width = 15, color = ft.Colors.ORANGE),
            right = ft.BorderSide(width = 15, color = ft.Colors.PURPLE)
        ),
        #border_radius = ft.border_radius.all(20) #Borda arredondada
        content = ft.Row(
            controls = [
                ft.ElevatedButton(text = "Texto 1"),
                ft.ElevatedButton(text = "Texto 2"),
                ft.ElevatedButton(text = "Texto 3"),
                ft.ElevatedButton(text = "Texto 4")
            ]
        )
    )

    page.add(container)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
