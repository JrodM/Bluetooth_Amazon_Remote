#!/usr/bin/env python
import skywriter
import signal
from time import sleep
import numpy as np
from keras.models import load_model

from gamepad import  Gamepad




#load our neural net.
NN_model = load_model('Model1.h5')

#for translating the classification tensor/vector into an appropriate letter or number
classification_map = {0: 'F', 1: 'r', 2: '0', 3: 'i', 4: 'c', 5: 'Y', 6: '6', 7: 'N', 8: '5', 9: 'M', 10: '8', 
		      11: 'p', 12: 'x', 13: 'I', 14: 'O', 15: 'W', 16: 'B', 17: 'H', 18: 'C', 19: 'y', 20: 'u', 
		      21: '3', 22: 'A', 23: 'Z', 24: 'Q', 25: 'V', 26: 'R', 27: '1', 28: 'P', 29: 'L', 30: 'G', 
		      31: 'K', 32: 'J', 33: 'n', 34: '9', 35: 'v', 36: 'g', 37: 'e', 38: 'o', 39: '2', 40: 'b',
		      41: 'E', 42: 'X', 43: 'a', 44: 'T', 45: 'j', 46: '7', 47: 'f', 48: 'S', 49: 'm', 50: 'z',
		      51: 'l', 52: 'w', 53: 'U', 54: 's', 55: 'D', 56: 'd', 57: 'k', 58: '4', 59: 'q', 60: 'h'}


image2classify = np.full ((100,100), 1,dtype = np.float32)
state = "remote" # either remote or keyboard mode
countdown = 0


#you have to tap to start writing in keyboard mode and then tap again to send

# for sending messages
#BT_Keyboard = Gamepad()

@skywriter.move()
def move(x, y, z):
  
  if state == "keyboard":
    if z*100 < 70 and countdown % 2 == 1:
      
      x = int(x*100)
      y = int(y*100)
      print(str(x) + "  " + str(y))
      
      #add thickness to the drawing and stay in bounds
      if x < 99 and x >1 and y > 1 and y < 99:
        image2classify[100-y,x]=-1
	image2classify[100-(y+1),x]=-1
	image2classify[100-(y-1),x]=-1
	image2classify[100-y,(x-1)]=-1
	image2classify[100-y,(x+1)]=-1
	image2classify[100-(y+1),(x+1)]=-1
	image2classify[100-(y-1),(x+1)]=-1
	image2classify[100-(y+1),(x-1)]=-1
	image2classify[100-(y-1),(x-1)]=-1
      
  elif state == "remote":
    print(str(x) + "  " + str(y))
    
  
@skywriter.flick()
def flick(start,finish):
  if state == "remote":
    
    if start.upper() == "EAST":# convert to appropriate directions
      
      #BT_Keyboard.send("KEY_RIGHT")

    elif start.upper() == "WEST":
      
      #BT_Keyboard.send("KEY_LEFT")
         
    elif start.upper() == "NORTH":
      
      #BT_Keyboard.send("KEY_UP")

    elif start.upper() == "SOUTH":
      
      #BT_Keyboard.send("KEY_DOWN")
      
  else: #if youre in keyboard mode
        #move left 
    if start.upper() == "EAST":
      print(" ")
	#move right
    elif start.upper() == "WEST":
      print(" ")
        #delete last character 
    elif start.upper() == "NORTH":
      print(" ")
	#make a space
    elif start.upper() == "SOUTH":
        #BT_Keyboard.TEST(Keyboard_test)

@skywriter.airwheel()
def spinny(delta):
  print('Airwheel:')

@skywriter.double_tap()
def doubletap(position): #state change from keyboard to controller
  if state == "remote":
    global state
    state = "keyboard"
    
  else:
    global state
    state = "remote"
  

@skywriter.tap()
def tap(position):

  if state == "remote":
  #this equals select.
    print(" ")
  else:# if keyboard
    
   
    global countdown
    countdown = countdown + 1 ## go to key
    
    #if we've tapped twice send a message otherwise pause before we start drawing.
    
    if countdown % 2 == 0:
    
      classification Tensor = NN_model.predict_on_batch(image2classify)
      
      max_prob = 0
      max_index = 0#  max probability index
      itr = 0
      
      for prob in classification_Tensor:
	
	if prob > max_prob:
	  max_prob = prob
	  max_index = itr
	itr = itr + 1
      
      
      print "max prob ", max_prob
    
    #Now we look up the classification mapping for the index of the classification tensor
      alphanum_Key  = classification_map[max_index]
      print "The result of your drawing ", alphanum_Key 
      ##BT_Keyboard.send(alphanum_Key)
    
    else:#set the image before you start drawing
      #wait a second for the user to prepare themselves
      global image2classify
      image2classify = np.full ((100,100),1, dtype = np.float32)
      sleep(1)

      
    

@skywriter.touch()
def touch(position):
  print(position)

signal.pause()
