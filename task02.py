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
    default_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
    key1 = "SECRET"
    key2 = "CRYPTO"

    print('---Permutations cipher---')
    text = ''
    text = input(("Give me something to encode >> ").strip())
    if len(text) < 1:
        text = default_text

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

