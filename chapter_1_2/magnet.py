import pygame
import math
import random
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Gravitational Swarm")
clock = pygame.time.Clock()

class Particle:
    def __init__(self):
        # Initial random placement across the screen
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        
        # Initial velocity (moving slightly in random directions)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        
        # Assign a dynamic color using HSV for a cohesive cyber/space palette
        self.color = pygame.Color(0, 0, 0)
        # Hue ranges from 180 (Cyan) to 280 (Purple)
        self.color.hsva = (random.uniform(180, 280), 100, 100, 100)

    def update(self, target_x, target_y):
        # 1. CALCULATE DISTANCE TO TARGET (The Gravity Well)
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)
        
        # Prevent division by zero and extreme slingshotting near the exact center
        if distance < 5:
            distance = 5

        # 2. GRAVITATIONAL PULL (Inverse-square law approximation)
        force = 500 / (distance ** 2) 
        angle = math.atan2(dy, dx)
        
        # Acceleration towards the center
        ax = math.cos(angle) * force
        ay = math.sin(angle) * force

        # 3. TANGENTIAL FORCE (The Swirl)
        # We rotate the angle by 90 degrees (pi/2) to apply force perpendicular to gravity
        tangent_angle = angle + math.pi / 2
        tax = math.cos(tangent_angle) * (force * 1.5)
        tay = math.sin(tangent_angle) * (force * 1.5)

        # 4. KINEMATICS: Update velocity with acceleration
        self.vx += ax + tax
        self.vy += ay + tay

        # 5. FRICTION/DRAG: Prevents infinite acceleration
        self.vx *= 0.96
        self.vy *= 0.96

        # 6. Apply final velocity to position
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        # Draw the particle
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 2)


# Generate the particle array
particles = [Particle() for _ in range(1500)]

# A separate surface to handle the fading trail effect
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a semi-transparent black box over the screen to create motion trails
    trail_surface.fill((0, 0, 0, 40))
    screen.blit(trail_surface, (0, 0))

    # The gravity well follows the mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # If the mouse leaves the window, default the gravity well to the center
    if not pygame.mouse.get_focused():
        mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2

    # Process physics and render
    for p in particles:
        p.update(mouse_x, mouse_y)
        p.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()