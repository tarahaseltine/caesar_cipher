def decrypt():
	char_place = []
	decoded_message = ""

	answer = raw_input("Would you like to decrypt a message? Enter y or n: ")
	if answer.lower() == 'y':
		message = raw_input("Please enter your coded message: ")
		for letter in message:
			chars = ord(letter)
			char_place.append(chars)
		code = raw_input("Please enter your message key: ")
		for i in char_place:
			decoded_message += chr(i - int(code))
		print ("The secret message is: {}").format(decoded_message)
	else:
		print("k, bye")
decrypt()
