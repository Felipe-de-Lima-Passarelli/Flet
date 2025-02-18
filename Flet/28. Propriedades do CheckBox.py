import flet as ft

def main(page: ft.Page):
    cb = ft.Checkbox(
        label = "Selecione aqui",
        label_position = ft.LabelPosition.LEFT,
        check_color = ft.Colors.AMBER,
        fill_color = {
            ft.ControlState.HOVERED: ft.Colors.GREEN,
            ft.ControlState.FOCUSED: ft.Colors.RED,
            ft.ControlState.DEFAULT: ft.Colors.BLACK
        },
        tristate = True,
        value = True,
        on_change = lambda _: print(f"O valor agora é {cb.value}")
    )

    page.add(cb)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
