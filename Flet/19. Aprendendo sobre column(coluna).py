import flet as ft

def main(page: ft.Page):
    col_1 = ft.Column(
        controls = [
            ft.ElevatedButton(text = "1", bgcolor = ft.Colors.RED, color = ft.Colors.WHITE),
            ft.ElevatedButton(text = "2", bgcolor = ft.Colors.RED, color = ft.Colors.WHITE),
            ft.ElevatedButton(text = "3", bgcolor = ft.Colors.RED, color = ft.Colors.WHITE)
        ],
        spacing = 20,
        run_spacing = 50
    )

    page.add(col_1)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
