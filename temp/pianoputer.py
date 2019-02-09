#!/usr/bin/env python

from scipy.io import wavfile
import argparse
import numpy as np
import pygame
import sys
import warnings
import time

def speedx(snd_array, factor):
    """ Speeds up / slows down a sound, by some factor. """
    indices = np.round(np.arange(0, len(snd_array), factor))
    indices = indices[indices < len(snd_array)].astype(int)
    return snd_array[indices]


def stretch(snd_array, factor, window_size, h):
    """ Stretches/shortens a sound, by some factor. """
    phase = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros(int(len(snd_array) / factor + window_size))

    for i in np.arange(0, len(snd_array) - (window_size + h), h*factor):
        i = int(i)
        # Two potentially overlapping subarrays
        a1 = snd_array[i: i + window_size]
        a2 = snd_array[i + h: i + window_size + h]

        # The spectra of these arrays
        s1 = np.fft.fft(hanning_window * a1)
        s2 = np.fft.fft(hanning_window * a2)

        # Rephase all frequencies
        phase = (phase + np.angle(s2/s1)) % 2*np.pi

        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
        i2 = int(i/factor)
        result[i2: i2 + window_size] += hanning_window*a2_rephased.real

    # normalize (16bit)
    result = ((2**(16-4)) * result/result.max())

    return result.astype('int16')


def pitchshift(snd_array, n, window_size=2**13, h=2**11):
    """ Changes the pitch of a sound by ``n`` semitones. """
    factor = 2**(1.0 * n / 12.0)
    stretched = stretch(snd_array, 1.0/factor, window_size, h)
    return speedx(stretched[window_size:], factor)


def parse_arguments():
    description = ('Use your computer keyboard as a "piano"')

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--wav', '-w',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='bowl.wav',
        help='WAV file (default: bowl.wav)')
    parser.add_argument(
        '--keyboard', '-k',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='typewriter.kb',
        help='keyboard file (default: typewriter.kb)')
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='verbose mode')

    return (parser.parse_args(), parser)


def main():
    # Parse command line arguments
    (args, parser) = parse_arguments()

    # Enable warnings from scipy if requested
    if not args.verbose:
        warnings.simplefilter('ignore')

    musicList = ["A2.wav", "Ds4.wav", "A4.wav", "A5.wav"]
    soundList = []
    for music in musicList:
      fps, sound = wavfile.read("/Users/kathleenruan/Documents/tartanhacks/temp/guitar-electric/"+music)
      soundList.append(sound)

    #tones = range(-25, 25)
    #sys.stdout.write('Transponding sound file... ')
    #sys.stdout.flush()
    #transposed_sounds = [pitchshift(sound, n) for n in tones]
    #print('DONE')

    # So flexible ;)
    pygame.mixer.init(fps, -16, 1, 2048)
    # For the focus
    screen = pygame.display.set_mode((150, 150))

    keys = args.keyboard.read().split('\n')
    sounds = map(pygame.sndarray.make_sound, soundList)
    key_sound = dict(zip(keys, sounds))
    is_playing = {k: False for k in keys}

    while True:
        event = pygame.event.wait()
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)
        if (event.type == pygame.KEYDOWN and key == "a"):
            #if (key in key_sound.keys()) and (not is_playing[key]):
            i = 0
            while True:
               print(i)
               i+=1
               sounds[0].play(fade_ms=10)
               time.sleep(0.2)
               sounds[1].play(fade_ms=10)
               time.sleep(0.2)  
 
        if (event.type == pygame.KEYDOWN and key == "d"):
            #if (key in key_sound.keys()) and (not is_playing[key]):
            sounds[1].play(fade_ms=200)


      

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
