import flet as ft

def main(page: ft.Page):
    page.fonts = {
        "Dragon Slayer": "Fontes/Dragon Slayer.ttf"
    }

    t1 = ft.Text(
        value = "Olá, mundo! Seja bem vindo ao curso de Flet do Programador Aventureiro",
        style = ft.TextThemeStyle.DISPLAY_SMALL,
        bgcolor = ft.colors.BLACK38,
        color = ft.colors.WHITE38,
        font_family = "Dragon Slayer"
    )

    page.add(t1)
    print(page.fonts)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
