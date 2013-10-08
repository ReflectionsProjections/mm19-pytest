#! /usr/bin/env python2

# Basic Test Client for MechMania 19
# Copyright (c) 2013 Association for Computing Machinery at the University
# of Illinois, Urbana-Champaign. Inherits license from main MechMania 19 code.

import json
import logging
import random

import Ship

class Client(object):
    """
    A class for managing the client's connection.

    TODO (competitors): You should add the API functions you need here. You can
    remove the inheritance from object if "new style" classes freak you out, it
    isn't important.
    """

    def __init__(self, address, name):
        """
        Initialize a client for interacting with the game.

        address -- The fully qualified server address
            (e.g. "http://example.com:8000")
        name -- Unique name of the client connecting
        """
        self.address = address
        self.name = name

    def prep_game(shiparray):
        """
        Handle all the pre-work for game setup.

        This function won't return until the server is connected and the game
        begins. There's no real need to call it asynchronously, as you can't
        actually do anything until the server is connected.

        shiparray -- The initial positions for all ships
        """

        logging.info("Connection target is %s", self.address)
        payload = {'playerName': self.name}
        # TODO (competitors): This is really ugly because the main ship is
        # special cased. I'm sorry. Feel free to fix.
        payload['mainShip'] = ships[0].getJSON()
        payload['ships'] = [ship.getJSON() for ships in ships[1:]]
        # TODO (dylan): Actually send something here

def main():
    establish_logger(logging.DEBUG)
    ships = generate_ships()

    # TODO (competitors): Change the client name, update ship positions, etc.
    client = Client("http://localhost:6969", "Whatever it's 2009")
    client.prep_game(ships)


def establish_logger(loglevel):
    logging.basicConfig(format="%(asctime)s %(message)s",
            datefmt='%m/%d/%Y %I:%M:%S %p', level=loglevel)
    logging.debug("Logger initialized")

def generate_ships():
    """This generates ships non-strategically for testing purposes."""
    # Let's get some ships
    ships = []
    ships.add(Ship("M", 5, 5, "H"))
    ships.add(Ship.random_ship("D"))
    ships.add(Ship.random_ship("D"))
    ships.add(Ship.random_ship("P"))
    ships.add(Ship.random_ship("P"))
    return ships

if __name__ == "__main__":
    main()
