"""
Python script to scan a computer or servers ports and check if they are open
"""

# Importing modules
import socket
import sys

file_path = r"C:/home/justincase/Desktop/my-first-repo/Assignments 1-5/Cyber-Project-week-8/Port-Result.txt"


# Function for getting user input
def get_target_range():

    # User input
    target = input("what is your target? ")
    
    # Uses Socket to grab hostname or ip from user input
    socket.gethostbyname(target)
    
    # Creates the start/stop point for user
    lower = int(input("Port start? "))
    upper = int(input("Port end? "))
    return target, lower, upper


# Function using inputs from get_target_range to scan
def scan_target(target, lower, upper):
    closed_ports = []
    open_ports = []

    try: 
        for port in range(lower,upper):
            # Using socket on default .af_inet and sock_stream
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # Checks if port is open or closed then adds to lists
            result = s.connect_ex((target,port))
            if result == 0:
                open_ports.append(port)
            else:
                closed_ports.append(port)
            s.close()

        #Saving info to .txt file
        with open(file_path, 'a') as f:
            f.write(f"Target: {target}\n")
            f.write(f"Port: {open_ports} is open\n")
            f.write(f"Port: {closed_ports} is closed\n")

    # Stops program early
    except KeyboardInterrupt:
            print("\n Stopping")
            sys.exit()
    return closed_ports, open_ports

def main():
    while True:
        target, lower, upper = get_target_range()
        scan_target(target, lower, upper)

        # Allows user to rerun with new inputs
        retry = input("Scan again? ").strip().lower()
        if retry != "y":
            print("goodbye")
            break


main()

"""
made this on my home computer which is not linked. I updated the file path to not show
personal information but have not tested if it work relitive to new path.
"""