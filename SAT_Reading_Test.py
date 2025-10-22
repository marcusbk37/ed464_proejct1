#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SAT Reading Comprehension Test
Created for EDUC 464 - 10 questions displayed simultaneously
"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'SAT Reading Test'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler for data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True

# store frame rate of monitor
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

# Setup ioHub
ioConfig = {}
ioConfig['Keyboard'] = dict(use_keymap='psychopy')
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Define the 10 SAT reading questions
questions = [
    {
        'question': '1. According to the passage, what is the primary purpose of the author\'s argument?',
        'options': ['A) To criticize modern technology', 'B) To advocate for environmental protection', 
                   'C) To analyze historical trends', 'D) To promote educational reform'],
        'correct': 1  # B is correct (0-indexed)
    },
    {
        'question': '2. The word "ubiquitous" in line 15 most nearly means:',
        'options': ['A) Rare', 'B) Widespread', 'C) Expensive', 'D) Temporary'],
        'correct': 1  # B is correct
    },
    {
        'question': '3. Which of the following best describes the author\'s tone?',
        'options': ['A) Optimistic', 'B) Pessimistic', 'C) Neutral', 'D) Sarcastic'],
        'correct': 2  # C is correct
    },
    {
        'question': '4. The passage suggests that the main character\'s motivation was:',
        'options': ['A) Financial gain', 'B) Personal recognition', 'C) Altruistic concern', 'D) Social pressure'],
        'correct': 2  # C is correct
    },
    {
        'question': '5. What can be inferred about the relationship between the two characters?',
        'options': ['A) They are siblings', 'B) They are colleagues', 'C) They are rivals', 'D) They are strangers'],
        'correct': 1  # B is correct
    },
    {
        'question': '6. The author\'s use of statistics in paragraph 3 serves to:',
        'options': ['A) Confuse the reader', 'B) Support the main argument', 'C) Introduce new topics', 'D) Create suspense'],
        'correct': 1  # B is correct
    },
    {
        'question': '7. Which statement best summarizes the central theme?',
        'options': ['A) Technology improves society', 'B) Change is inevitable', 'C) Tradition should be preserved', 'D) Progress requires sacrifice'],
        'correct': 1  # B is correct
    },
    {
        'question': '8. The phrase "in the long run" (line 22) suggests:',
        'options': ['A) Immediate consequences', 'B) Future implications', 'C) Historical context', 'D) Current events'],
        'correct': 1  # B is correct
    },
    {
        'question': '9. What is the author\'s attitude toward the subject matter?',
        'options': ['A) Indifferent', 'B) Enthusiastic', 'C) Critical', 'D) Ambivalent'],
        'correct': 2  # C is correct
    },
    {
        'question': '10. The passage is most likely from:',
        'options': ['A) A scientific journal', 'B) A newspaper editorial', 'C) A personal diary', 'D) A textbook'],
        'correct': 1  # B is correct
    }
]

# Initialize components for Instructions
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='SAT Reading Comprehension Test\n\nYou will see 10 multiple choice questions on the screen at once.\nEach question has 4 answer choices (A, B, C, D).\nClick on your chosen answer for each question.\nYou can answer the questions in any order.\nWhen you have answered all questions, click "Submit" to finish.\n\nClick anywhere to begin.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

mouse_instructions = event.Mouse(win=win)
mouse_instructions.mouseClock = core.Clock()

# Initialize components for Test Screen
TestClock = core.Clock()

# Create text stimuli for questions and answers
question_texts = []
answer_buttons = []
answer_rects = []

