class CaesarCipher:

    def __init__(self, shift):
        encoder = [None] * 26 # temp array for encryption
        decoder = [None] * 26 # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        print(encoder)
        print(decoder)
        print(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        self.forward = ''.join(encoder) # will store as string
        self.backward = ''.join(decoder) # since fixed

    def encrypt(self, message):
        return self. transform(message, self.forward)
    def decrypt(self, secret):
        return self. transform(secret, self.backward)
    def transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper( ):
                j = ord(msg[k]) - ord('A') # index from 0 to 25
                msg[k] = code[j] # replace this character
        return ''.join(msg)


if __name__ == '__main__' :
    # cipher = CaesarCipher(5)
    # message = "THE EAGLE IS IN PLAY; MEET AT JOE S. ALO BLZ ABCDEFGH"
    # coded = cipher.encrypt(message)
    # print(f'Secret: {coded}')
    # answer = cipher.decrypt(coded)
    # print(f'Message: {answer}')


    encoder = [None] * 26 # temp array for encryption
    decoder = [None] * 26 # temp array for decryption
    shift = 2

    for k in range (26):
        encoder[k] = chr((k + shift) % 26 + ord('A'))
        decoder[k] = chr((k - shift) % 26 + ord('A'))

    print(chr((1-shift)%26 + ord('A')))

    print(chr(68))