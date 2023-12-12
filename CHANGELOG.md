# Changelog

## [Version 1.0.0] - 2023-12-11

### Features
- Implemented GUI for the user
- Implemented 'Select File' button with functionality
- Implemented code to change aac or mp3 to wav
- Implemented 'Waveform' button to display audio file waveform
- Implemented 'High' button to display audio file RT60 with high frequency plot
- Implemented 'Low' button to display audio file RT60 with low frequency plot
- Implemented 'Mid' button to display audio file RT60 with mid frequency plot
- Implemented 'Combined' button to display audio file RT60 with high, mid, and low frequencies plot
- Implemented 'Spectrogram' button to display audio file spectrogram as choice function


### Bug Fixes
- Addressed critical bug in soundDisplay.py: high, low, and mid frequencies were not being pulled from the audio file, it was a manual input.
- Addressed critical bug in soundDisplay.py: difference was not being calculated, it was a manual input.
- Resolved issue with 'Alternate' button: fixed count to work