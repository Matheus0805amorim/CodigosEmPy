"""placa BitDogLab raspberry pi pico w
as GPIO dos leds rgb são: Vm -GPIO13, Az -GPIO12 e Vd -GPIO11"""

from machine import Pin, PWM
import time

# Definindo os pinos GPIO para as cores do LED RGB
vm = Pin(13, Pin.OUT)  # Vermelho (Vm)
az = Pin(12, Pin.OUT)  # Azul (Az)
vd = Pin(11, Pin.OUT)  # Verde (Vd)

# Configuração dos PWM para controlar a intensidade de cada cor
pwm_vm = PWM(vm)
pwm_az = PWM(az)
pwm_vd = PWM(vd)

# Definindo a frequência do PWM (a frequência pode ser ajustada conforme necessário)
pwm_vm.freq(1000)
pwm_az.freq(1000)
pwm_vd.freq(1000)

# Função para acender o LED com uma cor específica
def set_color(red, green, blue):
    pwm_vm.duty_u16(red)  # Ajusta a intensidade do vermelho
    pwm_vd.duty_u16(green)  # Ajusta a intensidade do verde
    pwm_az.duty_u16(blue)  # Ajusta a intensidade do azul

# Teste das cores
while True:
    set_color(65535, 0, 0)  # Vermelho
    time.sleep(1)
    set_color(0, 65535, 0)  # Verde
    time.sleep(1)
    set_color(0, 0, 65535)  # Azul
    time.sleep(1)
    set_color(65535, 65535, 0)  # Amarelo
    time.sleep(1)
    set_color(0, 65535, 65535)  # Ciano
    time.sleep(1)
    set_color(65535, 0, 65535)  # Magenta
    time.sleep(1)
    set_color(0, 0, 0)  # Desliga o LED
    time.sleep(1)

"""Código com Ajustes na Velocidade das Cores"""
from machine import Pin, PWM
import time

# Definindo os pinos GPIO para as cores do LED RGB
vm = Pin(13, Pin.OUT)  # Vermelho (Vm)
az = Pin(12, Pin.OUT)  # Azul (Az)
vd = Pin(11, Pin.OUT)  # Verde (Vd)

# Configuração dos PWM para controlar a intensidade de cada cor
pwm_vm = PWM(vm)
pwm_az = PWM(az)
pwm_vd = PWM(vd)

# Definindo a frequência do PWM (a frequência pode ser ajustada conforme necessário)
pwm_vm.freq(1000)
pwm_az.freq(1000)
pwm_vd.freq(1000)

# Função para acender o LED com uma cor específica
def set_color(red, green, blue):
    pwm_vm.duty_u16(red)  # Ajusta a intensidade do vermelho
    pwm_vd.duty_u16(green)  # Ajusta a intensidade do verde
    pwm_az.duty_u16(blue)  # Ajusta a intensidade do azul

# Teste das cores com diferentes velocidades
while True:
    set_color(65535, 0, 0)  # Vermelho
    time.sleep(0.5)  # Velocidade rápida
    set_color(0, 65535, 0)  # Verde
    time.sleep(0.5)  # Velocidade rápida
    set_color(0, 0, 65535)  # Azul
    time.sleep(0.5)  # Velocidade rápida
    set_color(65535, 65535, 0)  # Amarelo
    time.sleep(1)  # Velocidade média
    set_color(0, 65535, 65535)  # Ciano
    time.sleep(1)  # Velocidade média
    set_color(65535, 0, 65535)  # Magenta
    time.sleep(2)  # Velocidade lenta
    set_color(0, 0, 0)  # Desliga o LED
    time.sleep(2)  # Velocidade lenta

"""Projeto AmbientSense RP2040"""

## Software: Estrutura de Dados e Fluxograma

Estrutura de Dados:
Dados organizados na estrutura DataPacket e convertidos para JSON, por exemplo:
json
Copiar
Editar
{
  "temp": 24.3,
  "umid": 58.7,
  "qualAr": 130,
  "lum": 350,
  "timestamp": "2025-02-17T10:00:00Z"
}

"""código para o WebGraphviz que representa toda a estrutura do AmbientSense RP2040"""

digraph AmbientSense {
    rankdir=TB;
    
    subgraph cluster_0 {
        label="Estrutura do AmbientSense RP2040";
        style=filled;
        color=lightgrey;
        
        Fonte_Alimentacao [label="Fonte de Alimentação\n(5V/3.3V)", shape=box, style=filled, fillcolor="#D3D3D3"];
        RP2040 [label="RP2040 da BitDogLab\n(Pico W)", shape=box, style=filled, fillcolor="#ADD8E6"];
        Sensores [label="Sensores Ambientais\n(Temperatura, Umidade, Gás, Luminosidade)", shape=box, style=filled, fillcolor="#98FB98"];
        Display [label="Display OLED\n(SPI/I2C)", shape=box, style=filled, fillcolor="#FFD700"];
        WiFi [label="Wi-Fi Integrado\n(TCP/IP)", shape=box, style=filled, fillcolor="#FF6347"];
        
        Fonte_Alimentacao -> RP2040 [label="3.3V"];
        RP2040 -> Sensores [label="I2C/ADC"];
        RP2040 -> Display [label="SPI/I2C"];
        RP2040 -> WiFi [label="TCP/IP"];
    }
}

"""copie este código e salve como main.py dentro da placa"""

import machine
import network
import ujson
import utime
import dht

# Configuração dos sensores
sensor_dht = dht.DHT22(machine.Pin(4))  # Pino do sensor DHT22
sensor_mq135 = machine.ADC(26)  # Pino do sensor MQ135

# Configuração do Wi-Fi
SSID = "SEU_WIFI"
SENHA = "SUA_SENHA"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, SENHA)

while not wlan.isconnected():
    utime.sleep(1)

print("Wi-Fi Conectado!")

# Loop principal
while True:
    sensor_dht.measure()
    temp = sensor_dht.temperature()
    umid = sensor_dht.humidity()
    qualidade_ar = sensor_mq135.read()
    
    data = ujson.dumps({"temp": temp, "umid": umid, "qualidade": qualidade_ar})
    print(data)
    
    utime.sleep(2)
