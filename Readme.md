# 🛠 GPIO no Tinker Board S com Android

O **Tinker Board S** possui **GPIOs (General-Purpose Input/Output)** que permitem controlar dispositivos externos, como **relés, LEDs, sensores e botões**. No **Android**, o acesso ao GPIO pode ser feito via **sysfs** ou através de um aplicativo nativo.

---

## 📌 Características do GPIO no Tinker Board S
- **Tensão de operação:** 3.3V (⚠️ cuidado com dispositivos de 5V)
- **Modos de operação:** Entrada (Input) e Saída (Output)
- **Comunicação:** UART, I2C, SPI, PWM, GPIO padrão
- **Interface:** `/sys/class/gpio/`

---

## 🚀 Configuração do GPIO no Android (via Termux)

Para controlar os GPIOs no Android usando **Python**, siga os passos abaixo:

### 1️⃣ Instalar o Termux e Python
```sh
pkg update && pkg upgrade
pkg install python
