import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rs1 = ft.RangeSlider(
        start_value = 0,
        end_value = 400,
        active_color = ft.Colors.AMBER,
        inactive_color = ft.Colors.RED,
        overlay_color = ft.Colors.TEAL,
        divisions = 12,
        min = 0,
        max = 1200,
        on_change = lambda _: print(rs1.start_value, "->", rs1.end_value)
    )

    page.add(rs1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
