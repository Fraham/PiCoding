# Import Python header files
import RPi.GPIO as GPIO
import time

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PinPIR = 17
PinRedLED = 18
PinBlueLED = 24
PinBuzzer = 22

print "PIR Module Test (CTRL-C to exit)"

# Set pins as input/output

GPIO.setup(PinPIR, GPIO.IN)
GPIO.setup(PinRedLED, GPIO.OUT)
GPIO.setup(PinBlueLED, GPIO.OUT)
GPIO.setup(PinBuzzer, GPIO.OUT)

# Variables to hold the current and last states
Current_State = 0
Previous_State = 0

try:
	print "Waiting for no detection."
	# Loop until PIR output is 0
	while GPIO.input(PinPIR) == 1:
		Current_State = 0

	print "Ready, starting alarm"
	# Loop until users quits with CTRL - C
	while True :
		# Read PIR state
		Current_State = GPIO.input(PinPIR)

		if Current_State==1 and Previous_State==0:
			# PIR is triggered
			print "Motion detected!"
			# Flash lights and sound buzzer
			for x in range(0, 5):

				GPIO.output(PinBuzzer,	GPIO.HIGH)
				GPIO.output(PinRedLED,	GPIO.HIGH)
				time.sleep(0.1)

				GPIO.output(PinRedLED,	GPIO.LOW)
				GPIO.output(PinBlueLED,	GPIO.HIGH)
				time.sleep(0.1)

				GPIO.output(PinBlueLED,	GPIO.LOW)
				GPIO.output(PinBuzzer,	GPIO.LOW)
				time.sleep(0.1)

				# Record previous state
				Previous_State=1

		elif Current_State==0 and Previous_State==1:
			# PIR has returned to ready state
			print "Ready, starting alarm"
			Previous_State=0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	print "Quit, closing down"
	# Reset GPIO settings
	GPIO.cleanup()

	print "Goodbye"
