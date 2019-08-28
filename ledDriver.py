from gpiozero import PWMLED

# use pin 17 for constant 3.3V
# use pin 9 for ground
# use pin 17 for software PWM

def ledDriver(intensity):
    led = PWMLED(17)
    led.value = intensity / 100
