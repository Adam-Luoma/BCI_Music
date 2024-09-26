from pylsl import StreamInfo, StreamOutlet, local_clock
from psychopy import visual, sound, core, event as psychopy_event
from Chord_Class import *
import random
import time

# initialize various chord recordings
Cmaj = Chord('Cmaj','Cmaj.wav','tonic')
Amin = Chord('Amin','Amin.wav','tonic')
Fmaj = Chord('Fmaj','Fmaj.wav','sub_dom')
Dmin = Chord('Dmin','Dmin.wav', 'sub_dom')
Gmaj = Chord('Gmaj','Gmaj.wav','dom')
Bmin_dim = Chord('Bmin_dim','Bmin_dim.wav', 'dom')

chord_list = [Cmaj, Fmaj, Gmaj, Dmin, Bmin_dim]

# initialize backing track
Drums = sound.Sound("drum_backing.wav")

#Map timing to Unix epoch for IDUN
unix_offset = time.time() - local_clock()

marker_info = StreamInfo(name = 'MarkerStream', 
                         type = 'Markers', 
                         channel_count = 1, 
                         nominal_srate = 250,
                         channel_format='int32', 
                         source_id = 'Marker_Outlet')
marker_outlet = StreamOutlet(marker_info, 20, 360)

while True:
    win = visual.Window([800, 600], color='black')
    fixation = visual.TextStim(win, text='+', color='white', height=0.1)
    start_text = visual.TextStim(win, text='', color='white', height=0.1, pos=(0, 0))
     # Display  start message
    start_text.text = "Welcome to Music BCI, Press Enter to start."
    start_text.draw()
    win.flip()

    # Wait for Enter key to start the block
    while True:
        keys = psychopy_event.waitKeys()
        if 'return' in keys:
            break
        elif 'escape' in keys:
            win.close()
            core.quit()

    fixation.draw()
    win.flip()

    # initializing starting chord and length of progression
    current_chord = Cmaj
    progression_length = 1

    while progression_length < 4:
        chord_choices = []

        # depending on current chord function is, what subsequent chords should we look for (e.g. if the current chord has tonic function, we look for subdominant chords)
        if current_chord.function == 'tonic':
            for chord in chord_list:
                if chord.function == 'sub_dom':
                    chord_choices.append(chord)
                
        elif current_chord.function == 'sub_dom':
            for chord in chord_list:
                if chord.function == 'sub_dom':
                    chord_choices.append(chord) 

        elif current_chord.function == 'dom':
            for chord in chord_list:
                if chord.function == 'tonic':
                    chord_choices.append(chord) 

        two_options = random.sample(chord_choices, 2) # select 2 chords as options 

        decision = 0    #  holding 0 for BCI until it has made a decision on what chord is chosen

        while decision == 0:
            Drums.play()    #16 second long drum loop
            core.wait(1)    #wait 1 second before playing previously selected chord
            current_chord.audio.play() #play previously selected chord
            core.wait(1)    #wait 1 seconds





