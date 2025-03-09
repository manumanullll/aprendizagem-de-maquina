def pedir_frase():                     
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Erro: O campo não pode estar vazio. Tente novamente.")

def verificar_frase(frase):
    total_caracteres = len(frase)
    palavras = frase.split()
    total_palavras = len(palavras)
    palavra_maior = max(palavras, key=len) if palavras else "N/A"

    frase_invertida_caracteres = frase[::-1]
    frase_invertida_palavras = " ".join(palavras[::-1])
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)

    print("\n Resultados")
    print(f"Número de Caracteres: {total_caracteres}")
    print(f"Número de Palavras: {total_palavras}")
    print(f"Palavra Maior: {palavra_maior}")
    print(f"Frase invertida (caracteres): {frase_invertida_caracteres}")
    print(f"Frase invertida (palavras): {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiuscula}")
    print(f"Frase em minúsculas: {frase_minuscula}")
    print(f"Tupla de palavras: {tupla_palavras}")

if __name__ == "__main__":
    frase = pedir_frase()
    verificar_frase(frase)