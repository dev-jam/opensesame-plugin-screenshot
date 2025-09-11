"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Bob Rosbag"
__license__ = "GPLv3"

from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from libopensesame.exceptions import OSException
from libopensesame.oslogging import oslogger
from pathlib import Path
import os
from PIL import ImageGrab
from screeninfo import get_monitors


class Screenshot(Item):

    def reset(self):
        self.var.verbose = 'yes'
        self.var.window_stim_psycho = 'yes'
        self.var.window_stim_pil = 'yes'
        self.var.window_full_pil = 'no'
        self.var.filename_screenshot = ''

    def prepare(self):
        super().prepare()
        self.verbose = self.var.verbose

        if self.var.canvas_backend != 'psycho':
            raise OSException('Screenshot plugin only supports PsychoPy as backend')

        self.experiment_path = Path(os.path.normpath(os.path.dirname(self.var.logfile)))

        if self.var.window_stim_psycho == 'yes':
            self.path_stim_psycho = self.experiment_path / 'screenshots_stim_psycho' / f'subject-{self.var.subject_nr}'
            Path(self.path_stim_psycho).mkdir(parents=True, exist_ok=True)
        if self.var.window_stim_pil == 'yes':
            self.path_stim_pil = self.experiment_path / 'screenshots_stim_pil' / f'subject-{self.var.subject_nr}'
            Path(self.path_stim_pil).mkdir(parents=True, exist_ok=True)
        if self.var.window_full_pil == 'yes':
            self.path_full_pil = self.experiment_path / 'screenshots_full_pil' / f'subject-{self.var.subject_nr}'
            Path(self.path_full_pil).mkdir(parents=True, exist_ok=True)

        monitor1 = get_monitors()[0]
        self.x1 = monitor1.x
        self.y1 = monitor1.y
        self.x2 = monitor1.x + monitor1.width
        self.y2 = monitor1.y + monitor1.height

    def run(self):
        self.set_item_onset()

        if self.var.window_stim_psycho == 'yes':
            fname_stim_psycho =  self.path_stim_psycho / self.var.filename_screenshot
            image_stim_psycho = self.experiment.window._getFrame()
            image_stim_psycho.save(fname_stim_psycho)
            self._show_message(f'Screenshot saved to: {fname_stim_psycho}')
        if self.var.window_full == 'yes':
            fname_stim_pil =  self.path_stim_pil / self.var.filename_screenshot
            image_stim_pil = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))
            image_stim_pil.save(fname_stim_pil)
            self._show_message(f'Screenshot saved to: {fname_stim_pil}')
        if self.var.window_full == 'yes':
            fname_full_pil =  self.path_full_pil / self.var.filename_screenshot
            image_full_pil = ImageGrab.grab(all_screens=True)
            image_full_pil.save(fname_full_pil)
            self._show_message(f'Screenshot saved to: {fname_full_pil}')

    def _show_message(self, message):
        oslogger.debug(message)
        if self.verbose == 'yes':
            print(message)


class QtScreenshot(Screenshot, QtAutoPlugin):

    def __init__(self, name, experiment, script=None):
        Screenshot.__init__(self, name, experiment, script)
        QtAutoPlugin.__init__(self, __file__)
