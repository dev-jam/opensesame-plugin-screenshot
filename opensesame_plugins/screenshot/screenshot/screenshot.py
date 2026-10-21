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

import os
from pathlib import Path
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from libopensesame.exceptions import OSException
from libopensesame.oslogging import oslogger
from PIL import Image, ImageGrab
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
        self._init_var()

        if self.window_stim_psycho and self.var.canvas_backend != 'psycho':
            oslogger.warning('Screenshot: stimulus display (PsychoPy) is skipped, it needs the PsychoPy backend')
            self.window_stim_psycho = False

        self.log_folder = Path(os.path.normpath(os.path.dirname(self.var.logfile)))

        if self.window_stim_pil:
            monitor = get_monitors()[0]
            self.bbox_stim = (monitor.x, monitor.y,
                              monitor.x + monitor.width,
                              monitor.y + monitor.height)

    def _init_var(self):
        self.verbose = self.var.verbose == 'yes'
        self.window_stim_psycho = self.var.window_stim_psycho == 'yes'
        self.window_stim_pil = self.var.window_stim_pil == 'yes'
        self.window_full_pil = self.var.window_full_pil == 'yes'

    def run(self):
        self.set_item_onset()

        if not (self.window_stim_psycho or self.window_stim_pil
                or self.window_full_pil):
            return

        filename = str(self.var.filename_screenshot)
        extension = Path(filename).suffix.lower()
        if Image.registered_extensions().get(extension) not in Image.SAVE:
            raise OSException(f'Screenshot filename "{filename}" needs an extension that determines the picture format, e.g. .png or .jpg')

        if self.window_stim_psycho:
            self._save(self.experiment.window._getFrame(),
                       'screenshots_stim_psycho', filename)
        if self.window_stim_pil:
            self._save(ImageGrab.grab(bbox=self.bbox_stim),
                       'screenshots_stim_pil', filename)
        if self.window_full_pil:
            self._save(ImageGrab.grab(all_screens=True),
                       'screenshots_full_pil', filename)

    def _save(self, image, folder, filename):
        # The folder is made in the run phase, because an earlier item may
        # change subject_nr in its run phase
        path = self.log_folder / folder / f'subject-{self.var.subject_nr}'
        path.mkdir(parents=True, exist_ok=True)
        fname = path / filename
        image.save(fname)
        self._show_message(f'Screenshot saved to: {fname}')

    def _show_message(self, message):
        oslogger.debug(message)
        if self.verbose:
            print(message)


class QtScreenshot(Screenshot, QtAutoPlugin):

    def __init__(self, name, experiment, script=None):
        Screenshot.__init__(self, name, experiment, script)
        QtAutoPlugin.__init__(self, __file__)

    def edit_widget(self):
        widget = super().edit_widget()
        # auto_edit_widget() enables all checkboxes, so this is done after it
        checkbox = self.checkbox_window_stim_psycho
        if not hasattr(self, '_tooltip_stim_psycho'):
            self._tooltip_stim_psycho = checkbox.toolTip()
        psychopy = self.var.canvas_backend == 'psycho'
        checkbox.setEnabled(psychopy)
        checkbox.setToolTip(self._tooltip_stim_psycho if psychopy
                            else 'Only available with the PsychoPy backend')
        return widget
