import random
import numpy as np

# Step 1: PSO Parameters
NUM_PARTICLES = 30
DIMENSIONS = 2
MAX_ITERATIONS = 10
INERTIA = 0.7
COGNITIVE_WEIGHT = 1.49
SOCIAL_WEIGHT = 1.49
X_BOUND = (-10, 10)

def fitness(position):
  return sum([x**2 for x in position]) # the Sphere Function

class Particle:
  def __init__(self):
    self.position = np.array([random.uniform(X_BOUND[0], X_BOUND[1]) for _ in range(DIMENSIONS)])
    self.velocity = np.zeros(DIMENSIONS)
    self.best_position = np.copy(self.position)
    self.best_fitness = fitness(self.position)
  
  def update_velocity(self, global_best_position):
    inertia_component = INERTIA * self.velocity
    cognitive_component = COGNITIVE_WEIGHT * random.random() * (self.best_position - self.position)
    social_component = SOCIAL_WEIGHT * random.random() * (global_best_position - self.position)
    self.velocity = inertia_component + cognitive_component + social_component
  
  def update_position(self):
    self.position += self.velocity
    self.position = np.clip(self.position, X_BOUND[0], X_BOUND[1])

def pso():
  swarm = [Particle() for _ in range(NUM_PARTICLES)]
  global_best_position = min(swarm, key=lambda p: p.best_fitness).best_position
  global_best_fitness = fitness(global_best_position)

  for iteration in range(MAX_ITERATIONS):
    for particle in swarm:
      particle.update_velocity(global_best_position)
      particle.update_position()
      current_fitness = fitness(particle.position)
      if current_fitness < particle.best_fitness:
        particle.best_fitness = current_fitness
        particle.best_position = np.copy(particle.position)
      
      if current_fitness < global_best_fitness:
        global_best_fitness = current_fitness
        global_best_position = np.copy(particle.position)
  
    print(f"Iteration {iteration + 1}: Global Best Fitness = {global_best_fitness}")
  return global_best_position, global_best_fitness

best_position, best_fitness = pso()
print(f"Best Position: {best_position}, Best Fitness: {best_fitness}")

