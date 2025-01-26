import flet as ft

def main(page: ft.Page):
    page.title = "Início dos estudos em Flet" #Título do App

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Centraliza horizontalmente
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER # Centraliza verticalmente

    #page.padding = 20 (Espaçamento igual para todas direções)
    page.padding = ft.padding.only(top = 30, right = 100, bottom = 50, left = 10)
    page.spacing = 10 #Espaçamento entre elementos

    mensagem = ft.Text(value="Olá, seja bem vindo, essa é minha primeira interface no FLET!", size = 30)
    nome = ft.Text(value="Nome: Felipe de Lima Passarelli")
    curso = ft.Text(value="Curso: Análise e Desenvolvimento de Sistemas")
    concluido = ft.Text(value="Curso em Andamento")

    page.window.always_on_top = True #Deixa a janela sempre em 1º Plano
    page.window.height = 400
    page.window.max_height = 900
    page.window.min_height = 300
    page.window.width = 600
    page.window.max_width = 900
    page.window.min_width = 300

    page.window.top = 100
    page.window.left = 100

    page.window.movable = False #Proibe a movimentação da janela do App

    #def funcao_geral(e):
        #match e.data:
            #case _:
                #print(e.data)

    #page.window.on_event = funcao_geral #Função para verificar os nomes dos
                                         # eventos existentes na janela do App

    page.add( #Adicionar os elementos no App
        mensagem,
        nome,
        curso,
        concluido
    )

    page.update() #Atualizar as mudanças do App

ft.app(target=main) #Inicializar o App com a função Main
