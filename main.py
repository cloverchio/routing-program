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
[+] packages <HH:MM:SS> - to retrieve the status of all packages at a given 24 hour time
[+] mileage - to retrieve the total mileage of the trucks after delivery
[+] exit - to exit the program

"""


def print_output(output):
    print("[*]", output)


def print_error(error):
    print("[-]", error)


if __name__ == '__main__':
    print(banner())
    tracking_service = TrackingService()
    while True:
        try:
            user_input = input(menu()).split(' ')
            command = user_input[0].strip()
            # there are likely more parsing errors that can occur...
            # but no need to handle every case for this project
            no_valid_argument = len(user_input) == 1 or user_input[1] == ''
            if command == 'package':
                if no_valid_argument:
                    print_error("a package id is required")
                else:
                    print_output(tracking_service.status_by_package_id(user_input[1]))
            elif command == 'packages':
                if no_valid_argument:
                    print_error("a time in the format of HH:MM:SS is required")
                elif len(user_input[1].split(":")) != 3:
                    print_error("time must be in HH:MM:SS format")
                else:
                    for status in tracking_service.status_by_time(user_input[1]):
                        print_output(status)
            elif command == 'mileage':
                print_output(tracking_service.mileage())
            elif command == 'exit':
                exit(0)
            else:
                print_error("not a valid command")
        except KeyboardInterrupt:
            exit(0)
