from machine import Pin
import time

led = Pin(24, Pin.OUT) 
buzzer = Pin(8, Pin.OUT) 
relay = Pin(16, Pin.OUT) 

button_press = True # Estado do botão 

start_time = time.time()

if button_press:
   for contagem_regre in range(10, 0, -1):
       buzzer.on() 
       print(contagem_regre) 
       time.sleep(0.2) 
       buzzer.off() 
       print("Beep") 
       time.sleep(0.8) #Opção para cancelar a ignição 

       if(button_press == False): 
           print("Botão cancelar pressionado, relé desligado.") 
           relay.on() 
           break 
           buzzer.off() 

   led.on() 
   relay.on() 
   print("\nRelé e led acionados.") 
   time.sleep(5)
   