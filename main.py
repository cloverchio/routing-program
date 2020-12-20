# Christopher Loverchio #000875972
from service.tracking_service import TrackingService


def banner():
    return """
            ______            _   _                   
            | ___ \          | | (_)                  
            | |_/ /___  _   _| |_ _ _ __   __ _       
            |    // _ \| | | | __| | '_ \ / _` |      
            | |\ | (_) | |_| | |_| | | | | (_| |      
            ______\___/ \__,_|\__|_|_| |_|\__, |      
            | ___ \                        __/ |      
            | |_/ _ __ ___   __ _ _ __ __ ______ ___  
            |  __| '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
            | |  | | | (_) | (_| | | | (_| | | | | | |
            \_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                            __/ |                    
                            |___/                     
        """


def menu():
    return """
[+] package <package_id> - to retrieve the status of of an individual package
[+] packages <HH:MM_SS> - to retrieve the status of all packages at a given 24 hour time
[+] mileage - to retrieve the total mileage of the trucks after delivery
[+] exit - to exit the program

"""


if __name__ == '__main__':
    print(banner())
    tracking_service = TrackingService()
    while True:
        try:
            user_input = input(menu()).split(' ')
            command = user_input[0].strip()
            # there are likely more parsing errors that can occur...
            # but no need to handle every case for this project
            if command == 'package':
                if len(user_input) == 1 or user_input[1] == '':
                    print("[-] a package id is required")
                else:
                    print("[*]", tracking_service.status_by_package_id(user_input[1]))
            elif command == 'packages':
                if len(user_input) == 1 or user_input[1] == '':
                    print("[-] a time in the format of HH:MM:SS is required")
                elif len(user_input[1].split(":")) != 3:
                    print("[-] time must be in HH:MM:SS format")
                else:
                    for status in tracking_service.status_by_time(user_input[1]):
                        print("[*]", status)
            elif command == 'mileage':
                print("[*]", tracking_service.mileage())
            elif command == 'exit':
                exit(0)
            else:
                print("[-] not a valid command")
        except KeyboardInterrupt:
            exit(0)
