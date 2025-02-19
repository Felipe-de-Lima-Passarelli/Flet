import flet as ft
from string import ascii_uppercase
from random import choice

def letter_to_guess(letter):
    return ft.Container(
                bgcolor = ft.Colors.AMBER_500,
                height = 50,
                width = 50,
                border_radius = ft.border_radius.all(5),
                content = ft.Text(
                    value = letter,
                    color = ft.Colors.WHITE,
                    size = 30,
                    text_align = ft.TextAlign.CENTER,
                    weight = ft.FontWeight.BOLD
                )
            )


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600

    available_words = ["python", "flet", "programador", "aventureiros"]
    choiced = choice(available_words).upper()

    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter = letter)
                word.update()

        if e.control.content.value not in choiced:
            victim.data += 1
            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title = ft.Text(value = "Você perdeu! :("),
                    open = True
                )
                page.update()

            errors = victim.data
            victim.src = f"Imagens/hangman_{errors}.png"
            victim.update()

        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors = [ft.Colors.GREY])
        e.control.update()

    victim = ft.Image(
        data = 0,
        src = "Imagens/hangman_0.png",
        repeat = ft.ImageRepeat.NO_REPEAT,
        height = 300
    )

    word = ft.Row(
        wrap = True,
        alignment = ft.MainAxisAlignment.CENTER,
        controls = [
            letter_to_guess("_") for letter in choiced
        ]
    )

    cena = ft.Image(col = 12, src = "Imagens/scene.png")

    game = ft.Container(
        col = {"xs": 12, "lg": 6},
        padding = 20,
        content = ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                victim,
                word
            ]
        )
    )

    teclado = ft.Container(
        col = {"xs": 12, "lg": 6},
        image_src = "Imagens/keyboard.png",
        image_repeat = ft.ImageRepeat.NO_REPEAT,
        image_fit = ft.ImageFit.FILL,
        padding = ft.padding.only(top = 150, left = 80, right = 80, bottom = 50),
        content = ft.Row(
            wrap = True,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Container(
                    height = 50,
                    width = 50,
                    border_radius = ft.border_radius.all(5),
                    content = ft.Text(
                        value = letter,
                        color = ft.Colors.WHITE,
                        size = 30,
                        text_align = ft.TextAlign.CENTER,
                        weight = ft.FontWeight.BOLD
                    ),
                    gradient = ft.LinearGradient(
                        begin = ft.Alignment(0, -1),
                        end = ft.Alignment(0, 1),
                        colors = [ft.Colors.AMBER, ft.Colors.DEEP_ORANGE]
                    ),
                    on_click = validate_letter
                ) for letter in ascii_uppercase
            ]
        )
    )

    layout = ft.ResponsiveRow(
        columns = 12,
        controls = [
            cena,
            game,
            teclado,
            cena
        ],
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)

ft.app(target = main, assets_dir ="../Arquivos_Úteis") #Inicializar o App com a função Main
