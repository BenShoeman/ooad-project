from Device import *
from House import *
from Room import *
from Task import *
from TaskRunner import *
from Time import *
from User import *
import os
import pickle
import sys

# Command to clear terminal
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def exit_cleanup(house):
	# Save the house state for next simulation
	pickle.dump(house, open("data/house.p", "wb"))

def getInput(validCommands):
	valid = False
	while (not valid):
		cmd = input("> ")
		if cmd in validCommands:
			valid = True
			return cmd
		else:
			print("Please enter a valid command\n")


def updateDeviceStates():
	#this is where we can handle the automation
	# print("doing automation.....")
	# Tasks will print if they were performed or not now
	TaskRunner.get_task_runner().run_tasks()

def main():
	clear()

	if os.path.isfile("data/house.p"):
		house = pickle.load(open("data/house.p", "rb"))
		print("Users: {}".format(house.users))
		username = input("Choose a user: ")
		user = house.get_user(username)
	else:
		house = House()

		livingRoom = house.add_room("Living Room")
		kitchen = house.add_room("Kitchen")
		bedroom = house.add_room("Bedroom")
		bathroom = house.add_room("Bathroom")
		entry = house.add_room("Entry")

		livingRoom.add_device("light")
		livingRoom.add_device("light")
		livingRoom.add_device("speaker")
		livingRoom.add_device("fan")
		livingRoom.add_device("thermostat")
		livingRoom.add_device("plug")
		livingRoom.add_device("plug")

		kitchen.add_device("light")
		kitchen.add_device("fan")
		kitchen.add_device("plug")

		bedroom.add_device("light")
		bedroom.add_device("speaker")
		bedroom.add_device("lock")
		bedroom.add_device("plug")

		bathroom.add_device("light")
		bathroom.add_device("fan")
		bathroom.add_device("lock")
		bathroom.add_device("plug")

		user = RealUser("Bob", house)

	#Start up one UI if we are a real user, or another if we are simulating
	if type(user) != RealUser:

		print("simulating")

		#This needs to be more of an app-like menu

		#Display current state of all devices, and if there on a routine

		#Display all registered Users

		#The user will then have the options: 

		# 1: Add device


		# 2: Add User


		# 3: Edit device settings
		#This is where a user can create automated routines for devices

		
		# 4: View Energy Report

		
		#4: Standby (Ability to "watch" the house)
		#     Here devices will print when they are being turned on/off and various info
		#    about their current state, the house will print out energy info and time
		#    periodically. This is so a user could see what is happening in the house
		#    and it will prove that our app is actually doing something.

    #   Call on user.interacts() to alter some device in room user.getCurrentRoom()


	else:
		print("controlling")

		currentRoom = house.get_room("Entry")
		currentTime = Time.get_time()

		for Day in range (1,31):
			clear()
			updateDeviceStates()

			print ("Current Day: %d" % currentTime.day)
			print ("Current Room: %s \n" % currentRoom.name)
			print ("Commands:")
			print ("s: skip to next day | enter: continue with today")
			print ("exit: exit simulation\n")
			
			validCommands = ["s", "", "exit"]
			cmd = getInput(validCommands)

			if cmd == "":
				for hour in range(1,25):
					clear()
					updateDeviceStates()

					print("\nIt is currently %02d:00 hours" % currentTime.hour + " on day %d\n" % currentTime.day)
					
					interacting = True
					while (interacting):

						print ("Commands:")
						print ("r: go to a different room | l: leave the house | e: enter the house")
						print ("settings: edit device settings \n")
						print ("lights on/off: Turn on or off the lights")
						print ("play/pause: Play or pause music | set temp: Set room temperature\n")
						print ("wh: wait an hour | wt: wait until tommorrow \n")
						print ("devs: print all devices in the room and their states")
						print ("exit: exit simulation")

						validCommands = ["r", "l", "e", "settings", "wh", "wt", "lights on", "lights off", "play", "pause", "set temp", "devs", "exit"]
						cmd = getInput(validCommands)

						if cmd == "s":
							continue
						elif cmd == "r":
							currentRoom = house.get_room()
							print("\nYou are now in the: %s \n" % currentRoom.name)						
						elif cmd == "lights on":
							currentRoom.lights_on()
						elif cmd == "lights off":
							currentRoom.lights_off()
						elif cmd == "play":
							song = input("What song? ")
							currentRoom.play_music(song)
						elif cmd == "pause":
							currentRoom.stop_music(song)
						elif cmd == "set temp":
							valid = False
							while (not valid):
								print("\nEnter Temperature: \n ")
								temp = input("> ")
								try:
									temp = int(temp)
									if temp >= 50 and temp <= 80:
										currentRoom.set_temperature(temp)
										valid = True
									else:
										print ("\nTemperature must be between 50 and 80\n")

								except ValueError:
									print("Enter an integer\n")	

						elif cmd == "l":
							print ("left")
							#We could have the house do something when the user leaves

						elif cmd == "e":
							print ("entered")
							#We could hae the house do something when the user returns

						elif cmd == "settings":
							#This is where user could create automated tasks for a device in their room
							print("Setting things...")

						elif cmd == "wh":
							print ("\n Waiting one hour... \n")
							interacting = False

						elif cmd == "wt":
							print ("\nWaiting until tommorrow... \n")
							currentTime.next_day()
							interacting = False

						elif cmd == "devs":
							print()
							currentRoom.print_room_info()
							print()
						
						elif cmd == "exit":
							exit_cleanup(house)
							sys.exit(0)
					
					if cmd == "wt":
						break
					currentTime.add_hour()
			
			elif cmd == "s":
				currentTime.next_day()
			else:
				break
	
	exit_cleanup(house)

if __name__ == "__main__":
    main()