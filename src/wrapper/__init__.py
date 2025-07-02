"""
This module wraps and simplifies access to engine dependencies like pygame and pymunk.

It provides helper functions or classes that unify interfaces (such as vectors, shapes, etc.).
"""

from .shapes import Shape,Rect,Circle
from .text import Text
from .image import Image
from .music import Music
from .sfx import SoundEffect
from .functions import vector, rect
