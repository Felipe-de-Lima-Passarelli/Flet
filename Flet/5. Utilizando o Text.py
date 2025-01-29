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
        #font_family = "Dragon Slayer",
        italic = True,
        #max_lines = 5,
        #overflow = ft.TextOverflow.ELLIPSIS, -> Três pontinhos caso não caiba a frase
        #no_wrap = True, -> Não quebra para linha de baixo
        selectable = True, #Selecionar o texto para copiar
        size = 30,
        text_align = ft.TextAlign.CENTER,
        weight = ft.FontWeight.BOLD
    )

    link_style = ft.TextStyle(
        color = ft.colors.BLUE,
        decoration = ft.TextDecoration.UNDERLINE,
        decoration_color = ft.colors.BLUE
    )

    title_style = ft.TextStyle(
        bgcolor = ft.colors.AMBER,
        color = ft.colors.RED,
        decoration = ft.TextDecoration.OVERLINE,
        decoration_color = ft.colors.RED,
        decoration_thickness = 3,
        decoration_style = ft.TextDecorationStyle.DASHED,
        italic = True,
        size = 50
    )

    t2 = ft.Text(
        spans = [
            ft.TextSpan(text = "Texto com link ", style = link_style, url = "https://google.com"),
            ft.TextSpan(text = "continuação do texto... "),
            ft.TextSpan(text = "Texto em destaque!!!", style = title_style)
        ],
        size = 70
    )

    page.add(t1, t2)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
