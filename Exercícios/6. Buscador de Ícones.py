import flet as ft

def icon_container(icon: str):
    return ft.Container(
        padding = 20,
        bgcolor = ft.Colors.WHITE10,
        border_radius = ft.border_radius.all(10),
        alignment = ft.alignment.center,
        content = ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Icon(name = icon, size = 50),
                ft.Text(value = icon),
            ]
        ),
    )

def main(page: ft.Page):
    def search(e):
        valor = e.control.value.upper()
        icons_grid.controls.clear()

        for icon in dir(ft.Icons):
            if valor in icon:
                icons_grid.controls.append(icon_container(icon = icon))
        icons_grid.update()

    search_bar = ft.TextField(
        prefix_icon = ft.Icons.SEARCH,
        hint_text = "Digite algo para buscar...",
        on_submit = search
    )

    icons_grid = ft.GridView(
        expand = True,
        max_extent = 200,
        controls = [],
        child_aspect_ratio = 1.0
    )

    layout = ft.Column(
        expand = True,
        controls = [
            search_bar,
            icons_grid
        ]
    )

    page.add(layout)

ft.app(target = main, assets_dir ="../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
