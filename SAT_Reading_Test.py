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
experiment_one_questions = [
    {
        'question': 'Former astronaut Ellen Ochoa says that although she doesn\'t have a definite idea of when it might happen, she _______ that humans will someday need to be able to live in other environments than those found on Earth. This conjecture informs her interest in future research missions to the moon.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) demands', 'B) speculates', 'C) doubts', 'D) establishes'],
        'correct': 1  # B is correct (0-indexed)
    },
    {
        'question': 'Beginning in the 1950s, Navajo Nation legislator Annie Dodge Wauneka continuously worked to promote public health; this _______ effort involved traveling throughout the vast Navajo homeland and writing a medical dictionary for speakers of Diné bizaad, the Navajo language.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) impartial', 'B) offhand', 'C) persistent', 'D) mandatory'],
        'correct': 2  # C is correct
    },
    {
        'question': 'Following the principles of community-based participatory research, tribal nations and research institutions are equal partners in health studies conducted on reservations. A collaboration between the Crow Tribe and Montana State University _______ this model: tribal citizens worked alongside scientists to design the methodology and continue to assist in data collection.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) circumvents', 'B) eclipses', 'C) fabricates', 'D) exemplifies'],
        'correct': 3  # D is correct
    },
    {
        'question': 'The parasitic dodder plant increases its reproductive success by flowering at the same time as the host plant it has latched onto. In 2020, Jianqiang Wu and his colleagues determined that the tiny dodder achieves this _______ with its host by absorbing and utilizing a protein the host produces when it is about to flower.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) synchronization', 'B) hibernation', 'C) prediction', 'D) moderation'],
        'correct': 0  # A is correct
    },
    {
        'question': 'Given that the conditions in binary star systems should make planetary formation nearly impossible, it\'s not surprising that the existence of planets in such systems has lacked _______ explanation. Roman Rafikov and Kedron Silsbee shed light on the subject when they used modeling to determine a complex set of factors that could support planets\' development.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) a discernible', 'B) a straightforward', 'C) an inconclusive', 'D) an unbiased'],
        'correct': 1  # B is correct
    },
    {
        'question': 'Seminole/Muscogee director Sterlin Harjo _______ television\'s tendency to situate Native characters in the distant past: this rejection is evident in his series Reservation Dogs, which revolves around teenagers who dress in contemporary styles and whose dialogue is laced with current slang.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) repudiates', 'B) proclaims', 'C) foretells', 'D) recants'],
        'correct': 0  # A is correct
    },
    {
        'question': 'In 2007, computer scientist Luis von Ahn was working on converting printed books into a digital format. He found that some words were distorted enough that digital scanners couldn\'t recognize them, but most humans could easily read them. Based on that finding, von Ahn invented a simple security test to keep automated "bots" out of websites. The first version of the reCAPTCHA test asked users to type one known word and one of the many words scanners couldn\'t recognize. Correct answers proved the users were humans and added data to the book-digitizing project.\n\nWhich choice best states the main purpose of the text?',
        'options': ['A) To discuss von Ahn\'s invention of reCAPTCHA', 'B) To explain how digital scanners work', 'C) To call attention to von Ahn\'s book-digitizing project', 'D) To indicate how popular reCAPTCHA is'],
        'correct': 0  # A is correct
    },
    {
        'question': 'The following text is from Edith Wharton\'s 1905 novel The House of Mirth. Lily Bart and a companion are walking through a park.\n\nLily had no real intimacy with nature, but she had a passion for the appropriate and could be keenly sensitive to a scene which was the fitting background of her own sensations. The landscape outspread below her seemed an enlargement of her present mood, and she found something of herself in its calmness, its breadth, its long free reaches. On the nearer slopes the sugar-maples wavered like pyres of light; lower down was a massing of grey orchards, and here and there the lingering green of an oak-grove.\n\nWhich choice best describes the function of the underlined sentence in the text as a whole?',
        'options': ['A) It creates a detailed image of the physical setting of the scene.', 'B) It establishes that a character is experiencing an internal conflict.', 'C) It makes an assertion that the next sentence then expands on.', 'D) It illustrates an idea that is introduced in the previous sentence.'],
        'correct': 0  # A is correct
    },
    {
        'question': 'The following text is from Edith Wharton\'s 1905 novel The House of Mirth. Lily Bart and a companion are walking through a park.\n\nLily had no real intimacy with nature, but she had a passion for the appropriate and could be keenly sensitive to a scene which was the fitting background of her own sensations. The landscape outspread below her seemed an enlargement of her present mood, and she found something of herself in its calmness, its breadth, its long free reaches. On the nearer slopes the sugar-maples wavered like pyres of light; lower down was a massing of grey orchards, and here and there the lingering green of an oak-grove.\n\nWhich choice best describes the function of the underlined sentence in the text as a whole?',
        'options': ['A) It creates a detailed image of the physical setting of the scene.', 'B) It establishes that a character is experiencing an internal conflict.', 'C) It makes an assertion that the next sentence then expands on.', 'D) It illustrates an idea that is introduced in the previous sentence.'],
        'correct': 0  # A is correct
    },
    {
        'question': 'The following text is adapted from Edith Nesbit\'s 1906 novel The Railway Children.\n\nMother did not spend all her time in paying dull [visits] to dull ladies, and sitting dully at home waiting for dull ladies to pay [visits] to her. She was almost always there, ready to play with the children, and read to them, and help them to do their home-lessons. Besides this she used to write stories for them while they were at school, and read them aloud after tea, and she always made up funny pieces of poetry for their birthdays and for other great occasions.\n\nAccording to the text, what is true about Mother?',
        'options': ['A) She wishes that more ladies would visit her.', 'B) Birthdays are her favorite special occasion.', 'C) She creates stories and poems for her children.', 'D) Reading to her children is her favorite activity.'],
        'correct': 2  # C is correct
    }
]

