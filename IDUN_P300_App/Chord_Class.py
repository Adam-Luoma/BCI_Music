from psychopy import sound

class Chord:
    """A method for containing chords, their audio files and function in wester harmony"""
    def __init__(self, name, audio_file, function):
        self.name = name
        self.audio = sound.Sound(audio_file)
        self.function = function

