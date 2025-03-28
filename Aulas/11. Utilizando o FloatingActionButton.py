import flet as ft

def main(page: ft.Page):
    page.floating_action_button = ft.FloatingActionButton(
        icon = ft.Icons.ADD,
        #bgcolor = ft.Colors.GREEN,
        mini = False, #Serve para deixar o ícone menor, caso não tenha texto no botão
        shape = ft.CircleBorder(),
        tooltip = "Adicionar um novo produto"
    )

    page.update()

    page.add(
        ft.Container(
            content = ft.FloatingActionButton(text = "Botão flutuante"),
            bgcolor = ft.Colors.RED,
            expand = True,
            alignment = ft.Alignment(x = 0, y = 1)
        )
    )

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
