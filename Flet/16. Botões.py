import flet as ft

def main(page: ft.Page):
    estilo = ft.ButtonStyle(
        color = {
            ft.ControlState.DEFAULT: ft.Colors.BLACK,
            ft.ControlState.HOVERED: ft.Colors.WHITE,
            ft.ControlState.FOCUSED: ft.Colors.BLUE
        },
        bgcolor = {
            "": ft.Colors.YELLOW,
            ft.ControlState.HOVERED: ft.Colors.PINK
        },
        padding = {
            ft.ControlState.HOVERED: 20,
        },
        side = {
            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.BLUE),
            ft.ControlState.HOVERED: ft.BorderSide(5, ft.Colors.ORANGE),
        },
        shape = {
          ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius = 20),
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder()
        },
        animation_duration = 500,
    )

    #Todos botões possuem os métodos on_click
    def funcao(e):
        print("Fui clicado")

    page.add(
        ft.Text("Personalização", style = ft.TextThemeStyle.TITLE_LARGE),
        ft.ElevatedButton(text = "Botão com estilo personalizado", style = estilo),
        ft.Divider(),

        ft. Text("Para compor o tema", style = ft.TextThemeStyle.TITLE_LARGE),
        ft.FilledButton(text = "Primário", icon = ft.Icons.STAR, icon_color = ft.Colors.YELLOW),
        ft.FilledTonalButton(text = "Secundário", icon = ft.Icons.ADD),
        ft.OutlinedButton(text = "Terciário", icon = ft.Icons.ZOOM_IN),
        ft.Divider(),

        ft.Text("Para ações do usuário", style = ft.TextThemeStyle.TITLE_LARGE),
        ft.Container(ft.FloatingActionButton(icon = ft.Icons.ADD)),
        ft.IconButton(icon = ft.Icons.DELETE_FOREVER_ROUNDED, icon_color = ft.Colors.RED),
        ft.TextButton(text = "Editar", icon = ft.Icons.EDIT),
        ft.Divider(),

        ft.Text("Para menus", style = ft.TextThemeStyle.TITLE_LARGE),
        ft.PopupMenuButton(
            items = [
                ft.PopupMenuItem(text = "Item 1"),
                ft.PopupMenuItem(text="Item 2"),
                ft.PopupMenuItem(text="Item 3"),
                ft.PopupMenuItem(),
                ft.PopupMenuItem(text="Item 4"),
            ]
        ),
        ft.Divider(),

        ft.ElevatedButton(text = "Clique aqui", on_click = funcao),

        ft.FloatingActionButton(icon = ft.Icons.ADD, mini = True),

    )

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
