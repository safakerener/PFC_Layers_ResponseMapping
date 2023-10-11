#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on October 11, 2023, at 15:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\willi\\Desktop\\PFC_Layers\\PFC_Layers_ResponseMapping\\Pilot\\untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The experiment will begin soon.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stim"
stimClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixCrossR_2 = visual.ShapeStim(
    win=win, name='fixCrossR_2', vertices='cross',
    size=(0.02, 0.02),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "delay"
delayClock = core.Clock()
fixCrossR_4 = visual.ShapeStim(
    win=win, name='fixCrossR_4', vertices='cross',
    size=(0.02, 0.02),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "response"
responseClock = core.Clock()
fixCrossR_3 = visual.ShapeStim(
    win=win, name='fixCrossR_3', vertices='cross',
    size=(0.02, 0.02),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
cat = visual.TextStim(win=win, name='cat',
    text='cat',
    font='Open Sans',
    units='norm', pos=(-.6, .1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
turtle = visual.TextStim(win=win, name='turtle',
    text='turtle',
    font='Open Sans',
    units='norm', pos=(.2, .1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
auto = visual.TextStim(win=win, name='auto',
    text='auto',
    font='Open Sans',
    units='norm', pos=(-.2, -.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
hand = visual.TextStim(win=win, name='hand',
    text='hand',
    font='Open Sans',
    units='norm', pos=(.6, -.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
farleft = visual.TextStim(win=win, name='farleft',
    text='far left',
    font='Open Sans',
    units='norm', pos=[-.6, -.1], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
farright = visual.TextStim(win=win, name='farright',
    text='far right',
    font='Open Sans',
    units='norm', pos=(.6, .1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
nearleft = visual.TextStim(win=win, name='nearleft',
    text='near left',
    font='Open Sans',
    units='norm', pos=(.2, -.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
nearright = visual.TextStim(win=win, name='nearright',
    text='near right',
    font='Open Sans',
    units='norm', pos=(-.2, .1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
kb = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixCrossR = visual.ShapeStim(
    win=win, name='fixCrossR', vertices='cross',
    size=(0.02, 0.02),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
IntroComponents = [text]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trial = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('rootDesignMatrix.xlsx'),
    seed=None, name='trial')
thisExp.addLoop(trial)  # add the loop to the experiment
thisTrial = trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trial:
    currentLoop = trial
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    stimloop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stimloop')
    thisExp.addLoop(stimloop)  # add the loop to the experiment
    thisStimloop = stimloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStimloop.rgb)
    if thisStimloop != None:
        for paramName in thisStimloop:
            exec('{} = thisStimloop[paramName]'.format(paramName))
    
    for thisStimloop in stimloop:
        currentLoop = stimloop
        # abbreviate parameter names if possible (e.g. rgb = thisStimloop.rgb)
        if thisStimloop != None:
            for paramName in thisStimloop:
                exec('{} = thisStimloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stim"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        image.setImage(stimfile)
        # keep track of which components have finished
        stimComponents = [image, fixCrossR_2]
        for thisComponent in stimComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stim"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *fixCrossR_2* updates
            if fixCrossR_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixCrossR_2.frameNStart = frameN  # exact frame index
                fixCrossR_2.tStart = t  # local t and not account for scr refresh
                fixCrossR_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCrossR_2, 'tStartRefresh')  # time at next scr refresh
                fixCrossR_2.setAutoDraw(True)
            if fixCrossR_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixCrossR_2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixCrossR_2.tStop = t  # not accounting for scr refresh
                    fixCrossR_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixCrossR_2, 'tStopRefresh')  # time at next scr refresh
                    fixCrossR_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stim"-------
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stimloop.addData('image.started', image.tStartRefresh)
        stimloop.addData('image.stopped', image.tStopRefresh)
        stimloop.addData('fixCrossR_2.started', fixCrossR_2.tStartRefresh)
        stimloop.addData('fixCrossR_2.stopped', fixCrossR_2.tStopRefresh)
        
        # ------Prepare to start Routine "delay"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        # keep track of which components have finished
        delayComponents = [fixCrossR_4]
        for thisComponent in delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = delayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=delayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixCrossR_4* updates
            if fixCrossR_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixCrossR_4.frameNStart = frameN  # exact frame index
                fixCrossR_4.tStart = t  # local t and not account for scr refresh
                fixCrossR_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCrossR_4, 'tStartRefresh')  # time at next scr refresh
                fixCrossR_4.setAutoDraw(True)
            if fixCrossR_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixCrossR_4.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    fixCrossR_4.tStop = t  # not accounting for scr refresh
                    fixCrossR_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixCrossR_4, 'tStopRefresh')  # time at next scr refresh
                    fixCrossR_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "delay"-------
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stimloop.addData('fixCrossR_4.started', fixCrossR_4.tStartRefresh)
        stimloop.addData('fixCrossR_4.stopped', fixCrossR_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'stimloop'
    
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    cat.setColor('white', colorSpace='rgb')
    turtle.setColor('white', colorSpace='rgb')
    auto.setColor('white', colorSpace='rgb')
    hand.setColor('white', colorSpace='rgb')
    farleft.setColor('white', colorSpace='rgb')
    farright.setColor('white', colorSpace='rgb')
    nearleft.setColor('white', colorSpace='rgb')
    nearright.setColor('white', colorSpace='rgb')
    kb.keys = []
    kb.rt = []
    _kb_allKeys = []
    # Clear any existing key presses at the start of the routine
    kb.clearEvents()
    
    first_key_pressed = False
    
    
    # Initialize variables to keep track of text components and colors
    text_components = [cat, nearright, turtle,farright , farleft,auto , nearleft, hand]
    text_colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
    
    # keep track of which components have finished
    responseComponents = [fixCrossR_3, cat, turtle, auto, hand, farleft, farright, nearleft, nearright, kb]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = responseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixCrossR_3* updates
        if fixCrossR_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixCrossR_3.frameNStart = frameN  # exact frame index
            fixCrossR_3.tStart = t  # local t and not account for scr refresh
            fixCrossR_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCrossR_3, 'tStartRefresh')  # time at next scr refresh
            fixCrossR_3.setAutoDraw(True)
        if fixCrossR_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCrossR_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                fixCrossR_3.tStop = t  # not accounting for scr refresh
                fixCrossR_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCrossR_3, 'tStopRefresh')  # time at next scr refresh
                fixCrossR_3.setAutoDraw(False)
        
        # *cat* updates
        if cat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cat.frameNStart = frameN  # exact frame index
            cat.tStart = t  # local t and not account for scr refresh
            cat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cat, 'tStartRefresh')  # time at next scr refresh
            cat.setAutoDraw(True)
        if cat.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cat.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                cat.tStop = t  # not accounting for scr refresh
                cat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cat, 'tStopRefresh')  # time at next scr refresh
                cat.setAutoDraw(False)
        
        # *turtle* updates
        if turtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            turtle.frameNStart = frameN  # exact frame index
            turtle.tStart = t  # local t and not account for scr refresh
            turtle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(turtle, 'tStartRefresh')  # time at next scr refresh
            turtle.setAutoDraw(True)
        if turtle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > turtle.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                turtle.tStop = t  # not accounting for scr refresh
                turtle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(turtle, 'tStopRefresh')  # time at next scr refresh
                turtle.setAutoDraw(False)
        
        # *auto* updates
        if auto.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            auto.frameNStart = frameN  # exact frame index
            auto.tStart = t  # local t and not account for scr refresh
            auto.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(auto, 'tStartRefresh')  # time at next scr refresh
            auto.setAutoDraw(True)
        if auto.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > auto.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                auto.tStop = t  # not accounting for scr refresh
                auto.frameNStop = frameN  # exact frame index
                win.timeOnFlip(auto, 'tStopRefresh')  # time at next scr refresh
                auto.setAutoDraw(False)
        
        # *hand* updates
        if hand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hand.frameNStart = frameN  # exact frame index
            hand.tStart = t  # local t and not account for scr refresh
            hand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hand, 'tStartRefresh')  # time at next scr refresh
            hand.setAutoDraw(True)
        if hand.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hand.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                hand.tStop = t  # not accounting for scr refresh
                hand.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hand, 'tStopRefresh')  # time at next scr refresh
                hand.setAutoDraw(False)
        
        # *farleft* updates
        if farleft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            farleft.frameNStart = frameN  # exact frame index
            farleft.tStart = t  # local t and not account for scr refresh
            farleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(farleft, 'tStartRefresh')  # time at next scr refresh
            farleft.setAutoDraw(True)
        if farleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > farleft.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                farleft.tStop = t  # not accounting for scr refresh
                farleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(farleft, 'tStopRefresh')  # time at next scr refresh
                farleft.setAutoDraw(False)
        
        # *farright* updates
        if farright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            farright.frameNStart = frameN  # exact frame index
            farright.tStart = t  # local t and not account for scr refresh
            farright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(farright, 'tStartRefresh')  # time at next scr refresh
            farright.setAutoDraw(True)
        if farright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > farright.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                farright.tStop = t  # not accounting for scr refresh
                farright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(farright, 'tStopRefresh')  # time at next scr refresh
                farright.setAutoDraw(False)
        
        # *nearleft* updates
        if nearleft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nearleft.frameNStart = frameN  # exact frame index
            nearleft.tStart = t  # local t and not account for scr refresh
            nearleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nearleft, 'tStartRefresh')  # time at next scr refresh
            nearleft.setAutoDraw(True)
        if nearleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nearleft.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                nearleft.tStop = t  # not accounting for scr refresh
                nearleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nearleft, 'tStopRefresh')  # time at next scr refresh
                nearleft.setAutoDraw(False)
        
        # *nearright* updates
        if nearright.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nearright.frameNStart = frameN  # exact frame index
            nearright.tStart = t  # local t and not account for scr refresh
            nearright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nearright, 'tStartRefresh')  # time at next scr refresh
            nearright.setAutoDraw(True)
        if nearright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nearright.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                nearright.tStop = t  # not accounting for scr refresh
                nearright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nearright, 'tStopRefresh')  # time at next scr refresh
                nearright.setAutoDraw(False)
        
        # *kb* updates
        waitOnFlip = False
        if kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            kb.frameNStart = frameN  # exact frame index
            kb.tStart = t  # local t and not account for scr refresh
            kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kb, 'tStartRefresh')  # time at next scr refresh
            kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if kb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > kb.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                kb.tStop = t  # not accounting for scr refresh
                kb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(kb, 'tStopRefresh')  # time at next scr refresh
                kb.status = FINISHED
        if kb.status == STARTED and not waitOnFlip:
            theseKeys = kb.getKeys(keyList=['1','2','3','4','5','6','7','8'], waitRelease=False)
            _kb_allKeys.extend(theseKeys)
            if len(_kb_allKeys):
                kb.keys = _kb_allKeys[0].name  # just the first key pressed
                kb.rt = _kb_allKeys[0].rt
        
        # Define a function to change the color of a text component
        def change_text_color(text_index, color):
            text_components[text_index].color = color
        
        # Check if the first key has been pressed
        if not first_key_pressed:
            keys = kb.getKeys()
            
            if keys:
                # Get the first key press
                first_key = keys[0].name
                
                # Process the first key press (e.g., change text color to purple)
                if first_key in ['1', '2', '3', '4', '7', '8', '9', '0']:
                    button_index = ['1', '2', '3', '4', '7', '8', '9', '0'].index(first_key)
                    change_text_color(button_index, 'purple')
                
                # Set the variable to indicate the first key has been pressed
                first_key_pressed = True
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial.addData('fixCrossR_3.started', fixCrossR_3.tStartRefresh)
    trial.addData('fixCrossR_3.stopped', fixCrossR_3.tStopRefresh)
    trial.addData('cat.started', cat.tStartRefresh)
    trial.addData('cat.stopped', cat.tStopRefresh)
    trial.addData('turtle.started', turtle.tStartRefresh)
    trial.addData('turtle.stopped', turtle.tStopRefresh)
    trial.addData('auto.started', auto.tStartRefresh)
    trial.addData('auto.stopped', auto.tStopRefresh)
    trial.addData('hand.started', hand.tStartRefresh)
    trial.addData('hand.stopped', hand.tStopRefresh)
    trial.addData('farleft.started', farleft.tStartRefresh)
    trial.addData('farleft.stopped', farleft.tStopRefresh)
    trial.addData('farright.started', farright.tStartRefresh)
    trial.addData('farright.stopped', farright.tStopRefresh)
    trial.addData('nearleft.started', nearleft.tStartRefresh)
    trial.addData('nearleft.stopped', nearleft.tStopRefresh)
    trial.addData('nearright.started', nearright.tStartRefresh)
    trial.addData('nearright.stopped', nearright.tStopRefresh)
    # check responses
    if kb.keys in ['', [], None]:  # No response was made
        kb.keys = None
    trial.addData('kb.keys',kb.keys)
    if kb.keys != None:  # we had a response
        trial.addData('kb.rt', kb.rt)
    trial.addData('kb.started', kb.tStartRefresh)
    trial.addData('kb.stopped', kb.tStopRefresh)
    # Initialize variables to keep track of text components and colors
    text_components = [cat, turtle, auto, hand, farleft, farright, nearleft, nearright]
    text_colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial'


# ------Prepare to start Routine "ITI"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ITIComponents = [fixCrossR]
for thisComponent in ITIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ITI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ITIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ITIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixCrossR* updates
    if fixCrossR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        fixCrossR.frameNStart = frameN  # exact frame index
        fixCrossR.tStart = t  # local t and not account for scr refresh
        fixCrossR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixCrossR, 'tStartRefresh')  # time at next scr refresh
        fixCrossR.setAutoDraw(True)
    if fixCrossR.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixCrossR.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            fixCrossR.tStop = t  # not accounting for scr refresh
            fixCrossR.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixCrossR, 'tStopRefresh')  # time at next scr refresh
            fixCrossR.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ITI"-------
for thisComponent in ITIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixCrossR.started', fixCrossR.tStartRefresh)
thisExp.addData('fixCrossR.stopped', fixCrossR.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
