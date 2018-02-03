import serial

port = "COM17"
ser = serial.Serial(port=port, baudrate=9600, timeout=2)

b = "\\x01"
print(type(b))
print(b)

b = eval('b"'+b+'"')
print(type(b))
print(b)

ser.write(b)


