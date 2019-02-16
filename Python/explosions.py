import random
import math
WIDTH = 800
HEIGHT = 600 # The size of the screen
DRAG = 0.8 # How much a particle slows down by each second
# The colour of each particle in R, G, B values
PARTICLE_COLOUR = 255, 230, 128
MAX_AGE = 3 # The time in seconds for which a particle is displayed
particles = [] # An array to hold the details of the explosion particles

def explode(x, y, speed=300): # Creates a new explosion at x,y co-ordinates
    age = 0 # These are new particles, so set their age to 0
    for _ in range(100): # Generate 100 particles per explosion
        # For each particle, generate a random angle and distance
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 1) ** 0.5
        # Convert angle and distance from the explosion into x and y velocity
        vx = speed * radius * math.sin(angle)
        vy = speed * radius * math.cos(angle)
        # Add the particle's position, velocity and age to the array
        particles.append((x, y, vx, vy, age))

def draw():
# This function redraws the screen by plotting each particle in the array
    screen.clear()
    for x, y, *_ in particles: # Loop through all the particles in the array
        # For each particle in the array, plot its position on the screen
        screen.surface.set_at((int(x), int(y)), PARTICLE_COLOUR)

def update(dt): # This function updates the array of particles
    new_particles = [] # To update the particle array, create a new empty array
    # Loop through the existing particle array
    for(x, y, vx, vy, age) in particles:
        #If a particle was created more than a certain time ago, it can be removed
        if age + dt > MAX_AGE:
            continue
        drag = DRAG ** dt # Update the particle's velocity - they slow down over time
        vx *= drag
        vy *= drag
        x += vx * dt
        y += vy * dt # Update the particle's position according to its velocity
        age += dt # Update the particle's age
        # Add the particle's new position, velocity and age to the new array:
        new_particles.append((x, y, vx, vy, age))
    particles[:] = new_particles # Replace current array with the new one

def explode_random(): # Creates an explosion at random location
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT) # Select a random position on the screen
    explode(x,y) # call the explosion function for that position

# Call the random explosion function every 1.5 seconds:
clock.schedule_interval(explode_random, 1.5)
        
