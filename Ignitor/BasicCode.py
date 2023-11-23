import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # BCM números depois do GPIO

led = 24
buzzer = 8
relay = 16

GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)

GPIO.output(buzzer, GPIO.LOW)
GPIO.output(led, GPIO.LOW)
GPIO.output(relay, GPIO.HIGH)

button_press = True # Estado do botão

if button_press:
    for contagem_regre in range(10, 0, -1):
       GPIO.output(buzzer, GPIO.HIGH)
       print(contagem_regre)
       time.sleep(0.2)
       GPIO.output(buzzer, GPIO.LOW)
       print("Beep")
       time.sleep(0.8)

       #Opção para cancelar a ignição
       if(button_press == False):
           print("Botão cancelar pressionado, relé desligado.")
           GPIO.output(relay, GPIO.HIGH)
           GPIO.output(buzzer, GPIO.LOW)
           break

    GPIO.output(buzzer, GPIO.LOW)
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(relay, GPIO.LOW)
    print("\nRelé e led acionados.")
    time.sleep(5)

GPIO.cleanup() # Limpar/desconfigurar todos os pinos GPIO
