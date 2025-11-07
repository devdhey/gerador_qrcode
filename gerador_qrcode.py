import qrcode 
from qrcode.constants import ERROR_CORRECT_H
import os

# ----------------------------------------------------
# 1. Defina a URL do seu Google Form AQUI
# ----------------------------------------------------
# A URL de visualização/partilha do seu formulário
FORM_URL = "<url_do_seu_formulario_google_forms_aqui>"

# 2. Defina o nome do arquivo de saída
OUTPUT_FILENAME = "<nome_do_arquivo_qrcode>.png"
# ----------------------------------------------------


def generate_qr_code(url, filename):
    """
    Gera um QR Code a partir de uma URL e o salva como um arquivo PNG.
    """
    # 1. Configuração do objeto QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H, 
        box_size=10,
        border=4,
    )

    # 2. Adiciona os dados (a URL)
    qr.add_data(url)
    qr.make(fit=True)

    # 3. Cria e Salva a imagem
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    # Informa ao usuário
    print(f"✅ QR Code gerado com sucesso!")
    print(f"Arquivo salvo como: {os.path.abspath(filename)}")


# --- Execução (Simplificada) ---
# Executa a função diretamente agora que a URL foi definida
generate_qr_code(FORM_URL, OUTPUT_FILENAME)