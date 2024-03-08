import os


def remover_hifen_descricao(pasta):
    imagens_por_codigo = {}
    for arquivo in os.listdir(pasta):
        nome, extensao = os.path.splitext(arquivo)
        codigo = nome.split('-')[0]
        if codigo not in imagens_por_codigo:
            imagens_por_codigo[codigo] = 1
            novo_nome = f'{codigo}{extensao}'
        else:
            numero_imagem = imagens_por_codigo[codigo]
            imagens_por_codigo[codigo] += 1
            novo_nome = f'{codigo}-{numero_imagem}{extensao}'
        os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))


pasta_imagens = '/home/mello/Documents/WorkSpace/AutomationsInPython/DownloadPhotosViaUrlExcel/Imagens_Tray'
remover_hifen_descricao(pasta_imagens)
