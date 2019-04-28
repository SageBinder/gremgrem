import sys
import re

def decode(message, n):
	if n == 0:
		return message

	message = re.sub("[ \\n\\r\\t]+", "", message)
	if len(message) == 0 or len(message) % 8 != 0:
		raise ValueError("Error: not a gremgrem message! (length not a multiple of 8)")
	encoding_key = "gremgrem"
	for i, c in enumerate(message):
		if c.lower() != encoding_key[i % 8]:
			raise ValueError("Error: not a gremgrem message! (did not match gremgrem pattern)")

	ascii_decoded = ""
	binary_decoded = "".join(["1" if c.isupper() else "0" for c in message])
	for i in range(0, (len(binary_decoded) // 8)):
		bytestring = ""
		for j in range(0, 8):
			bytestring += binary_decoded[(i * 8) + j]
		ascii_decoded += chr(int(bytestring, base=2))
	return decode(ascii_decoded, n - 1)
		

while True:
	encoded_message = input("Enter encoded grem message: ").rstrip()
	n = int(input("Enter number of decoding cycles: "))
	try:
		print("Decoded message:\n---\n" + decode(encoded_message, n) + "\n---\n")
	except ValueError as e:
		print(str(e))

