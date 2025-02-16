import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.symmetric(vertical = 200, horizontal = 20)

    tf_1 = ft.TextField(
        label = "E-mail",
        label_style = ft.TextStyle(weight = ft.FontWeight.BOLD),
        border = ft.InputBorder.UNDERLINE,
        border_color = ft.Colors.WHITE,
        border_radius = ft.border_radius.all(20),
        border_width = 2,
        capitalization = ft.TextCapitalization.CHARACTERS,
        cursor_color = ft.Colors.WHITE,

        #error_text = "Valor Inválido",
        #error_style = ft.TextStyle(size = 20),

        helper_text = "Seu melhor e-mail",
        helper_style = ft.TextStyle(italic = True),
        hint_text = "seu_email@xmail.com",

        focused_bgcolor = ft.Colors.GREEN,
        focused_border_color = ft.Colors.AMBER,
        focused_border_width = 5,
        focused_color = ft.Colors.PINK,

        input_filter = ft.InputFilter(
            allow = True,
            regex_string = r"[0-9]",
            replacement_string = "",
        ),
        #input_filter = ft.NumbersOnlyInputFilter(),
        #input_filter = ft.TextOnlyInputFilter(),

        #keyboard_type = ft.KeyboardType.NUMBER,

        max_length = 50,
        max_lines = 2,
        #min_lines = 1,

        #prefix_text = "https://",
        #prefix_icon = ft.Icons.LINK,
        #prefix_style = ft.TexyStyle(size = 20),

        #suffix_text = ".com",
        #suffix_icon = ft.Icons.ABC,
        #suffix_style = ft.TextStyle(size = 20),

        read_only = True,
    )

    page.add(tf_1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
