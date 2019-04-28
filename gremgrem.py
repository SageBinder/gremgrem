import sys

while True:
    message_to_encode = input("Enter message to encode: ").rstrip()
    message_to_encode_binary = ""
    for c in message_to_encode:
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
    print("Encoded message: \n---\n" + encoded_message + "\n---\n")