import flet as ft

def main(page: ft.Page):
    botao_1 = ft.TextButton(
        text = "Editar",
        icon = ft.Icons.EDIT,
        icon_color = ft.Colors.WHITE,
        tooltip = "Clique aqui para editar o texto",
        #url = "https://www.google.com",
        style = ft.ButtonStyle(color = ft.Colors.WHITE),
        on_click = lambda _: print("Editando o conteúdo...")
    )

    page.add(botao_1)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
