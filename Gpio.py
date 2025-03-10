import ASUS.GPIO as GPIO
import time

RELE_PIN = 17  # Escolha um pino GPIO livre para o relé

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELE_PIN, GPIO.OUT)  # Configura o GPIO como saída

try:
    while True:
        GPIO.output(RELE_PIN, GPIO.HIGH)  # Liga o relé
        time.sleep(2)
        GPIO.output(RELE_PIN, GPIO.LOW)   # Desliga o relé
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()  # Limpa a configuração ao sair