experiment_two_questions = [
    {
        'question': 'As Mexico\'s first president from an Indigenous community, Benito Juárez became one of the most _______ figures in his country\'s history: among the many significant accomplishments of his long tenure in office (1858–1872), Juárez consolidated the authority of the national government and advanced the rights of Indigenous peoples.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) unpredictable', 'B) important', 'C) secretive', 'D) ordinary'],
        'correct': 1  # B is correct
    },
    {
        'question': 'Due to their often strange images, highly experimental syntax, and opaque subject matter, many of John Ashbery\'s poems can be quite difficult to _______ and thus are the object of heated debate among scholars.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) delegate', 'B) compose', 'C) interpret', 'D) renounce'],
        'correct': 2  # C is correct
    },
    {
        'question': 'The Cambrian explosion gets its name from the sudden appearance and rapid diversification of animal remains in the fossil record about 541 million years ago, during the Cambrian period. Some scientists argue that this _______ change in the fossil record might be because of a shift in many organisms to body types that were more likely to be preserved.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) catastrophic', 'B) elusive', 'C) abrupt', 'D) imminent'],
        'correct': 2  # C is correct
    },
    {
        'question': 'During a 2014 archaeological dig in Spain, Vicente Lull and his team uncovered the skeleton of a woman from El Algar, an Early Bronze Age society, buried with valuable objects signaling a high position of power. This finding may persuade researchers who have argued that Bronze Age societies were ruled by men to _______ that women may have also held leadership roles.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) waive', 'B) concede', 'C) refute', 'D) require'],
        'correct': 1  # B is correct
    },
    {
        'question': 'Within baleen whale species, some individuals develop an accessory spleen—a seemingly functionless formation of splenetic tissue outside the normal spleen. Given the formation\'s greater prevalence among whales known to make deeper dives, some researchers hypothesize that its role isn\'t _______; rather, the accessory spleen may actively support diving mechanisms.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) replicable', 'B) predetermined', 'C) operative', 'D) latent'],
        'correct': 2  # C is correct
    },
    {
        'question': 'According to a US tax policy expert, state taxes are _______ other factors when considering an interstate move. Even significant differences in state taxation have almost no effect on most people\'s decisions, while differences in employment opportunities, housing availability, and climate are strong influences.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) consistent with', 'B) representative of', 'C) overshadowed by', 'D) irrelevant'],
        'correct': 2  # C is correct
    },
    {
        'question': 'The author\'s claim about the relationship between Neanderthals and Homo sapiens is _______, as it fails to account for several recent archaeological discoveries. To be convincing, his argument would need to address recent finds of additional hominid fossils, such as the latest Denisovan specimens and Homo longi.\n\nWhich choice completes the text with the most logical and precise word or phrase?',
        'options': ['A) disorienting', 'B) tenuous', 'C) nuanced', 'D) unoriginal'],
        'correct': 1  # B is correct
    },
    {
        'question': 'The following text is from Georgia Douglas Johnson\'s 1922 poem "Benediction."\n\nGo forth, my son,\n Winged by my heart\'s desire!\n Great reaches, yet unknown,\n Await\n For your possession.\n I may not, if I would,\n Retrace the way with you,\n My pilgrimage is through,\n But life is calling you!\n\nWhich choice best states the main purpose of the text?',
        'options': ['A) To express hope that a child will have the same accomplishments as his parent did', 'B) To suggest that raising a child involves many struggles', 'C) To warn a child that he will face many challenges throughout his life', 'D) To encourage a child to embrace the experiences life will offer'],
        'correct': 3  # D is correct
    },
    {
        'question': 'The following text is adapted from Indian Boyhood (1902) by Ohiyesa (Charles A. Eastman), a Santee Dakota writer. In the text, Ohiyesa recalls how the women in his tribe harvested maple syrup during his childhood.\n\nNow the women began to test the trees—moving leisurely among them, axe in hand, and striking a single quick blow, to see if the sap would appear. The trees, like people, have their individual characters; some were ready to yield up their life-blood, while others were more reluctant. Now one of the birchen basins was set under each tree, and a hardwood chip driven deep into the cut which the axe had made. From the corners of this chip—at first drop by drop, then more freely—the sap trickled into the little dishes.\n\nWhich choice best describes the function of the underlined sentence in the text as a whole?',
        'options': ['A) It portrays the range of personality traits displayed by the women as they work.', 'B) It foregrounds the beneficial relationship between humans and maple trees.', 'C) It demonstrates how human behavior can be influenced by the natural environment.', 'D) It elaborates on an aspect of the maple trees that the women evaluate.'],
        'correct': 3  # D is correct
    },
    {
        'question': 'Text 1:\nEcologists have long wondered how thousands of microscopic phytoplankton species can live together near ocean surfaces competing for the same resources. According to conventional wisdom, one species should emerge after outcompeting the rest. So why do so many species remain? Ecologists\' many efforts to explain this phenomenon still haven\'t uncovered a satisfactory explanation.\n\nText 2:\nEcologist Michael Behrenfeld and colleagues have connected phytoplankton\'s diversity to their microscopic size. Because these organisms are so tiny, they are spaced relatively far apart from each other in ocean water and, moreover, experience that water as a relatively dense substance. This in turn makes it hard for them to move around and interact with one another. Therefore, says Behrenfeld\'s team, direct competition among phytoplankton probably happens much less than previously thought.\n\nBased on the texts, how would Behrenfeld and colleagues (Text 2) most likely respond to the "conventional wisdom" discussed in Text 1?',
        'options': ['A) By arguing that it is based on a misconception about phytoplankton species competing with one another', 'B) By asserting that it fails to recognize that routine replenishment of ocean nutrients prevents competition between phytoplankton species', 'C) By suggesting that their own findings help clarify how phytoplankton species are able to compete with larger organisms', 'D) By recommending that more ecologists focus their research on how competition among phytoplankton species is increased with water density'],
        'correct': 0  # A is correct
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

# Answer options
answer_texts = []
answer_rects = []

for i in range(4):
    # Answer text
    answer_text = visual.TextStim(win=win, name=f'answer_{i}',
        text='',
        font='Arial',
        pos=(0, 0.05 - i*0.08), height=0.018, wrapWidth=1.6, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        languageStyle='LTR', depth=-1.0)
    answer_texts.append(answer_text)
    
    # Clickable rectangle for each answer
    answer_rect = visual.Rect(win=win, name=f'answer_rect_{i}',
        width=1.6, height=0.08,
        pos=(0, 0.05 - i*0.08),
            fillColor=None, lineColor='white', lineWidth=1,
            opacity=0, depth=-2.0)
    answer_rects.append(answer_rect)

# Continue instruction
continue_text = visual.TextStim(win=win, name='continue_text',
    text='Press RIGHT ARROW to continue',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0,
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
    
    # Set question text
    question_text.setText(f"Question {question_num} of {total_questions}\n\n{question_data['question']}")
    
    # Set answer options
    for i, option in enumerate(question_data['options']):
        answer_texts[i].setText(option)
        answer_texts[i].color = 'white'  # Reset color
    
    # Reset mouse
    mouse_question.clicked_name = []
    prevButtonState = mouse_question.getPressed()
    
    # Setup components
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
        
        # *question_text* updates
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
        
        # Store individual question data
        thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_question_{i+1}_selected', selected)
        thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_question_{i+1}_correct', question['correct'])
        thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_question_{i+1}_right', is_correct)
        thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_question_{i+1}_time', q_time)
    
    # Store experiment summary data
    thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_total_time', total_time)
    thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_correct_answers', correct_answers)
    thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_total_questions', len(questions))
    thisExp.addData(f'{experiment_name.lower().replace(" ", "_")}_percentage', (correct_answers / len(questions)) * 100)
    
    return correct_answers, total_time, len(questions)

# ------Run Experiment One-------
exp_one_correct, exp_one_time, exp_one_total = run_experiment(experiment_one_questions, "Experiment One")

# ------Run Experiment Two-------
exp_two_correct, exp_two_time, exp_two_total = run_experiment(experiment_two_questions, "Experiment Two")

# Calculate overall results
total_correct = exp_one_correct + exp_two_correct
total_questions = exp_one_total + exp_two_total
total_time = exp_one_time + exp_two_time

# Store overall data
thisExp.addData('overall_correct_answers', total_correct)
thisExp.addData('overall_total_questions', total_questions)
thisExp.addData('overall_total_time', total_time)
thisExp.addData('overall_percentage', (total_correct / total_questions) * 100)

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
