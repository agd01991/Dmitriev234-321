translation_dict = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', "`": 'ё'
}

def translate_to_russian_layout(text):
    translated_text = ''
    for char in text:
        if char.lower() in translation_dict:
            translated_char = translation_dict[char.lower()]
            if char.isupper():
                translated_char = translated_char.upper()
            translated_text += translated_char
        else:
            translated_text += char
    return translated_text

english_text = input()
russian_text = translate_to_russian_layout(english_text)
print(russian_text) 