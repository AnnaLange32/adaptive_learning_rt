import serial

# Open a serial port (adjust the port and baudrate according to your setup)
reader1_port = serial.Serial('/dev/ttyUSB0', 9600)

# Write data to the serial port
#ser.write(b'Hello, Arduino!')

# Read data from the serial port
data = reader1_port.readline()
print('Received:', data)

reader1_port.close()

#def read_from_reader(serial_port):
    # Read data from the serial port
    #data = serial_port.readline().decode('utf-8').strip()
    #return data


#try:
  #  while True:
        # Read data from the first reader
     #   data_reader1 = read_from_reader(reader1_port)
      #  if data_reader1:
       #     print("Data from Reader 1:", data_reader1)

        # Read data from the second reader
       # data_reader2 = read_from_reader(reader2_port)
        #if data_reader2:
         #   print(f"Data from Reader 2: {data_reader2}")

#except KeyboardInterrupt:
    #pass
#finally:
    # Close the serial ports when done
   # reader1_port.close()
    #reader2_port.close()
