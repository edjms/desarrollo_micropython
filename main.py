from machine import Pin, PWM
import time
from time import sleep

pwm1_pin = Pin(32, Pin.OUT)
pwm2_pin = Pin(33, Pin.OUT)
pwm1 = PWM(pwm1_pin)
pwm2 = PWM(pwm2_pin)
pwm1.freq(1000)
pwm2.freq(1000)
pwm1.duty(896)
pwm2.duty(896)

Motor1A = 14
Motor1B = 27
Motor2C = 26
Motor2D = 25

motor1A = Pin(Motor1A, Pin.OUT)
motor2C = Pin(Motor2C, Pin.OUT)
motor1B = Pin(Motor1B, Pin.OUT)
motor2D = Pin(Motor2D, Pin.OUT)

def adelante():
    motor1A.value(1)
    motor2C.value(1)

def parar():
    motor1A.value(0)
    motor2C.value(0)
    motor1B.value(0)
    motor2D.value(0)

def derecha():
    motor2C.value(1)
    motor1B.value(1)

def izquierda():
    motor1A.value(1)
    motor2D.value(1)

def atras():
    motor1B.value(1)
    motor2D.value(1)

trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

def get_distance():
    # Generar pulso de disparo
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(5)
    trigger.off()
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()

    duration = pulse_end - pulse_start
    distance = (duration * 0.034) / 2
    return distance

while True:
    try:
        time.sleep(0.05)
        distance = get_distance()

        if distance < 10:
            parar()
            sleep(1)
            derecha()
            sleep(2)
            parar()
            sleep(1)
            distance = get_distance()
            if distance < 10:
                atras()
                sleep(3)
                parar()
        else:
            adelante()
    except KeyboardInterrupt:
        print("Programa detenido por el usuario")
        break
pwm1.deinit()
pwm2.deinit()

