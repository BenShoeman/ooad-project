from Device import *
from House import *
from Room import *
from Task import *
from TaskRunner import *
from Time import *
from User import *

# THIRD PARTY LIBs USED IN THIS FILE.
# os and sys are used to utilize system functions like clearing the terminal and
# exiting cleanly, and pickle is used to save the state of the House.
import os
import pickle
import sys

# Clears the terminal.
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Saves the house state for next simulation.
def exit_cleanup(house):
	pickle.dump(house, open("data/house.p", "wb"))

# Gets user input and only accepts valid commands.
def getInput(validCommands):
	valid = False
	while (not valid):
		cmd = input("> ")
		if cmd in validCommands:
			valid = True
			return cmd
		else:
			print("Please enter a valid command\n")

# Tells the TaskRunner to run its tasks.
def updateDeviceStates():
	# Tasks will print if they were performed or not now
	TaskRunner.get_task_runner().run_tasks()

# Lets the real user add a task.
def addTask():
	print("\nAdding a new task\n")

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

		entry.add_device("light")

		print("Would you like to control the home or run a simulation?")
		print("c: control")
		print("s: simulate")
		validIn = ["s", "c"]
		inp = getInput(validIn)
		if inp == "c":
			user = RealUser("Bob", house)
		else:
			user = InfrequentUser("Bob", house)

	#Start up one UI if we are a real user, or another if we are simulating
	if type(user) != RealUser:
		#This is more of an app-like menu
		print("Simulating")

		#Display all registered Users

		print("Welcome to smart home! \n")
		
		interacting = True
		while(interacting):
			print("Options: ")
			print("Device: Add a device")
			print("User: Add a user")
			print("Edit: Edit device settings")
			print("Energy: View energy report")
			print("Standby: View house state")
			print("exit: Close the app")

			validCommands = ["Device", "User", "Edit", "Energy", "Standby", "exit"]
			cmd = getInput(validCommands)

			if cmd == "Device":
				# 1: Add device
				print("\nFirst, pick the room the device is in")
				room = house.get_room()
				valid = False
				while(not valid):
					print("Now, Enter device type: (light, speaker, thermostat, plug, fan, lock, security camera)")
					name = input("> ")
					valid = room.add_device(name)
					print("\n")

				print("Success! \n")

			elif cmd == "User":
				print("\nFirst, specify the type of user: (infrequent, regular, automation, power)")
				validTypes = ["infrequent", "regular", "automation", "power"]
				inp = getInput(validTypes)
				print("\nNow, enter a name: ")
				name = input("> ")
				if inp == "infrequent":
					user = InfrequentUser(name, house)
				elif inp == "regular":
					user = RegularUser(name, house)
				elif inp == "automation":
					user = AutomationUser(name, house)
				elif inp == "power":
					user = PowerUser(name, house)

				print("\nSuccess!\n")

			elif cmd == "Edit":
				# 3: Edit device settings, this is where a user can create automated routines for devices

				#Show all devices
				print()
				house.print_house_info()
				print()

				#The user now needs to select one
				room = house.get_room()
				device = room.get_device()

				print("\nSelected: " + device.name + str(device) + "\n\n")

				print("Options: ")
				print("State: Edit device state ")
				print("Task: Edit device tasks")
				print("Back: Go back to main menu\n")

				validCommands = ["State", "Task", "Back"]
				cmd = getInput(validCommands)

				if cmd == "State":
					print("\nState variables: ")
					for t in device.allowed_states:
						print("-" + t)
					print("\n")
					
					valid = False
					while (not valid):
						print("Enter variable to change: ")
						stateVar = input("> ")
						if not device.is_allowable_state(stateVar):
							print(stateVar, "is not allowed for", type(device))
						else:
							valType = device.getType(stateVar)
							print("Enter new value: " + "Type: " + str(valType) + ")")
							stateVal = input("> ")

							valid = device.change_state(**{stateVar:stateVal})

					print("\nSuccess, " + device.name + " state changed. State: " + str(device) + "\n")


				elif cmd == "Task":
					addTask()
			
			elif cmd == "Energy":
				# 4: View Energy Report
				print("House is currently using %d watts" % house.get_overall_power_usage())

			elif cmd == "Standby":
				#    4: Standby (Ability to "watch" the house)
				#    Here devices will print when they are being turned on/off and various info
				#    about their current state, the house will print out energy info and time
				#    periodically. This is so a user could see what is happening in the house
				#    and it will prove that our app is actually doing something.

				#Display current state of all devices, and if there on a routine
				print()
				house.print_house_info()
				print()

				for user in house.users:
					user.interact()
					user.automate()

			elif cmd == "exit":
				interacting = False
			



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
						print ("rdevs: print all devices in the room and their states")
						print ("hdevs: print all devices in the house and their states")
						print ("exit: exit simulation")
						

						validCommands = ["r", "l", "e", "settings", "wh", "wt", "lights on", "lights off", "play", "pause", "set temp", "rdevs", "hdevs", "exit"]
						cmd = getInput(validCommands)
						clear()

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
							print ("You've left the house, entering sleep mode")
							house.sleep()

						elif cmd == "e":
							print ("You've entered the house, welcome back")
							house.wake()

						elif cmd == "settings":
							print()
							currentRoom.print_room_info()
							print()
							device = currentRoom.get_device()

							print("\nSelected: " + device.name + str(device) + "\n\n")

							print("Options: ")
							print("State: Edit device state ")
							print("Task: Edit device tasks")
							print("Back: Go back to main menu\n")

							validCommands = ["State", "Task", "Back"]
							cmd = getInput(validCommands)

							if cmd == "State":
								print("\nState variables: ")
								for t in device.allowed_states:
									print("-" + t)
								print("\n")
								
								valid = False
								while (not valid):
									print("Enter variable to change: ")
									stateVar = input("> ")
									if not device.is_allowable_state(stateVar):
										print(stateVar, "is not allowed for", type(device))
									else:
										valType = device.getType(stateVar)
										print("Enter new value: " + "Type: " + str(valType) + ")")
										stateVal = input("> ")

										valid = device.change_state(**{stateVar:stateVal})

								print("\nSuccess, " + device.name + " state changed. State: " + str(device) + "\n")
								
							elif cmd == "Task":
								addTask()

						elif cmd == "wh":
							print ("\n Waiting one hour... \n")
							interacting = False

						elif cmd == "wt":
							print ("\nWaiting until tommorrow... \n")
							currentTime.next_day()
							interacting = False

						elif cmd == "rdevs":
							print()
							currentRoom.print_room_info()
							print()

						elif cmd == "hdevs":
							print()
							house.print_house_info()
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