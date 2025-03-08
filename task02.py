def generate_permutation(key):
    # Генеруємо порядок перестановки на основі ключа
    key = key.upper()
    # Сортуємо унікальні символи та створюємо порядок
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    permutation = [x[0] for x in sorted_key]
    return permutation

def transposition_encrypt(text, key):
    text = text.upper().replace(" ", "")  # Видаляємо пробіли
    permutation = generate_permutation(key)
    key_length = len(key)
    
    # Доповнюємо текст до кратного довжині ключа
    if len(text) % key_length != 0:
        text += 'X' * (key_length - len(text) % key_length)
    
    encrypted = ""
    # Обробляємо текст блоками по довжині ключа
    for i in range(0, len(text), key_length):
        block = text[i:i + key_length]
        # Переставляємо символи в блоці за порядком
        encrypted_block = [''] * key_length
        for j, pos in enumerate(permutation):
            encrypted_block[pos] = block[j]
        encrypted += ''.join(encrypted_block)
    
    return encrypted

def transposition_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    permutation = generate_permutation(key)
    key_length = len(key)
    
    # Створюємо зворотну перестановку
    inverse_permutation = [0] * key_length
    for i, pos in enumerate(permutation):
        inverse_permutation[pos] = i
    
    decrypted = ""
    # Обробляємо текст блоками
    for i in range(0, len(encrypted_text), key_length):
        block = encrypted_text[i:i + key_length]
        # Зворотна перестановка
        decrypted_block = [''] * key_length
        for j, pos in enumerate(inverse_permutation):
            decrypted_block[pos] = block[j]
        decrypted += ''.join(decrypted_block)
    
    return decrypted

# key1: "SECRET" → Порядок: [2, 1, 3, 0, 4, 5].
# key2: "CRYPTO" → Порядок: [1, 0, 4, 5, 3, 2] (C=1, R=0, Y=4, P=5, T=3, O=2).
# Текст шифрується першим ключем, потім результат — другим ключем.
# Дешифрування відбувається у зворотному порядку: спочатку зворотна перестановка для "CRYPTO", потім для "SECRET".

def double_transposition_encrypt(text, key1, key2):
    # Перше шифрування з key1
    intermediate = transposition_encrypt(text, key1)
    # Друге шифрування з key2
    encrypted = transposition_encrypt(intermediate, key2)
    return encrypted

def double_transposition_decrypt(encrypted_text, key1, key2):
    # Перше дешифрування з key2
    intermediate = transposition_decrypt(encrypted_text, key2)
    # Друге дешифрування з key1
    decrypted = transposition_decrypt(intermediate, key1)
    return decrypted

def main():
    key1 = "SECRET"
    key2 = "CRYPTO"

    print('---Permutations cipher---')
    text = ''
    while len(text) < 1:
        text = input(("Give me something to encode >> ").strip())

    while True:
        choice = input('Let\'s encrypt(1), decrypt(2), double_transposition_encrypt(3) or double_transposition_decrypt(4): ')
        if not choice:
            print('Make your choice')
            continue

        if choice in ["close", "exit", "q"]:
            print('Good luck!')
            break
        elif choice == '1':
            encrypted_text = transposition_encrypt(text, key1)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            decrypted_text = transposition_decrypt(encrypted_text, key1)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            dt_encrypted = double_transposition_encrypt(text, key1, key2)
            print("Decrypted text:", dt_encrypted)
        elif choice == '4':
            dt_decrypted = double_transposition_decrypt(dt_encrypted, key1, key2)
            print("Decrypted text:", dt_decrypted)

if __name__ == "__main__":
    main()

