import flet as ft
from flet.core.markdown import MarkdownCodeTheme

def main(page: ft.Page):
    page.padding = 0
    page.title = "Markdown Editor"

    def update_view(e):
        view.value = editor.value
        view.update()

    editor = ft.TextField(
        multiline = True,
        min_lines = 30,
        max_lines = 30,
        color = ft.Colors.BLACK,
        content_padding = 30,
        border = ft.InputBorder.NONE,
        bgcolor = ft.Colors.BLUE_GREY,
        on_change = update_view
    )

    how_to = ft.Container(
        expand = True,
        padding = 30,
        content = ft.Column(
            scroll = ft.ScrollMode.ALWAYS,
            controls = [
                ft.Text(value = "Para criar títulos em diferentes tamanhos", weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK),
                ft.Text(value = "# H1", color = ft.Colors.GREY_700),
                ft.Text(value = "## H2", color = ft.Colors.GREY_700),
                ft.Text(value = "### H3", color = ft.Colors.GREY_700),
                ft.Divider(color = ft.Colors.GREY, height = 40),
                ft.Text(value = "Para formatar o estilo do texto", weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK),
                ft.Text(value = "** Texto em Negrito **", color = ft.Colors.GREY_700),
                ft.Text(value = "* Texto em Itálico *", color = ft.Colors.GREY_700),
                ft.Text(value = "~~ Texto Tachado ~~", color = ft.Colors.GREY_700),
                ft.Divider(color = ft.Colors.GREY, height = 40),
                ft.Text(value = "Para criar listas", weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK),
                ft.Text(value = "1. Ordenada", color = ft.Colors.GREY_700),
                ft.Text(value = "- Não Ordenada", color = ft.Colors.GREY_700),
                ft.Divider(color = ft.Colors.GREY, height = 40),
                ft.Text(value = "Inserir links e imagens", weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK),
                ft.Text(value = "[Texto do link](URL)", color = ft.Colors.GREY_700),
                ft.Text(value = "![Label da imagem](URL)", color = ft.Colors.GREY_700),
                ft.Divider(color = ft.Colors.GREY, height = 40),
                ft.Text(value = "Para inserir código", weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK),
                ft.Text(value = "`Código em uma linha`", color = ft.Colors.GREY_700),
                ft.Text(value = '```\nprint("Código em múltiplas linhas") \n```', color = ft.Colors.GREY_700),
                ft.Divider(color = ft.Colors.GREY, height = 40)
            ]
        )
    )

    view = ft.Markdown(
        selectable = True,
        extension_set = ft.MarkdownExtensionSet.GITHUB_WEB,
        value = editor.value,
        code_theme = MarkdownCodeTheme.MONOKAI,
        on_tap_link = lambda e: page.launch_url(e.data)
    )

    layout = ft.Row(
        expand = True,
        spacing = 0,
        vertical_alignment = ft.CrossAxisAlignment.STRETCH,
        controls = [
            ft.Container(
                expand = True,
                bgcolor = ft.Colors.WHITE,
                content = ft.Column(
                    controls = [
                        editor,
                        how_to
                    ]
                )
            ),
            ft.Container(
                expand = True,
                bgcolor=ft.Colors.BLACK,
                padding = 30,
                content = view
            )
        ]
    )

    page.add(layout)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
