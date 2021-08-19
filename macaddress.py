import re, uuid

print ("The MAC address is : ", end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
