
def encrypt(message, key):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
          if char.islower():
            shift = (ord(char) - ord("a") + key) % 26
            encrypted_text += chr((shift + ord ("a")))
          else:
            shift = (ord(char) - ord("A") + key) % 26
            encrypted_text += chr ((shift + ord ("A")))
        else:
           encrypted_text += char
    return encrypted_text

##As operações será aqui em cima

def main():
    while True:
        print("Caro usuário, escolha uma opção desejado")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        choice = input ("Digite o NÚMERO da opção desejada: ")

        if choice == "1":
          message = input("Informe o texto para criptografar: ")
          key = int(input("Digite o valor da rotação da criptografia: "))
          encrypt_text = encrypt(message, key)
          print("Texto criptografado: ", encrypt_text)
        
if __name__ == "__main__":
    main()
