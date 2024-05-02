from controller import Robot, Keyboard

bot = Robot()
keyboard = Keyboard()

timestep = 64

keyboard.enable(timestep)

shoulder_lift = bot.getDevice("A motor")
shoulder_pan = bot.getDevice("B motor")
elbow = bot.getDevice("C motor")
wrist1 = bot.getDevice("D motor")
wrist2 = bot.getDevice("E motor")
wrist3 = bot.getDevice("F motor")

def moveBot(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist1.setPosition(d)
    wrist2.setPosition(e)
    wrist3.setPosition(f)
    
moveBot()

shoulder_lift_pos = 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist1_pos = 0
wrist2_pos = 0
wrist3_pos = 0

while bot.step(timestep) !=-1:
    keyPressed = keyboard.getKey()
#    print(keyPressed)
    
    if (keyPressed == 317):
        shoulder_lift_pos += 0.01
        
    elif(keyPressed == 315):
        shoulder_lift_pos -= 0.01
        
    elif(keyPressed == 314):
        shoulder_pan_pos += 0.01
        
    elif(keyPressed == 316):
        shoulder_pan_pos -= 0.01
        
    elif(keyPressed == 87):
        elbow_pos -= 0.01
        
    elif(keyPressed == 83):
        elbow_pos += 0.01
        
    elif(keyPressed == 65):
        wrist1_pos += 0.01
        
    elif(keyPressed == 68):
        wrist1_pos -= 0.01
        
    elif(keyPressed == 49):
        wrist2_pos += 0.01
        
    elif(keyPressed == 50):
        wrist2_pos -= 0.01
        
    elif(keyPressed == 51):
        wrist3_pos += 0.01
        
    elif(keyPressed == 52):
        wrist3_pos -= 0.01
        
    moveBot(shoulder_lift_pos, shoulder_pan_pos, elbow_pos, wrist1_pos, wrist2_pos, wrist3_pos)