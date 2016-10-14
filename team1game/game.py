from map import rooms
from player import *
from items import *
from gameparser import *
from NPCs import *
from encounter import *

#refer to the templates to fill in the main game loop, although where we use classes remember to use 'class.property' rather than 'dictionary[key]' where applicable

def execute_talk(NPC_id, topic):
#This functions takes two parameters from the user's command (you will have to use
#command[1] and command[2] and use the 'len(command) > 2 in execute_command').
#Raw input would look something like 'talk NPCid topic' then it's your job
#to make it so this function get the relevant NPC from the current room's
#NPC list, then use the NPC's dictionary called 'dialogue' to determine the
#response for a given topic if the topic isn't in their 'dialogue' dictionary
#make it return 'X doesn't know what to say.' This may be change later.
#The format which the response comes at as should be 'NPC's name: NPC's dialogue'.
# comments because """ """ kept giving me an indentation error
	pass

def check_victory():
"""This is a placeholder for a function which will determine when the game has been won"""

	pass
	
def main():
	game_won = False
	
	#main game loop
	while not game_won:
		
		#print current status; room, inventory, current task/mission? etc.
		
		#show the player what they can do and read in their command
		
		#execute the command
		
		#check victory conditions, if conditions are met, set game_wone to True
		pass
		
if __name__ == "__main__":
    main()