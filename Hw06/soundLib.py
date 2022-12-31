# ISE 150 soundLib
# Wav file creator and player

import numpy as np
from scipy.io.wavfile import write
import simpleaudio as sa

# Sample rate per second for waves
SAMPLE_RATE = 44100

# Filename for final output
WAV_FILE_NAME = "output.wav"

# BPM range
MIN_BPM = 50
MAX_BPM = 300
currentBmp = 150

# Make the sounds as loud as possible
AMPLITUDE = np.iinfo(np.int16).max

# Setup for musical notes
NOTE_NAMES = list("CcDdEFfGgAaB")
noteDict = {}
BASE_FREQ = 16.3516
NUM_OCTAVES = 9

# Holds the note names and durations
song = []

def getWave(freq, beats):
    '''
    Returns a sine-wave representing the note for a particular number of beats
    :param freq: A frequency in Hz
    :param beats: A number of beats (can be fractions of a beat)
    :return: A wave -- which is really just a NumPy array of the samples
    '''
    # Determine how many seconds the note should play
    duration = float(beats) / float(currentBmp) * 60.

    # Calculate how many samples the note should be
    time = np.linspace(0, duration, int(SAMPLE_RATE * duration))

    # Generate the wave that represents the beep
    wave = AMPLITUDE * np.sin(2 * np.pi * freq * time)

    return wave



def genNotes(noteDict):
    '''
    Generates the note names and frequencies and stores them into the inputted dictionary
    :param noteDict: An empty dictionary to recieve the key/value pairs of noteName & frequency (in Hz)
    :return: None
    '''
    currBase = BASE_FREQ
    for j in range(NUM_OCTAVES):
        for i in range(len(NOTE_NAMES)):
            # Generate the right note name
            currNote = ""
            possibleFlat = ""
            if (NOTE_NAMES[i].islower()):
                currNote = NOTE_NAMES[i].upper() + str(j) + "sharp"
                possibleFlat = NOTE_NAMES[i+1].upper() + str(j) + "flat"
            else:
                currNote = NOTE_NAMES[i] + str(j)

            # Generate the right note frequency
            noteWave = currBase * pow(2, (i / float(len(NOTE_NAMES))))

            # Add it to the dictionary
            noteDict[currNote] = noteWave

            # Handle the flat if it's there
            if possibleFlat:
                noteDict[possibleFlat] = noteWave

        # Done with one octave, move up an octave
        currBase *= 2

    # add a rest
    noteDict["rest"] = 0




def initSound():
    '''
    Initializer for the sound system
    TODO: could add BPM adjustments
    :return: None
    '''
    # Generate the note frequencies
    genNotes(noteDict)

    # initialize song list
    song.clear()


def addNote(noteName, beats):
    '''
    Adds a note to the "song" array -- that's just a series of strings
    with each element of the form "noteName,beats" -- so an example would be
    ["C4,1", "D4sharp,0.5"]
    :param noteName: The name of the note, in the form of "C4", "G2sharp" or "B6flat"
    :param beats: Number of beats (can be fractional
    :return: None
    '''
    song.append(noteName + "," + str(beats))


def playSound():
    '''
    Uses the song array to generate sound waves to make a song
    :return:
    '''

    # Setup final sound output
    output = []

    # Go through all the elements made up of "note,beat" strings.
    for pair in song:
        # Get note name and beats
        noteName = pair.split(",")[0]
        noteBeats = float(pair.split(",")[1])

        # get the frequency of the note and add it to the output
        output.append(getWave(noteDict[noteName], noteBeats))

        # add a tiny rest to break up the notes
        output.append(getWave(noteDict["rest"], 0.1))

    # Put all the waves together
    fileOutput = np.concatenate(output)

    # Write out the final WAV file
    write(WAV_FILE_NAME, SAMPLE_RATE, fileOutput.astype(np.int16))

    # Play the final WAV file
    waveObj = sa.WaveObject.from_wave_file(WAV_FILE_NAME)
    playObj = waveObj.play()
    playObj.wait_done()


def addMorseDot():
    song.append("C4" + "," + str(0.5))

def addMorseDash():
    song.append("C4" + "," + str(1))

def addMorsePause():
    song.append("rest, " + str(2))


