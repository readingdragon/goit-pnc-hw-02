from task01 import vigenere_cipher

def generate_column_order(key):
    # Генеруємо порядок стовпців на основі ключа
    key = key.upper()
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    order = [x[0] for x in sorted_key]
    return order

def table_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key_length = len(key)
    order = generate_column_order(key)
    
    # Доповнюємо текст до кратного довжині ключа
    if len(text) % key_length != 0:
        text += 'X' * (key_length - len(text) % key_length)
    
    # Створюємо таблицю
    rows = len(text) // key_length
    table = [['' for _ in range(key_length)] for _ in range(rows)]
    for i, char in enumerate(text):
        row = i // key_length
        col = i % key_length
        table[row][col] = char
    
    # Зчитуємо по стовпцях у порядку ключа
    encrypted = ""
    for col in order:
        for row in range(rows):
            encrypted += table[row][col]
    
    return encrypted

def table_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key_length = len(key)
    order = generate_column_order(key)
    rows = len(encrypted_text) // key_length
    
    # Створюємо таблицю для дешифрування
    table = [['' for _ in range(key_length)] for _ in range(rows)]
    index = 0
    for col in order:
        for row in range(rows):
            table[row][col] = encrypted_text[index]
            index += 1
    
    # Зчитуємо по рядках
    decrypted = ""
    for row in range(rows):
        for col in range(key_length):
            decrypted += table[row][col]
    
    return decrypted

def double_encrypt(text, key):
    vigenere_encoded = vigenere_cipher(text, key)
    encrypted_text = table_encrypt(vigenere_encoded, key)
    return encrypted_text

def main():
    key1 = "MATRIX"
    key2 = "CRYPTO"

    print('---VIGENERE---')
    text = ''
    while len(text) < 1:
        text = input(("Give me something to encode >> ").strip())

    while True:
        choice = input('Let\'s encrypt(1), decrypt(2), double_encrypt(3): ')
        if not choice:
            print('Make your choice')
            continue

        if choice in ["close", "exit", "q"]:
            print('Good luck!')
            break
        elif choice == '1':
            encrypted_text = table_encrypt(text, key1)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            decrypted_text = table_decrypt(encrypted_text, key1)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            dt_encrypted = double_encrypt(text, key2)
            print("Encrypted text:", dt_encrypted)

if __name__ == "__main__":
    main()

