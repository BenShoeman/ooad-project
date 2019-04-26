# Simulated Smarthome

## Team Members

- Michael Hering
- Benjamin Shoeman

## Project Overview

This is a simulated smarthome that contains the major functions of modern smarthomes, and it also simulates users living within the smarthome. There are multiple styles of users with different home interactions, including a real user that can interact directly with the home through terminal input. This simulation runs day by day and allows for a real user to interrupt the simulation and manually change the state of the home at any time. The underlying smart home system is somewhat complex, but the homeowners will be abstracted away from the complexities of the smarthome system and will be able to use it with ease.

## Files

- `Device.py`: contains implementation of Device class
- `House.py`: contains implementation of House class
- `main.py`: the main script that runs the simulation
- `README.md`: the file you're reading!
- `Room.py`: contains implementation of Room class
- `Task.py`: contains implementation of Task class
- `TaskRunner.py`: contains implementation of TaskRunner class
- `Time.py`: contains implementation of Time class
- `User.py`: contains implementation of User class

## How to Execute

Make sure that you have Python 3 installed and working. Once that is done, simply run

```sh
python main.py
```

or

```sh
python3 main.py
```

to execute the simulation, depending on your OS.