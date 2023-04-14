
def encrypt(message, key):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
          if char.islower(): ## Aqui faz que o caracter torna minúsculo
            shift = (ord(char) - ord("a") + key) % 26 ## Aqui faz o "correr" alfabeto em minúsculo para trazer o resultado
            encrypted_text += chr((shift + ord ("a")))
          else:
            shift = (ord(char) - ord("A") + key) % 26 ## Aqui faz o "correr" alfabeto em maiúsculo para trazer o resultado
            encrypted_text += chr ((shift + ord ("A")))
        else:
           encrypted_text += char
    return encrypted_text

def decrypt(message, key):
    decrypted_text = ""
    for char in message:
        if char.isalpha():
            if char.islower(): ## Aqui faz que o caracter torna minúsculo
                shift = (ord(char) - ord('a') - key) % 26 ## Aqui faz o "correr" alfabeto em minúsculo para trazer o resultado
                decrypted_text += chr((shift + ord('a')))
            else:
                shift = (ord(char) - ord('A') - key) % 26## Aqui faz o "correr" alfabeto em maiúsculo para trazer o resultado
                decrypted_text += chr((shift + ord('A')))
        else:
            decrypted_text += char
    return decrypted_text
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
        
        elif choice == "2":
          message = input ("Informe o texto que vai ser descriptografado: ")
          key = int(input("Digite o valor da rotação da criptografia: "))
          decrypted_text = decrypt(message, key)
          print("Texto Descriptografado: ", decrypted_text)

        elif choice == "3":
           print("Você saiu com sucesso.")
           break
        
        else:
           print("Opção inválida. Por favor, digite a opções disponíveis")
        
if __name__ == "__main__":
    main()
