import pygame as pg

from settings import *
from classes.portal import *

class Endportal(Portal):

    def __init__(self, pos, color, player, groups):
        super().__init__(pos, color, groups)

        self.type = "endportal-" + player