MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def converter(text):
    morse_text = ''
    for character in text:
        if character != ' ':
            morse_text += f'{MORSE_CODE_DICT[character]} '
        else:
            morse_text += ' + '
    return morse_text


converter_on = True

while converter_on:
    converter_input = input("Please enter the word or sentence you would like to convert: ").upper()
    print(f'Your text converted to morse code is: {converter(converter_input)}')
    convert_again = input("Type 'Exit' if you are done, otherwise type anything to continue: ").lower()
    if convert_again == 'exit':
        converter_on = False
