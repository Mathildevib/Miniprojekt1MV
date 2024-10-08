import pygame
import math
from datetime import datetime 

pygame.init() # initializing pygame

# Set screen size and starting position in the centre. 
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
start_position = (screen_size[0] // 2, screen_size[1] // 2)  
radius = 200  # Large circle radius
line_length = 10  # Hour marker line lenght
line_length1 = 5  # 5 minute marker line lenght

# Main event loop to control program, clock object to control fps
running = True
clock = pygame.time.Clock() 

while running:
    #Reset the background color to white for every frame
    screen.fill([200, 200, 200])
    # Make 6 smaller circles around the large circle to represent flower petals
    for marker_angle2 in range(0, 360, 60):
        # Calculating the position of the small circles based upon the position of the large circle
        offset_x = radius * math.cos(math.radians(marker_angle2))
        offset_y = radius * math.sin(math.radians(marker_angle2))
        small_circle_position = (int(start_position[0] + offset_x), int(start_position[1] + offset_y))
        # Draw the smaller circles
        pygame.draw.circle(screen, (150, 0, 255), small_circle_position, 120, 0)
        pygame.draw.circle(screen, (150, 150, 255), small_circle_position, 100, 0)
        
    # Draw large circle in the centre to represent the smiley face
    pygame.draw.circle(screen, (255, 200, 10), start_position, radius, 0)

    #Drawing eyes in the top half of the circle (with pupils)
    pygame.draw.circle(screen, (150, 0, 255), start_position, 205, 5)
    pygame.draw.ellipse(screen, (255, 255, 255) , (300, 200, 50, 80))
    pygame.draw.ellipse(screen, (255, 255, 255) , (450, 200, 50, 80))
    pygame.draw.ellipse(screen, (0, 100, 255) , (315, 230, 20, 40))
    pygame.draw.ellipse(screen, (0, 100, 255) , (465, 230, 20, 40))
    pygame.draw.ellipse(screen, (0, 0, 0) , (470, 240, 10, 20))
    pygame.draw.ellipse(screen, (0, 0, 0) , (320, 240, 10, 20))
    
    #draw a arc to represent eyelids ( or an arc that has been filled in )
    eyelid_rect1 = (300, 200, 50, 50)  # left eyelid
    start_angle = 0
    end_angle = math.pi  
    pygame.draw.arc(screen, (175, 125, 6), eyelid_rect1, start_angle, end_angle, 100)
    eyelid_rect2 = (450, 200, 50, 50)  # right eyelid
    pygame.draw.arc(screen, (175, 125, 6), eyelid_rect2, start_angle, end_angle, 100)

    # Making a smiling mouth using an arc
    mouth_rect = (285, 250, 230, 160) 
    start_angle1 = math.pi
    end_angle1 = 0
    pygame.draw.arc(screen, (100, 0, 0), mouth_rect, start_angle1, end_angle1, 10)
    

    # Draw radiating short lines to represent hour markings (10 pixels in lenght) 
    for marker_angle in range(0, 360, 30):
        start_offset = [radius * math.cos(math.radians(marker_angle)), radius * math.sin(math.radians(marker_angle))]
        end_offset = [(radius - line_length) * math.cos(math.radians(marker_angle)),
                      (radius - line_length) * math.sin(math.radians(marker_angle))]
        line_start = (start_position[0] + start_offset[0], start_position[1] + start_offset[1])
        line_end = (start_position[0] + end_offset[0], start_position[1] + end_offset[1])
        pygame.draw.line(screen, (0, 0, 0), line_start, line_end, 4)

    # Draw smaller radiating lines to represent 5 minute intervals (5 pixels in lenght)
    for marker_angle1 in range(0, 360, 6):
        start_offset1 = [radius * math.cos(math.radians(marker_angle1)), radius * math.sin(math.radians(marker_angle1))]
        end_offset1 = [(radius - line_length1) * math.cos(math.radians(marker_angle1)),
                       (radius - line_length1) * math.sin(math.radians(marker_angle1))]
        line_start1 = (start_position[0] + start_offset1[0], start_position[1] + start_offset1[1])
        line_end1 = (start_position[0] + end_offset1[0], start_position[1] + end_offset1[1])
        pygame.draw.line(screen, (0, 0, 0), line_start1, line_end1, 2)

    # Define and get the current time to calculate clock hand position
    now = datetime.now()
    hour = now.hour % 12  # To fit the analog clock
    minute = now.minute
    second = now.second

     # Making the smiley wink when seconds = 0.
    if second == 0:
        pygame.draw.circle(screen, (175, 125, 6), start_position, 20, 0)
        pygame.draw.ellipse(screen, (255, 200, 10) , (300, 200, 50, 80))
        pygame.draw.line(screen,(0,0,0), (280, 240), (340, 240), 5)
        pygame.draw.line(screen,(0,0,0), (280, 240), (270, 235), 5)
    # Making the smiley gasp when seconds = 30 
    if second == 30:
        mouth_rect1 = (285, 250, 230, 160)
        start_angle1 = math.pi
        end_angle1 = 0
        pygame.draw.arc(screen, (255, 200, 20), mouth_rect1, start_angle1, end_angle1, 10)
        pygame.draw.circle(screen, (10, 25, 10), (400, 370), 50, 0)
        pygame.draw.circle(screen, (100, 0, 0), (400, 370), 50, 10)

    # Calculating angles for the clock hands (-90 degrees is to make the hands be at 12 when the angle is 0)
    second_angle = (second / 60) * 360 - 90  # 6 degrees every second
    minute_angle = (minute / 60) * 360 + (second / 60) * 6 - 90  # 6 degrees per minute and adjustment based upon seconds (how much of the minute has passed)
    hour_angle = (hour / 12) * 360 + (minute / 60) * 30 - 90  # 30 degrees per hour and adjustment based upon minutes.

    # Calculating the handposition (the distance and the position of the tip of the clock hands)
    second_hand_offset = [radius * 0.9 * math.cos(math.radians(second_angle)), radius * 0.9 * math.sin(math.radians(second_angle))]
    minute_hand_offset = [radius * 0.75 * math.cos(math.radians(minute_angle)), radius * 0.75 * math.sin(math.radians(minute_angle))]
    hour_hand_offset = [radius * 0.6 * math.cos(math.radians(hour_angle)), radius * 0.6 * math.sin(math.radians(hour_angle))]

    second_hand_position = (start_position[0] + second_hand_offset[0], start_position[1] + second_hand_offset[1])
    minute_hand_position = (start_position[0] + minute_hand_offset[0], start_position[1] + minute_hand_offset[1])
    hour_hand_position = (start_position[0] + hour_hand_offset[0], start_position[1] + hour_hand_offset[1])
    # drawing the clock hands (anti aliased lines for a smoother appearance)
    pygame.draw.aaline(screen, (0, 0, 0), start_position, second_hand_position, 1)  # seconds
    pygame.draw.aaline(screen, (0, 0, 0), start_position, minute_hand_position, 1)  # minutes
    pygame.draw.aaline(screen, (0, 0, 0), start_position, hour_hand_position, 1)  # hours

   # setting the fps (could be higher but only one is necessary)
    clock.tick(1)
    # Update the display with the new drawing
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
