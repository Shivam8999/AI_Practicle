import random
# Define the objective function (you can replace this with your own)
def objective_function(x):
    return -(x**2 + 4*x)  #Example: maximize x^2 + 4x (negate for max.)
    
def hill_climbing(max_iterations, step_size):
  current_solution = random.uniform(-10, 10)
  # returns random floating number between -10 & 10
  print(current_solution)
  current_value = objective_function(current_solution)
  for _ in range(max_iterations):
    neighbor = current_solution + random.uniform(-step_size, step_size)
    neighbor_value = objective_function(neighbor)
    if neighbor_value>current_value:
      current_solution = neighbor
      current_value = neighbor_value
  return current_solution, current_value

if __name__ == "__main__":
  max_iterations = 1000  # Maximum number of iterations
  step_size = 0.1  # Step size for making small changes
  final_solution, final_value = hill_climbing(max_iterations, 
step_size)
  print("Final Solution:", final_solution)
  print("Objective Value at Final Solution:", final_value)
