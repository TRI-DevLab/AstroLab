# The file with the blue print to create Celestial bodies 

from collections import deque 

class CelestialBody:

    def __init__(
            self, 
            x: float,                       # current x position
            y: float,                       # current y position
            mass: float,                    # the mass of the celestial body - NP for calculations
            radius: int,                    # the radius of the celestial body - NP Drawing & Movement
            color: tuple[int, int, int]     # color of the celestial body
    ):

        # Positions 
        self.x = x
        self.y = y


        # Physical properties 
        self.mass = mass
        self.radius = radius


        # Velocity
        self.vx = 0.0                       # Velocities will be given later to establish their orbits
        self.vy = 0.0


        # Acceleration
        self.ax = 0.0
        self.ay = 0.0


        # Appearance 
        self.color = color


        # Movement history or Trail
        self.trail = deque(maxlen = 150)



def main():
    # Test Run making sure everything works 


    planet = CelestialBody(
        x = 400,
        y = 300,
        mass = 50,
        radius = 10,
        color = (80, 160, 225)
    )

    print(f"Position: (x: {planet.x}, y: {planet.y})")
    print(f"Mass: {planet.mass}")
    print(f"Velocity: (x: {planet.vx}, y: {planet.vy})")
    print(f"Acceleration: (x: {planet.ax}, y: {planet.ay})")
    print(f"Trail: {planet.trail}")

    

