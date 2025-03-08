from collections import Counter

def vigenere_cipher(text, key, decrypt=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    key_length = len(key)
    
    for char in text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            if decrypt:
                shift = -shift
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
            key_index = (key_index + 1) % key_length
        else:
            result += char
    
    return result

def find_repeated_sequences(text, length=3):
    sequences = {}
    for i in range(len(text) - length + 1):
        seq = text[i:i+length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    return {k: v for k, v in sequences.items() if len(v) > 1}


def find_repeated_sequences(text, min_length=3, max_length=5):
    # Пошук повторюваних послідовностей
    sequences = {}
    for length in range(min_length, max_length + 1):
        for i in range(len(text) - length):
            seq = text[i:i + length]
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]
    # Залишаємо лише послідовності, які повторюються
    repeated = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    return repeated

def gcd(a, b):
    # Найбільший спільний дільник
    while b:
        a, b = b, a % b
    return a

def estimate_key_length(text):
    # Метод Касіскі: шукаємо відстані між повторами
    repeated = find_repeated_sequences(text)
    distances = []
    for positions in repeated.values():
        for i in range(len(positions) - 1):
            distances.append(positions[i + 1] - positions[i])
    
    # Знаходимо спільні дільники
    if not distances:
        return 3  # Значення за замовчуванням
    g = distances[0]
    for d in distances[1:]:
        g = gcd(g, d)
    return g

def frequency_analysis(text):
    # Частотний аналіз: найпоширеніша літера в англійській мові 'E'
    freq = Counter(text)
    most_common = freq.most_common(1)[0][0]
    shift = (ord(most_common) - ord('E')) % 26
    return chr(shift + ord('A'))

def crack_vigenere(encrypted_text):
    # Оцінюємо довжину ключа
    key_length = estimate_key_length(encrypted_text)
    print(f"Ймовірна довжина ключа: {key_length}")
    
    # Розбиваємо текст на групи за довжиною ключа
    groups = ['' for _ in range(key_length)]
    for i in range(len(encrypted_text)):
        groups[i % key_length] += encrypted_text[i]
    
    # Виконуємо частотний аналіз для кожної групи
    key = ''
    for group in groups:
        if group:
            key += frequency_analysis(group)
    
    print(f"Ймовірний ключ: {key}")
    
    # Розшифровуємо текст
    decrypted = vigenere_cipher(encrypted_text, key, decrypt=True)
    return decrypted


def main():
    key = "CRYPTOGRAPHY"

    print('---VIGENEREvsKASISKI---')
    text = ''
    while len(text) < 1:
        text = input(("Give me something to encode >> ").strip())

    while True:
        choice = input('Let\'s encrypt(1), decrypt(2) or try2hack(3): ')
        if not choice:
            print('Make your choice')
            continue

        if choice in ["close", "exit", "q"]:
            print('Good luck!')
            break
        elif choice == '1':
            encrypted_text = vigenere_cipher(text, key)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            decrypted_text = vigenere_cipher(encrypted_text, key, decrypt=True)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            decrypted_text = crack_vigenere(encrypted_text)
            print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()