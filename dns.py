import socket

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))

def getflags(flags):
 byte1 = bytes(flags[:1])
 byte2 = bytes(flags[1:2])
 
 rflags = ''
 
 QR = '1'

 OPCODE = ''
 for bit in range(1,5):
   OPCODE += str(ord(byte1)&(1<<bit))
 
 AA = '1'

 TC = '0'
 
 RD = '1'

 RA = '0'

 Z = '000'

 RCODE = '0000'

 return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder = 'big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder = 'big')

def buildresponse(data):
 
 #Transaction ID
 TransactionID = data[:2]
 TID = ''
 for byte in TransactionID:
   TID += hex(byte)[2:]
   print(TID)
 
 # Get the flags
 Flags = getflags(data[2:4])
 print(Flags)
while 1:
 data,addr = sock.recvfrom(512)
 r = buildresponse(data)
 sock.sendto(r,addr) 
