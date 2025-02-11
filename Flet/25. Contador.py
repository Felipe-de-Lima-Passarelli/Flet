import flet as ft

def main(page: ft.Page):
    page.title = "Contador"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    text_number = ft.TextField(value = "0", text_align = ft.TextAlign.CENTER, width = 100, disabled = True)

    def aumentar(e):
        text_number.value = str((int(text_number.value) + 1))
        text_number.update()

    def diminuir(e):
        if text_number.value == "0":
            pass
        else:
            text_number.value = str((int(text_number.value) - 1))
            text_number.update()

    def reset(e):
        text_number.value = "0"
        text_number.update()

    def trocar_cor_fundo(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    page.add(
        ft.Row(
            controls = [
                ft.IconButton(icon = ft.Icons.REMOVE, on_click = diminuir),
                text_number,
                ft.IconButton(icon = ft.Icons.ADD, on_click = aumentar)
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls = [
                ft.ElevatedButton(
                    text = "Resetar",
                    width = 250,
                    on_click = reset
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon = ft.Icons.ADD,
        on_click = trocar_cor_fundo
    )

    page.update()

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
