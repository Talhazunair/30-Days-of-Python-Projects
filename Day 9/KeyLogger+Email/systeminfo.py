import socket
import platform
check=socket.gethostname()
ip=socket.gethostbyname(check)
plat=platform.processor()
system=platform.system()
machine=platform.machine()
print(system)
print(machine)