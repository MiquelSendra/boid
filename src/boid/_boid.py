import numpy as np
import matplotlib.pyplot as plt


class Boid:

    def update_velocity(self, *, dt: float) -> None:
        """
        Update the velocity of the boid based on its acceleration

        Args:
            dt: The time step for the simulation
        """
        # Write the code that updates the velocity of the boid based on its acceleration
        self.velocity += self.acceleration * dt

    def move_boid(self, *, dt: float) -> None:
        """
        Move the boid based on its velocity

        Args:
            dt: The time step for the simulation
        """
        self.position = self.position + self.velocity * dt
        # update the velocity below
        self.update_velocity(dt=dt)

    def plot_trajectory(self, *, dt: float, num_steps: int) -> None:
        """
        Plot the trajectory of the boid

        Args:
            dt: The time step for the simulation
            num_steps: The number of steps to simulate
        """
        # Write the code to plot the trajectory of the boid
        traj = np.empty(
            (2, num_steps), dtype=float
        )  # good practice to specify the type. np is on C++
        for i in range(num_steps):
            self.move_boid(dt=dt)
            traj[:, i] = self.position

        _, ax = (
            plt.subplots()
        )  # variables that you define and are not using puts them in bright blue, better practice then to put _
        ax.plot(*traj, "o-")
        ax.set_aspect("equal")

    def __init__(self, position, velocity, acceleration):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)


def run_app():
    my_obj = Boid("Hi!")
    print(f"{my_obj.arg = }")
