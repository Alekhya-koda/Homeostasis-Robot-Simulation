import robot, time, random, math
from controller import GPS

# Parameters
HUNGER = 1000
THIRST = 1000
SLEEP = 1000

# Variables
hunger_threshold = 500
thirst_threshold = 500
sleep_threshold = 500

# Functions
def eating():
    global HUNGER
    if HUNGER < 1000:
        HUNGER += 30

def sleeping():
    global SLEEP
    if SLEEP < 1000:
        SLEEP += 50

def drinking():
    global THIRST
    if THIRST < 1000:
        THIRST += 50

def alive():
    if SLEEP <= 0:
        return False
    elif HUNGER <= 0:
        return False
    elif THIRST <= 0:
        return False
    else:
        return True

def meta():
    global SLEEP, HUNGER, THIRST
    SLEEP -= 1
    HUNGER -= 0.2
    THIRST -= 0.2

# Randomised multiplier to move robot forward depending on distance to obstacles
def Behaviour0(object):
    value = 0.0
    if object.distance_range > 0.06 and object.distance_range <= 0.07:
        value = random.uniform(0.5, 0.9)
    elif object.distance_range > 0.05 and object.distance_range <= 0.06:
        value = random.uniform(0.3, 0.45)
    elif (object.distance_range > 0.03 and object.distance_range <= 0.05) or object.front_obstacles_detected():
        value = 0.0
    object.move(value, value)

# Avoid obstacles by turning left
def Behaviour1(object):
    object.move_backward()
    object.turn_left()

def Behaviour2(object):
    object.move_backward()
    object.turn_right()

# Move robot turn left 180 degrees
def Behaviour3(object):
    object.move_forward()
    object.turn_left()
    object.turn_left()
    object.turn_left()

def Behaviour4(object):
    object.move_forward()
    object.turn_right()
    object.turn_right()
    object.turn_right()
    
def localize(object):
    red = 0
    green = 0
    blue = 0
    
    red, green, blue = object.get_camera_image(5)  
    image =(red,green,blue)
    # color range for food 
    food_red_range = range(110, 140)
    food_green_range = range(150, 180)
    food_blue_range = range(130, 150)

    if (food_red_range.start <= red <= food_red_range.stop and
            food_green_range.start <= green <= food_green_range.stop and
            food_blue_range.start <= blue <= food_blue_range.stop):
      return food_x,food_y 
    return None, None

def updateSensors(object):
    global SLEEP, HUNGER, THIRST
    red = 0
    green = 0
    blue = 0

    # Determine the object based on RGB colours detected
    red, green, blue = object.get_camera_image(5)

    if (red >= 110 and red <= 140) and \
       (green >= 150 and green <= 180) and \
       (blue >= 130 and blue <= 150):
        print("I see food!!")
        eating()
    #print("I just ate, I'm too full!")


    elif(red >= 132 and red <= 183) and \
         (green >= 170 and green <= 192) and \
         (blue >= 155 and blue <= 185):
        print("I see water!!")
        drinking()
    #print("I am drinking water :)")


    if SLEEP < sleep_threshold:
        for i in range(15):
            sleeping()
        print("I just woke up!")
        time.sleep(5)
        

    if HUNGER < hunger_threshold:
        for i in range(5):
            eating()

    if THIRST < thirst_threshold:
        for i in range(4):
            drinking()

    # Decrement SLEEP, HUNGER, THIRST variables
    meta()

def main():
    range = 0.0
    robot1 = robot.ARAP()
    robot1.init_devices()

    while True and alive():
        try:
            robot1.reset_actuator_values()
            range = robot1.get_sensor_input()
            robot1.blink_leds()
            gps = GPS('gps')
            gps.enable(32)
            a = gps.getValues() 

            updateSensors(robot1)

            if robot1.front_obstacles_detected():
                robot1.move_backward()
                robot1.turn_left()
            else:
                robot1.run_braitenberg()

            robot1.set_actuators()
            robot1.step()

        except KeyboardInterrupt:
            break
        finally:
            if not alive():
                print("\nRobot is dead\n")

if __name__ == "__main__":
    main()
