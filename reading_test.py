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

# Define the SAT reading questions for both experiments
# Test 1: All questions are now images
experiment_one_questions = [
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question1.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 1  # B
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question2.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question3.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 3  # D
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question4.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 0  # A
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question5.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 1  # B
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question6.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 0  # A
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question7.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 0  # A
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question8.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 3  # D
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question9.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test1', 'question10.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    }
]

# Test 2: All questions are now images
experiment_two_questions = [
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question1.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 1  # B
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question2.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question3.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question4.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 1  # B
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question5.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 3  # D
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question6.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 2  # C
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question7.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 1  # B
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question8.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 3  # D
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question9.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 3  # D
    },
    {
        'type': 'image',
        'image_path': os.path.join(_thisDir, 'images', 'test2', 'question10.png'),
        'options': ['A', 'B', 'C', 'D'],
        'correct': 0  # A
    }
]

# Initialize components for Experiment One Instructions
ExpOneInstructionsClock = core.Clock()
exp_one_instructions = visual.TextStim(win=win, name='exp_one_instructions',
    text='Experiment One\n\nYou will be shown 10 SAT Reading questions one at a time.\nEach question has 4 answer choices (A, B, C, D).\nClick on your chosen answer, then press the RIGHT ARROW key to continue to the next question.\n\nPress any key to begin.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

# Initialize components for Experiment Two Instructions
ExpTwoInstructionsClock = core.Clock()
exp_two_instructions = visual.TextStim(win=win, name='exp_two_instructions',
    text='Experiment Two\n\nYou will now be shown 10 more SAT Reading questions one at a time.\nEach question has 4 answer choices (A, B, C, D).\nClick on your chosen answer, then press the RIGHT ARROW key to continue to the next question.\n\nPress any key to begin.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

# Initialize components for single question display
QuestionClock = core.Clock()

# Question text
question_text = visual.TextStim(win=win, name='question_text',
    text='',
    font='Arial',
    pos=(0, 0.15), height=0.022, wrapWidth=1.8, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR', depth=0.0)

# Question image (for image-based questions)
question_image = visual.ImageStim(win=win, name='question_image',
    image=None,
    pos=(0, 0.15), size=None, ori=0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Answer options - displayed horizontally at the bottom
answer_texts = []
answer_rects = []

# Positions for A, B, C, D horizontally
x_positions = [-0.6, -0.2, 0.2, 0.6]
y_position = -0.4

for i in range(4):
    # Answer text
    answer_text = visual.TextStim(win=win, name=f'answer_{i}',
        text='',
        font='Arial',
        pos=(x_positions[i], y_position), height=0.04, wrapWidth=0.3, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR', depth=-1.0)
    answer_texts.append(answer_text)
    
    # Clickable rectangle for each answer
    answer_rect = visual.Rect(win=win, name=f'answer_rect_{i}',
        width=0.35, height=0.1,
        pos=(x_positions[i], y_position),
        fillColor=None, lineColor='white', lineWidth=2,
        opacity=1, depth=-2.0)
    answer_rects.append(answer_rect)

# Continue instruction
continue_text = visual.TextStim(win=win, name='continue_text',
    text='Press RIGHT ARROW to continue',
    font='Arial',
    pos=(0, -0.47), height=0.02, wrapWidth=None, ori=0,
    color='yellow', colorSpace='rgb', opacity=1,
    languageStyle='LTR', depth=-3.0)

# Mouse for question interaction
mouse_question = event.Mouse(win=win)
mouse_question.mouseClock = core.Clock()

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

# Function to run instruction screen
def run_instruction_screen(instruction_text):
    continueRoutine = True
    
    # Setup components
    instruction_text.setAutoDraw(True)
    
    # Reset keyboard
    defaultKeyboard.clearEvents()
    
    while continueRoutine:
        # Check for any key press using event.getKeys
        keys = event.getKeys(keyList=None)
        if keys:
            continueRoutine = False
    
        # Check for quit
        if endExpNow:
            core.quit()
    
        win.flip()

    instruction_text.setAutoDraw(False)

# Function to run a single question
def run_single_question(question_data, question_num, total_questions):
    continueRoutine = True
    selected_answer = None
    question_start_time = None
    
    # Determine question type (default to 'text' if not specified)
    question_type = question_data.get('type', 'text')
    
    # Set up question display based on type
    if question_type == 'image':
        # Use image display
        question_image.setImage(question_data['image_path'])
        # Scale image to fit screen width while maintaining aspect ratio
        question_image.size = (1.6, None)  # Width of 1.6, height auto-calculated
        question_image.pos = (0, 0.05)  # Center in upper portion of screen
        question_text.setText('')  # Clear text
        use_image = True
    else:
        # Use text display
        question_text.setText(f"Question {question_num} of {total_questions}\n\n{question_data['question']}")
        question_image.setImage(None)  # Clear image
        use_image = False
    
    # Set answer options
    for i, option in enumerate(question_data['options']):
        answer_texts[i].setText(option)
        answer_texts[i].color = 'white'  # Reset color
    
    # Reset mouse
    mouse_question.clicked_name = []
    prevButtonState = mouse_question.getPressed()
    
    # Clear any lingering key presses
    event.clearEvents(eventType='keyboard')
    
    # Setup components - include both text and image, but only one will be visible
    if use_image:
        QuestionComponents = [question_image] + answer_texts + answer_rects + [continue_text, mouse_question]
    else:
        QuestionComponents = [question_text] + answer_texts + answer_rects + [continue_text, mouse_question]
    for thisComponent in QuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # Create a new clock for this question
    question_clock = core.Clock()
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    question_clock.reset()
    frameN = -1

    while continueRoutine:
        t = question_clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=question_clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        # Record question start time
        if question_start_time is None:
            question_start_time = t
        
        # *question_text* or *question_image* updates
        if use_image:
            if question_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                question_image.frameNStart = frameN
                question_image.tStart = t
                question_image.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(question_image, 'tStartRefresh')
                question_image.setAutoDraw(True)
        else:
            if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                question_text.frameNStart = frameN
                question_text.tStart = t
                question_text.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(question_text, 'tStartRefresh')
                question_text.setAutoDraw(True)
        
        # *answer_texts* updates
        for i, answer_text in enumerate(answer_texts):
            if answer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                answer_text.frameNStart = frameN
                answer_text.tStart = t
                answer_text.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(answer_text, 'tStartRefresh')
                answer_text.setAutoDraw(True)
        
        # *answer_rects* updates
        for i, answer_rect in enumerate(answer_rects):
            if answer_rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                answer_rect.frameNStart = frameN
                answer_rect.tStart = t
                answer_rect.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(answer_rect, 'tStartRefresh')
                answer_rect.setAutoDraw(True)
        
        # *continue_text* updates
        if continue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            continue_text.frameNStart = frameN
            continue_text.tStart = t
            continue_text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(continue_text, 'tStartRefresh')
            continue_text.setAutoDraw(True)
        
        # *mouse_question* updates
        if mouse_question.status == NOT_STARTED and t >= 0-frameTolerance:
            mouse_question.frameNStart = frameN
            mouse_question.tStart = t
            mouse_question.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(mouse_question, 'tStartRefresh')
            mouse_question.status = STARTED
            mouse_question.mouseClock.reset()
            prevButtonState = mouse_question.getPressed()
        
        if mouse_question.status == STARTED:
            buttons = mouse_question.getPressed()
            if buttons != prevButtonState:
                prevButtonState = buttons
                if sum(buttons) > 0:
                    # Check for clicks on answer options
                    for i, rect in enumerate(answer_rects):
                        if rect.contains(mouse_question):
                            selected_answer = i
                            # Visual feedback - change color of selected answer
                            answer_texts[i].color = 'yellow'
                            # Reset other options
                            for j, other_answer in enumerate(answer_texts):
                                if j != i:
                                    other_answer.color = 'white'
                
        # Check for right arrow key to continue
        keys = event.getKeys(keyList=["right"])
        if keys and selected_answer is not None:
            continueRoutine = False
    
        # check for quit
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
    
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in QuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
    
        if continueRoutine:
            win.flip()

    # Clean up
    for thisComponent in QuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    question_time = t - question_start_time if question_start_time else 0
    is_correct = selected_answer == question_data['correct'] if selected_answer is not None else False
    
    return selected_answer, question_time, is_correct

# Function to run experiment
def run_experiment(questions, experiment_name):
    # Run instruction screen
    if experiment_name == "Experiment One":
        run_instruction_screen(exp_one_instructions)
    else:
        run_instruction_screen(exp_two_instructions)
    
    # Track results
    selected_answers = []
    question_times = []
    correct_answers = 0
    total_time = 0
    
    # Run each question
    for i, question in enumerate(questions):
        selected, q_time, is_correct = run_single_question(question, i+1, len(questions))
        selected_answers.append(selected)
        question_times.append(q_time)
        total_time += q_time
        if is_correct:
            correct_answers += 1
        
        # Store individual question data as a row
        thisExp.addData('experiment', experiment_name)
        thisExp.addData('question_number', i+1)
        thisExp.addData('time_seconds', round(q_time, 2))
        thisExp.addData('selected_answer', selected if selected is not None else 'N/A')
        thisExp.addData('correct_answer', question['correct'])
        thisExp.addData('is_correct', is_correct)
        thisExp.nextEntry()  # Move to next row for next question
    
    return correct_answers, total_time, len(questions)

# ------Run Experiment One-------
exp_one_correct, exp_one_time, exp_one_total = run_experiment(experiment_one_questions, "Experiment One")

# ------Run Experiment Two-------
exp_two_correct, exp_two_time, exp_two_total = run_experiment(experiment_two_questions, "Experiment Two")

# Calculate overall results
total_correct = exp_one_correct + exp_two_correct
total_questions = exp_one_total + exp_two_total
total_time = exp_one_time + exp_two_time

# Add summary rows
# Experiment One Summary
thisExp.addData('experiment', 'Experiment One Summary')
thisExp.addData('question_number', 'N/A')
thisExp.addData('time_seconds', round(exp_one_time, 2))
thisExp.addData('selected_answer', 'N/A')
thisExp.addData('correct_answer', f'{exp_one_correct}/{exp_one_total}')
thisExp.addData('is_correct', f'{(exp_one_correct/exp_one_total)*100:.1f}%')
thisExp.nextEntry()

# Experiment Two Summary
thisExp.addData('experiment', 'Experiment Two Summary')
thisExp.addData('question_number', 'N/A')
thisExp.addData('time_seconds', round(exp_two_time, 2))
thisExp.addData('selected_answer', 'N/A')
thisExp.addData('correct_answer', f'{exp_two_correct}/{exp_two_total}')
thisExp.addData('is_correct', f'{(exp_two_correct/exp_two_total)*100:.1f}%')
thisExp.nextEntry()

# Overall Summary
thisExp.addData('experiment', 'Overall Summary')
thisExp.addData('question_number', 'N/A')
thisExp.addData('time_seconds', round(total_time, 2))
thisExp.addData('selected_answer', 'N/A')
thisExp.addData('correct_answer', f'{total_correct}/{total_questions}')
thisExp.addData('is_correct', f'{(total_correct/total_questions)*100:.1f}%')
thisExp.nextEntry()

# ------Prepare to start Routine "Results"-------
continueRoutine = True
routineTimer.add(5.000000)

# Update results text
results_text.setText(f'Test Complete!\n\nExperiment One: {exp_one_correct}/{exp_one_total} correct\nExperiment Two: {exp_two_correct}/{exp_two_total} correct\n\nOverall: {total_correct}/{total_questions} correct\nTotal Time: {total_time:.2f} seconds\nOverall Percentage: {(total_correct/total_questions)*100:.1f}%')

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
