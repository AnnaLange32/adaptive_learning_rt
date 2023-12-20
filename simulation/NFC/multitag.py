import serial
import time

# Set to store processed tag and reader combinations
processed_combinations = set()

def process_data(tag_uid, reader_id):
    combination = (tag_uid, reader_id)

    if combination not in processed_combinations:
        # Process the data for the first-time occurrence
        print("Processing data from tag with UID ", tag_uid, "on reader ", reader_id)
        # Add the combination to the set to mark it as processed
        processed_combinations.add(combination)

# Define the serial ports for your readers
reader1_port = serial.Serial('/dev/ttyUSB0', 9600)
#reader2_port = serial.Serial('COM2', 9600)

try:
    while True:
        # Read data from the first reader
        data_reader1 = reader1_port.readline().decode('utf-8').strip()
        if data_reader1:
            tag_uid = data_reader1  # Replace this with the actual parsing logic for your data
            process_data(tag_uid, 'reader1')

        # Read data from the second reader
        #data_reader2 = reader2_port.readline().decode('utf-8').strip()
        #if data_reader2:
           # tag_uid = data_reader2  # Replace this with the actual parsing logic for your data
           # process_data(tag_uid, 'reader2')

        # Add a short delay to avoid excessive CPU usage
        time.sleep(0.5)
        print('These are the combination processed: ', processed_combinations)

except KeyboardInterrupt:
    pass
finally:
    # Close the serial ports when done
    reader1_port.close()
    #reader2_port.close()