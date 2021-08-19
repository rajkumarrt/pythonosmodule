import platform
os_name=str(platform.system())
release=str(platform.release())
version=str(platform.version()) 
machine=str(platform.machine())
uname=str(platform.uname)
print(f"{os_name}  + {release} + {version} + {machine} + {uname} ")
