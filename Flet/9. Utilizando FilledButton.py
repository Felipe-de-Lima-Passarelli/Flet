import flet as ft

def main(page: ft.Page):
    estilo = ft.ButtonStyle(
        padding = 50,
        animation_duration = 1000,
        side = {
            ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.RED),
            ft.ControlState.HOVERED: ft.BorderSide(10, ft.Colors.GREEN)
        },
        shape = {
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius = 0),
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius = 30)
        }
    )

    botao_1 = ft.FilledButton(
        text = "Botão primário"
    )

    botao_2 = ft.FilledButton(
        text = "Botão com ícone",
        icon = ft.Icons.STAR,
        icon_color = ft.Colors.AMBER
    )

    botao_3 = ft.FilledButton(
        text = "Botão personalizado",
        style = estilo
    )

    botao_4 = ft.FilledButton(
        text = "Botão com link",
        url = "https://www.google.com",
        tooltip = "Clique aqui para ir para o site do Google"
    )

    page.add(botao_1, botao_2, botao_3, botao_4)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
