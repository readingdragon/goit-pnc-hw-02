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
    default_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
    key1 = "MATRIX"
    key2 = "CRYPTO"

    print('---VIGENERE---')
    text = ''
    text = input(("Give me something to encode >> ").strip())
    if len(text) < 1:
        text = default_text

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

