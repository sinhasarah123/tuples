import pygame
import random
# Initialize pygame
pygame.init()


# Custom event IDs for color change events
sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2


# Define basic colors using pygame.Color
# Background colors
blue=pygame.Color('blue')
light_blue=pygame.Color('lightblue')
dark_blue=pygame.Color('darkblue')

# Sprite colors
yellow=pygame.Color('yellow')
magenta=pygame.Color('magenta')
orange=pygame.Color('orange')
white=pygame.Color('white')

# Sprite class representing the moving object
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.x += self.velocity[0]
        boundry_hit = False
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top < 0 or self.rect.bottom > 400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))
    def change_color(self):
        self.image.fill(random.choice([yellow, magenta, orange, white]))
    

def change_background_color():
    global background_color
    background_color = random.choice([blue, light_blue, dark_blue])

all_sprites_list=pygame.sprite.Group()
sp1=sprite(yellow,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,380)
all_sprites_list.add(sp1)
screen=pygame.display.set_mode([500,400])
pygame.display.set_caption('Sprite Bounce with Color Change')
background_color=blue
screen.fill(background_color)
exit=False
clock=pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==sprite_color_change_event:
            sp1.change_color()
        elif event.type==background_color_change_event:
            change_background_color()
    all_sprites_list.update()
    screen.fill(background_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()    
    clock.tick(240)
pygame.quit()
    # Call to the parent class (Sprite) constructor

    # Create the sprite's surface with dimensions and color

    # Get the sprite's rect defining its position and size

    # Set initial velocity with random direction


  # Method to update the sprite's position

    # Move the sprite by its velocity

    # Flag to track if the sprite hits a boundary

    # Check for collision with left or right boundaries and reverse direction

    # Check for collision with top or bottom boundaries and reverse direction

    # If a boundary was hit, post events to change colors


  # Method to change the sprite's color



# Function to change the background color



# Create a group to hold the sprite

# Instantiate the sprite

# Randomly position the sprite

# Add the sprite to the group

# Create the game window

# Set the window title

# Set the initial background color

# Apply the background color

# Game loop control flag

# Create a clock object to control frame rate


# Main game loop

  # Event handling loop

    # If the window's close button is clicked, exit the game

    # If the sprite color change event is triggered, change the sprite's color

    # If the background color change event is triggered, change the background color


  # Update all sprites

  # Fill the screen with the current background color

  # Draw all sprites to the screen


  # Refresh the display

  # Limit the frame rate to 240 fps

# Uninitialize all pygame modules and close the window

