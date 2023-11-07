#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 06, 2023, at 17:20
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
expName = 'pilotv1'  # from the Builder filename that created this script
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

# Construct the file path using participant and session values
numParticipant = expInfo.get('participant', '')  # Get the participant value
numSession = expInfo.get('session', '')  # Get the session value
trialsFilepath = f'trialMatrices/trialMatrix_s{numParticipant}_{numSession}.xlsx'


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
        originPath='C:\\Users\\willi\\Desktop\\PFC_Layers\\PFC_Layers_ResponseMapping\\Pilot\\pilotv1.py',
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
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-0.2235, -0.2314, -0.2314], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.2235, -0.2314, -0.2314]
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
    
    # --- Initialize components for Routine "welcome" ---
    welcometext = visual.TextStim(win=win, name='welcometext',
        text='Welcome! \n\nThis program will guide you through the task. Please read each page carefully and ask the experimenter if you have any questions.\n\n\nPlease press the space bar to go to the next page. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instructions" ---
    instr_2 = visual.TextStim(win=win, name='instr_2',
        text='In the following experiment, you will see a series of symbols and images. \n\nYour task is to pay attention to the image that you are shown, and choose the correct response. \n\n\npress space to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instr2" ---
    key_resp_3 = keyboard.Keyboard()
    text_2 = visual.TextStim(win=win, name='text_2',
        text='The images you will see are similar to the image below. \n\n\n\n\n\n\nYou will be asked to choose either what the object in the image is, or which way the object is facing, depending on the symbol that is shown to you before each image. \n\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='stim/car2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .18), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "symb1" ---
    key_resp_4 = keyboard.Keyboard()
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='stim/obj1.png', mask=None, anchor='center',
        ori=0.0, pos=(-.1, .25), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='stim/obj2.png', mask=None, anchor='center',
        ori=0.0, pos=(.1, .25), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='stim/car2.png', mask=None, anchor='center',
        ori=0.0, pos=(-.33,-.05), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='stim/turtle3.png', mask=None, anchor='center',
        ori=0.0, pos=(-.11,-.05), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_22 = visual.ImageStim(
        win=win,
        name='image_22', 
        image='stim/shoe4.png', mask=None, anchor='center',
        ori=0.0, pos=(.11,-.05), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image_23 = visual.ImageStim(
        win=win,
        name='image_23', 
        image='stim/horse1.png', mask=None, anchor='center',
        ori=0.0, pos=(.33,-.05), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='If you are shown one of these two symbols,\n\n\n\n\nYou are asked to choose what the object is, for example:\n\n\n\n\n Car        Turtle       Shoe       Horse      \n\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "symb2" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='stim/ori1.png', mask=None, anchor='center',
        ori=0.0, pos=(-.1, .25), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', 
        image='stim/ori2.png', mask=None, anchor='center',
        ori=0.0, pos=(.1, .25), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='stim/car1.png', mask=None, anchor='center',
        ori=0.0, pos=(-.4,-.06), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', 
        image='stim/car2.png', mask=None, anchor='center',
        ori=0.0, pos=(-.15,-.06), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', 
        image='stim/car3.png', mask=None, anchor='center',
        ori=0.0, pos=(.13,-.06), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', 
        image='stim/car4.png', mask=None, anchor='center',
        ori=0.0, pos=(.39,-.06), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Or, if you see one of these two symbols, \n\n\n\nYou are asked to select which way the object is facing.\n\n\n\n\nfull left       slight left      slight right     full right\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_6 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "memor" ---
    key_resp_7 = keyboard.Keyboard()
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Please spend a few moments memorizing which symbol corresponds to which question.\n\n\n\n\n\n\n\n\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_13 = visual.ImageStim(
        win=win,
        name='image_13', 
        image='stim/obj1.png', mask=None, anchor='center',
        ori=0.0, pos=(-.45, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_14 = visual.ImageStim(
        win=win,
        name='image_14', 
        image='stim/obj2.png', mask=None, anchor='center',
        ori=0.0, pos=(-.25, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_15 = visual.ImageStim(
        win=win,
        name='image_15', 
        image='stim/ori1.png', mask=None, anchor='center',
        ori=0.0, pos=(.25, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_16 = visual.ImageStim(
        win=win,
        name='image_16', 
        image='stim/ori2.png', mask=None, anchor='center',
        ori=0.0, pos=(.45, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_6 = visual.TextStim(win=win, name='text_6',
        text='  Which object was it?',
        font='Open Sans',
        pos=(-.4, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    text_7 = visual.TextStim(win=win, name='text_7',
        text='Which way was it facing?',
        font='Open Sans',
        pos=(.4, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
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
    
    # --- Initialize components for Routine "gratz" ---
    text_12 = visual.TextStim(win=win, name='text_12',
        text='Perfect!\n\nPlease remember these symbols as you will need them for the experiment.\n\nThey will be shown once again before the experiment starts.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_8 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "respo1" ---
    key_resp_9 = keyboard.Keyboard()
    text_13 = visual.TextStim(win=win, name='text_13',
        text='Once you are shown the symbol and the object, you will see a group of answers on the screen\n\n\n\n\n\n\nThe order of these options will be scrambled each time you see them. Your task is to select the correct one, depending on the symbol (question) and the image you just saw.\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_25 = visual.ImageStim(
        win=win,
        name='image_25', 
        image='stim/response_instr.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .13), size=(0.7, 0.21),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "respo2" ---
    key_resp_10 = keyboard.Keyboard()
    text_14 = visual.TextStim(win=win, name='text_14',
        text='Regardless of your answer being in the first or second row of the screen, you should only respond between 1, 2, 3, or 4.\n\n\n\n\n\nIn this example, if your desired response is “full right", since it is the 3rd option on the row, you should press 3. Only the number of the relevant row is important. \n\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_24 = visual.ImageStim(
        win=win,
        name='image_24', 
        image='stim/response_instr.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .13), size=(0.7, 0.21),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "respo3" ---
    key_resp_11 = keyboard.Keyboard()
    text_15 = visual.TextStim(win=win, name='text_15',
        text='\n\n\n\n\nSimilarly, if your response is "turtle", you should respond by also pressing 3, because it is the 3rd item in the correct row. You can ignore the row with the answers that are not relevant to this question.\n\n\npress space to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_21 = visual.ImageStim(
        win=win,
        name='image_21', 
        image='stim/response_instr.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .25), size=(0.7, 0.21),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "memor" ---
    key_resp_7 = keyboard.Keyboard()
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Please spend a few moments memorizing which symbol corresponds to which question.\n\n\n\n\n\n\n\n\n\nPress space to continue\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    image_13 = visual.ImageStim(
        win=win,
        name='image_13', 
        image='stim/obj1.png', mask=None, anchor='center',
        ori=0.0, pos=(-.45, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_14 = visual.ImageStim(
        win=win,
        name='image_14', 
        image='stim/obj2.png', mask=None, anchor='center',
        ori=0.0, pos=(-.25, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_15 = visual.ImageStim(
        win=win,
        name='image_15', 
        image='stim/ori1.png', mask=None, anchor='center',
        ori=0.0, pos=(.25, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_16 = visual.ImageStim(
        win=win,
        name='image_16', 
        image='stim/ori2.png', mask=None, anchor='center',
        ori=0.0, pos=(.45, .06), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_6 = visual.TextStim(win=win, name='text_6',
        text='  Which object was it?',
        font='Open Sans',
        pos=(-.4, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    text_7 = visual.TextStim(win=win, name='text_7',
        text='Which way was it facing?',
        font='Open Sans',
        pos=(.4, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
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
    
    # --- Initialize components for Routine "ITI" ---
    fixCrossR = visual.ShapeStim(
        win=win, name='fixCrossR', vertices='cross',
        size=(0.02, 0.02),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "codeAcc" ---
    # Run 'Begin Experiment' code from code_4
    total = 0
    match = 0
    
    
    
    # --- Initialize components for Routine "tybb" ---
    text_17 = visual.TextStim(win=win, name='text_17',
        text='End of run, please relax for a moment.',
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
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    welcomeComponents = [welcometext, key_resp]
    for thisComponent in welcomeComponents:
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
    
    # --- Run Routine "welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcometext* updates
        
        # if welcometext is starting this frame...
        if welcometext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcometext.frameNStart = frameN  # exact frame index
            welcometext.tStart = t  # local t and not account for scr refresh
            welcometext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcometext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcometext.started')
            # update status
            welcometext.status = STARTED
            welcometext.setAutoDraw(True)
        
        # if welcometext is active this frame...
        if welcometext.status == STARTED:
            # update params
            pass
        
        # if welcometext is stopping this frame...
        if welcometext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > welcometext.tStartRefresh + 1000000-frameTolerance:
                # keep track of stop time/frame for later
                welcometext.tStop = t  # not accounting for scr refresh
                welcometext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'welcometext.stopped')
                # update status
                welcometext.status = FINISHED
                welcometext.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
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
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcome.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [instr_2, key_resp_2]
    for thisComponent in InstructionsComponents:
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
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_2* updates
        
        # if instr_2 is starting this frame...
        if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2.frameNStart = frameN  # exact frame index
            instr_2.tStart = t  # local t and not account for scr refresh
            instr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_2.started')
            # update status
            instr_2.status = STARTED
            instr_2.setAutoDraw(True)
        
        # if instr_2 is active this frame...
        if instr_2.status == STARTED:
            # update params
            pass
        
        # if instr_2 is stopping this frame...
        if instr_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_2.tStartRefresh + 1000000000000000000000-frameTolerance:
                # keep track of stop time/frame for later
                instr_2.tStop = t  # not accounting for scr refresh
                instr_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instr_2.stopped')
                # update status
                instr_2.status = FINISHED
                instr_2.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
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
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr2.started', globalClock.getTime())
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    instr2Components = [key_resp_3, text_2, image_2]
    for thisComponent in instr2Components:
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
    
    # --- Run Routine "instr2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 100000-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            pass
        
        # if image_2 is stopping this frame...
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 1000000000000-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.stopped')
                # update status
                image_2.status = FINISHED
                image_2.setAutoDraw(False)
        
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
        for thisComponent in instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr2" ---
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr2.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "symb1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('symb1.started', globalClock.getTime())
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    symb1Components = [key_resp_4, image_3, image_4, image_5, image_6, image_22, image_23, text_3]
    for thisComponent in symb1Components:
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
    
    # --- Run Routine "symb1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *image_3* updates
        
        # if image_3 is starting this frame...
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            # update status
            image_3.status = STARTED
            image_3.setAutoDraw(True)
        
        # if image_3 is active this frame...
        if image_3.status == STARTED:
            # update params
            pass
        
        # if image_3 is stopping this frame...
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.stopped')
                # update status
                image_3.status = FINISHED
                image_3.setAutoDraw(False)
        
        # *image_4* updates
        
        # if image_4 is starting this frame...
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            # update status
            image_4.status = STARTED
            image_4.setAutoDraw(True)
        
        # if image_4 is active this frame...
        if image_4.status == STARTED:
            # update params
            pass
        
        # if image_4 is stopping this frame...
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.stopped')
                # update status
                image_4.status = FINISHED
                image_4.setAutoDraw(False)
        
        # *image_5* updates
        
        # if image_5 is starting this frame...
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5.started')
            # update status
            image_5.status = STARTED
            image_5.setAutoDraw(True)
        
        # if image_5 is active this frame...
        if image_5.status == STARTED:
            # update params
            pass
        
        # if image_5 is stopping this frame...
        if image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_5.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.stopped')
                # update status
                image_5.status = FINISHED
                image_5.setAutoDraw(False)
        
        # *image_6* updates
        
        # if image_6 is starting this frame...
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.started')
            # update status
            image_6.status = STARTED
            image_6.setAutoDraw(True)
        
        # if image_6 is active this frame...
        if image_6.status == STARTED:
            # update params
            pass
        
        # if image_6 is stopping this frame...
        if image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_6.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.stopped')
                # update status
                image_6.status = FINISHED
                image_6.setAutoDraw(False)
        
        # *image_22* updates
        
        # if image_22 is starting this frame...
        if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_22.frameNStart = frameN  # exact frame index
            image_22.tStart = t  # local t and not account for scr refresh
            image_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_22.started')
            # update status
            image_22.status = STARTED
            image_22.setAutoDraw(True)
        
        # if image_22 is active this frame...
        if image_22.status == STARTED:
            # update params
            pass
        
        # if image_22 is stopping this frame...
        if image_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_22.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_22.tStop = t  # not accounting for scr refresh
                image_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_22.stopped')
                # update status
                image_22.status = FINISHED
                image_22.setAutoDraw(False)
        
        # *image_23* updates
        
        # if image_23 is starting this frame...
        if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_23.frameNStart = frameN  # exact frame index
            image_23.tStart = t  # local t and not account for scr refresh
            image_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_23.started')
            # update status
            image_23.status = STARTED
            image_23.setAutoDraw(True)
        
        # if image_23 is active this frame...
        if image_23.status == STARTED:
            # update params
            pass
        
        # if image_23 is stopping this frame...
        if image_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_23.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_23.tStop = t  # not accounting for scr refresh
                image_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_23.stopped')
                # update status
                image_23.status = FINISHED
                image_23.setAutoDraw(False)
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
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
        for thisComponent in symb1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "symb1" ---
    for thisComponent in symb1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('symb1.stopped', globalClock.getTime())
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "symb1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "symb2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('symb2.started', globalClock.getTime())
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    symb2Components = [image_7, image_8, image_9, image_10, image_11, image_12, text_4, key_resp_6]
    for thisComponent in symb2Components:
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
    
    # --- Run Routine "symb2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_7* updates
        
        # if image_7 is starting this frame...
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_7.started')
            # update status
            image_7.status = STARTED
            image_7.setAutoDraw(True)
        
        # if image_7 is active this frame...
        if image_7.status == STARTED:
            # update params
            pass
        
        # if image_7 is stopping this frame...
        if image_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_7.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_7.tStop = t  # not accounting for scr refresh
                image_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.stopped')
                # update status
                image_7.status = FINISHED
                image_7.setAutoDraw(False)
        
        # *image_8* updates
        
        # if image_8 is starting this frame...
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_8.started')
            # update status
            image_8.status = STARTED
            image_8.setAutoDraw(True)
        
        # if image_8 is active this frame...
        if image_8.status == STARTED:
            # update params
            pass
        
        # if image_8 is stopping this frame...
        if image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_8.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.stopped')
                # update status
                image_8.status = FINISHED
                image_8.setAutoDraw(False)
        
        # *image_9* updates
        
        # if image_9 is starting this frame...
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_9.started')
            # update status
            image_9.status = STARTED
            image_9.setAutoDraw(True)
        
        # if image_9 is active this frame...
        if image_9.status == STARTED:
            # update params
            pass
        
        # if image_9 is stopping this frame...
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.stopped')
                # update status
                image_9.status = FINISHED
                image_9.setAutoDraw(False)
        
        # *image_10* updates
        
        # if image_10 is starting this frame...
        if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_10.frameNStart = frameN  # exact frame index
            image_10.tStart = t  # local t and not account for scr refresh
            image_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_10.started')
            # update status
            image_10.status = STARTED
            image_10.setAutoDraw(True)
        
        # if image_10 is active this frame...
        if image_10.status == STARTED:
            # update params
            pass
        
        # if image_10 is stopping this frame...
        if image_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_10.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_10.tStop = t  # not accounting for scr refresh
                image_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.stopped')
                # update status
                image_10.status = FINISHED
                image_10.setAutoDraw(False)
        
        # *image_11* updates
        
        # if image_11 is starting this frame...
        if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_11.started')
            # update status
            image_11.status = STARTED
            image_11.setAutoDraw(True)
        
        # if image_11 is active this frame...
        if image_11.status == STARTED:
            # update params
            pass
        
        # if image_11 is stopping this frame...
        if image_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_11.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_11.tStop = t  # not accounting for scr refresh
                image_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_11.stopped')
                # update status
                image_11.status = FINISHED
                image_11.setAutoDraw(False)
        
        # *image_12* updates
        
        # if image_12 is starting this frame...
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_12.started')
            # update status
            image_12.status = STARTED
            image_12.setAutoDraw(True)
        
        # if image_12 is active this frame...
        if image_12.status == STARTED:
            # update params
            pass
        
        # if image_12 is stopping this frame...
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_12.stopped')
                # update status
                image_12.status = FINISHED
                image_12.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
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
        for thisComponent in symb2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "symb2" ---
    for thisComponent in symb2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('symb2.stopped', globalClock.getTime())
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "symb2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "memor" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('memor.started', globalClock.getTime())
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    memorComponents = [key_resp_7, text_5, image_13, image_14, image_15, image_16, text_6, text_7]
    for thisComponent in memorComponents:
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
    
    # --- Run Routine "memor" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # *image_13* updates
        
        # if image_13 is starting this frame...
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_13.started')
            # update status
            image_13.status = STARTED
            image_13.setAutoDraw(True)
        
        # if image_13 is active this frame...
        if image_13.status == STARTED:
            # update params
            pass
        
        # if image_13 is stopping this frame...
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_13.stopped')
                # update status
                image_13.status = FINISHED
                image_13.setAutoDraw(False)
        
        # *image_14* updates
        
        # if image_14 is starting this frame...
        if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_14.started')
            # update status
            image_14.status = STARTED
            image_14.setAutoDraw(True)
        
        # if image_14 is active this frame...
        if image_14.status == STARTED:
            # update params
            pass
        
        # if image_14 is stopping this frame...
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_14.stopped')
                # update status
                image_14.status = FINISHED
                image_14.setAutoDraw(False)
        
        # *image_15* updates
        
        # if image_15 is starting this frame...
        if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_15.started')
            # update status
            image_15.status = STARTED
            image_15.setAutoDraw(True)
        
        # if image_15 is active this frame...
        if image_15.status == STARTED:
            # update params
            pass
        
        # if image_15 is stopping this frame...
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.stopped')
                # update status
                image_15.status = FINISHED
                image_15.setAutoDraw(False)
        
        # *image_16* updates
        
        # if image_16 is starting this frame...
        if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_16.frameNStart = frameN  # exact frame index
            image_16.tStart = t  # local t and not account for scr refresh
            image_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_16.started')
            # update status
            image_16.status = STARTED
            image_16.setAutoDraw(True)
        
        # if image_16 is active this frame...
        if image_16.status == STARTED:
            # update params
            pass
        
        # if image_16 is stopping this frame...
        if image_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_16.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_16.tStop = t  # not accounting for scr refresh
                image_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_16.stopped')
                # update status
                image_16.status = FINISHED
                image_16.setAutoDraw(False)
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # if text_7 is stopping this frame...
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                # update status
                text_7.status = FINISHED
                text_7.setAutoDraw(False)
        
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
        for thisComponent in memorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "memor" ---
    for thisComponent in memorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('memor.stopped', globalClock.getTime())
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "memor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    thisExp.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       thisExp.addData('button.timesOn', button.timesOn)
       thisExp.addData('button.timesOff', button.timesOff)
    else:
       thisExp.addData('button.timesOn', "")
       thisExp.addData('button.timesOff', "")
    thisExp.addData('button_2.numClicks', button_2.numClicks)
    if button_2.numClicks:
       thisExp.addData('button_2.timesOn', button_2.timesOn)
       thisExp.addData('button_2.timesOff', button_2.timesOff)
    else:
       thisExp.addData('button_2.timesOn', "")
       thisExp.addData('button_2.timesOff', "")
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
    thisExp.addData('button_3.numClicks', button_3.numClicks)
    if button_3.numClicks:
       thisExp.addData('button_3.timesOn', button_3.timesOn)
       thisExp.addData('button_3.timesOff', button_3.timesOff)
    else:
       thisExp.addData('button_3.timesOn', "")
       thisExp.addData('button_3.timesOff', "")
    thisExp.addData('button_4.numClicks', button_4.numClicks)
    if button_4.numClicks:
       thisExp.addData('button_4.timesOn', button_4.timesOn)
       thisExp.addData('button_4.timesOff', button_4.timesOff)
    else:
       thisExp.addData('button_4.timesOn', "")
       thisExp.addData('button_4.timesOff', "")
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
    thisExp.addData('button_5.numClicks', button_5.numClicks)
    if button_5.numClicks:
       thisExp.addData('button_5.timesOn', button_5.timesOn)
       thisExp.addData('button_5.timesOff', button_5.timesOff)
    else:
       thisExp.addData('button_5.timesOn', "")
       thisExp.addData('button_5.timesOff', "")
    thisExp.addData('button_7.numClicks', button_7.numClicks)
    if button_7.numClicks:
       thisExp.addData('button_7.timesOn', button_7.timesOn)
       thisExp.addData('button_7.timesOff', button_7.timesOff)
    else:
       thisExp.addData('button_7.timesOn', "")
       thisExp.addData('button_7.timesOff', "")
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
    thisExp.addData('button_6.numClicks', button_6.numClicks)
    if button_6.numClicks:
       thisExp.addData('button_6.timesOn', button_6.timesOn)
       thisExp.addData('button_6.timesOff', button_6.timesOff)
    else:
       thisExp.addData('button_6.timesOn', "")
       thisExp.addData('button_6.timesOff', "")
    thisExp.addData('button_8.numClicks', button_8.numClicks)
    if button_8.numClicks:
       thisExp.addData('button_8.timesOn', button_8.timesOn)
       thisExp.addData('button_8.timesOff', button_8.timesOff)
    else:
       thisExp.addData('button_8.timesOn', "")
       thisExp.addData('button_8.timesOff', "")
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10000.000000)
    
    # --- Prepare to start Routine "gratz" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('gratz.started', globalClock.getTime())
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    gratzComponents = [text_12, key_resp_8]
    for thisComponent in gratzComponents:
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
    
    # --- Run Routine "gratz" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        
        # if text_12 is starting this frame...
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_12.started')
            # update status
            text_12.status = STARTED
            text_12.setAutoDraw(True)
        
        # if text_12 is active this frame...
        if text_12.status == STARTED:
            # update params
            pass
        
        # if text_12 is stopping this frame...
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_12.stopped')
                # update status
                text_12.status = FINISHED
                text_12.setAutoDraw(False)
        
        # *key_resp_8* updates
        waitOnFlip = False
        
        # if key_resp_8 is starting this frame...
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            # update status
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                key_resp_8.duration = _key_resp_8_allKeys[-1].duration
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
        for thisComponent in gratzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "gratz" ---
    for thisComponent in gratzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('gratz.stopped', globalClock.getTime())
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    thisExp.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        thisExp.addData('key_resp_8.rt', key_resp_8.rt)
        thisExp.addData('key_resp_8.duration', key_resp_8.duration)
    thisExp.nextEntry()
    # the Routine "gratz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "respo1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('respo1.started', globalClock.getTime())
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    respo1Components = [key_resp_9, text_13, image_25]
    for thisComponent in respo1Components:
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
    
    # --- Run Routine "respo1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_9* updates
        waitOnFlip = False
        
        # if key_resp_9 is starting this frame...
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            # update status
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_13* updates
        
        # if text_13 is starting this frame...
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_13.started')
            # update status
            text_13.status = STARTED
            text_13.setAutoDraw(True)
        
        # if text_13 is active this frame...
        if text_13.status == STARTED:
            # update params
            pass
        
        # if text_13 is stopping this frame...
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_13.stopped')
                # update status
                text_13.status = FINISHED
                text_13.setAutoDraw(False)
        
        # *image_25* updates
        
        # if image_25 is starting this frame...
        if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_25.frameNStart = frameN  # exact frame index
            image_25.tStart = t  # local t and not account for scr refresh
            image_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_25.started')
            # update status
            image_25.status = STARTED
            image_25.setAutoDraw(True)
        
        # if image_25 is active this frame...
        if image_25.status == STARTED:
            # update params
            pass
        
        # if image_25 is stopping this frame...
        if image_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_25.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_25.tStop = t  # not accounting for scr refresh
                image_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_25.stopped')
                # update status
                image_25.status = FINISHED
                image_25.setAutoDraw(False)
        
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
        for thisComponent in respo1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "respo1" ---
    for thisComponent in respo1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('respo1.stopped', globalClock.getTime())
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    thisExp.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        thisExp.addData('key_resp_9.rt', key_resp_9.rt)
        thisExp.addData('key_resp_9.duration', key_resp_9.duration)
    thisExp.nextEntry()
    # the Routine "respo1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "respo2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('respo2.started', globalClock.getTime())
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    respo2Components = [key_resp_10, text_14, image_24]
    for thisComponent in respo2Components:
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
    
    # --- Run Routine "respo2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_10* updates
        waitOnFlip = False
        
        # if key_resp_10 is starting this frame...
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            # update status
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_14* updates
        
        # if text_14 is starting this frame...
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_14.started')
            # update status
            text_14.status = STARTED
            text_14.setAutoDraw(True)
        
        # if text_14 is active this frame...
        if text_14.status == STARTED:
            # update params
            pass
        
        # if text_14 is stopping this frame...
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_14.stopped')
                # update status
                text_14.status = FINISHED
                text_14.setAutoDraw(False)
        
        # *image_24* updates
        
        # if image_24 is starting this frame...
        if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_24.frameNStart = frameN  # exact frame index
            image_24.tStart = t  # local t and not account for scr refresh
            image_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_24.started')
            # update status
            image_24.status = STARTED
            image_24.setAutoDraw(True)
        
        # if image_24 is active this frame...
        if image_24.status == STARTED:
            # update params
            pass
        
        # if image_24 is stopping this frame...
        if image_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_24.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_24.tStop = t  # not accounting for scr refresh
                image_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_24.stopped')
                # update status
                image_24.status = FINISHED
                image_24.setAutoDraw(False)
        
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
        for thisComponent in respo2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "respo2" ---
    for thisComponent in respo2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('respo2.stopped', globalClock.getTime())
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    thisExp.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        thisExp.addData('key_resp_10.rt', key_resp_10.rt)
        thisExp.addData('key_resp_10.duration', key_resp_10.duration)
    thisExp.nextEntry()
    # the Routine "respo2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "respo3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('respo3.started', globalClock.getTime())
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    respo3Components = [key_resp_11, text_15, image_21]
    for thisComponent in respo3Components:
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
    
    # --- Run Routine "respo3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_15* updates
        
        # if text_15 is starting this frame...
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_15.started')
            # update status
            text_15.status = STARTED
            text_15.setAutoDraw(True)
        
        # if text_15 is active this frame...
        if text_15.status == STARTED:
            # update params
            pass
        
        # if text_15 is stopping this frame...
        if text_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_15.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_15.tStop = t  # not accounting for scr refresh
                text_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_15.stopped')
                # update status
                text_15.status = FINISHED
                text_15.setAutoDraw(False)
        
        # *image_21* updates
        
        # if image_21 is starting this frame...
        if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_21.frameNStart = frameN  # exact frame index
            image_21.tStart = t  # local t and not account for scr refresh
            image_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_21.started')
            # update status
            image_21.status = STARTED
            image_21.setAutoDraw(True)
        
        # if image_21 is active this frame...
        if image_21.status == STARTED:
            # update params
            pass
        
        # if image_21 is stopping this frame...
        if image_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_21.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_21.tStop = t  # not accounting for scr refresh
                image_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_21.stopped')
                # update status
                image_21.status = FINISHED
                image_21.setAutoDraw(False)
        
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
        for thisComponent in respo3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "respo3" ---
    for thisComponent in respo3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('respo3.stopped', globalClock.getTime())
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "respo3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "memor" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('memor.started', globalClock.getTime())
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    memorComponents = [key_resp_7, text_5, image_13, image_14, image_15, image_16, text_6, text_7]
    for thisComponent in memorComponents:
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
    
    # --- Run Routine "memor" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # *image_13* updates
        
        # if image_13 is starting this frame...
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_13.started')
            # update status
            image_13.status = STARTED
            image_13.setAutoDraw(True)
        
        # if image_13 is active this frame...
        if image_13.status == STARTED:
            # update params
            pass
        
        # if image_13 is stopping this frame...
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_13.stopped')
                # update status
                image_13.status = FINISHED
                image_13.setAutoDraw(False)
        
        # *image_14* updates
        
        # if image_14 is starting this frame...
        if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_14.started')
            # update status
            image_14.status = STARTED
            image_14.setAutoDraw(True)
        
        # if image_14 is active this frame...
        if image_14.status == STARTED:
            # update params
            pass
        
        # if image_14 is stopping this frame...
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_14.stopped')
                # update status
                image_14.status = FINISHED
                image_14.setAutoDraw(False)
        
        # *image_15* updates
        
        # if image_15 is starting this frame...
        if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_15.started')
            # update status
            image_15.status = STARTED
            image_15.setAutoDraw(True)
        
        # if image_15 is active this frame...
        if image_15.status == STARTED:
            # update params
            pass
        
        # if image_15 is stopping this frame...
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.stopped')
                # update status
                image_15.status = FINISHED
                image_15.setAutoDraw(False)
        
        # *image_16* updates
        
        # if image_16 is starting this frame...
        if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_16.frameNStart = frameN  # exact frame index
            image_16.tStart = t  # local t and not account for scr refresh
            image_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_16.started')
            # update status
            image_16.status = STARTED
            image_16.setAutoDraw(True)
        
        # if image_16 is active this frame...
        if image_16.status == STARTED:
            # update params
            pass
        
        # if image_16 is stopping this frame...
        if image_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_16.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image_16.tStop = t  # not accounting for scr refresh
                image_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_16.stopped')
                # update status
                image_16.status = FINISHED
                image_16.setAutoDraw(False)
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # if text_7 is stopping this frame...
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                # update status
                text_7.status = FINISHED
                text_7.setAutoDraw(False)
        
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
        for thisComponent in memorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "memor" ---
    for thisComponent in memorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('memor.stopped', globalClock.getTime())
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "memor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
        trialList = data.importConditions(trialsFilepath),
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
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
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
                    correct = "full left"
                elif stimfile[-5] == "2":       
                    correct = "slight left"
                elif stimfile[-5] == "3":      
                    correct = "slight right"
                elif stimfile[-5] == "4":      
                    correct = "full right"
                    
                if respAll[int(float(kb.keys) - 1)] == correct:
                    match += 1
        
        
            if "obj1" in taskCue or "obj2" in taskCue:
                task = 'obj'
        
                if objFirst == "False":
                    kb.keys = str(float(kb.keys) + 4)
        
                if respAll[int(float(kb.keys) - 1)] in stimfile:
                    match += 1
        
        
            total += 1
            accuracy = (match / total)
        
        if accuracy > 0.8 and total > 10:
            trials.finished = True  # Close the current loop and go to the next loop
        
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
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trial'
    
    
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
