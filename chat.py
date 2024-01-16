#Título Hashzap
#Botão de Iniciar o chat
    #Botão de Iniciar o chat
    #Popup
        #Bem vindo ao Hashzap
        #Escreva seu nome
        #Entrar no chat
#Chat
    #Usuario entrou no chat
    #Mensagens do usuario
#Campo para enviar mensagem
#Botão de enviar

#Passo 1
import flet as ft 

#Passo 2
#Tudo que estiver aqui dentro, aparecerá na tela.
def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True 
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    

#Passo 3
#ft.app(main) para exibir em formato de aplicativo
#ft.app(main, view=ft.WEB_BROWSER) para exibir em formato de site
ft.app(main, view=ft.WEB_BROWSER)


# Título Hashzap
# Botão de Iniciar o chat
#     Botão de Iniciar o chat
#     Popup
#         Bem vindo ao Hashzap
#         Escreva seu nome
#         Entrar no chat
# Chat
#     Usuario entrou no chat
#     Mensagens do usuario
# Campo para enviar mensagem
# Botão de enviar

# Passo 1
# import flet as ft 

# Passo 2
# Tudo que estiver aqui dentro, aparecerá na tela.
# def main(pagina):
#     titulo = ft.Text("Hashzap")

#     chat = ft.Column()

#     nome_usuario = ft.TextField(label="Escreva seu nome")

#     def enviar_mensagem_tunel(informacoes):
#         chat.controls.append(ft.Text(informacoes))
#         pagina.update

#     pagina.pubsub.subscribe(enviar_mensagem_tunel)

#     def enviar_mensagem(evento):
#         texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
#         pagina.pubsub.send_all(texto_campo_mensagem)
        
#         campo_mensagem.value = ""
#         pagina.update()

#     campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui",
#                                   on_submit=enviar_mensagem)
#     botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

#     def entrar_chat(evento):
#         popup.open = False
#         pagina.remove(botao_iniciar)
#         pagina.add(chat)
#         pagina.add(ft.Row(
#             [campo_mensagem, botao_enviar]
#         ))
#         texto = f"{nome_usuario.value} entrou no chat"
#         pagina.pubsub.send_all(texto)
#         pagina.update()

#     popup = ft.AlertDialog(
#         open=False, 
#         modal=True,
#         title=ft.Text("Bem vindo ao Hashzap"),
#         content=nome_usuario,
#         actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
#         )

#     def iniciar_chat(evento):
#         pagina.dialog = popup
#         popup.open = True 
#         pagina.update()

#     botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
#     pagina.add(titulo)
#     pagina.add(botao_iniciar)
    

# #Passo 3
# #ft.app(main) para exibir em formato de aplicativo
# #ft.app(main, view=ft.WEB_BROWSER) para exibir em formato de site
# ft.app(main, view=ft.WEB_BROWSER)