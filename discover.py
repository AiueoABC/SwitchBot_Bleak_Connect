"""
Scan blutooth devices and print them
"""
import asyncio
from bleak import BleakScanner
devices = {}


def detection_callback(device, advertisement_data):
    print(device.address, "RSSI:", device.rssi, advertisement_data)
    if b"`U\xf9+]\xc6\x01\x00\x00'\x00\x00" in tuple(advertisement_data.manufacturer_data.values()):
        # I guess manufacturer data should always be same?
        devices[device.address] = advertisement_data


async def main():
    scanner = BleakScanner()
    scanner.register_detection_callback(detection_callback)
    await scanner.start()
    await asyncio.sleep(5.0)
    await scanner.stop()

    # for d in scanner.discovered_devices:
    #     print(d)
    print(devices)

asyncio.run(main())
