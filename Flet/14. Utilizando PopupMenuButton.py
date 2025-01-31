import flet as ft

def main(page: ft.Page):
    def selecionar(e):
        e.control.checked = not e.control.checked
        e.control.update()

    pop_up_menu = ft.PopupMenuButton(
        icon = ft.Icons.MENU_BOOK,
        items = [
            ft.PopupMenuItem(text = "Item 1", icon = ft.Icons.POWER_INPUT, on_click = lambda _: print("Clicou no Item 1")),
            ft.PopupMenuItem(text = "Item 2", icon = ft.Icons.ADD, on_click = lambda _: print("Clicou no Item 2")),
            ft.PopupMenuItem(text = "Item 3", icon = ft.Icons.REMOVE, on_click = lambda _: print("Clicou no Item 3")),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text = "Selecione esse item", checked = False, on_click = selecionar)
        ]
    )

    page.add(pop_up_menu)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
