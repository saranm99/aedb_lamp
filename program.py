from controllers import LampController

if __name__ == "__main__":
    controller = LampController()
    while True:
        line = input()

        if line == "":
            exit(0)
        
        commands = line.split("")
        
        if commands[0] == "CL":
            # Create simple lamp with ID
            lamp_id = commands[1]
        elif commands[0] == "CCL":
            # Create color lamp with ID
            lamp_color = commands[1]
            lamp_id = commands[2]
        elif commands[0] == "CLA": 
            # Create an empty lamp array with ID
            lamp_id = commands[1]
        elif commands[0] == "ALA":
            # Add lamp to array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
        elif commands[0] == "RLA":
            # Remove lamp from array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
        elif commands[0] == "S":
            # Get state of ID
            lamp_id = commands[1]
        elif commands[0] == "ON":
            # Set ID on
            lamp_id = commands[1]
        elif commands[0] == "OFF":
            # Set ID off
            lamp_id = commands[1]
        else:
            print("Invalid command.") 