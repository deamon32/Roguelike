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


def simulation(cowboys_aliens_tupple):
    """
    Simulation will fight Cowboys vs Aliens to the death and print out how many turns it took and how many of each unit
    is left after one side has been wiped out

    cowboys_aliens_tupple: Tupple that contains the number of cowboys and aliens used in the simulation


    :return: None
    """

    # Our constants
    CONST_COWBOY_HEALTH = 100
    CONST_COWBOY_ATTACK_POWER = 35
    CONST_COWBOY_PERCENT_TO_HIT = 0.5
    CONST_ALIEN_HEALTH= 200
    CONST_ALIEN_ATTACK_POWER = 20
    CONST_ALIEN_PERCENT_TO_HIT = 0.2

    number_of_rounds = 0  # Initializes number of rounds variable
    cowboys_alive = cowboys_aliens_tupple[0]  # Initializes variable from user input
    aliens_alive = cowboys_aliens_tupple[1]  # Initializes variable from user input

    # Main loop until either cowboys or aliense alive are 0
    while cowboys_alive > 0 and aliens_alive > 0:
        cowboy_health = CONST_COWBOY_HEALTH  # Initializes the cowboy_health variable
        alien_health = CONST_ALIEN_HEALTH  # Initializes the alien_health variable

        # Loop until either cowboy_health or alien_health drops to 0 or below, signaling that unit has died
        # When unit dies it needs to be removed from the alive variable for the specific unit, it may be possible that
        # Both a cowboy and alien die in the same attack round as attacks sre simultaneously
        # This is how the main loop will exit after one or bowh units reach zero and determine a draw or winner

        while cowboy_health > 0 and alien_health > 0:
            alien_health = attack(alien_health, CONST_COWBOY_ATTACK_POWER, CONST_COWBOY_PERCENT_TO_HIT)  # Cowboy attack round
            cowboy_health = attack(cowboy_health, CONST_ALIEN_ATTACK_POWER, CONST_ALIEN_PERCENT_TO_HIT)

            number_of_rounds += 1

        if cowboy_health <= 0:  # Check if cowboy died and reduce alive cowboys by one
            cowboys_alive -= 1
        if alien_health <= 0:  # Check if alien died and reduce alive aliens by one
            aliens_alive -= 1

    #  Determines the winner, or if the game ended in a draw
    if cowboys_alive > 0:
        print('Cowboys WON!')
    elif aliens_alive > 0:
        print('Aliens WON!')
    else:
        print ("It's a Draw.")

    print('Number of Cowboys left alive: {}\n'
          'Number of Aliens left alive: {}\n'
          'Number of combat rounds: {}'.format(cowboys_alive, aliens_alive, number_of_rounds))


def get_input():
    """
    Function will ask the user how many units of Cowboys and Aliens he would like to simulate in combat and returns
    it in a tupple

    :return: tuple(number_of_cowboys, number_of_aliens)
    """

    print('Please enter the number of Cowboys you would like to fight with: ')
    cowboys = int(input())

    print('Please enter the number of Aliens you would like to fight with: ')
    aliens = int(input())
    cowboys_aliens = (cowboys, aliens)

    return cowboys_aliens


def run_again():
    """Asks the user if he wants to simulate the fight once again using the same number of units.


    :return: Boolian - if the user wants to run the previous simulation once more
    """

    print('Do you want to run the simulation again?: [Y]/n')
    choice = input()

    if choice.lower() == 'n':
        return False
    else:
        return True


def attack(health, attack_power, percent_to_hit):
    """Function that simulates a single attack round

    health - starting health of the unit being attacked
    attack_power - the attack power which dertermines damage done to the attacked unit if the attack hits
    percent_to_hit - the chance that an attack will hit or miss

    :return: Integer - Health of the attacked unit
    """

    import random

    if random.random() < (1 - percent_to_hit):  # Attack misses and does zero damage
        return health
    else:  # Arrack hits and health gets reduced by the attack power
        return (health - attack_power)




def main():
    ''' Main function

    :return: None
    '''
    cowboys_aliens = get_input()  # Stores the tuple of cowboys and aliens in cowboys_aliens

    simulate = True
    while(simulate):
        simulation(cowboys_aliens)  # Calls the main simlate function where everything will happen
        simulate = run_again()  # Checks if the user would like to simulate again


if __name__ == "__main__":
    main()
