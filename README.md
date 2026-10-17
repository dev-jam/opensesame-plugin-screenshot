OpenSesame Plug-in: Screenshot
==========

*An OpenSesame plug-in for saving screenshots of stimuli and other screens within an experiment.*  

Copyright, 2024, Bob Rosbag  


## About

This plug-in saves screenshots of stimuli and other screens within an experiment.

The screenshots are saved in the folder of the log file, in a subfolder per capture method and subject, for example `screenshots_stim_psycho/subject-1/filename.png`.

This plug-in has the following options:

- *Verbose mode*: print the path of each saved screenshot.
- *Stimulus display (PsychoPy)*: capture the PsychoPy window, saved in `screenshots_stim_psycho`. Only available with the PsychoPy backend.
- *Stimulus display (PIL)*: capture the first monitor with PIL, saved in `screenshots_stim_pil`.
- *Composite of all displays (PIL)*: capture all monitors with PIL, saved in `screenshots_full_pil`.
- *Filename*: the filename with extension; the extension determines the picture format (`.png`, `.jpg`, etc.). Variables can be used, e.g. `trial_[count_trial_sequence].png`.


## License

This software is distributed under the terms of the GNU General Public License 3. The full license should be included in the file `COPYING`, or can be obtained from:

- <http://www.gnu.org/licenses/gpl.txt>

This plug-in contains works of others. Icons are derivatives of the Faenza icon theme.

  
## Documentation

Installation instructions and documentation on OpenSesame are available on the documentation website:

- <http://osdoc.cogsci.nl/>
