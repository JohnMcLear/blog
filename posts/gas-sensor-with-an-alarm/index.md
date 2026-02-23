---
title: "Gas sensor with an alarm"
date: 2012-10-06
---

My first arduino project thanks to Tom Hudson for lending me his Uno

Very simple code, comments should explain it:

I'm using an MQ2 gas sensor.

\[code\] #include "pitches.h"

int gasSensor = 0; // select input pin for gas Sensor int val = 0; // variable to store the value coming from the sensor int greenLed = 3; // the LED port int redLed = 4; // the LED port int speaker = 8; // Speaker

// notes in the melody: int melody\[\] = { NOTE\_C4, NOTE\_G3,NOTE\_G3, NOTE\_A3, NOTE\_G3,0, NOTE\_B3, NOTE\_C4 };

// note durations: 4 = quarter note, 8 = eighth note, etc.: int noteDurations\[\] = { 4, 8, 8, 4,4,4,4,4 };

void setup() { Serial.begin(9600); }

void loop() { val = analogRead(gasSensor); // read the value from the pot Serial.println( val ); delay(100); if(val > 100){ digitalWrite(greenLed, LOW); // turn the green LED off by making the voltage LOW digitalWrite(redLed, HIGH); // turn the red LED off // iterate over the notes of the melody: for (int thisNote = 0; thisNote < 8; thisNote++) {

// to calculate the note duration, take one second // divided by the note type. //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc. int noteDuration = 1000/noteDurations\[thisNote\]; tone(speaker, melody\[thisNote\],noteDuration); // to distinguish the notes, set a minimum time between them. // the note's duration + 30% seems to work well: int pauseBetweenNotes = noteDuration \* 1.30; delay(pauseBetweenNotes); // stop the tone playing: noTone(speaker); } }else{ // everyting okay. digitalWrite(greenLed, HIGH); // The the green LED on digitalWrite(redLed, LOW); // The the red LED off } } \[/code\]
