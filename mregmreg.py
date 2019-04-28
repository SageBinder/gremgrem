import sys
import re

while True:
	encoded_message = input("Enter encoded grem message: ").rstrip()
	encoded_message = re.sub("[ \\n\\r\\t]+", "", encoded_message)

	if len(encoded_message) == 0 or len(encoded_message) % 8 != 0:
		print("Error: not a gremgrem message! (length not a multiple of 8)\n")
		continue

	encoding_key = "gremgrem"
	for i, c in enumerate(encoded_message):
		if c.lower() != encoding_key[i % 8]:
			print("Error: not a gremgrem message! (did not match gremgrem pattern)\n")
			break
	else:
		ascii_decoded = ""
		binary_decoded = "".join(["1" if c.isupper() else "0" for c in encoded_message])
		for i in range(0, (len(binary_decoded) // 8)):
			bytestring = ""
			for j in range(0, 8):
				bytestring += binary_decoded[(i * 8) + j]
			ascii_decoded += chr(int(bytestring, base=2))
		print("Decoded message:\n---\n" + ascii_decoded + "\n---\n")

