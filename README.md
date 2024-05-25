This version is a basic implementation of a way to type japanese using a gamepad connected to the computer. This version is little more than a proof of concept. It is currently capable of:
- Connecting to a gamepad device
- Listening for keypresses and executing relevant functions
- Linking to arbitrary external objects and signaling to them when a button is pressed
- Doing the same with joystick data, but instead providing a constant stream
- Using the data from the joysticks to type varying japanese hiragana characters.
-- This is done by rotating the left stick to select a consonant and rotating the right stick to select a vowel. Pushing the right trigger types the character provided by these two inputs.
The upcoming versions will add:
- Visual feedback to let the user know which character will be typed if they select now
- The ability to switch typed hiragana characters to their katakana analog
- The ability to substitute a string of typed hiragana for a single matching kanji character
- the ability to switch the gamepad to 'interaction' mode so that the user can use it to navigate the desktop
