import time
import os
import sys
import termios
import tty
from thread import start_new_thread

red = 17
green = 22
blue = 24

redAmount = 0
greenAmount = 0
blueAmount = 0

abort = False

def setAll(re, gr, bl):
	setLights(red, re)
	setLights(green, gr)
	setLights(blue, bl)

def setLights(pin, amount):
	global redAmount
	global greenAmount
	global blueAmount

	if (amount > 1):
		if (pin == red):
			redAmount -= 1
		elif (pin == green):
			greenAmount -= 1
		elif (pin == blue):
			blueAmount -= 1

		setLights(pin, amount - 1)
	elif (amount < 0):
		if (pin == red):
			redAmount += 1
		elif (pin == green):
			greenAmount += 1
		elif (pin == blue):
			blueAmount += 1

		setLights(pin, amount + 1)
	else:
		os.system("echo %i=%f > /dev/pi-blaster" % (pin, amount))
def getCh():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	
	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	return ch

def getCharacter():
	global abort

	while (True):
		c = getCh()

		if c == 'a':
			abort = True

def turnOff():
	setLights(red, 0)
	setLights(green, 0)
	setLights(blue, 0)
	print("Finished")

def turnOn():
	r = 0
	x = 0

	while (abort == False):
		if (x == 0):
			setAll(1, 0, 0)
			x = 1
		elif(x == 1):
			setAll(0, 1, 0)
			x = 2
		elif(x == 2):
			setAll(0, 0, 1)
			x = 0

		time.sleep(0.1)
		r += 1

start_new_thread(getCharacter, ())

turnOn()

turnOff()
