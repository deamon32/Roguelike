"""Combat Simulator
Challenge one: https://www.youtube.com/watch?v=n2ybTZbOHP8&t=1001s

Cowboys vs Aliens

Requirements:
    * Cowboys and aliens attach each other to the death
    * Each cowboy and alien have a chance to hit < 100%
    * Player can input the number of cowboys and number of aliens
    * Rerun simulation with same input

Design:
    Data:
        Cowboys:
            Health: 100
            attack power: 35
            percent to hit: 0.5 (50%)
        Aliens:
            Health: 200
            attack power: 20
            percent to hit: 0.2 (20%)
        Set random seed

    Functions:
        Attack:
            health
            attack power
            percent to hit
        Simulation:
            how many cowboys? Default: 40
            how many aliens? Default: 500
        Capture input:
            numbers
            rerun

Implementation:

Test:

"""