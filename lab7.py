
import time
import RPi.GPIO as GPIO
import mcp3008


LED_channel = 11
# Change
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_channel, GPIO.OUT)

# Initialize values before starting main loop
count = 0
light = 0
sound = 0
string = ""
on = False


while True:
    print("Testing Light")
    while count <= 50:
        adc = mcp3008.MCP3008()
        light = adc.read([mcp3008.CH0])  #light
        if int(light) > 20:   #threshold
            string = "Raw: " +str(light)+ ", is Bright"
        else:
            string = "Raw: " +str(light)+ ", is Dim"

        print(string)
        adc.close()
        time.sleep(0.100)   # 100 ms
        count += 1
        if count % 5 == 0 and count <= 25:
            if on:
                GPIO.output(LED_channel, GPIO.LOW)
                on = False
            else:
                GPIO.output(LED_channel, GPIO.HIGH)
                on = True
    
    count = 0
    print("Testing Sound")
    while count <= 50:
        adc = mcp3008.MCP3008()
        sound = adc.read([mcp3008.CH1])  #sound
        string = "Raw: " + str(sound)

        if int(sound) > 500: #threshold
            GPIO.output(LED_channel, GPIO.HIGH)
            time.sleep(0.100)
            GPIO.output(LED_channel, GPIO.LOW)

        print(string)
        adc.close()
        time.sleep(0.100)   # 100 ms
        count += 1
        if count % 2 == 0 and count <= 8:
            if on:
                GPIO.output(LED_channel, GPIO.LOW)
                on = False
            else:
                GPIO.output(LED_channel, GPIO.HIGH)
                on = True
    count = 0

