from controler import LampController

if __name__ == "__main__":
    controller = LampController()
    while True:
        line = input()

        if line == "":
            exit(0)

        commands = line.split(" ")

        if commands[0] == "CL":
            # Create simple lamp with ID
            lamp_id = commands[1]
            lamp = controller.create_lamp(lamp_id)
            controller.add_lamp(lamp)
            print(f'Lamp {lamp_id} created.')

        elif commands[0] == "CCL":
            # Create color lamp with ID
            lamp_color = commands[1]
            lamp_id = commands[2]
            lamp = controller.create_color_lamp(lamp_id)
            lamp.set_color(lamp_color)
            controller.add_lamp(lamp)
            print(f'{lamp_color} ColorLamp {lamp_id} created.')

        elif commands[0] == "CLA":
            # Create an empty lamp array with ID
            array_id = commands[1]
            array = controller.create_array(array_id)
            controller.add_array(array)
            print(f'LampArray {array_id} created.')

        elif commands[0] == "ALA":
            # Add lamp to array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            array = controller.get_array_object(lamp_array_id)
            lamp = controller.get_lamp_object(lamp_id)
            array.append_lamp(lamp)
            print(f'{lamp_id} added to {lamp_array_id}.')

        elif commands[0] == "RLA":
            # Remove lamp from array
            lamp_id = commands[1]
            lamp_array_id = commands[2]
            array = controller.get_array_object(lamp_array_id)
            lamp = controller.get_lamp_object(lamp_id)
            array.remove_lamp(lamp)
            print(f'{lamp_id} removed from {lamp_array_id}.')

        elif commands[0] == "S":
            # Get state of ID
            ID = commands[1]
            if controller.get_object_by_id(ID).get_state() == True:
                print(f'{ID} is ON.')
            else:
                print(f'{ID} is OFF.')

        elif commands[0] == "ON":
            # Set ID on
            ID = commands[1]
            if type(controller.get_object_by_id(ID)) != 'LampArray':
                if controller.is_lamp_in_array(controller.get_object_by_id(ID)):
                    print("Can't change state when part of an array.")
                else:
                    controller.get_object_by_id(ID).set_on()
                    print(f'{ID} turned ON.')
            else:
                controller.get_object_by_id(ID).set_on()
                print(f'{ID} turned ON.')

        elif commands[0] == "OFF":
            # Set ID off
            ID = commands[1]
            if type(controller.get_object_by_id(ID)) != 'LampArray':
                if controller.is_lamp_in_array(controller.get_object_by_id(ID)):
                    print("Can't change state when part of an array.")
                else:
                    controller.get_object_by_id(ID).set_off()
                    print(f'{ID} turned OFF.')
            else:
                controller.get_object_by_id(ID).set_off()
                print(f'{ID} turned OFF.')

        else:
            print("Invalid command.")
