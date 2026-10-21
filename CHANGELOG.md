# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

- fixed: since 0.7.0, the item stopped with a filename error when there was nothing to capture (all options off, or only the PsychoPy option with another backend); it does nothing again, as 0.6.1 did with all options off

## [0.7.2] - 2026-10-17

- fixed regressions from 0.7.0: the "saved to" message shows the normalised log folder again, and the PsychoPy checkbox keeps its original tooltip with the PsychoPy backend
- note on 0.7.0: the filename is read once per screenshot, so all captures get the same name; before 0.7.0 an expression such as `{clock.time()}` was evaluated per capture

## [0.7.1] - 2026-10-17

- the version label in the item is read from the installed package, so the version is only set in `pyproject.toml`

## [0.7.0] - 2026-10-17

- fixed unclear error when the filename is empty or has no or an unsupported extension
- the PIL options now also work with other backends than PsychoPy; the PsychoPy option is then disabled in the GUI and skipped with a warning
- the subject folder now uses the subject number at the time of the screenshot, so an earlier inline script can change it
- the monitor size is only looked up when the PIL stimulus display option is on
- code cleanup: removed py3compat, read settings once in prepare, removed duplicate code
- fixed license in package metadata (was shown as proprietary on PyPI)
- added pillow as dependency
- updated readme

## [0.6.1] - 2025-09-12

- fixed PIL checkboxes not working

## [0.6.0] - 2025-09-12

- added capture of stim display with PIL

## [0.5.0] - 2025-09-05

- convert string handling to f-strings

## [0.4.0] - 2025-07-17

- license cleanup

## [0.3.0] - 2024-12-21

- added info about mandatory filename extension
- fixed windows not capturing all screens

## [0.2.0] - 2024-10-01

- for stimulus screenshot getMovieFrame() was replaced with \_getFrame()
- added composite of all displays option through ImageGrab.grab()

## [0.1.1] - 2024-09-18

- check for psychopy as backend

## [0.1.0] - 2024-09-18

Initial release of OpenSesame Screenshot plugin.


[Unreleased]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.7.2...HEAD
[0.7.2]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.7.1...0.7.2
[0.7.1]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.6.1...0.7.0
[0.6.1]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/dev-jam/opensesame-plugin-screenshot/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/dev-jam/opensesame-plugin-screenshot/releases/tag/0.1.0
