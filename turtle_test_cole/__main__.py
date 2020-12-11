#Import the turtle library for  
# drawing the required curve 
import turtle as tt
import random
# Set the background color as black, 
# pensize as 2 and speed of drawing  
# curve as 10(relative) 
tt.pensize(2) 
tt.speed(10) 
  
# Iterate six times in total 
for i in range(random.randint(0,20)): 
    
      # Choose your color combination 
    for color in ('red', 'magenta', 'blue',  
                  'cyan', 'green', 
                  'yellow'): 
        tt.color(color) 
          
        # Draw a circle of choosen size, 100 here 
        tt.circle(random.randint(0,100)) 
          
        # Move 10 pixels left to draw another circle 
        tt.left(random.randint(-100,100)) 
      
    # Hide the cursor(or turtle) which drew the circle 
    tt.hideturtle()