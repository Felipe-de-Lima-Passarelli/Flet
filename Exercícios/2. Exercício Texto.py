import flet as ft

def main(page: ft.Page):
    page.fonts = {
        "Dragon Slayer": "Fontes/Dragon Slayer.ttf"
    }

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        value = "Mensagem do Dia",
        color = ft.colors.BLUE,
        style = ft.TextThemeStyle.DISPLAY_LARGE,
        font_family = "Dragon Slayer",
        text_align = ft.TextAlign.RIGHT
    )

    sub_titulo = ft.Text(
        value = "Aqui está uma citação motivacional para você:",
        italic = True,
        style = ft.TextThemeStyle.DISPLAY_SMALL
    )

    citacao = ft.Text(
        value = "A persistência é o caminho do êxito.",
        style = ft.TextThemeStyle.DISPLAY_MEDIUM,
        color = ft.colors.PINK_50,
        text_align = ft.TextAlign.CENTER,
    )

    page.update()
    page.add(titulo, sub_titulo, citacao)

ft.app(target = main, assets_dir = "Arquivos_Úteis") #Inicializar o App com a função Main
