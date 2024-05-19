# pip install PyPDF2
import PyPDF2

def proteger_pdf(arquivo_origem, arquivo_destino, senha):
    # Abre o arquivo PDF existente
    with open(arquivo_origem, 'rb') as arquivo_original:
        # Cria um objeto para a leitura do arquivo PDf
        leitor = PyPDF2.PdfReader(arquivo_original)
        # Cria um objeto para a escrita do arquivo PDf
        escritor = PyPDF2.PdfWriter()

        # Copia todas as páginas para o novo objeto de escrita
        for page_num in range(len(leitor.pages)):
            escritor.add_page(leitor.pages[page_num])

        # Encripta o arquivo PDF com a senha
        escritor.encrypt(senha)

        # Salva o novo PDF protegido com a senha
        with open(arquivo_destino, 'wb') as arquivo_destino_file:
            escritor.write(arquivo_destino_file)

# Exemplo de uso
arquivo_origem = input('Selecione um arquivo PDF: ').replace('"', '')
arquivo_destino = 'arquivo_protegido.pdf'
senha = input('Digite a senha: ')

proteger_pdf(arquivo_origem, arquivo_destino, senha)
input('\nArquivo protegido com sucesso!\nAperte ENTER para sair...')