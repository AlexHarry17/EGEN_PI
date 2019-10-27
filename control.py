# Source for code below: https://circuitdigest.com/microcontroller-projects/controlling-raspberry-pi-gpio-using-android-app-over-bluetooth/
# Source for code below: https://github.com/karulis/pybluez
import threading
import time
import bluetooth


# Class for controlling the motors from the raspberry pi
class Control:


    def __init__(self):
        self.allowed_device_address = ['30:4B:07:51:40:C5', ]
        self.device = self.find_device()  # Search for device

    def find_device(self):  # Searches for a connected device
        device = []  # Initiate the list for the while loop
        start_time = time.time()  # Initiate start time
        print('Searching for device')

        while True:  # Loop while no device is found
            # Source for code below: https://github.com/karulis/pybluez
            # device = bluetooth.discover_devices(lookup_names=True)  # Search for the bluetooth device
            # print(bluetooth.)
            device = bluetooth.find_service('30:4B:07:51:40:C5')
            try:
                device_name = device[0][1]
                device_address = device[0][0]
                if device_address in self.allowed_device_address:  # If device is found, only allows our devices
                    print('\nFound device: ', device_name)  # Print name of device found
                    print('Device address: ', device_address, '\n')  # Print address of device found
                    return device
                else:
                    time_taken = round(time.time() - start_time)  # Count current time taken
                    print('\nSearching for device')
                    print('Time Taken: ', time_taken, 'seconds') 
            except:
                time_taken = round(time.time() - start_time)  # Count current time taken
                print('Time Taken: ', time_taken, 'seconds') 
                print('\nSearching for device')


control = Control()