# Create question texts and answer buttons
for i, q in enumerate(questions):
    # Question text
    q_text = visual.TextStim(win=win, name=f'question_{i+1}',
        text=q['question'],
        font='Arial',
        pos=(0, 0.4 - i*0.08), height=0.025, wrapWidth=1.8, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR', depth=0.0)
    question_texts.append(q_text)
    
    # Answer options for this question
    q_answers = []
    q_rects = []
    for j, option in enumerate(q['options']):
        # Answer text
        answer_text = visual.TextStim(win=win, name=f'answer_{i+1}_{j}',
            text=option,
            font='Arial',
            pos=(-0.6 + j*0.4, 0.35 - i*0.08), height=0.02, wrapWidth=0.35, ori=0,
            color='white', colorSpace='rgb', opacity=1,
            languageStyle='LTR', depth=-1.0)
        q_answers.append(answer_text)
        
        # Invisible rectangle for clicking
        answer_rect = visual.Rect(win=win, name=f'click_rect_{i+1}_{j}',
            width=0.35, height=0.05,
            pos=(-0.6 + j*0.4, 0.35 - i*0.08),
            fillColor=None, lineColor='white', lineWidth=1,
            opacity=0, depth=-2.0)
        q_rects.append(answer_rect)
    
    answer_buttons.append(q_answers)
    answer_rects.append(q_rects)

# Submit button
submit_button = visual.Rect(win=win, name='submit_button',
    width=0.3, height=0.08,
    pos=(0, -0.4),
    fillColor='green', lineColor='white', lineWidth=2,
    opacity=1, depth=-1.0)

submit_text = visual.TextStim(win=win, name='submit_text',
    text='Submit Answers',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR', depth=-2.0)

# Mouse for test
mouse_test = event.Mouse(win=win)
mouse_test.mouseClock = core.Clock()

# Initialize components for Results
ResultsClock = core.Clock()
results_text = visual.TextStim(win=win, name='results_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR', depth=0.0)

# Initialize components for End
EndClock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Thank you for completing the SAT Reading Test!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR', depth=0.0)

# Create some handy timers
globalClock = core.Clock()
routineTimer = core.CountdownTimer()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
mouse_instructions.clicked_name = []
gotValidClick = False

InstructionsComponents = [instructions, mouse_instructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        instructions.frameNStart = frameN
        instructions.tStart = t
        instructions.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(instructions, 'tStartRefresh')
        instructions.setAutoDraw(True)
    
    # *mouse_instructions* updates
    if mouse_instructions.status == NOT_STARTED and t >= 0-frameTolerance:
        mouse_instructions.frameNStart = frameN
        mouse_instructions.tStart = t
        mouse_instructions.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(mouse_instructions, 'tStartRefresh')
        mouse_instructions.status = STARTED
        mouse_instructions.mouseClock.reset()
        prevButtonState = mouse_instructions.getPressed()
    
    if mouse_instructions.status == STARTED:
        buttons = mouse_instructions.getPressed()
        if buttons != prevButtonState:
            prevButtonState = buttons
            if sum(buttons) > 0:
                gotValidClick = True
                if gotValidClick:
                    continueRoutine = False
    
    # check for quit
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "Test"-------
continueRoutine = True

# Initialize tracking variables
selected_answers = [None] * 10  # Track selected answer for each question
test_start_time = None
test_end_time = None

# Setup mouse for test
mouse_test.clicked_name = []
gotValidClick = False

# Keep track of which components have finished
TestComponents = question_texts + [item for sublist in answer_buttons for item in sublist] + [item for sublist in answer_rects for item in sublist] + [submit_button, submit_text, mouse_test]

for thisComponent in TestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TestClock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Test"-------
while continueRoutine:
    t = TestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    # Record test start time
    if test_start_time is None:
        test_start_time = t
    
    # *question_texts* updates
    for i, q_text in enumerate(question_texts):
        if q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            q_text.frameNStart = frameN
            q_text.tStart = t
            q_text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(q_text, 'tStartRefresh')
            q_text.setAutoDraw(True)
    
    # *answer_buttons* updates
    for i, q_answers in enumerate(answer_buttons):
        for j, answer in enumerate(q_answers):
            if answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                answer.frameNStart = frameN
                answer.tStart = t
                answer.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(answer, 'tStartRefresh')
                answer.setAutoDraw(True)
    
    # *answer_rects* updates (invisible clickable areas)
    for i, q_rects in enumerate(answer_rects):
        for j, rect in enumerate(q_rects):
            if rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                rect.frameNStart = frameN
                rect.tStart = t
                rect.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(rect, 'tStartRefresh')
                rect.setAutoDraw(True)
    
    # *submit_button* updates
    if submit_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        submit_button.frameNStart = frameN
        submit_button.tStart = t
        submit_button.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(submit_button, 'tStartRefresh')
        submit_button.setAutoDraw(True)
    
    # *submit_text* updates
    if submit_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        submit_text.frameNStart = frameN
        submit_text.tStart = t
        submit_text.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(submit_text, 'tStartRefresh')
        submit_text.setAutoDraw(True)
    
    # *mouse_test* updates
    if mouse_test.status == NOT_STARTED and t >= 0-frameTolerance:
        mouse_test.frameNStart = frameN
        mouse_test.tStart = t
        mouse_test.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(mouse_test, 'tStartRefresh')
        mouse_test.status = STARTED
        mouse_test.mouseClock.reset()
        prevButtonState = mouse_test.getPressed()
    
    if mouse_test.status == STARTED:
        buttons = mouse_test.getPressed()
        if buttons != prevButtonState:
            prevButtonState = buttons
            if sum(buttons) > 0:
                # Check for clicks on answer options
                for i, q_rects in enumerate(answer_rects):
                    for j, rect in enumerate(q_rects):
                        if rect.contains(mouse_test):
                            selected_answers[i] = j
                            # Visual feedback - change color of selected answer
                            answer_buttons[i][j].color = 'yellow'
                            # Reset other options for this question
                            for k, other_answer in enumerate(answer_buttons[i]):
                                if k != j:
                                    other_answer.color = 'white'
                
                # Check for submit button click
                if submit_button.contains(mouse_test):
                    # Check if all questions are answered
                    if None not in selected_answers:
                        test_end_time = t
                        continueRoutine = False
    
    # check for quit
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

# -------Ending Routine "Test"-------
for thisComponent in TestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Calculate results
total_time = test_end_time - test_start_time if test_end_time and test_start_time else 0
correct_answers = 0

for i, selected in enumerate(selected_answers):
    if selected is not None and selected == questions[i]['correct']:
        correct_answers += 1

# Store data
thisExp.addData('total_time', total_time)
thisExp.addData('correct_answers', correct_answers)
thisExp.addData('total_questions', 10)
thisExp.addData('percentage', (correct_answers / 10) * 100)

# Store individual question data
for i, selected in enumerate(selected_answers):
    thisExp.addData(f'question_{i+1}_selected', selected)
    thisExp.addData(f'question_{i+1}_correct', questions[i]['correct'])
    thisExp.addData(f'question_{i+1}_right', selected == questions[i]['correct'] if selected is not None else False)

thisExp.nextEntry()

# ------Prepare to start Routine "Results"-------
continueRoutine = True
routineTimer.add(5.000000)

# Update results text
results_text.setText(f'Test Complete!\n\nCorrect Answers: {correct_answers}/10\nTotal Time: {total_time:.2f} seconds\nPercentage: {(correct_answers/10)*100:.1f}%')

ResultsComponents = [results_text]
for thisComponent in ResultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ResultsClock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "Results"-------
while continueRoutine and routineTimer.getTime() > 0:
    t = ResultsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ResultsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    # *results_text* updates
    if results_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        results_text.frameNStart = frameN
        results_text.tStart = t
        results_text.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(results_text, 'tStartRefresh')
        results_text.setAutoDraw(True)
    
    # check for quit
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in ResultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

# -------Ending Routine "Results"-------
for thisComponent in ResultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)

EndComponents = [thank_you]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        thank_you.frameNStart = frameN
        thank_you.tStart = t
        thank_you.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(thank_you, 'tStartRefresh')
        thank_you.setAutoDraw(True)
    
    # check for quit
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    
    if continueRoutine:
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time
win.flip()

# Save data
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()

# Clean up
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()
win.close()
core.quit()
