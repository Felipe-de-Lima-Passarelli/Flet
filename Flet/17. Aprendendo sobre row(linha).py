import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.only(top = 100)

    row_1 = ft.Row(
        controls = [
            ft.ElevatedButton(text = "1", bgcolor = ft.Colors.RED, color = ft.Colors.WHITE),
            ft.ElevatedButton(text = "2", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text = "3", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
        ],
        alignment = ft.MainAxisAlignment.SPACE_AROUND,
        spacing = 30,
        run_spacing = 30 #Distância entre linhas
        # wrap = True,
        #scroll = ft.ScrollMode.AUTO #Caso exceda o espaço do App, habilita a rolagem
        #auto_scroll = True #Rolagem automática
    )

    page.add(row_1)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
