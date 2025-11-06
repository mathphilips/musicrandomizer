import random
import time
import sys

instruments = [
  # guitars
  'electric guitar',
  'nylon acoustic guitar',
  'steel acoustic guitar',
  'bass guitar',

  # percussive
  'drums',
  'cajon',
  'tambourine',
  'shakers',
  'claps',
  'snaps',

  # keyboards
  'upright piano',
  'grand piano',
  'electric piano',
  'rhodes electric piano',
  'hammond organ',
  'Yamaha GS1',
  'Yamaha DX7',

  # others
  "sitar",
  "xylophone",
  "marimba",
  "vibraphone",
  "accordion",

  # orchestral
  # strings
  'violin section',
  'viola section',
  'cello section',
  'double bass section',
  'string ensemble',

  # woodwinds
  'piccolo section',
  'flute section',
  'oboe section',
  'clarinet section',
  'bassoon section',
  'woodwind ensemble',

  # brass
  'horn section',
  'trumpet section',
  'tenor trombone section',
  'bass trombone section',
  'tuba section',
  'brass ensemble',
]

print("Welcome to Music Randomizer! Here your mind will be inspired with random things. Just relax.")
time.sleep(3)
print("By Matheus Philip.")
time.sleep(2)
print("Let's go...")
time.sleep(2)
print("Do you consider yourself a lucky person?")

resposta = input("Click 'Enter' to find out your lucky musical instrument. Click any other key to exit.\n")
if resposta != '':
    print("How sad. See you next time!")
    sys.exit()

print("Beautiful! Let it begin...")

print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(5)

while True:
  print("Thinking in instruments...")
  time.sleep(5)
  instrument = random.choice(instruments)
  print(f"Your instrument is: {instrument}!")
  time.sleep(2)

  want = input("Do you want another instrument? Press 'Enter' to raffle another instrument. Press any key to exit.\n")
  if want != '':
      print("See ya!")
      break