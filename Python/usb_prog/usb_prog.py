import usb.core
import usb.util

# Define the vendor and product IDs of your SBC
VENDOR_ID = 0x1234
PRODUCT_ID = 0x5678

def find_device(vendor_id, product_id):
    """
    Find the USB device with the specified vendor and product IDs.
    
    :param vendor_id: The vendor ID of the device.
    :param product_id: The product ID of the device.
    :return: The found USB device or None if not found.
    """
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
    if device is None:
        raise ValueError("Device not found")
    return device

def detach_kernel_driver(device, interface=0):
    """
    Detach the kernel driver from the device if it is active.
    
    :param device: The USB device.
    :param interface: The interface number to check and detach the driver from.
    """
    if device.is_kernel_driver_active(interface):
        device.detach_kernel_driver(interface)

def set_device_configuration(device):
    """
    Set the configuration for the USB device.
    
    :param device: The USB device.
    """
    device.set_configuration()

def send_command(device, endpoint_out, command):
    """
    Send a command to the USB device.
    
    :param device: The USB device.
    :param endpoint_out: The endpoint to send the command to.
    :param command: The command data to send.
    """
    device.write(endpoint_out, command)

def receive_data(device, endpoint_in, size):
    """
    Receive data from the USB device.
    
    :param device: The USB device.
    :param endpoint_in: The endpoint to read data from.
    :param size: The maximum amount of data to read.
    :return: The data received from the device.
    """
    return device.read(endpoint_in, size)

def reattach_kernel_driver(device, interface=0):
    """
    Reattach the kernel driver to the device if it was detached.
    
    :param device: The USB device.
    :param interface: The interface number to reattach the driver to.
    """
    if not device.is_kernel_driver_active(interface):
        device.attach_kernel_driver(interface)

def main():
    """
    Main function to execute the USB communication with the SBC.
    """
    # Find the SBC device
    device = find_device(VENDOR_ID, PRODUCT_ID)

    try:
        # Detach kernel driver if active
        detach_kernel_driver(device)

        # Set configuration
        set_device_configuration(device)

        # Example: Send a command to the SBC
        endpoint_out = 0x01  # Assuming this is the output endpoint
        command = b"\x01\x02\x03\x04"  # Example command
        send_command(device, endpoint_out, command)

        # Example: Receive data from the SBC
        endpoint_in = 0x81  # Assuming this is the input endpoint
        data = receive_data(device, endpoint_in, 64)  # Read up to 64 bytes of data
        print("Received data:", data)

    except usb.core.USBError as e:
        print(f"USB Error: {e}")

    finally:
        # Reattach kernel driver if it was detached
        try:
            reattach_kernel_driver(device)
        except usb.core.USBError as e:
            print(f"Error reattaching kernel driver: {e}")

if __name__ == "__main__":
    main()
