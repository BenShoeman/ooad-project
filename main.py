from Device import *
from House import *
from Room import *
from Task import *
from TaskRunner import *
from User import *

def getInput(validCommands):
	valid = False
	while (not valid):
		cmd = input("> ")
		if cmd in validCommands:
			valid = True
			return cmd
		else:
			print("Please enter a valid command\n")


def updateDeviceStates(hour):
	#this is where we can handle the automation
	print("doing automation.....")


def main():

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

	user = RealUser("Bob")

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
		#Here devices will print when they are being turned on/off and various info
		#    about their current state, the house will print out energy info and time
		#    periodically. This is so a user could see what is happening in the house
		#    and it will prove that our app is actually doing something.


	else:
		print("controlling")

		currentRoom = entry

		for Day in range (1,31):
			print ("\nCurrent Day: %d" % Day)
			print ("Current Room: %s \n" % currentRoom.name)
			print ("Commands: \n s: skip to next day \n enter: continue with today \n")
			
			validCommands = ["s", ""]
			cmd = getInput(validCommands)

			if cmd != "s":
				for hour in range(1,25):

					updateDeviceStates(hour)

					print("\nIt is currently %d:00 hours \n " % hour)
					
					interacting = True
					while (interacting):

						print ("Commands:")
						print ("r: go to a different room")
						print ("l: leave the house")
						print ("e: enter the house")
						print ("settings: edit device settings \n")
						print ("lights on: Turn on the lights")
						print ("lights off: Turn off the lights")
						print ("play: Play music")
						print ("pause: Pause music")
						print ("set temp: Set room temperature\n")
						print ("wait1: wait an hour")
						print ("wait2: wait until tommorrow \n")

						validCommands = ["r", "l", "e", "settings", "wait1", "wait2", "lights on", "lights off", "play", "pause", "set temp"]
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
							currentRoom.play_music()
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
							#This is where user could create automated tasks for a device in their room							print("Setting things...")

						elif cmd == "wait1":
							print ("\n Waiting one hour... \n")
							interacting = False

						elif cmd == "wait2":
							print ("\nWaiting until tommorrow... \n")
							interacting = False
							break
					

				


if __name__ == "__main__":
    main()