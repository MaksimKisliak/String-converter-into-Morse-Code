MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', '!': '-.-.--'
}


def convert_to_morse_code(text: str) -> str:
    """
    Converts a string to Morse code.

    Args:
        text (str): The input text to convert.

    Returns:
        str: The converted Morse code string.
    """
    # Convert input text to uppercase
    text = text.upper()

    # Initialize an empty string to hold the Morse code
    morse_code = ""

    # Loop through each character in the input text
    for char in text:
        # Check if the character is a space
        if char == " ":
            # If it is, add a space to the Morse code string
            morse_code += " "
        else:
            # Otherwise, get the Morse code representation for the character
            # from the MORSE_CODE_DICT and add it to the Morse code string
            morse_code += MORSE_CODE_DICT[char] + " "

    # Return the Morse code string
    return morse_code


text = input('Input a string to convert:\n')
morse_code = convert_to_morse_code(text)
print(f'Here\'s the output:\n{morse_code}')
