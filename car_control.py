import RPi.GPIO as GPIO
from time import sleep
import threading

in1 = 24
in2 = 23
ena = 25
in3 = 17
in4 = 27
enb = 18
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

# Set Low
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

# PWM with 100 duty cycle
q=GPIO.PWM(enb,10)
p=GPIO.PWM(ena,10)
p.start(100)
q.start(100)


# Time (in seconds) to Run the action
# Fine tune it according to your rover
t_forward = 0.61
t_turn = 0.295


# Handling individual pins
def start_pin(pin, time):
    GPIO.output(pin, GPIO.HIGH)
    t = threading.Timer(time, end)
    t.start()

def end():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)


# Call these functions to execute unit movements

def move_forword():
    start_pin(in1, t_forward)
    start_pin(in3, t_forward)
    sleep(t_forward)

def turn_left():
    start_pin(in3, t_turn)
    start_pin(in2, t_turn)
    sleep(t_turn)
    
def turn_right():
    start_pin(in1, t_turn)
    start_pin(in4, t_turn)
    sleep(t_turn)


