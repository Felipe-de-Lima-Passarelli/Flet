import flet as ft

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme = ft.ColorScheme(
            primary = ft.Colors.RED
        ),
        text_theme = ft.TextTheme(
            title_large = ft.TextStyle(size = 50, weight = ft.FontWeight.W_900)
        ),
    )

    page.add(
        ft.Container(
        height = 100,
        width = 200,
        padding = 10,
        content = ft.Column(
            controls = [
                ft.Text(value = "Título", style = ft.TextThemeStyle.TITLE_LARGE),
                ft.ElevatedButton(text = "Botão", color = ft.Colors.AMBER),
                ft.FilledButton(text = "Botão Primário"),
            ]
        ),
        bgcolor = ft.Colors.PRIMARY
        ),
        ft.Container(
            height = 100,
            width = 200,
            padding = 10,
            content = ft.Column(
                controls = [
                    ft.Text(value = "Título", style = ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text = "Botão", color = ft.Colors.AMBER),
                    ft.FilledButton(text = "Botão Primário")
                ]
            ),
            bgcolor = ft.Colors.PRIMARY,
            #theme = theme
        ),
    )

    page.theme_mode = ft.ThemeMode.DARK

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.CHANGE_CIRCLE, on_click=change_theme
    )

    page.update()

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
