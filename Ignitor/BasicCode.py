import RPi.GPIO as GPIO
import time

# Configuração dos pinos
GPIO.setmode(GPIO.BCM) # BCM números depois do GPIO

led = 24
buzzer = 8
relay = 16

# Configuração dos pinos como saída
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)

# Inicialização dos pinos
GPIO.output(buzzer, GPIO.LOW)
GPIO.output(led, GPIO.LOW)
GPIO.output(relay, GPIO.HIGH)

# Estado do botão
button_press = True 
exit_loops = False

# Se o botão estiver pressionado
while button_press and not exit_loops:
  # Contagem regressiva
  for contagem_regre in range(10, 0, -1):
      # Liga o buzzer
      GPIO.output(buzzer, GPIO.HIGH)
      print(contagem_regre)
      time.sleep(0.2)
      # Desliga o buzzer
      GPIO.output(buzzer, GPIO.LOW)
      time.sleep(0.8)

      # Opção para cancelar a ignição
      if button_press == False:
          print("Botão cancelar pressionado, relé desligado.")
          GPIO.output(relay, GPIO.HIGH)
          GPIO.output(buzzer, GPIO.LOW)
          exit_loops = True
          break
      
      #button_press = False
  
  if button_press == True:
    # Liga o led e desliga o relé
    GPIO.output(buzzer, GPIO.LOW)
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(relay, GPIO.LOW)
    print("\nRelé e led acionados.")
    time.sleep(5)
  
  break;

# Limpeza dos pinos
GPIO.cleanup() 


