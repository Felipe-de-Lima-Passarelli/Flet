import flet as ft

def main(page: ft.Page):
    def play_pause(e):
        e.control.selected = not e.control.selected #Inverte o boolean da propriedade
        e.control.update()

    botao_1 = ft.IconButton(
        icon = ft.Icons.DELETE_FOREVER_ROUNDED,
        icon_color = ft.Colors.PINK,
        icon_size = 50,
        tooltip = "Deletar ação"
    )

    botao_2 = ft.IconButton(
        icon = ft.Icons.PLAY_CIRCLE,
        selected_icon = ft.Icons.PAUSE_CIRCLE,
        icon_size = 150,
        selected = False,
        on_click = play_pause
    )

    page.add(botao_1, botao_2)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
