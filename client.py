#! /usr/bin/env python2

# Basic Test Client for MechMania 19
# Copyright (c) 2013 Association for Computing Machinery at the University
# of Illinois, Urbana-Champaign. Inherits license from main MechMania 19 code.

import json
import logging
import random
import socket

from ship import Ship

class Client(object):
    """
    A class for managing the client's connection.

    TODO (competitors): You should add the API functions you need here. You can
    remove the inheritance from object if "new style" classes freak you out, it
    isn't important.
    """

    def require_connection(func):
        """
        This is a decorator to wrap a function to require a server connection.

        func -- A Client class function with self as the first argument.
        """
        def wrapped(self, *args):
            if self.sock == None:
                logging.error("Connection not established")
            else:
                return func(self, *args)

        return wrapped

    def __init__(self, host, port, name):
        """
        Initialize a client for interacting with the game.

        host -- The hostname of the server to connect
                (e.g.  "example.com")
        port -- The port to connect on (e.g. 6969)
        name -- Unique name of the client connecting
        """
        self.host = host
        self.port = port
        self.name = name
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Connection target is %s:%d", self.host, self.port)
        self.sock.connect((self.host, self.port))
        logging.info("Connection established")

    @require_connection
    def prep_game(self, shiparray):
        """
        Handle all the pre-work for game setup.

        This function won't return until the server is connected and the game
        begins. There's no real need to call it asynchronously, as you can't
        actually do anything until the server is connected.

        shiparray -- The initial positions for all ships
        """

        payload = {'playerName': self.name}
        # TODO (competitors): This is really ugly because the main ship is
        # special cased. I'm sorry. Feel free to fix.
        payload['mainShip'] = shiparray[0].getJSON()
        payload['ships'] = [ship.getJSON() for ship in shiparray[1:]]
        # Send this information to the server
        self.sock.sendall(json.dumps(payload))

def main():
    establish_logger(logging.DEBUG)
    ships = generate_ships()

    # TODO (competitors): Change the client name, update ship positions, etc.
    client = Client("localhost", 6969, "Whatever it's 2009")
    client.connect()
    client.prep_game(ships)


def establish_logger(loglevel):
    logging.basicConfig(format="%(asctime)s %(message)s",
            datefmt='%m/%d/%Y %I:%M:%S %p', level=loglevel)
    logging.debug("Logger initialized")

def generate_ships():
    """This generates ships non-strategically for testing purposes."""
    # Let's get some ships
    ships = []
    ships.append(Ship("M", 5, 5, "H"))
    ships.append(Ship.random_ship("D"))
    ships.append(Ship.random_ship("D"))
    ships.append(Ship.random_ship("P"))
    ships.append(Ship.random_ship("P"))
    return ships

if __name__ == "__main__":
    main()
