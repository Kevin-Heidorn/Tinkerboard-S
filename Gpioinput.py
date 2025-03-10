BOTAO_PIN = 18  # Pino do botão

GPIO.setup(BOTAO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Entrada com pull-up

while True:
    if GPIO.input(BOTAO_PIN) == GPIO.LOW:  # Se apertar o botão
        GPIO.output(RELE_PIN, GPIO.HIGH)   # Liga o relé
    else:
        GPIO.output(RELE_PIN, GPIO.LOW)    # Desliga o relé
    time.sleep(0.1)
