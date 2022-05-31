import asyncio
from bleak import BleakClient
import time
import threading
from queue import Queue

# Use MAC Address of your SwitchBot 
# [how and where to find?] Use discover.py or take a note of the address shown in setting app 
address = " "
# UUID.SwitchBot
UUID = "cba20002-224d-11e6-9fb8-0002a5d5c51b"


cmd_q = Queue()


def cmd_sender():
    while True:
        temp = input("* if error occured, just type 'exit' and hit Enter")
        cmd_q.put(temp)
        # YOU CAN PUT YOUR OWN CODE HERE WORKING WITH SWITCH
        if temp == "exit":
            break


p = threading.Thread(target=cmd_putter)
p.start()


async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        # Sleep, waiting for connection
        time.sleep(5)

        # Check connection
        x = await client.is_connected()
        print(f"Connected: {x}")  # [Connected: False] means connection failure
        # Check Status, showing last command
        y = await client.read_gatt_char(UUID)
        print(y)
        print("Connected, Enter your command\nCommand Available => press,on,off,exit")
        while True:
            # get command
            command = cmd_q.get()
            if command == "press":
                write_byte = bytearray(b'\x57\x01\x00')
            elif command == "on":
                write_byte = bytearray(b'\x57\x01\x01')
            elif command == "off":
                write_byte = bytearray(b'\x57\x01\x02')
            elif command == "exit":
                # [exit] to close connection
                await asyncio.sleep(1.0, loop=loop)
                break
            else:
                print("Enter your command\nCommand Available => press,on,off,exit")
                continue

            # Send bytes to SwitchBot using GATT
            await client.write_gatt_char(UUID, write_byte)
            # Check Status, showing last command
            y = await client.read_gatt_char(UUID)
            print(y)
            # Sleep, for stability
            time.sleep(2)


# Start communication
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))
