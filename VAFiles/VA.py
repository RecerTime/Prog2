import tkinter as tk
import random
import numpy as np
import concurrent.futures as future

canvas_width = 1900
canvas_height = 1000

sim_speed = 1
num_particles = 50

canvas = None
particles = None

G = 10
bounce_damp = 0.8

after_id = None

rad_max = 15

class Particle:
    def __init__(self, pos: np.array, vel: np.array = None, radius: np.array = None):
        self.pos = pos

        if vel:
            self.vel = vel
        else:
            self.vel = 0.05*np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
        
        if radius:
            self.radius = radius
        else:
            self.radius = random.uniform(rad_max/2, rad_max)

    def update_pos(self):
        self.pos += self.vel

        # Boundary collision
        if self.pos[0] - self.radius < 0 or self.pos[0] + self.radius > canvas_width:
            self.vel[0] *= -bounce_damp
        if self.pos[1] - self.radius < 0 or self.pos[1] + self.radius > canvas_height:
            self.vel[1] *= -bounce_damp
   
        self.pos[0] = max(self.radius, min(canvas_width - self.radius, self.pos[0]))
        self.pos[1] = max(self.radius, min(canvas_height - self.radius, self.pos[1]))

def initialize_particles(num_particles):
    global particles
    particles = [Particle(np.array([random.uniform(0, canvas_width), random.uniform(0, canvas_height)]))
             for _ in range(int(num_particles))]
    
def update():
    canvas.delete("all")

    for i, p in enumerate(particles):
        p.update_pos()

        # Check for collisions
        for p2 in particles[i+1:]:
            direction = p2.pos - p.pos
            distance = np.linalg.norm(direction)
            normal = direction / distance

            p.vel += normal * G * p2.radius / distance**2
            p2.vel -= normal * G * p.radius / distance**2
            
            if distance <= p.radius + p2.radius:
                v_normal = np.dot(p2.vel - p.vel, normal)

                p.vel += bounce_damp*v_normal*normal
                p2.vel -= bounce_damp*v_normal*normal
            
        canvas.create_oval(
            p.pos[0] - p.radius, 
            p.pos[1] - p.radius, 
            p.pos[0] + p.radius, 
            p.pos[1] + p.radius, 
            fill="cyan", 
            outline=""
        )

    global after_id
    after_id = canvas.after(int(16/sim_speed), update)  # Update every 16/sim_speed ms

def stop():
    canvas.after_cancel(after_id)

def start():
    if after_id != None:
        stop()

    apply()
    initialize_particles(num_particles)
    update()

def apply():
    global num_particles
    global sim_speed
    global G

    if num_particles != int(particle_box.get()):
        num_particles = int(particle_box.get())
        initialize_particles(num_particles)

    sim_speed = float(speed_box.get())
    G = float(G_box.get())

if __name__ == "__main__":
    window = tk.Tk()
    window.title("VA")
    
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
    canvas.pack()
                
    frame = tk.Frame(window)
    frame.pack(pady=10)
        
    tk.Label(frame, text="Number of Particles:").grid(row=0, column=0)
    particle_box = tk.Entry(frame)
    particle_box.grid(row=0, column=1)
    particle_box.insert(0, f'{num_particles}')

    tk.Label(frame, text="Simulation Speed:").grid(row=1, column=0)
    speed_box = tk.Entry(frame)
    speed_box.grid(row=1, column=1)
    speed_box.insert(0, f'{sim_speed}')

    tk.Label(frame, text="Gravitational Constant:").grid(row=2, column=0)
    G_box = tk.Entry(frame)
    G_box.grid(row=2, column=1)
    G_box.insert(0, f'{G}')

    start_button = tk.Button(frame, text='Start', command=start)
    start_button.grid(row=0, column=2)

    stop_button = tk.Button(frame, text='Stop', command=stop)
    stop_button.grid(row=1, column=2)

    apply_button = tk.Button(frame, text='Apply', command=apply)
    apply_button.grid(row=2, column=2)

    canvas.mainloop()