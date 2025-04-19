Monte Carlo Simulation
======================

===============
Throwing a Dice
===============

.. code-block:: python

    import random

    def dice():
        return random.randint(1, 6)

    def dice_simulation(n):
        return [dice() for _ in range(n)]

    n = 1000
    simulation = dice_simulation(n)
    print(simulation)


    