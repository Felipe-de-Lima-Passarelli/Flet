import flet as ft

def image(num: int):
    return ft.Image(
        src = f"https://picsum.photos/150/150?{num}",
        fit = ft.ImageFit.COVER,
        repeat = ft.ImageRepeat.NO_REPEAT
    )

def main(page: ft.Page):
    def change_view(e):
        btn1.style = btn_style
        btn2.style = btn_style
        e.control.style = btn_style_selected
        #btn1.update() Não precisa mais atualizar porque o
        #btn2.update() layout.update() ao final já resolve

        if e.control.text == "Agrupadas":
            layout.controls[0] = grid2
        else:
            layout.controls[0] = grid1
        layout.update()

    grid1 = ft.GridView(
        controls = [image(num) for num in range(0, 50)],
        expand = True,
        #runs_count = 5,
        max_extent = 150,
        child_aspect_ratio = 1.0,
        spacing = 5,
        run_spacing = 5,
    )

    grid2 = ft.Column(
        expand = True,
        controls = [
            ft.Text(value = "2023", size = 30),
            ft.GridView(
                controls = [image(num) for num in range(0, 3)],
                #runs_count = 4,
                max_extent=150,
                spacing = 5,
                run_spacing = 5
            ),
            ft.Text(value="2024", size=30),
            ft.GridView(
                controls=[image(num) for num in range(3, 6)],
                #runs_count=4,
                max_extent=150,
                spacing=5,
                run_spacing=5
            ),
            ft.Text(value="2025", size=30),
            ft.GridView(
                controls=[image(num) for num in range(6, 9)],
                #runs_count=4,
                max_extent=150,
                spacing=5,
                run_spacing=5
            ),
        ]
    )

    btn_style_selected = ft.ButtonStyle(
        bgcolor = ft.Colors.BLACK54,
        color = ft.Colors.WHITE,
        elevation = 0,
        overlay_color = ft.Colors.BLACK12
    )

    btn_style = ft.ButtonStyle(
        bgcolor = ft.Colors.TRANSPARENT,
        color = ft.Colors.BLACK54,
        elevation = 0,
        overlay_color = ft.Colors.BLACK12
    )

    footer = ft.Container(
        margin = ft.margin.symmetric(vertical = 5, horizontal = 10),
        padding = 5,
        bgcolor=ft.Colors.WHITE70,
        border_radius = ft.border_radius.all(50),
        content = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                btn1 := ft.ElevatedButton(
                    text = "Todas as fotos",
                    style = btn_style_selected,
                    on_click = change_view
                ),
                btn2 := ft.ElevatedButton(
                    text = "Agrupadas",
                    style = btn_style,
                    on_click = change_view
                )
            ],
            tight = True
        )
    )

    layout = ft.Column(
        expand = True,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls = [
            grid1,
            footer
        ]
    )

    page.add(layout)

ft.app(
    target = main, assets_dir ="../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
