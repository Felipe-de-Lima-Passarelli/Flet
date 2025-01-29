import flet as ft

def main(page: ft.Page):
    icone1 = ft.Icon(
        name = ft.icons.FAVORITE,
        color = ft.colors.PINK,
        size = 150
    )

    icone2 = ft.Icon(
        name = ft.icons.AUDIOTRACK,
        color = ft.colors.GREEN_400,
        size = 150,
    )

    icone3 = ft.Icon(
        name = ft.icons.BEACH_ACCESS,
        color = ft.colors.BLUE,
        size = 80
    )

    page.add(icone1, icone2, icone3)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
