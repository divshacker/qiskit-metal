# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""File contains dictionary for Rectangle and the make()."""

from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.base import QComponent


class Rectangle(QComponent):
    """A single configurable square.

        Inherits QComponent class.

        The class will add default_options class Dict to QComponent class before calling make.

        Default Options:
            * width: '500um'
            * height: '300um'
            * pos_x: '0um'
            * pos_y: '0um'
            * rotation: '0'
            * subtract: 'False'
            * helper: 'False'
            * chip: 'main'
            * layer: '1'
    """

    default_options = Dict(width='500um',
                           height='300um',
                           pos_x='0um',
                           pos_y='0um',
                           rotation='0',
                           subtract='False',
                           helper='False',
                           chip='main',
                           layer='1')
    """Default drawing options"""

    def make(self):
        """
        The make function implements the logic that creates the geoemtry
        (poly, path, etc.) from the qcomponent.options dictionary of parameters,
        and the adds them to the design, using qcomponent.add_qgeometry(...),
        adding in extra needed information, such as layer, subtract, etc.
        """
        p = self.p  # p for parsed parameters. Access to the parsed options.

        # create the geometry
        rect = draw.rectangle(p.width, p.height, p.pos_x, p.pos_y)
        rect = draw.rotate(rect, p.rotation)
        ##############################################
        # add qgeometry
        self.add_qgeometry('poly', {'rectangle': rect},
                           subtract=p.subtract,
                           helper=p.helper,
                           layer=p.layer,
                           chip=p.chip)
