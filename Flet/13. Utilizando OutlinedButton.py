import flet as ft

def main(page: ft.Page):
    botao_1 = ft.OutlinedButton(
        text = "Botão terciário",
        icon = ft.Icons.ZOOM_IN,
        icon_color = ft.Colors.TEAL,
        tooltip = "Clique aqui",
        style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius = 5)),
        url = "https://www.google.com",
        on_click = lambda _: print("Fui clicado")
    )

    page.add(botao_1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
