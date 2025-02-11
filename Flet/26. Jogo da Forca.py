import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600

    cena = ft.Image(col = 12, src = "Imagens/scene.png")
    game = ft.Container()
    teclado = ft.Container()
    layout = ft.ResponsiveRow(
        columns = 12,
        controls = [
            cena,
            game,
            teclado,
            cena
        ]
    )

    page.add(layout)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
