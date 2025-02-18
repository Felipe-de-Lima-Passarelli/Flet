import flet as ft

def main(page: ft.Page):
    switch = ft.Switch(
        active_color = ft.Colors.GREEN,
        active_track_color = ft.Colors.AMBER,
        inactive_thumb_color = ft.Colors.BLUE,
        inactive_track_color = ft.Colors.WHITE,
        label = "Deseja ativar?",
        label_position = ft.LabelPosition.RIGHT,

        thumb_color = {
            ft.ControlState.HOVERED: ft.Colors.GREEN,
            ft.ControlState.FOCUSED: ft.Colors.RED,
            ft.ControlState.DEFAULT: ft.Colors.PURPLE
        },

        thumb_icon = {
            ft.ControlState.SELECTED: ft.Icons.CHECK,
            ft.ControlState.DISABLED: ft.Icons.CLOSE,
            ft.ControlState.DEFAULT: ft.Icons.QUESTION_MARK
        },
        track_color = {
            ft.ControlState.HOVERED: ft.Colors.RED,
            ft.ControlState.FOCUSED: ft.Colors.AMBER,
            ft.ControlState.DEFAULT: ft.Colors.WHITE
        }
    )

    page.add(switch)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
