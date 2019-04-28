import sys

def encode(message, n):
    if n == 0:
        return message

    message_to_encode_binary = ""
    for c in message:
        binary = bin(ord(c))[2:]
        while len(binary) < 8:
            binary = "0" + binary
        message_to_encode_binary += binary

    encode_key = "gremgrem"
    encoded_message = ""
    for i, c in enumerate(message_to_encode_binary):
        encoded_message += encode_key[i % 8] if c == "0" else encode_key[i % 8].upper()
        if i % 8 == 7:
            encoded_message += " "
    encoded_message = encoded_message.rstrip()
    return encode(encoded_message, n - 1)

while True:
    message_to_encode = input("Enter message to encode: ").rstrip()
    n = int(input("Enter number of encoding cycles: ").rstrip())
    encoded_message = encode(message_to_encode, n)
    print("Encoded message: \n---\n" + encoded_message + "\n---\n")