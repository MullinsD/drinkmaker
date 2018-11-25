import RPi.GPIO as GPIO

def turnOn(request, pin_id):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(pin_id, 1)
    sleep(10)
    GPIO.output(pin_id, 0)
    return HttpResponse('')

