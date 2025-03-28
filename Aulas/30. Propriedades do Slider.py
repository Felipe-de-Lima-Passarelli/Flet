import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    s1 = ft.Slider(
        active_color = ft.Colors.AMBER,
        inactive_color = ft.Colors.RED,
        thumb_color = ft.Colors.GREEN,
        divisions = 12,
        label = "{value}",
        min = 0,
        max = 1200,
        round = 2,
        value = 100,
    )

    page.add(s1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
