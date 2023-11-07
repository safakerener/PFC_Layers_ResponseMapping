#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 07, 2023, at 11:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'pilotv2'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\willi\\Desktop\\PFC_Layers\\PFC_Layers_ResponseMapping\\Pilot\\pilotv2_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-0.4039, -0.4039, -0.4039], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.4039, -0.4039, -0.4039]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
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
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "trainingPrep" ---
    
    # --- Initialize components for Routine "instructionPrep" ---
    # Run 'Begin Experiment' code from code_5
    cur_row = 0
    button_pressed = "none"
    show_instructions = 1
    max_slides = 5
    
    # --- Initialize components for Routine "Instructions1" ---
    imageInstruct = visual.ImageStim(
        win=win,
        name='imageInstruct', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.6, 1.00736),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    buttonNext = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(.72,-.44),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext',
        depth=-1
    )
    buttonNext.buttonClock = core.Clock()
    buttonBack = visual.ButtonStim(win, 
        text='<< Back', font='Arial',
        pos=(-.72, -.44),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='buttonBack',
        depth=-2
    )
    buttonBack.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "test1" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text='Please click on the correct option \n\n\n\n\n\nthis symbol means:    \n\n\n \n\n\n\nPress space to continue\n\n',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button = visual.ButtonStim(win, 
        text='Which object was it?', font='Arvo',
        pos=(-.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button',
        depth=-1
    )
    button.buttonClock = core.Clock()
    button_2 = visual.ButtonStim(win, 
        text='Which way was it facing?', font='Arvo',
        pos=(.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_2',
        depth=-2
    )
    button_2.buttonClock = core.Clock()
    image_17 = visual.ImageStim(
        win=win,
        name='image_17', 
        image='stim/ori1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .23), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "test2" ---
    text_9 = visual.TextStim(win=win, name='text_9',
        text='Please click on the correct option \n\n\n\n\n\nthis symbol means:    \n\n\n \n\n\n\nPress space to continue\n\n',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_3 = visual.ButtonStim(win, 
        text='Which object was it?', font='Arvo',
        pos=(-.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_3',
        depth=-1
    )
    button_3.buttonClock = core.Clock()
    button_4 = visual.ButtonStim(win, 
        text='Which way was it facing?', font='Arvo',
        pos=(.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_4',
        depth=-2
    )
    button_4.buttonClock = core.Clock()
    image_18 = visual.ImageStim(
        win=win,
        name='image_18', 
        image='stim/obj2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .23), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "test3" ---
    text_10 = visual.TextStim(win=win, name='text_10',
        text='Please click on the correct option \n\n\n\n\n\nthis symbol means:    \n\n\n \n\n\n\nPress space to continue\n\n',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_5 = visual.ButtonStim(win, 
        text='Which object was it?', font='Arvo',
        pos=(-.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_5',
        depth=-1
    )
    button_5.buttonClock = core.Clock()
    button_7 = visual.ButtonStim(win, 
        text='Which way was it facing?', font='Arvo',
        pos=(.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_7',
        depth=-2
    )
    button_7.buttonClock = core.Clock()
    image_19 = visual.ImageStim(
        win=win,
        name='image_19', 
        image='stim/ori2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .23), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "test4" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text='Please click on the correct option \n\n\n\n\n\nthis symbol means:    \n\n\n \n\n\n\nPress space to continue\n\n',
        font='Open Sans',
        pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_6 = visual.ButtonStim(win, 
        text='Which object was it?', font='Arvo',
        pos=(-.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_6',
        depth=-1
    )
    button_6.buttonClock = core.Clock()
    button_8 = visual.ButtonStim(win, 
        text='Which way was it facing?', font='Arvo',
        pos=(.2, -.15),
        letterHeight=0.025,
        size=(0.20, 0.15), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='button_8',
        depth=-2
    )
    button_8.buttonClock = core.Clock()
    image_20 = visual.ImageStim(
        win=win,
        name='image_20', 
        image='stim/obj1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .23), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "instruction2prep" ---
    # Run 'Begin Experiment' code from code_3
    cur2_row = 0
    button_pressed = "none"
    show_instructions2 = 1
    max_slides2 = 5
    
    # --- Initialize components for Routine "Instructions2" ---
    imageInstruct_2 = visual.ImageStim(
        win=win,
        name='imageInstruct_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.6, 1.00736),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    buttonNext_2 = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(.72,-.44),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='buttonNext_2',
        depth=-1
    )
    buttonNext_2.buttonClock = core.Clock()
    buttonBack_2 = visual.ButtonStim(win, 
        text='<< Back', font='Arial',
        pos=(-.72, -.44),
        letterHeight=0.03,
        size=(0.2, 0.08), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=False, italic=False,
        padding=None,
        anchor='center',
        name='buttonBack_2',
        depth=-2
    )
    buttonBack_2.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "Intro" ---
    text = visual.TextStim(win=win, name='text',
        text='The experiment will begin soon. Get ready!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "taskcue" ---
    cue = visual.ImageStim(
        win=win,
        name='cue', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "stim" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
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
    
    # --- Initialize components for Routine "delay" ---
    fixCrossR_4 = visual.ShapeStim(
        win=win, name='fixCrossR_4', vertices='cross',
        size=(0.02, 0.02),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "response" ---
    fixCross = visual.ShapeStim(
        win=win, name='fixCross', vertices='cross',
        size=(0.02, 0.02),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    text1 = visual.TextStim(win=win, name='text1',
        text='',
        font='Open Sans',
        units='norm', pos=(-.5, .1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text2 = visual.TextStim(win=win, name='text2',
        text='',
        font='Open Sans',
        units='norm', pos=(-.1666, .1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text3 = visual.TextStim(win=win, name='text3',
        text='',
        font='Open Sans',
        units='norm', pos=(.166, .1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text4 = visual.TextStim(win=win, name='text4',
        text='',
        font='Open Sans',
        units='norm', pos=(.5, .1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text5 = visual.TextStim(win=win, name='text5',
        text='',
        font='Open Sans',
        units='norm', pos=[-.5, -.1], height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    text6 = visual.TextStim(win=win, name='text6',
        text='',
        font='Open Sans',
        units='norm', pos=(-.1666, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    text7 = visual.TextStim(win=win, name='text7',
        text='',
        font='Open Sans',
        units='norm', pos=(.1666, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    text8 = visual.TextStim(win=win, name='text8',
        text='',
        font='Open Sans',
        units='norm', pos=(.5,-.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    kb = keyboard.Keyboard()
    num1 = visual.TextStim(win=win, name='num1',
        text='',
        font='Open Sans',
        units='norm', pos=(-.5, .3), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    num2 = visual.TextStim(win=win, name='num2',
        text='',
        font='Open Sans',
        units='norm', pos=(-.1666, .3), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    num3 = visual.TextStim(win=win, name='num3',
        text='',
        font='Open Sans',
        units='norm', pos=(.1666, .3), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    num4 = visual.TextStim(win=win, name='num4',
        text='',
        font='Open Sans',
        units='norm', pos=(.5, .3), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    # Run 'Begin Experiment' code from changecolour
    response_map = {
        '1': [text1, text5, num1],
        '2': [text2, text6, num2],
        '3': [text3, text7, num3],
        '4': [text4, text8, num4],  # Add more entries as needed for additional text components
    }
    
    # --- Initialize components for Routine "codeAcc" ---
    # Run 'Begin Experiment' code from code_4
    total = 0
    match = 0
    
    
    
    # --- Initialize components for Routine "ITI" ---
    fixCrossR = visual.ShapeStim(
        win=win, name='fixCrossR', vertices='cross',
        size=(0.02, 0.02),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    text_total = visual.TextStim(win=win, name='text_total',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_acc = visual.TextStim(win=win, name='text_acc',
        text=None,
        font='Open Sans',
        pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "tybb" ---
    text_17 = visual.TextStim(win=win, name='text_17',
        text='End of the run, please relax for a moment.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_13 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "trainingPrep" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trainingPrep.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_6
    # Construct the file path using participant and session values
    numParticipant = expInfo.get('participant', '')  # Get the participant value
    numSession = expInfo.get('session', '')  # Get the session value
    trialsFilepath = f'trialMatrices/trialMatrix_s{numParticipant}_{numSession}.xlsx'
    
    if numSession == "0":
        trainingEnter = 1
    else:
        trainingEnter = 0
    # keep track of which components have finished
    trainingPrepComponents = []
    for thisComponent in trainingPrepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trainingPrep" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingPrepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trainingPrep" ---
    for thisComponent in trainingPrepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trainingPrep.stopped', globalClock.getTime())
    # the Routine "trainingPrep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trainingLoop = data.TrialHandler(nReps=trainingEnter, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trainingLoop')
    thisExp.addLoop(trainingLoop)  # add the loop to the experiment
    thisTrainingLoop = trainingLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrainingLoop.rgb)
    if thisTrainingLoop != None:
        for paramName in thisTrainingLoop:
            globals()[paramName] = thisTrainingLoop[paramName]
    
    for thisTrainingLoop in trainingLoop:
        currentLoop = trainingLoop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrainingLoop.rgb)
        if thisTrainingLoop != None:
            for paramName in thisTrainingLoop:
                globals()[paramName] = thisTrainingLoop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        instructions_controller = data.TrialHandler(nReps=999.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='instructions_controller')
        thisExp.addLoop(instructions_controller)  # add the loop to the experiment
        thisInstructions_controller = instructions_controller.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions_controller.rgb)
        if thisInstructions_controller != None:
            for paramName in thisInstructions_controller:
                globals()[paramName] = thisInstructions_controller[paramName]
        
        for thisInstructions_controller in instructions_controller:
            currentLoop = instructions_controller
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisInstructions_controller.rgb)
            if thisInstructions_controller != None:
                for paramName in thisInstructions_controller:
                    globals()[paramName] = thisInstructions_controller[paramName]
            
            # --- Prepare to start Routine "instructionPrep" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('instructionPrep.started', globalClock.getTime())
            # Run 'Begin Routine' code from code_5
            if (button_pressed == "next"):
                cur_row += 1
            elif (button_pressed == "back"):
                cur_row -= 1
                
            button_pressed = "none"
            
            
            if cur_row < 0:
                cur_row = 0
                
            if cur_row > max_slides:
                instructions_controller.finished = 1
                show_instructions = 0
                cur_row = max_slides 
            # keep track of which components have finished
            instructionPrepComponents = []
            for thisComponent in instructionPrepComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instructionPrep" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instructionPrepComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instructionPrep" ---
            for thisComponent in instructionPrepComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('instructionPrep.stopped', globalClock.getTime())
            # the Routine "instructionPrep" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            instruction_slide_loop = data.TrialHandler(nReps=show_instructions, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('instructions/Instructions_doc.xlsx', selection=str(cur_row)),
                seed=None, name='instruction_slide_loop')
            thisExp.addLoop(instruction_slide_loop)  # add the loop to the experiment
            thisInstruction_slide_loop = instruction_slide_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisInstruction_slide_loop.rgb)
            if thisInstruction_slide_loop != None:
                for paramName in thisInstruction_slide_loop:
                    globals()[paramName] = thisInstruction_slide_loop[paramName]
            
            for thisInstruction_slide_loop in instruction_slide_loop:
                currentLoop = instruction_slide_loop
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisInstruction_slide_loop.rgb)
                if thisInstruction_slide_loop != None:
                    for paramName in thisInstruction_slide_loop:
                        globals()[paramName] = thisInstruction_slide_loop[paramName]
                
                # --- Prepare to start Routine "Instructions1" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Instructions1.started', globalClock.getTime())
                imageInstruct.setImage(InstructionsFilepath)
                # reset buttonNext to account for continued clicks & clear times on/off
                buttonNext.reset()
                # reset buttonBack to account for continued clicks & clear times on/off
                buttonBack.reset()
                # keep track of which components have finished
                Instructions1Components = [imageInstruct, buttonNext, buttonBack]
                for thisComponent in Instructions1Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Instructions1" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *imageInstruct* updates
                    
                    # if imageInstruct is starting this frame...
                    if imageInstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        imageInstruct.frameNStart = frameN  # exact frame index
                        imageInstruct.tStart = t  # local t and not account for scr refresh
                        imageInstruct.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(imageInstruct, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'imageInstruct.started')
                        # update status
                        imageInstruct.status = STARTED
                        imageInstruct.setAutoDraw(True)
                    
                    # if imageInstruct is active this frame...
                    if imageInstruct.status == STARTED:
                        # update params
                        pass
                    # *buttonNext* updates
                    
                    # if buttonNext is starting this frame...
                    if buttonNext.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        buttonNext.frameNStart = frameN  # exact frame index
                        buttonNext.tStart = t  # local t and not account for scr refresh
                        buttonNext.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(buttonNext, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'buttonNext.started')
                        # update status
                        buttonNext.status = STARTED
                        buttonNext.setAutoDraw(True)
                    
                    # if buttonNext is active this frame...
                    if buttonNext.status == STARTED:
                        # update params
                        pass
                        # check whether buttonNext has been pressed
                        if buttonNext.isClicked:
                            if not buttonNext.wasClicked:
                                # if this is a new click, store time of first click and clicked until
                                buttonNext.timesOn.append(buttonNext.buttonClock.getTime())
                                buttonNext.timesOff.append(buttonNext.buttonClock.getTime())
                            elif len(buttonNext.timesOff):
                                # if click is continuing from last frame, update time of clicked until
                                buttonNext.timesOff[-1] = buttonNext.buttonClock.getTime()
                            if not buttonNext.wasClicked:
                                # end routine when buttonNext is clicked
                                continueRoutine = False
                            if not buttonNext.wasClicked:
                                # run callback code when buttonNext is clicked
                                button_pressed = "next"
                    # take note of whether buttonNext was clicked, so that next frame we know if clicks are new
                    buttonNext.wasClicked = buttonNext.isClicked and buttonNext.status == STARTED
                    # *buttonBack* updates
                    
                    # if buttonBack is starting this frame...
                    if buttonBack.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        buttonBack.frameNStart = frameN  # exact frame index
                        buttonBack.tStart = t  # local t and not account for scr refresh
                        buttonBack.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(buttonBack, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'buttonBack.started')
                        # update status
                        buttonBack.status = STARTED
                        buttonBack.setAutoDraw(True)
                    
                    # if buttonBack is active this frame...
                    if buttonBack.status == STARTED:
                        # update params
                        pass
                        # check whether buttonBack has been pressed
                        if buttonBack.isClicked:
                            if not buttonBack.wasClicked:
                                # if this is a new click, store time of first click and clicked until
                                buttonBack.timesOn.append(buttonBack.buttonClock.getTime())
                                buttonBack.timesOff.append(buttonBack.buttonClock.getTime())
                            elif len(buttonBack.timesOff):
                                # if click is continuing from last frame, update time of clicked until
                                buttonBack.timesOff[-1] = buttonBack.buttonClock.getTime()
                            if not buttonBack.wasClicked:
                                # end routine when buttonBack is clicked
                                continueRoutine = False
                            if not buttonBack.wasClicked:
                                # run callback code when buttonBack is clicked
                                button_pressed = "back"
                    # take note of whether buttonBack was clicked, so that next frame we know if clicks are new
                    buttonBack.wasClicked = buttonBack.isClicked and buttonBack.status == STARTED
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Instructions1Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Instructions1" ---
                for thisComponent in Instructions1Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Instructions1.stopped', globalClock.getTime())
                instruction_slide_loop.addData('buttonNext.numClicks', buttonNext.numClicks)
                if buttonNext.numClicks:
                   instruction_slide_loop.addData('buttonNext.timesOn', buttonNext.timesOn)
                   instruction_slide_loop.addData('buttonNext.timesOff', buttonNext.timesOff)
                else:
                   instruction_slide_loop.addData('buttonNext.timesOn', "")
                   instruction_slide_loop.addData('buttonNext.timesOff', "")
                instruction_slide_loop.addData('buttonBack.numClicks', buttonBack.numClicks)
                if buttonBack.numClicks:
                   instruction_slide_loop.addData('buttonBack.timesOn', buttonBack.timesOn)
                   instruction_slide_loop.addData('buttonBack.timesOff', buttonBack.timesOff)
                else:
                   instruction_slide_loop.addData('buttonBack.timesOn', "")
                   instruction_slide_loop.addData('buttonBack.timesOff', "")
                # the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed show_instructions repeats of 'instruction_slide_loop'
            
            # get names of stimulus parameters
            if instruction_slide_loop.trialList in ([], [None], None):
                params = []
            else:
                params = instruction_slide_loop.trialList[0].keys()
            # save data for this loop
            instruction_slide_loop.saveAsExcel(filename + '.xlsx', sheetName='instruction_slide_loop',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            instruction_slide_loop.saveAsText(filename + 'instruction_slide_loop.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 999.0 repeats of 'instructions_controller'
        
        # get names of stimulus parameters
        if instructions_controller.trialList in ([], [None], None):
            params = []
        else:
            params = instructions_controller.trialList[0].keys()
        # save data for this loop
        instructions_controller.saveAsExcel(filename + '.xlsx', sheetName='instructions_controller',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        instructions_controller.saveAsText(filename + 'instructions_controller.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "test1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test1.started', globalClock.getTime())
        # reset button to account for continued clicks & clear times on/off
        button.reset()
        # reset button_2 to account for continued clicks & clear times on/off
        button_2.reset()
        # keep track of which components have finished
        test1Components = [text_8, button, button_2, image_17]
        for thisComponent in test1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10000.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # if text_8 is stopping this frame...
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_8.stopped')
                    # update status
                    text_8.status = FINISHED
                    text_8.setAutoDraw(False)
            # *button* updates
            
            # if button is starting this frame...
            if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button.frameNStart = frameN  # exact frame index
                button.tStart = t  # local t and not account for scr refresh
                button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button.started')
                # update status
                button.status = STARTED
                button.setAutoDraw(True)
            
            # if button is active this frame...
            if button.status == STARTED:
                # update params
                pass
                # check whether button has been pressed
                if button.isClicked:
                    if not button.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button.timesOn.append(button.buttonClock.getTime())
                        button.timesOff.append(button.buttonClock.getTime())
                    elif len(button.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button.timesOff[-1] = button.buttonClock.getTime()
                    if not button.wasClicked:
                        # run callback code when button is clicked
                        pass
            # take note of whether button was clicked, so that next frame we know if clicks are new
            button.wasClicked = button.isClicked and button.status == STARTED
            
            # if button is stopping this frame...
            if button.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button.tStop = t  # not accounting for scr refresh
                    button.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button.stopped')
                    # update status
                    button.status = FINISHED
                    button.setAutoDraw(False)
            # *button_2* updates
            
            # if button_2 is starting this frame...
            if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_2.frameNStart = frameN  # exact frame index
                button_2.tStart = t  # local t and not account for scr refresh
                button_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_2.started')
                # update status
                button_2.status = STARTED
                button_2.setAutoDraw(True)
            
            # if button_2 is active this frame...
            if button_2.status == STARTED:
                # update params
                pass
                # check whether button_2 has been pressed
                if button_2.isClicked:
                    if not button_2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_2.timesOn.append(button_2.buttonClock.getTime())
                        button_2.timesOff.append(button_2.buttonClock.getTime())
                    elif len(button_2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_2.timesOff[-1] = button_2.buttonClock.getTime()
                    if not button_2.wasClicked:
                        # end routine when button_2 is clicked
                        continueRoutine = False
                    if not button_2.wasClicked:
                        # run callback code when button_2 is clicked
                        pass
            # take note of whether button_2 was clicked, so that next frame we know if clicks are new
            button_2.wasClicked = button_2.isClicked and button_2.status == STARTED
            
            # if button_2 is stopping this frame...
            if button_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_2.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_2.tStop = t  # not accounting for scr refresh
                    button_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_2.stopped')
                    # update status
                    button_2.status = FINISHED
                    button_2.setAutoDraw(False)
            
            # *image_17* updates
            
            # if image_17 is starting this frame...
            if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_17.frameNStart = frameN  # exact frame index
                image_17.tStart = t  # local t and not account for scr refresh
                image_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_17.started')
                # update status
                image_17.status = STARTED
                image_17.setAutoDraw(True)
            
            # if image_17 is active this frame...
            if image_17.status == STARTED:
                # update params
                pass
            
            # if image_17 is stopping this frame...
            if image_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_17.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    image_17.tStop = t  # not accounting for scr refresh
                    image_17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_17.stopped')
                    # update status
                    image_17.status = FINISHED
                    image_17.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test1" ---
        for thisComponent in test1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test1.stopped', globalClock.getTime())
        trainingLoop.addData('button.numClicks', button.numClicks)
        if button.numClicks:
           trainingLoop.addData('button.timesOn', button.timesOn)
           trainingLoop.addData('button.timesOff', button.timesOff)
        else:
           trainingLoop.addData('button.timesOn', "")
           trainingLoop.addData('button.timesOff', "")
        trainingLoop.addData('button_2.numClicks', button_2.numClicks)
        if button_2.numClicks:
           trainingLoop.addData('button_2.timesOn', button_2.timesOn)
           trainingLoop.addData('button_2.timesOff', button_2.timesOff)
        else:
           trainingLoop.addData('button_2.timesOn', "")
           trainingLoop.addData('button_2.timesOff', "")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10000.000000)
        
        # --- Prepare to start Routine "test2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test2.started', globalClock.getTime())
        # reset button_3 to account for continued clicks & clear times on/off
        button_3.reset()
        # reset button_4 to account for continued clicks & clear times on/off
        button_4.reset()
        # keep track of which components have finished
        test2Components = [text_9, button_3, button_4, image_18]
        for thisComponent in test2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10000.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_9* updates
            
            # if text_9 is starting this frame...
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.started')
                # update status
                text_9.status = STARTED
                text_9.setAutoDraw(True)
            
            # if text_9 is active this frame...
            if text_9.status == STARTED:
                # update params
                pass
            
            # if text_9 is stopping this frame...
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_9.stopped')
                    # update status
                    text_9.status = FINISHED
                    text_9.setAutoDraw(False)
            # *button_3* updates
            
            # if button_3 is starting this frame...
            if button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_3.frameNStart = frameN  # exact frame index
                button_3.tStart = t  # local t and not account for scr refresh
                button_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_3.started')
                # update status
                button_3.status = STARTED
                button_3.setAutoDraw(True)
            
            # if button_3 is active this frame...
            if button_3.status == STARTED:
                # update params
                pass
                # check whether button_3 has been pressed
                if button_3.isClicked:
                    if not button_3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_3.timesOn.append(button_3.buttonClock.getTime())
                        button_3.timesOff.append(button_3.buttonClock.getTime())
                    elif len(button_3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_3.timesOff[-1] = button_3.buttonClock.getTime()
                    if not button_3.wasClicked:
                        # end routine when button_3 is clicked
                        continueRoutine = False
                    if not button_3.wasClicked:
                        # run callback code when button_3 is clicked
                        pass
            # take note of whether button_3 was clicked, so that next frame we know if clicks are new
            button_3.wasClicked = button_3.isClicked and button_3.status == STARTED
            
            # if button_3 is stopping this frame...
            if button_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_3.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_3.tStop = t  # not accounting for scr refresh
                    button_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_3.stopped')
                    # update status
                    button_3.status = FINISHED
                    button_3.setAutoDraw(False)
            # *button_4* updates
            
            # if button_4 is starting this frame...
            if button_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_4.frameNStart = frameN  # exact frame index
                button_4.tStart = t  # local t and not account for scr refresh
                button_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_4.started')
                # update status
                button_4.status = STARTED
                button_4.setAutoDraw(True)
            
            # if button_4 is active this frame...
            if button_4.status == STARTED:
                # update params
                pass
                # check whether button_4 has been pressed
                if button_4.isClicked:
                    if not button_4.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_4.timesOn.append(button_4.buttonClock.getTime())
                        button_4.timesOff.append(button_4.buttonClock.getTime())
                    elif len(button_4.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_4.timesOff[-1] = button_4.buttonClock.getTime()
                    if not button_4.wasClicked:
                        # run callback code when button_4 is clicked
                        pass
            # take note of whether button_4 was clicked, so that next frame we know if clicks are new
            button_4.wasClicked = button_4.isClicked and button_4.status == STARTED
            
            # if button_4 is stopping this frame...
            if button_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_4.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_4.tStop = t  # not accounting for scr refresh
                    button_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_4.stopped')
                    # update status
                    button_4.status = FINISHED
                    button_4.setAutoDraw(False)
            
            # *image_18* updates
            
            # if image_18 is starting this frame...
            if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_18.frameNStart = frameN  # exact frame index
                image_18.tStart = t  # local t and not account for scr refresh
                image_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_18.started')
                # update status
                image_18.status = STARTED
                image_18.setAutoDraw(True)
            
            # if image_18 is active this frame...
            if image_18.status == STARTED:
                # update params
                pass
            
            # if image_18 is stopping this frame...
            if image_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_18.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    image_18.tStop = t  # not accounting for scr refresh
                    image_18.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_18.stopped')
                    # update status
                    image_18.status = FINISHED
                    image_18.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test2" ---
        for thisComponent in test2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test2.stopped', globalClock.getTime())
        trainingLoop.addData('button_3.numClicks', button_3.numClicks)
        if button_3.numClicks:
           trainingLoop.addData('button_3.timesOn', button_3.timesOn)
           trainingLoop.addData('button_3.timesOff', button_3.timesOff)
        else:
           trainingLoop.addData('button_3.timesOn', "")
           trainingLoop.addData('button_3.timesOff', "")
        trainingLoop.addData('button_4.numClicks', button_4.numClicks)
        if button_4.numClicks:
           trainingLoop.addData('button_4.timesOn', button_4.timesOn)
           trainingLoop.addData('button_4.timesOff', button_4.timesOff)
        else:
           trainingLoop.addData('button_4.timesOn', "")
           trainingLoop.addData('button_4.timesOff', "")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10000.000000)
        
        # --- Prepare to start Routine "test3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test3.started', globalClock.getTime())
        # reset button_5 to account for continued clicks & clear times on/off
        button_5.reset()
        # reset button_7 to account for continued clicks & clear times on/off
        button_7.reset()
        # keep track of which components have finished
        test3Components = [text_10, button_5, button_7, image_19]
        for thisComponent in test3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10000.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            
            # if text_10 is starting this frame...
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.started')
                # update status
                text_10.status = STARTED
                text_10.setAutoDraw(True)
            
            # if text_10 is active this frame...
            if text_10.status == STARTED:
                # update params
                pass
            
            # if text_10 is stopping this frame...
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_10.stopped')
                    # update status
                    text_10.status = FINISHED
                    text_10.setAutoDraw(False)
            # *button_5* updates
            
            # if button_5 is starting this frame...
            if button_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_5.frameNStart = frameN  # exact frame index
                button_5.tStart = t  # local t and not account for scr refresh
                button_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_5.started')
                # update status
                button_5.status = STARTED
                button_5.setAutoDraw(True)
            
            # if button_5 is active this frame...
            if button_5.status == STARTED:
                # update params
                pass
                # check whether button_5 has been pressed
                if button_5.isClicked:
                    if not button_5.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_5.timesOn.append(button_5.buttonClock.getTime())
                        button_5.timesOff.append(button_5.buttonClock.getTime())
                    elif len(button_5.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_5.timesOff[-1] = button_5.buttonClock.getTime()
                    if not button_5.wasClicked:
                        # run callback code when button_5 is clicked
                        pass
            # take note of whether button_5 was clicked, so that next frame we know if clicks are new
            button_5.wasClicked = button_5.isClicked and button_5.status == STARTED
            
            # if button_5 is stopping this frame...
            if button_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_5.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_5.tStop = t  # not accounting for scr refresh
                    button_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_5.stopped')
                    # update status
                    button_5.status = FINISHED
                    button_5.setAutoDraw(False)
            # *button_7* updates
            
            # if button_7 is starting this frame...
            if button_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_7.frameNStart = frameN  # exact frame index
                button_7.tStart = t  # local t and not account for scr refresh
                button_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_7.started')
                # update status
                button_7.status = STARTED
                button_7.setAutoDraw(True)
            
            # if button_7 is active this frame...
            if button_7.status == STARTED:
                # update params
                pass
                # check whether button_7 has been pressed
                if button_7.isClicked:
                    if not button_7.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_7.timesOn.append(button_7.buttonClock.getTime())
                        button_7.timesOff.append(button_7.buttonClock.getTime())
                    elif len(button_7.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_7.timesOff[-1] = button_7.buttonClock.getTime()
                    if not button_7.wasClicked:
                        # end routine when button_7 is clicked
                        continueRoutine = False
                    if not button_7.wasClicked:
                        # run callback code when button_7 is clicked
                        pass
            # take note of whether button_7 was clicked, so that next frame we know if clicks are new
            button_7.wasClicked = button_7.isClicked and button_7.status == STARTED
            
            # if button_7 is stopping this frame...
            if button_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_7.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_7.tStop = t  # not accounting for scr refresh
                    button_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_7.stopped')
                    # update status
                    button_7.status = FINISHED
                    button_7.setAutoDraw(False)
            
            # *image_19* updates
            
            # if image_19 is starting this frame...
            if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_19.frameNStart = frameN  # exact frame index
                image_19.tStart = t  # local t and not account for scr refresh
                image_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_19.started')
                # update status
                image_19.status = STARTED
                image_19.setAutoDraw(True)
            
            # if image_19 is active this frame...
            if image_19.status == STARTED:
                # update params
                pass
            
            # if image_19 is stopping this frame...
            if image_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_19.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    image_19.tStop = t  # not accounting for scr refresh
                    image_19.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_19.stopped')
                    # update status
                    image_19.status = FINISHED
                    image_19.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test3" ---
        for thisComponent in test3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test3.stopped', globalClock.getTime())
        trainingLoop.addData('button_5.numClicks', button_5.numClicks)
        if button_5.numClicks:
           trainingLoop.addData('button_5.timesOn', button_5.timesOn)
           trainingLoop.addData('button_5.timesOff', button_5.timesOff)
        else:
           trainingLoop.addData('button_5.timesOn', "")
           trainingLoop.addData('button_5.timesOff', "")
        trainingLoop.addData('button_7.numClicks', button_7.numClicks)
        if button_7.numClicks:
           trainingLoop.addData('button_7.timesOn', button_7.timesOn)
           trainingLoop.addData('button_7.timesOff', button_7.timesOff)
        else:
           trainingLoop.addData('button_7.timesOn', "")
           trainingLoop.addData('button_7.timesOff', "")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10000.000000)
        
        # --- Prepare to start Routine "test4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test4.started', globalClock.getTime())
        # reset button_6 to account for continued clicks & clear times on/off
        button_6.reset()
        # reset button_8 to account for continued clicks & clear times on/off
        button_8.reset()
        # keep track of which components have finished
        test4Components = [text_11, button_6, button_8, image_20]
        for thisComponent in test4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10000.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            # *button_6* updates
            
            # if button_6 is starting this frame...
            if button_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_6.frameNStart = frameN  # exact frame index
                button_6.tStart = t  # local t and not account for scr refresh
                button_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_6.started')
                # update status
                button_6.status = STARTED
                button_6.setAutoDraw(True)
            
            # if button_6 is active this frame...
            if button_6.status == STARTED:
                # update params
                pass
                # check whether button_6 has been pressed
                if button_6.isClicked:
                    if not button_6.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_6.timesOn.append(button_6.buttonClock.getTime())
                        button_6.timesOff.append(button_6.buttonClock.getTime())
                    elif len(button_6.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_6.timesOff[-1] = button_6.buttonClock.getTime()
                    if not button_6.wasClicked:
                        # end routine when button_6 is clicked
                        continueRoutine = False
                    if not button_6.wasClicked:
                        # run callback code when button_6 is clicked
                        pass
            # take note of whether button_6 was clicked, so that next frame we know if clicks are new
            button_6.wasClicked = button_6.isClicked and button_6.status == STARTED
            
            # if button_6 is stopping this frame...
            if button_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_6.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_6.tStop = t  # not accounting for scr refresh
                    button_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_6.stopped')
                    # update status
                    button_6.status = FINISHED
                    button_6.setAutoDraw(False)
            # *button_8* updates
            
            # if button_8 is starting this frame...
            if button_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_8.frameNStart = frameN  # exact frame index
                button_8.tStart = t  # local t and not account for scr refresh
                button_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_8.started')
                # update status
                button_8.status = STARTED
                button_8.setAutoDraw(True)
            
            # if button_8 is active this frame...
            if button_8.status == STARTED:
                # update params
                pass
                # check whether button_8 has been pressed
                if button_8.isClicked:
                    if not button_8.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_8.timesOn.append(button_8.buttonClock.getTime())
                        button_8.timesOff.append(button_8.buttonClock.getTime())
                    elif len(button_8.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_8.timesOff[-1] = button_8.buttonClock.getTime()
                    if not button_8.wasClicked:
                        # run callback code when button_8 is clicked
                        pass
            # take note of whether button_8 was clicked, so that next frame we know if clicks are new
            button_8.wasClicked = button_8.isClicked and button_8.status == STARTED
            
            # if button_8 is stopping this frame...
            if button_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_8.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    button_8.tStop = t  # not accounting for scr refresh
                    button_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_8.stopped')
                    # update status
                    button_8.status = FINISHED
                    button_8.setAutoDraw(False)
            
            # *image_20* updates
            
            # if image_20 is starting this frame...
            if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_20.frameNStart = frameN  # exact frame index
                image_20.tStart = t  # local t and not account for scr refresh
                image_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_20.started')
                # update status
                image_20.status = STARTED
                image_20.setAutoDraw(True)
            
            # if image_20 is active this frame...
            if image_20.status == STARTED:
                # update params
                pass
            
            # if image_20 is stopping this frame...
            if image_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_20.tStartRefresh + 10000-frameTolerance:
                    # keep track of stop time/frame for later
                    image_20.tStop = t  # not accounting for scr refresh
                    image_20.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_20.stopped')
                    # update status
                    image_20.status = FINISHED
                    image_20.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test4" ---
        for thisComponent in test4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test4.stopped', globalClock.getTime())
        trainingLoop.addData('button_6.numClicks', button_6.numClicks)
        if button_6.numClicks:
           trainingLoop.addData('button_6.timesOn', button_6.timesOn)
           trainingLoop.addData('button_6.timesOff', button_6.timesOff)
        else:
           trainingLoop.addData('button_6.timesOn', "")
           trainingLoop.addData('button_6.timesOff', "")
        trainingLoop.addData('button_8.numClicks', button_8.numClicks)
        if button_8.numClicks:
           trainingLoop.addData('button_8.timesOn', button_8.timesOn)
           trainingLoop.addData('button_8.timesOff', button_8.timesOff)
        else:
           trainingLoop.addData('button_8.timesOn', "")
           trainingLoop.addData('button_8.timesOff', "")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10000.000000)
        
        # set up handler to look after randomisation of conditions etc
        instructions2_controller = data.TrialHandler(nReps=999.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='instructions2_controller')
        thisExp.addLoop(instructions2_controller)  # add the loop to the experiment
        thisInstructions2_controller = instructions2_controller.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions2_controller.rgb)
        if thisInstructions2_controller != None:
            for paramName in thisInstructions2_controller:
                globals()[paramName] = thisInstructions2_controller[paramName]
        
        for thisInstructions2_controller in instructions2_controller:
            currentLoop = instructions2_controller
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisInstructions2_controller.rgb)
            if thisInstructions2_controller != None:
                for paramName in thisInstructions2_controller:
                    globals()[paramName] = thisInstructions2_controller[paramName]
            
            # --- Prepare to start Routine "instruction2prep" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('instruction2prep.started', globalClock.getTime())
            # Run 'Begin Routine' code from code_3
            if (button_pressed == "next"):
                cur2_row += 1
            elif (button_pressed == "back"):
                cur2_row -= 1
                
            button_pressed = "none"
            
            
            if cur2_row < 0:
                cur2_row = 0
                
            if cur2_row > max_slides2:
                cur2_row = max_slides2 
                instructions2_controller.finished = 1
                show_instructions2 = 0
                cur_row2 = max_slides2 
            # keep track of which components have finished
            instruction2prepComponents = []
            for thisComponent in instruction2prepComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instruction2prep" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instruction2prepComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instruction2prep" ---
            for thisComponent in instruction2prepComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('instruction2prep.stopped', globalClock.getTime())
            # the Routine "instruction2prep" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            instruction2_slide_loop = data.TrialHandler(nReps=show_instructions2, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('instructions/Instructions2_doc.xlsx', selection=str(cur2_row)),
                seed=None, name='instruction2_slide_loop')
            thisExp.addLoop(instruction2_slide_loop)  # add the loop to the experiment
            thisInstruction2_slide_loop = instruction2_slide_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisInstruction2_slide_loop.rgb)
            if thisInstruction2_slide_loop != None:
                for paramName in thisInstruction2_slide_loop:
                    globals()[paramName] = thisInstruction2_slide_loop[paramName]
            
            for thisInstruction2_slide_loop in instruction2_slide_loop:
                currentLoop = instruction2_slide_loop
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisInstruction2_slide_loop.rgb)
                if thisInstruction2_slide_loop != None:
                    for paramName in thisInstruction2_slide_loop:
                        globals()[paramName] = thisInstruction2_slide_loop[paramName]
                
                # --- Prepare to start Routine "Instructions2" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Instructions2.started', globalClock.getTime())
                imageInstruct_2.setImage(Instructions2Filepath)
                # reset buttonNext_2 to account for continued clicks & clear times on/off
                buttonNext_2.reset()
                # reset buttonBack_2 to account for continued clicks & clear times on/off
                buttonBack_2.reset()
                # keep track of which components have finished
                Instructions2Components = [imageInstruct_2, buttonNext_2, buttonBack_2]
                for thisComponent in Instructions2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Instructions2" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *imageInstruct_2* updates
                    
                    # if imageInstruct_2 is starting this frame...
                    if imageInstruct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        imageInstruct_2.frameNStart = frameN  # exact frame index
                        imageInstruct_2.tStart = t  # local t and not account for scr refresh
                        imageInstruct_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(imageInstruct_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'imageInstruct_2.started')
                        # update status
                        imageInstruct_2.status = STARTED
                        imageInstruct_2.setAutoDraw(True)
                    
                    # if imageInstruct_2 is active this frame...
                    if imageInstruct_2.status == STARTED:
                        # update params
                        pass
                    # *buttonNext_2* updates
                    
                    # if buttonNext_2 is starting this frame...
                    if buttonNext_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        buttonNext_2.frameNStart = frameN  # exact frame index
                        buttonNext_2.tStart = t  # local t and not account for scr refresh
                        buttonNext_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(buttonNext_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'buttonNext_2.started')
                        # update status
                        buttonNext_2.status = STARTED
                        buttonNext_2.setAutoDraw(True)
                    
                    # if buttonNext_2 is active this frame...
                    if buttonNext_2.status == STARTED:
                        # update params
                        pass
                        # check whether buttonNext_2 has been pressed
                        if buttonNext_2.isClicked:
                            if not buttonNext_2.wasClicked:
                                # if this is a new click, store time of first click and clicked until
                                buttonNext_2.timesOn.append(buttonNext_2.buttonClock.getTime())
                                buttonNext_2.timesOff.append(buttonNext_2.buttonClock.getTime())
                            elif len(buttonNext_2.timesOff):
                                # if click is continuing from last frame, update time of clicked until
                                buttonNext_2.timesOff[-1] = buttonNext_2.buttonClock.getTime()
                            if not buttonNext_2.wasClicked:
                                # end routine when buttonNext_2 is clicked
                                continueRoutine = False
                            if not buttonNext_2.wasClicked:
                                # run callback code when buttonNext_2 is clicked
                                button_pressed = "next"
                    # take note of whether buttonNext_2 was clicked, so that next frame we know if clicks are new
                    buttonNext_2.wasClicked = buttonNext_2.isClicked and buttonNext_2.status == STARTED
                    # *buttonBack_2* updates
                    
                    # if buttonBack_2 is starting this frame...
                    if buttonBack_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        buttonBack_2.frameNStart = frameN  # exact frame index
                        buttonBack_2.tStart = t  # local t and not account for scr refresh
                        buttonBack_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(buttonBack_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'buttonBack_2.started')
                        # update status
                        buttonBack_2.status = STARTED
                        buttonBack_2.setAutoDraw(True)
                    
                    # if buttonBack_2 is active this frame...
                    if buttonBack_2.status == STARTED:
                        # update params
                        pass
                        # check whether buttonBack_2 has been pressed
                        if buttonBack_2.isClicked:
                            if not buttonBack_2.wasClicked:
                                # if this is a new click, store time of first click and clicked until
                                buttonBack_2.timesOn.append(buttonBack_2.buttonClock.getTime())
                                buttonBack_2.timesOff.append(buttonBack_2.buttonClock.getTime())
                            elif len(buttonBack_2.timesOff):
                                # if click is continuing from last frame, update time of clicked until
                                buttonBack_2.timesOff[-1] = buttonBack_2.buttonClock.getTime()
                            if not buttonBack_2.wasClicked:
                                # end routine when buttonBack_2 is clicked
                                continueRoutine = False
                            if not buttonBack_2.wasClicked:
                                # run callback code when buttonBack_2 is clicked
                                button_pressed = "back"
                    # take note of whether buttonBack_2 was clicked, so that next frame we know if clicks are new
                    buttonBack_2.wasClicked = buttonBack_2.isClicked and buttonBack_2.status == STARTED
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Instructions2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Instructions2" ---
                for thisComponent in Instructions2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Instructions2.stopped', globalClock.getTime())
                instruction2_slide_loop.addData('buttonNext_2.numClicks', buttonNext_2.numClicks)
                if buttonNext_2.numClicks:
                   instruction2_slide_loop.addData('buttonNext_2.timesOn', buttonNext_2.timesOn)
                   instruction2_slide_loop.addData('buttonNext_2.timesOff', buttonNext_2.timesOff)
                else:
                   instruction2_slide_loop.addData('buttonNext_2.timesOn', "")
                   instruction2_slide_loop.addData('buttonNext_2.timesOff', "")
                instruction2_slide_loop.addData('buttonBack_2.numClicks', buttonBack_2.numClicks)
                if buttonBack_2.numClicks:
                   instruction2_slide_loop.addData('buttonBack_2.timesOn', buttonBack_2.timesOn)
                   instruction2_slide_loop.addData('buttonBack_2.timesOff', buttonBack_2.timesOff)
                else:
                   instruction2_slide_loop.addData('buttonBack_2.timesOn', "")
                   instruction2_slide_loop.addData('buttonBack_2.timesOff', "")
                # the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed show_instructions2 repeats of 'instruction2_slide_loop'
            
            # get names of stimulus parameters
            if instruction2_slide_loop.trialList in ([], [None], None):
                params = []
            else:
                params = instruction2_slide_loop.trialList[0].keys()
            # save data for this loop
            instruction2_slide_loop.saveAsExcel(filename + '.xlsx', sheetName='instruction2_slide_loop',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            instruction2_slide_loop.saveAsText(filename + 'instruction2_slide_loop.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 999.0 repeats of 'instructions2_controller'
        
        # get names of stimulus parameters
        if instructions2_controller.trialList in ([], [None], None):
            params = []
        else:
            params = instructions2_controller.trialList[0].keys()
        # save data for this loop
        instructions2_controller.saveAsExcel(filename + '.xlsx', sheetName='instructions2_controller',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        instructions2_controller.saveAsText(filename + 'instructions2_controller.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed trainingEnter repeats of 'trainingLoop'
    
    # get names of stimulus parameters
    if trainingLoop.trialList in ([], [None], None):
        params = []
    else:
        params = trainingLoop.trialList[0].keys()
    # save data for this loop
    trainingLoop.saveAsExcel(filename + '.xlsx', sheetName='trainingLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trainingLoop.saveAsText(filename + 'trainingLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Intro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Intro.started', globalClock.getTime())
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    IntroComponents = [text, key_resp_5]
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
    frameN = -1
    
    # --- Run Routine "Intro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['5'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
                key_resp_5.duration = [key.duration for key in _key_resp_5_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Intro" ---
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Intro.stopped', globalClock.getTime())
    # Run 'End Routine' code from code
    win.winHandle.activate()
    
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(trialsFilepath),
        seed=None, name='trial')
    thisExp.addLoop(trial)  # add the loop to the experiment
    thisTrial = trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trial:
        currentLoop = trial
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "taskcue" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('taskcue.started', globalClock.getTime())
        cue.setImage(taskCue)
        # keep track of which components have finished
        taskcueComponents = [cue]
        for thisComponent in taskcueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "taskcue" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cue* updates
            
            # if cue is starting this frame...
            if cue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cue.frameNStart = frameN  # exact frame index
                cue.tStart = t  # local t and not account for scr refresh
                cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cue.started')
                # update status
                cue.status = STARTED
                cue.setAutoDraw(True)
            
            # if cue is active this frame...
            if cue.status == STARTED:
                # update params
                pass
            
            # if cue is stopping this frame...
            if cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    cue.tStop = t  # not accounting for scr refresh
                    cue.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cue.stopped')
                    # update status
                    cue.status = FINISHED
                    cue.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in taskcueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "taskcue" ---
        for thisComponent in taskcueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('taskcue.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
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
                globals()[paramName] = thisStimloop[paramName]
        
        for thisStimloop in stimloop:
            currentLoop = stimloop
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisStimloop.rgb)
            if thisStimloop != None:
                for paramName in thisStimloop:
                    globals()[paramName] = thisStimloop[paramName]
            
            # --- Prepare to start Routine "stim" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stim.started', globalClock.getTime())
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
            frameN = -1
            
            # --- Run Routine "stim" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    if frameN >= 15:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *fixCrossR_2* updates
                
                # if fixCrossR_2 is starting this frame...
                if fixCrossR_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    fixCrossR_2.frameNStart = frameN  # exact frame index
                    fixCrossR_2.tStart = t  # local t and not account for scr refresh
                    fixCrossR_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixCrossR_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixCrossR_2.started')
                    # update status
                    fixCrossR_2.status = STARTED
                    fixCrossR_2.setAutoDraw(True)
                
                # if fixCrossR_2 is active this frame...
                if fixCrossR_2.status == STARTED:
                    # update params
                    pass
                
                # if fixCrossR_2 is stopping this frame...
                if fixCrossR_2.status == STARTED:
                    if frameN >= 15:
                        # keep track of stop time/frame for later
                        fixCrossR_2.tStop = t  # not accounting for scr refresh
                        fixCrossR_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixCrossR_2.stopped')
                        # update status
                        fixCrossR_2.status = FINISHED
                        fixCrossR_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stim" ---
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stim.stopped', globalClock.getTime())
            # the Routine "stim" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "delay" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('delay.started', globalClock.getTime())
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
            frameN = -1
            
            # --- Run Routine "delay" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixCrossR_4* updates
                
                # if fixCrossR_4 is starting this frame...
                if fixCrossR_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    fixCrossR_4.frameNStart = frameN  # exact frame index
                    fixCrossR_4.tStart = t  # local t and not account for scr refresh
                    fixCrossR_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixCrossR_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixCrossR_4.started')
                    # update status
                    fixCrossR_4.status = STARTED
                    fixCrossR_4.setAutoDraw(True)
                
                # if fixCrossR_4 is active this frame...
                if fixCrossR_4.status == STARTED:
                    # update params
                    pass
                
                # if fixCrossR_4 is stopping this frame...
                if fixCrossR_4.status == STARTED:
                    if frameN >= 15:
                        # keep track of stop time/frame for later
                        fixCrossR_4.tStop = t  # not accounting for scr refresh
                        fixCrossR_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixCrossR_4.stopped')
                        # update status
                        fixCrossR_4.status = FINISHED
                        fixCrossR_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in delayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "delay" ---
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('delay.stopped', globalClock.getTime())
            # the Routine "delay" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 3.0 repeats of 'stimloop'
        
        # get names of stimulus parameters
        if stimloop.trialList in ([], [None], None):
            params = []
        else:
            params = stimloop.trialList[0].keys()
        # save data for this loop
        stimloop.saveAsExcel(filename + '.xlsx', sheetName='stimloop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        stimloop.saveAsText(filename + 'stimloop.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response.started', globalClock.getTime())
        fixCross.setFillColor('black')
        fixCross.setLineColor('black')
        text1.setColor('white', colorSpace='rgb')
        text1.setText(resp1)
        text2.setColor('white', colorSpace='rgb')
        text2.setText(resp2
        )
        text3.setColor('white', colorSpace='rgb')
        text3.setText(resp3)
        text4.setColor('white', colorSpace='rgb')
        text4.setText(resp4
        )
        text5.setColor('white', colorSpace='rgb')
        text5.setText(resp5)
        text6.setColor('white', colorSpace='rgb')
        text6.setText(resp6)
        text7.setColor('white', colorSpace='rgb')
        text7.setText(resp7)
        text8.setColor('white', colorSpace='rgb')
        text8.setText(resp8)
        kb.keys = []
        kb.rt = []
        _kb_allKeys = []
        num1.setColor('white', colorSpace='rgb')
        num1.setText('1')
        num2.setColor('white', colorSpace='rgb')
        num2.setText('2')
        num3.setColor('white', colorSpace='rgb')
        num3.setText('3')
        num4.setColor('white', colorSpace='rgb')
        num4.setText('4')
        # Run 'Begin Routine' code from changecolour
        key_pressed = False  # Initialize the flag as False
        event.clearEvents(eventType='keyboard')  # Clear keyboard events
        
        # keep track of which components have finished
        responseComponents = [fixCross, text1, text2, text3, text4, text5, text6, text7, text8, kb, num1, num2, num3, num4]
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
        frameN = -1
        
        # --- Run Routine "response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixCross* updates
            
            # if fixCross is starting this frame...
            if fixCross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixCross.frameNStart = frameN  # exact frame index
                fixCross.tStart = t  # local t and not account for scr refresh
                fixCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixCross.started')
                # update status
                fixCross.status = STARTED
                fixCross.setAutoDraw(True)
            
            # if fixCross is active this frame...
            if fixCross.status == STARTED:
                # update params
                pass
            
            # if fixCross is stopping this frame...
            if fixCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixCross.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixCross.tStop = t  # not accounting for scr refresh
                    fixCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixCross.stopped')
                    # update status
                    fixCross.status = FINISHED
                    fixCross.setAutoDraw(False)
            
            # *text1* updates
            
            # if text1 is starting this frame...
            if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text1.frameNStart = frameN  # exact frame index
                text1.tStart = t  # local t and not account for scr refresh
                text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text1.started')
                # update status
                text1.status = STARTED
                text1.setAutoDraw(True)
            
            # if text1 is active this frame...
            if text1.status == STARTED:
                # update params
                pass
            
            # if text1 is stopping this frame...
            if text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text1.tStop = t  # not accounting for scr refresh
                    text1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text1.stopped')
                    # update status
                    text1.status = FINISHED
                    text1.setAutoDraw(False)
            
            # *text2* updates
            
            # if text2 is starting this frame...
            if text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text2.frameNStart = frameN  # exact frame index
                text2.tStart = t  # local t and not account for scr refresh
                text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text2.started')
                # update status
                text2.status = STARTED
                text2.setAutoDraw(True)
            
            # if text2 is active this frame...
            if text2.status == STARTED:
                # update params
                pass
            
            # if text2 is stopping this frame...
            if text2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text2.tStop = t  # not accounting for scr refresh
                    text2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text2.stopped')
                    # update status
                    text2.status = FINISHED
                    text2.setAutoDraw(False)
            
            # *text3* updates
            
            # if text3 is starting this frame...
            if text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text3.frameNStart = frameN  # exact frame index
                text3.tStart = t  # local t and not account for scr refresh
                text3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text3.started')
                # update status
                text3.status = STARTED
                text3.setAutoDraw(True)
            
            # if text3 is active this frame...
            if text3.status == STARTED:
                # update params
                pass
            
            # if text3 is stopping this frame...
            if text3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text3.tStop = t  # not accounting for scr refresh
                    text3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text3.stopped')
                    # update status
                    text3.status = FINISHED
                    text3.setAutoDraw(False)
            
            # *text4* updates
            
            # if text4 is starting this frame...
            if text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text4.frameNStart = frameN  # exact frame index
                text4.tStart = t  # local t and not account for scr refresh
                text4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text4.started')
                # update status
                text4.status = STARTED
                text4.setAutoDraw(True)
            
            # if text4 is active this frame...
            if text4.status == STARTED:
                # update params
                pass
            
            # if text4 is stopping this frame...
            if text4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text4.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text4.tStop = t  # not accounting for scr refresh
                    text4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text4.stopped')
                    # update status
                    text4.status = FINISHED
                    text4.setAutoDraw(False)
            
            # *text5* updates
            
            # if text5 is starting this frame...
            if text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text5.frameNStart = frameN  # exact frame index
                text5.tStart = t  # local t and not account for scr refresh
                text5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text5.started')
                # update status
                text5.status = STARTED
                text5.setAutoDraw(True)
            
            # if text5 is active this frame...
            if text5.status == STARTED:
                # update params
                pass
            
            # if text5 is stopping this frame...
            if text5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text5.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text5.tStop = t  # not accounting for scr refresh
                    text5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text5.stopped')
                    # update status
                    text5.status = FINISHED
                    text5.setAutoDraw(False)
            
            # *text6* updates
            
            # if text6 is starting this frame...
            if text6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text6.frameNStart = frameN  # exact frame index
                text6.tStart = t  # local t and not account for scr refresh
                text6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text6.started')
                # update status
                text6.status = STARTED
                text6.setAutoDraw(True)
            
            # if text6 is active this frame...
            if text6.status == STARTED:
                # update params
                pass
            
            # if text6 is stopping this frame...
            if text6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text6.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text6.tStop = t  # not accounting for scr refresh
                    text6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text6.stopped')
                    # update status
                    text6.status = FINISHED
                    text6.setAutoDraw(False)
            
            # *text7* updates
            
            # if text7 is starting this frame...
            if text7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text7.frameNStart = frameN  # exact frame index
                text7.tStart = t  # local t and not account for scr refresh
                text7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text7.started')
                # update status
                text7.status = STARTED
                text7.setAutoDraw(True)
            
            # if text7 is active this frame...
            if text7.status == STARTED:
                # update params
                pass
            
            # if text7 is stopping this frame...
            if text7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text7.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text7.tStop = t  # not accounting for scr refresh
                    text7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text7.stopped')
                    # update status
                    text7.status = FINISHED
                    text7.setAutoDraw(False)
            
            # *text8* updates
            
            # if text8 is starting this frame...
            if text8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text8.frameNStart = frameN  # exact frame index
                text8.tStart = t  # local t and not account for scr refresh
                text8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text8.started')
                # update status
                text8.status = STARTED
                text8.setAutoDraw(True)
            
            # if text8 is active this frame...
            if text8.status == STARTED:
                # update params
                pass
            
            # if text8 is stopping this frame...
            if text8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text8.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text8.tStop = t  # not accounting for scr refresh
                    text8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text8.stopped')
                    # update status
                    text8.status = FINISHED
                    text8.setAutoDraw(False)
            
            # *kb* updates
            waitOnFlip = False
            
            # if kb is starting this frame...
            if kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                kb.frameNStart = frameN  # exact frame index
                kb.tStart = t  # local t and not account for scr refresh
                kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kb.started')
                # update status
                kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(kb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if kb is stopping this frame...
            if kb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > kb.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    kb.tStop = t  # not accounting for scr refresh
                    kb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'kb.stopped')
                    # update status
                    kb.status = FINISHED
                    kb.status = FINISHED
            if kb.status == STARTED and not waitOnFlip:
                theseKeys = kb.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _kb_allKeys.extend(theseKeys)
                if len(_kb_allKeys):
                    kb.keys = _kb_allKeys[0].name  # just the first key pressed
                    kb.rt = _kb_allKeys[0].rt
                    kb.duration = _kb_allKeys[0].duration
            
            # *num1* updates
            
            # if num1 is starting this frame...
            if num1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num1.frameNStart = frameN  # exact frame index
                num1.tStart = t  # local t and not account for scr refresh
                num1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'num1.started')
                # update status
                num1.status = STARTED
                num1.setAutoDraw(True)
            
            # if num1 is active this frame...
            if num1.status == STARTED:
                # update params
                pass
            
            # if num1 is stopping this frame...
            if num1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    num1.tStop = t  # not accounting for scr refresh
                    num1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'num1.stopped')
                    # update status
                    num1.status = FINISHED
                    num1.setAutoDraw(False)
            
            # *num2* updates
            
            # if num2 is starting this frame...
            if num2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num2.frameNStart = frameN  # exact frame index
                num2.tStart = t  # local t and not account for scr refresh
                num2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'num2.started')
                # update status
                num2.status = STARTED
                num2.setAutoDraw(True)
            
            # if num2 is active this frame...
            if num2.status == STARTED:
                # update params
                pass
            
            # if num2 is stopping this frame...
            if num2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    num2.tStop = t  # not accounting for scr refresh
                    num2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'num2.stopped')
                    # update status
                    num2.status = FINISHED
                    num2.setAutoDraw(False)
            
            # *num3* updates
            
            # if num3 is starting this frame...
            if num3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num3.frameNStart = frameN  # exact frame index
                num3.tStart = t  # local t and not account for scr refresh
                num3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'num3.started')
                # update status
                num3.status = STARTED
                num3.setAutoDraw(True)
            
            # if num3 is active this frame...
            if num3.status == STARTED:
                # update params
                pass
            
            # if num3 is stopping this frame...
            if num3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num3.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    num3.tStop = t  # not accounting for scr refresh
                    num3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'num3.stopped')
                    # update status
                    num3.status = FINISHED
                    num3.setAutoDraw(False)
            
            # *num4* updates
            
            # if num4 is starting this frame...
            if num4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                num4.frameNStart = frameN  # exact frame index
                num4.tStart = t  # local t and not account for scr refresh
                num4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(num4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'num4.started')
                # update status
                num4.status = STARTED
                num4.setAutoDraw(True)
            
            # if num4 is active this frame...
            if num4.status == STARTED:
                # update params
                pass
            
            # if num4 is stopping this frame...
            if num4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > num4.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    num4.tStop = t  # not accounting for scr refresh
                    num4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'num4.stopped')
                    # update status
                    num4.status = FINISHED
                    num4.setAutoDraw(False)
            # Run 'Each Frame' code from changecolour
            if not key_pressed:
                keys = event.getKeys(keyList=['1', '2', '3', '4'])
                if keys:
                    key_pressed = True
                    for key, response_components in response_map.items():
                        if key in keys:
                            fixCross.setColor([1, 0, 1], 'rgb')  # Set the color of the fixCross
                            for component in response_components:
                                component.setColor([1, 0, 1], 'rgb')  # Set the color of each text component
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response" ---
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response.stopped', globalClock.getTime())
        # check responses
        if kb.keys in ['', [], None]:  # No response was made
            kb.keys = None
        trial.addData('kb.keys',kb.keys)
        if kb.keys != None:  # we had a response
            trial.addData('kb.rt', kb.rt)
            trial.addData('kb.duration', kb.duration)
        # Run 'End Routine' code from changecolour
        fixCross.setColor([0, 0, 0], 'rgb')  # Set to black 
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "codeAcc" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('codeAcc.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_4
        respAll = [resp1, resp2, resp3, resp4, resp5, resp6, resp7, resp8]
        
        if kb.keys is None:
            total += 1
            accuracy = (match / total)
            continue  # Skip the current iteration and continue with the next one
        
        else:
            if "ori1" in taskCue or "ori2" in taskCue:
                task = 'ori'
        
                if objFirst == "True":
                    kb.keys = str(float(kb.keys) + 4)
        
                if stimfile[-5] == "1":
                    correct = "Full Left"
                elif stimfile[-5] == "2":       
                    correct = "Half Left"
                elif stimfile[-5] == "3":      
                    correct = "Half Right"
                elif stimfile[-5] == "4":      
                    correct = "Full Right"
                    
                if respAll[int(float(kb.keys) - 1)] == correct:
                    match += 1
        
        
            if "obj1" in taskCue or "obj2" in taskCue:
                task = 'obj'
        
                if objFirst == "False":
                    kb.keys = str(float(kb.keys) + 4)
        
                if respAll[int(float(kb.keys) - 1)].lower() in stimfile.lower():
                    match += 1
        
        
            total += 1
            accuracy = (match / total)
        
        if accuracy > 0.3 and total > 3:
            break  # Close the current loop and go to the next loop
        
        # keep track of which components have finished
        codeAccComponents = []
        for thisComponent in codeAccComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "codeAcc" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in codeAccComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "codeAcc" ---
        for thisComponent in codeAccComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('codeAcc.stopped', globalClock.getTime())
        # the Routine "codeAcc" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        text_total.setText('')
        # Run 'Begin Routine' code from code_7
        # Update text stimuli with the current values
        text_total.setText(f"Total: {total}")
        text_acc.setText(f"Accuracy: {accuracy}")
        
        # keep track of which components have finished
        ITIComponents = [fixCrossR, text_total, text_acc]
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
        frameN = -1
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixCrossR* updates
            
            # if fixCrossR is starting this frame...
            if fixCrossR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixCrossR.frameNStart = frameN  # exact frame index
                fixCrossR.tStart = t  # local t and not account for scr refresh
                fixCrossR.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCrossR, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixCrossR.started')
                # update status
                fixCrossR.status = STARTED
                fixCrossR.setAutoDraw(True)
            
            # if fixCrossR is active this frame...
            if fixCrossR.status == STARTED:
                # update params
                pass
            
            # if fixCrossR is stopping this frame...
            if fixCrossR.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixCrossR.tStartRefresh + interval-frameTolerance:
                    # keep track of stop time/frame for later
                    fixCrossR.tStop = t  # not accounting for scr refresh
                    fixCrossR.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixCrossR.stopped')
                    # update status
                    fixCrossR.status = FINISHED
                    fixCrossR.setAutoDraw(False)
            
            # *text_total* updates
            
            # if text_total is starting this frame...
            if text_total.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_total.frameNStart = frameN  # exact frame index
                text_total.tStart = t  # local t and not account for scr refresh
                text_total.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_total, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_total.started')
                # update status
                text_total.status = STARTED
                text_total.setAutoDraw(True)
            
            # if text_total is active this frame...
            if text_total.status == STARTED:
                # update params
                pass
            
            # if text_total is stopping this frame...
            if text_total.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_total.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_total.tStop = t  # not accounting for scr refresh
                    text_total.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_total.stopped')
                    # update status
                    text_total.status = FINISHED
                    text_total.setAutoDraw(False)
            
            # *text_acc* updates
            
            # if text_acc is starting this frame...
            if text_acc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_acc.frameNStart = frameN  # exact frame index
                text_acc.tStart = t  # local t and not account for scr refresh
                text_acc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_acc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_acc.started')
                # update status
                text_acc.status = STARTED
                text_acc.setAutoDraw(True)
            
            # if text_acc is active this frame...
            if text_acc.status == STARTED:
                # update params
                pass
            
            # if text_acc is stopping this frame...
            if text_acc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_acc.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_acc.tStop = t  # not accounting for scr refresh
                    text_acc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_acc.stopped')
                    # update status
                    text_acc.status = FINISHED
                    text_acc.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trial'
    
    # get names of stimulus parameters
    if trial.trialList in ([], [None], None):
        params = []
    else:
        params = trial.trialList[0].keys()
    # save data for this loop
    trial.saveAsExcel(filename + '.xlsx', sheetName='trial',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trial.saveAsText(filename + 'trial.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "tybb" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('tybb.started', globalClock.getTime())
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    tybbComponents = [text_17, key_resp_13]
    for thisComponent in tybbComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tybb" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        
        # if text_17 is starting this frame...
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_17.started')
            # update status
            text_17.status = STARTED
            text_17.setAutoDraw(True)
        
        # if text_17 is active this frame...
        if text_17.status == STARTED:
            # update params
            pass
        
        # if text_17 is stopping this frame...
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_17.stopped')
                # update status
                text_17.status = FINISHED
                text_17.setAutoDraw(False)
        
        # *key_resp_13* updates
        waitOnFlip = False
        
        # if key_resp_13 is starting this frame...
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_13.started')
            # update status
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['9'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = [key.name for key in _key_resp_13_allKeys]  # storing all keys
                key_resp_13.rt = [key.rt for key in _key_resp_13_allKeys]
                key_resp_13.duration = [key.duration for key in _key_resp_13_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tybbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tybb" ---
    for thisComponent in tybbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('tybb.stopped', globalClock.getTime())
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    thisExp.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        thisExp.addData('key_resp_13.rt', key_resp_13.rt)
        thisExp.addData('key_resp_13.duration', key_resp_13.duration)
    thisExp.nextEntry()
    # the Routine "tybb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from code_4
    print("Total shown:", total)
    print("Accuracy:", accuracy)
    print("Run", block ," finished:")
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
