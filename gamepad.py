
#!/usr/bin/python

import os
import sys
import time
import keymap
import dbus
from dbus.mainloop.glib import DBusGMainLoop
#import evdev # used to get input from the keyboard
#from evdev import *
#import keymap # used to map evdev input to hid keodes
import bl as Bluetooth

class Gamepad():

	def __init__(self):

		#self.buttons = keytable

#used wireshark to sniff bluetooth packets. I realized that the packet I was using wasn't standardized and packets tend not to be.

#I have the gamepad sdp working but might copy the amazon controller if  have to.
		self.state = [
		0xA1,# A = data type message and 1 is input report. it might be removed once its there.
		0x10,
		0x02,#changes for arrows
		0x00]


		self.arrows =[0x04, #down 
			0x02, #left 
			]


DBusGMainLoop(set_as_default=True)
g = Gamepad()
myservice = Bluetooth.BTKbService();

for i in range(0,10):
	myservice.send_pad(g.state)



