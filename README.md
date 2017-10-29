# Bluetooth_Amazon_Remote
Turned my Raspberry Pi into a Bluetooth (EDR)  "Gamepad" (HID). It advertises using its class of device
number and then with the xml SDP Record. I messed around with making my own SDP records but to be honest I found it easier to sniff records using sdptool browse --xml and then mix and match from there. 
One issue I ran into is I kept assuming there were standardized packets for gamepads HID devices but I was wrong. Rather then search or guess and check it was much easier to use WireShark on a known working device to figure out the fields and size of the periphral outward bound input report. 
