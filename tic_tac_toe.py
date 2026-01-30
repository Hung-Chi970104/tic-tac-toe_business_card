import machine
import utime

# Set buttons
button_left = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# Set location
location = 0

# Set current player
current_player = 1

# Set grid
grid = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
    ]

# Set corresponding pin numbers
player_1_LEDs_pin = [
    13, 7, 1,
    11, 5, 28,
    9, 3, 26
    ]

player_2_LEDs_pin = [
    12, 6, 0,
    10, 4, 27,
    8, 2, 22
    ]

# Assign pin number to corresponding LEDs
player_1_LEDs = []
player_2_LEDs = []

for pin in player_1_LEDs_pin:
    led = machine.Pin(pin, machine.Pin.OUT)
    player_1_LEDs.append(led)
    
for pin in player_2_LEDs_pin:
    led = machine.Pin(pin, machine.Pin.OUT)
    player_2_LEDs.append(led)
    
for led in player_1_LEDs:
    led.value(0)
for led in player_2_LEDs:
    led.value(0)

player_1_LEDs[location].value(1)

print(player_1_LEDs)
print(player_2_LEDs)

while True:
    # Press left button for next
    if button_left.value() == 0:
        print("Left Button Pressed")
        location += 1
        while button_left.value() == 0:
            utime.sleep_ms(1)

    if location > 8:
        location = 0
    while grid[location] != 0:
        location += 1
        if location > 8:
            location = 0
            
    # Press right button to select
    if button_right.value() == 0:
        print("Right Button Pressed")
        if current_player == 1:
            grid[location] = 1
            current_player = 2
        else:
            grid[location] = 2
            current_player = 1
        location = 0
        print(grid)
        while button_right.value() == 0:
            utime.sleep_ms(1)
        
    # Control selected LED
    if current_player == 1:
        for led in player_1_LEDs:
            led.value(0)
        player_1_LEDs[location].value(1)
        for led in player_2_LEDs:
            led.value(0)
    else:
        for led in player_2_LEDs:
            led.value(0)
        player_2_LEDs[location].value(1)
        for led in player_1_LEDs:
            led.value(0)
            
    # Light up current grid
    for led in range(len(grid)):
        if grid[led] == 1:
            player_1_LEDs[led].value(1)
        elif grid[led] == 2:
            player_2_LEDs[led].value(1)
            
    ### GAME LOGIC
