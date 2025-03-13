
import time
import RPi.GPIO as GPIO
import mcp3008


LED_channel = 0

GPIO.setup(LED_channel, GPIO.OUT)

# Initialize values before starting main loop
count = 0
light = 0
sound = 0
string = ""
on = False


while True:
    while count >= 50:
        adc = mcp3008.MCP3008()
        light = adc.read([mcp3008.CH0])  #light
        if light > 1000:   #threshold
            string = f"Raw: {light}, is Bright\n"
        else:
            string = f"Raw: {light}, is Dim\n"

        print(string)
        adc.close()
        time.sleep(0.100)   # 100 ms
        count += 1
        if count % 5 == 0:
            if on:
                GPIO.ouput(LED_channel, GPIO.LOW)
                on = False
            else:
                GPIO.ouput(LED_channel, GPIO.HIGH)
                on = True
    
    count = 0
    while count >= 50:
        adc = mcp3008.MCP3008()
        sound = adc.read([mcp3008.CH1])  #sound
        string = f"Raw: {sound}\n"
        
        if sound > 1000: #threshold

            GPIO.ouput(LED_channel, GPIO.HIGH)
            time.sleep(0.100)
            GPIO.ouput(LED_channel, GPIO.LOW)

        print(string)
        adc.close()
        time.sleep(0.100)   # 100 ms
        count += 1
        if count % 5 == 0:
            if on:
                GPIO.ouput(LED_channel, GPIO.LOW)
                on = False
            else:
                GPIO.ouput(LED_channel, GPIO.HIGH)
                on = True
    count = 0


    