import pygame
import math
import random
import sys

pygame.init()
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart")
clock = pygame.time.Clock() 
size = min(WIDTH, HEIGHT) * 0.022
ticket = 0

class Particle: 
    def __init__(self, angle):
        self.angle = angle
        self.offset = random.random() * math.pi
        self.x = 0
        self.y = 0

    def move(self, current_ticket):
        noise = math.sin(self.angle + current_ticket + self.offset) * (0.3 * size)
        r = size + noise
        
        # Parametric equations for a heart shape
        self.x = r * 16 * (math.sin(self.angle) ** 3)
        self.y = -r * (
            13 * math.cos(self.angle)
            - 5 * math.cos(2 * self.angle)
            - 2 * math.cos(3 * self.angle)
            - math.cos(4 * self.angle)
        )
        self.angle += 0.004

particles = []
count = 2000 # Reduced to a manageable number for 60 FPS
for i in range(count):
    angle = i * (2 * math.pi / count)
    particles.append(Particle(angle))

# --- MISSING MAIN LOOP ADDED ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) # Clear screen

    # Center coordinates
    cx, cy = WIDTH // 2, HEIGHT // 2

    for p in particles:
        p.move(ticket)
        # Convert floating point math to screen coordinates
        draw_x = int(cx + p.x)
        draw_y = int(cy + p.y)
        
        # Draw particle (RGB Red)
        screen.set_at((draw_x, draw_y), (255, 50, 50))

    pygame.display.flip()
    clock.tick(60)
    ticket += 0.05 # Increment to animate the noise

pygame.quit()
sys.exit()