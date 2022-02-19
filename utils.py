import pygame

def scale_image(img,factor):
    size=round(img.get_width()*factor),round(img.get_height()*factor)
    return pygame.transform.scale(img,size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image=pygame.transform.rotate(image, angle)
    new_rect=rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


"""This is the code used to define the computer car path.
Include this code in the for loop in the while run loop.
if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            computer_car.path.append(pos)

Before the pygame.quit() at the end of the programme, you're also going to need to print the path list:

print(computer_car.path)
"""

def blit_text_centre(win,font,text):
    render=font.render(text,1,(200,200,200))
    win.blit(render,(int(win.get_width()/2 - render.get_width()/2), int(win.get_height()/2 - render.get_height()/2)))