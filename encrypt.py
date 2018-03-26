def encrypt():
	char_place = []
	new_message = ""
	
	answer = raw_input("Would you like to encrypt a message? Enter y or n: ")
	if answer.lower() == "y":
		message = raw_input("Please enter your message here: ")
		for letter in message:
			chars = ord(letter)
			char_place.append(chars)
		amount = raw_input("Enter a key number (1-9): ")
		for i in char_place:
			new_message += chr(i + int(amount))
		print("Your coded message is: {}").format(new_message)
	else:
		print("Well then get the hell outta here!")

encrypt()
