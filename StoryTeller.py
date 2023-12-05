import random

import pyttsx3
import pyglet

txt_speech = pyttsx3.init()

txt_speech1 = pyttsx3.init()

txt_speech2 = pyttsx3.init()

txt_speech3 = pyttsx3.init()

when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']

who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']

went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']

what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']

p1 = (random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(
    what) + '.')

Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']

character = [' there lived a king.', ' there was a man named Jack.',

             ' there lived a farmer.']

time = [' One day', ' One full-moon night']

story_plot = [' he was passing by', ' he was going for a picnic to ']

place = [' the mountains', ' the garden']

second_character = [' he saw a man', ' he saw a young lady']

age = [' who seemed to be in late 20s', ' who seemed very old and feeble']

work = [' searching something.', ' digging a well on roadside.']

p2 = (random.choice(Sentence_starter) + random.choice(character) +

      random.choice(time) + random.choice(story_plot) +

      random.choice(place) + random.choice(second_character) +

      random.choice(age) + random.choice(work))

p3 = """There was once a fisherman whose livelihood depended on his catch.One day, he was able to catch only one small fish.

The fish, in its desperation to live, says Please leave me kind sir. I am small and of no use to you. Let me back into the river and

I can grow bigger. You can then catch me and make more money.

The wise fisherman replies, I will not give up a certain profit for one that

doesn’t exist yet.

Moral of the story forgo a certain gain for an uncertain profit."""

p4 = """The kids were lost. A group of children from a small village at the edge of the Orinoco River had stolen a canoe to have some fun, but the currents carried them far out into the delta. They shouted for help, but deep in the jungle there was no one to come to their rescue. As night fell the children were afraid they would never be found and end up being eaten by a jaguar. 

Tired and hungry, they were on the verge of tears when they heard a gentle whisper. They looked up to see a Moriche palm tree, waving in the wind. The palm offered the children its fruit. With food in their stomach, the children gained strength to look around. The Moriche palm introduced them to other members of the forest and soon the children had many friends. They learnt to use wood to build houses and leaves for roofs. They found places to find food and water, herbs for medicine and even ways to dress up and decorate themselves.

Many years later, a group of adventures canoeing down the river were surprised to see a small settlement on a forested island deep in the jungles. The children had learnt the ways of the forest and were now living comfortably amidst the labyrinth of waterways. The Moriche palm came to be known as the ‘tree of life’ and the children grew up to be the Warao Indians also known as ‘canoe people’.

Moral: When in trouble, look to nature for answers."""

txt_speech2.say("choose the topic")
txt_speech2.runAndWait()
user = input("choose the topic  (animals/fish/forest/random) : ")



if (user == "animals"):

    txt_speech.say(p1)

    print(p1)

elif (user == "fish"):

    txt_speech2.say(p3)

    print(p3)

elif (user == "forest"):

    txt_speech3.say(p4)
    print(p4)


    vidPath = 's.mp4'
    window = pyglet.window.Window()
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vidPath)

    player.queue(MediaLoad)
    player.play()


    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(50, 50)


    pyglet.app.run()



else:

    txt_speech1.say(p2)

    print(p2)

txt_speech.runAndWait()