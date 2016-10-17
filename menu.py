from msvcrt import getch
def options_menu(option_message, options):
	option_selected = False
	current_option = 0
	update_output = True
	
	while not option_selected:
		if update_output:
		
			print("")
			print(str(option_message))
			print("")
	
			for index, option in enumerate(options):
				if (current_option == index):
					print(">" + str(option))
				else:
					print(" " + str(option))
			
			update_output = False
			
		key = ord(getch())
		
		if key == 13:
			option_selected = True
		elif key == 72:
			current_option = (current_option - 1) % len(options)
			update_output = True
		elif key == 80:
			current_option = (current_option + 1) % len(options)
			update_output = True
		else:
			pass
			
	return(options[current_option])

print(options_menu("What is the best colour?", ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]))