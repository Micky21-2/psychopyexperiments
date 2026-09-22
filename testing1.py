#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on September 22, 2026, at 14:29
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
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'testing1'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1152, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
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
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
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
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\SPPA\\CMKL\\Animation_Project\\Summer\\Experiment_Workflows\\Testing1\\testing1.py',
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
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
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
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color="'#808080'", colorSpace='hex',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = "'#808080'"
        win.colorSpace = 'hex'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
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
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('introresp') is None:
        # initialise introresp
        introresp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='introresp',
        )
    if deviceManager.getDevice('instruct_resp') is None:
        # initialise instruct_resp
        instruct_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instruct_resp',
        )
    if deviceManager.getDevice('warning_resp') is None:
        # initialise warning_resp
        warning_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='warning_resp',
        )
    if deviceManager.getDevice('quz_instruction_text') is None:
        # initialise quz_instruction_text
        quz_instruction_text = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='quz_instruction_text',
        )
    if deviceManager.getDevice('key_resp_quizending') is None:
        # initialise key_resp_quizending
        key_resp_quizending = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_quizending',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
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
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
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
    
    # --- Initialize components for Routine "consent" ---
    consentText = visual.TextBox2(
         win, text='Participant Information and Consent\n\nPURPOSE OF THE STUDY\n- This study looks at how people learn from recorded lectures.\n- You will watch short lecture videos and answer questions about them.\n- The study is run by [researcher names] at [university/department].\n\nWHAT YOU WILL DO\n- Watch [number] lecture video segments on the screen.\n- Answer questions about what you understood.\n- Answer questions about what you thought of the lecture.\n- Fill in a short form about your age, gender, and education.\n\nHOW LONG IT TAKES\n- The whole session takes about 30 to 45 minutes.\n- Please do not pause, skip, or rewind the videos.\n- Please follow the instructions on the screen.\n\nPAYMENT\n- You will receive [amount] baht after you finish the session.\n- Payment is made by [cash / method decided by the school].\n\nYOUR RIGHTS\n- Taking part is voluntary.\n- You can stop and leave at any time. You do not have to give a reason.\n- If you leave, your data will not be stored or used.\n- There is no risk beyond what you meet in everyday life.\n\nPRIVACY\n- Your name will not be written in your data. You will only have a participant number.\n- Your signed consent form will be kept locked in a separate place.\n- Your data will be stored securely for [number] years.\n- Results will only be reported for the whole group. No one will be identified.\n\nWHO CAN TAKE PART\n- You must be 18 years or older.\n- You must have normal vision, or vision corrected with glasses or lenses.\n- You must have normal hearing.\n- You must be able to follow a lecture in English.\n\nQUESTIONS\n- You can ask the experimenter any question before you start.\n- For questions later, contact [name, email, phone].\n- If you have concerns about how the study was run, contact [ethics committee contact].\n\nCONSENT\n- I have read this information, or it was read to me.\n- I understand that I can stop at any time.\n- I agree to take part in this study.\n\nIf you agree, please tell the experimenter. You will sign the printed consent form before you begin.', placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(-0.65, 0.38), draggable=False, units='height',     letterHeight=0.03,
         size=(1.3, None), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='top-left',
         anchor='top-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='consentText',
         depth=0, autoLog=True,
    )
    topMask = visual.Rect(
        win=win, name='topMask',units='height', 
        width=(3, 0.14)[0], height=(3, 0.14)[1],
        ori=0.0, pos=(0, 0.47), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor="'#808080'",
        opacity=None, depth=-1.0, interpolate=True)
    bottomMask = visual.Rect(
        win=win, name='bottomMask',units='height', 
        width=(3, 0.16)[0], height=(3, 0.16)[1],
        ori=0.0, pos=(0, -0.42), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor="'#808080'",
        opacity=None, depth=-2.0, interpolate=True)
    # Run 'Begin Experiment' code from scrollCode
    from psychopy import event
    mouse = event.Mouse(win=win)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "intro" ---
    intro_text = visual.TextBox2(
         win, text="Welcome to this research study on educational video content.\n\n(This study will take approximately 30 minutes to complete.)\n\nYour responses will be kept confidential and used for research \npurposes only. No personally identifying information will be shared \nin any publication resulting from this research.\n\nBy continuing, you confirm that you agree to participate in this study.\n\nPress 'SPACE'  to continue.", placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='intro_text',
         depth=0, autoLog=True,
    )
    introresp = keyboard.Keyboard(deviceName='introresp')
    
    # --- Initialize components for Routine "instructions" ---
    instruction_header = visual.TextBox2(
         win, text='Instructions', placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0.65), draggable=False,      letterHeight=0.15,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='instruction_header',
         depth=0, autoLog=True,
    )
    instruction_text = visual.TextBox2(
         win, text="In this study, you will:\n\n1. Watch a short educational video\n2. Answer a series of questions about what you watched\n3. Answer a few questions about your experience\n\nPress 'SPACE' to continue.", placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.1,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='instruction_text',
         depth=-1, autoLog=True,
    )
    instruct_resp = keyboard.Keyboard(deviceName='instruct_resp')
    
    # --- Initialize components for Routine "warning" ---
    warning_header = visual.TextBox2(
         win, text='IMPORTANT', placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0.65), draggable=False,      letterHeight=0.15,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='warning_header',
         depth=0, autoLog=True,
    )
    warning_text = visual.TextBox2(
         win, text="- You will watch one video in full. Please do not skip, pause, or \n  rewind during playback.\n- Pay close attention, as you will be tested on the content \n  immediately afterward.\n- The video and quiz cannot be repeated once completed.\n- Please do not switch to other tabs, applications, or windows \n  during the video.\n\nPress 'SPACE' when you are ready to begin the video.", placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, -0.15), draggable=False,      letterHeight=0.1,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='warning_text',
         depth=-1, autoLog=True,
    )
    warning_resp = keyboard.Keyboard(deviceName='warning_resp')
    
    # --- Initialize components for Routine "video" ---
    
    # --- Initialize components for Routine "quizinstruction" ---
    textbox = visual.TextBox2(
         win, text="Thank you for watching the video.\n\nYou will now answer some questions about what you just watched.\n\nPlease answer based on your own understanding.\n\nBefore the main questions, you will first complete a short sample \nquiz to help you get familiar with how the questions work.\n\nPress 'SPACE' to begin the questions.", placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=0, autoLog=True,
    )
    quz_instruction_text = keyboard.Keyboard(deviceName='quz_instruction_text')
    
    # --- Initialize components for Routine "quiz" ---
    
    # --- Initialize components for Routine "quizending" ---
    textbox_2 = visual.TextBox2(
         win, text="You have completed the quiz.\n\nJust a few more short questions about your experience, and then \nyou'll be finished.\n\nPress 'SPACE' to continue.", placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(1.85, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_2',
         depth=0, autoLog=True,
    )
    key_resp_quizending = keyboard.Keyboard(deviceName='key_resp_quizending')
    
    # --- Initialize components for Routine "likert" ---
    likertText = visual.TextStim(win=win, name='likertText',
        text='',
        font='Times New Roman',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color="'#000000'", colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    likert_slider = visual.Slider(win=win, name='likert_slider',
        startValue=None, size=(1.5, 0.1), pos=(0, -0.4), units=win.units,
        labels=('Strongly disagree', 'Disagree', 'Somewhat disagree', 'Neither agree nor disagree', 'Somewhat agree', 'Agree', 'Strongly agree'), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor="'#000000'", markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.036,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    nextButton = visual.ButtonStim(win, 
        text='Next>>', font='Times New Roman',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.15, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextButton',
        depth=-2
    )
    nextButton.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "end" ---
    ending_text = visual.TextBox2(
         win, text='Thank you for participating in this study!\n\nYour responses have been recorded successfully.', placeholder='Type here...', font='Times New Roman',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(1.8, 0.5), borderWidth=2.0,
         color="'#000000'", colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='ending_text',
         depth=0, autoLog=True,
    )
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "consent" ---
    # create an object to store info about Routine consent
    consent = data.Routine(
        name='consent',
        components=[consentText, topMask, bottomMask, key_resp],
    )
    consent.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    consentText.reset()
    # Run 'Begin Routine' code from scrollCode
    scrollY = 0
    startX = -0.65       # left edge of the text
    startY = 0.38        # top edge of the text
    maxScroll = 1.4      
    scrollSpeed = 0.05
    atBottom = False
    DEBUG = True         # set to False when you finish tuning
    event.clearEvents()
    mouse.getWheelRel()  # discard old wheel movement
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for consent
    consent.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    consent.tStart = globalClock.getTime(format='float')
    consent.status = STARTED
    thisExp.addData('consent.started', consent.tStart)
    consent.maxDuration = None
    # keep track of which components have finished
    consentComponents = consent.components
    for thisComponent in consent.components:
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
    
    # --- Run Routine "consent" ---
    consent.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *consentText* updates
        
        # if consentText is starting this frame...
        if consentText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consentText.frameNStart = frameN  # exact frame index
            consentText.tStart = t  # local t and not account for scr refresh
            consentText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consentText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consentText.started')
            # update status
            consentText.status = STARTED
            consentText.setAutoDraw(True)
        
        # if consentText is active this frame...
        if consentText.status == STARTED:
            # update params
            pass
        
        # *topMask* updates
        
        # if topMask is starting this frame...
        if topMask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            topMask.frameNStart = frameN  # exact frame index
            topMask.tStart = t  # local t and not account for scr refresh
            topMask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(topMask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'topMask.started')
            # update status
            topMask.status = STARTED
            topMask.setAutoDraw(True)
        
        # if topMask is active this frame...
        if topMask.status == STARTED:
            # update params
            pass
        
        # *bottomMask* updates
        
        # if bottomMask is starting this frame...
        if bottomMask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottomMask.frameNStart = frameN  # exact frame index
            bottomMask.tStart = t  # local t and not account for scr refresh
            bottomMask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottomMask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bottomMask.started')
            # update status
            bottomMask.status = STARTED
            bottomMask.setAutoDraw(True)
        
        # if bottomMask is active this frame...
        if bottomMask.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from scrollCode
        wheel = mouse.getWheelRel()[1]
        keys = event.getKeys(keyList=['up', 'down', 'space'])
        if 'down' in keys:
            wheel -= 2
        if 'up' in keys:
            wheel += 2
        
        scrollY -= wheel * scrollSpeed
        scrollY = max(0, min(maxScroll, scrollY))
        consentText.pos = (startX, startY + scrollY)
        
        atBottom = scrollY >= maxScroll - 0.01
        
        if atBottom and 'space' in keys:
            continueRoutine = False
        
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
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=consent,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            consent.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consent.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consent.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for consent
    consent.tStop = globalClock.getTime(format='float')
    consent.tStopRefresh = tThisFlipGlobal
    thisExp.addData('consent.stopped', consent.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "intro" ---
    # create an object to store info about Routine intro
    intro = data.Routine(
        name='intro',
        components=[intro_text, introresp],
    )
    intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    intro_text.reset()
    # create starting attributes for introresp
    introresp.keys = []
    introresp.rt = []
    _introresp_allKeys = []
    # store start times for intro
    intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    intro.tStart = globalClock.getTime(format='float')
    intro.status = STARTED
    thisExp.addData('intro.started', intro.tStart)
    intro.maxDuration = None
    # keep track of which components have finished
    introComponents = intro.components
    for thisComponent in intro.components:
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
    
    # --- Run Routine "intro" ---
    intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        
        # if intro_text is starting this frame...
        if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.tStart = t  # local t and not account for scr refresh
            intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_text.started')
            # update status
            intro_text.status = STARTED
            intro_text.setAutoDraw(True)
        
        # if intro_text is active this frame...
        if intro_text.status == STARTED:
            # update params
            pass
        
        # *introresp* updates
        waitOnFlip = False
        
        # if introresp is starting this frame...
        if introresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            introresp.frameNStart = frameN  # exact frame index
            introresp.tStart = t  # local t and not account for scr refresh
            introresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(introresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'introresp.started')
            # update status
            introresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(introresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(introresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if introresp.status == STARTED and not waitOnFlip:
            theseKeys = introresp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _introresp_allKeys.extend(theseKeys)
            if len(_introresp_allKeys):
                introresp.keys = _introresp_allKeys[-1].name  # just the last key pressed
                introresp.rt = _introresp_allKeys[-1].rt
                introresp.duration = _introresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=intro,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for intro
    intro.tStop = globalClock.getTime(format='float')
    intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('intro.stopped', intro.tStop)
    # check responses
    if introresp.keys in ['', [], None]:  # No response was made
        introresp.keys = None
    thisExp.addData('introresp.keys',introresp.keys)
    if introresp.keys != None:  # we had a response
        thisExp.addData('introresp.rt', introresp.rt)
        thisExp.addData('introresp.duration', introresp.duration)
    thisExp.nextEntry()
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[instruction_header, instruction_text, instruct_resp],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    instruction_header.reset()
    instruction_text.reset()
    # create starting attributes for instruct_resp
    instruct_resp.keys = []
    instruct_resp.rt = []
    _instruct_resp_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
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
    
    # --- Run Routine "instructions" ---
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_header* updates
        
        # if instruction_header is starting this frame...
        if instruction_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_header.frameNStart = frameN  # exact frame index
            instruction_header.tStart = t  # local t and not account for scr refresh
            instruction_header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_header, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_header.started')
            # update status
            instruction_header.status = STARTED
            instruction_header.setAutoDraw(True)
        
        # if instruction_header is active this frame...
        if instruction_header.status == STARTED:
            # update params
            pass
        
        # *instruction_text* updates
        
        # if instruction_text is starting this frame...
        if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text.frameNStart = frameN  # exact frame index
            instruction_text.tStart = t  # local t and not account for scr refresh
            instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text.started')
            # update status
            instruction_text.status = STARTED
            instruction_text.setAutoDraw(True)
        
        # if instruction_text is active this frame...
        if instruction_text.status == STARTED:
            # update params
            pass
        
        # *instruct_resp* updates
        waitOnFlip = False
        
        # if instruct_resp is starting this frame...
        if instruct_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_resp.frameNStart = frameN  # exact frame index
            instruct_resp.tStart = t  # local t and not account for scr refresh
            instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruct_resp.started')
            # update status
            instruct_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruct_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruct_resp.status == STARTED and not waitOnFlip:
            theseKeys = instruct_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instruct_resp_allKeys.extend(theseKeys)
            if len(_instruct_resp_allKeys):
                instruct_resp.keys = _instruct_resp_allKeys[-1].name  # just the last key pressed
                instruct_resp.rt = _instruct_resp_allKeys[-1].rt
                instruct_resp.duration = _instruct_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if instruct_resp.keys in ['', [], None]:  # No response was made
        instruct_resp.keys = None
    thisExp.addData('instruct_resp.keys',instruct_resp.keys)
    if instruct_resp.keys != None:  # we had a response
        thisExp.addData('instruct_resp.rt', instruct_resp.rt)
        thisExp.addData('instruct_resp.duration', instruct_resp.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "warning" ---
    # create an object to store info about Routine warning
    warning = data.Routine(
        name='warning',
        components=[warning_header, warning_text, warning_resp],
    )
    warning.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    warning_header.reset()
    warning_text.reset()
    # create starting attributes for warning_resp
    warning_resp.keys = []
    warning_resp.rt = []
    _warning_resp_allKeys = []
    # store start times for warning
    warning.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    warning.tStart = globalClock.getTime(format='float')
    warning.status = STARTED
    thisExp.addData('warning.started', warning.tStart)
    warning.maxDuration = None
    # keep track of which components have finished
    warningComponents = warning.components
    for thisComponent in warning.components:
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
    
    # --- Run Routine "warning" ---
    warning.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *warning_header* updates
        
        # if warning_header is starting this frame...
        if warning_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            warning_header.frameNStart = frameN  # exact frame index
            warning_header.tStart = t  # local t and not account for scr refresh
            warning_header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning_header, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warning_header.started')
            # update status
            warning_header.status = STARTED
            warning_header.setAutoDraw(True)
        
        # if warning_header is active this frame...
        if warning_header.status == STARTED:
            # update params
            pass
        
        # *warning_text* updates
        
        # if warning_text is starting this frame...
        if warning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            warning_text.frameNStart = frameN  # exact frame index
            warning_text.tStart = t  # local t and not account for scr refresh
            warning_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warning_text.started')
            # update status
            warning_text.status = STARTED
            warning_text.setAutoDraw(True)
        
        # if warning_text is active this frame...
        if warning_text.status == STARTED:
            # update params
            pass
        
        # *warning_resp* updates
        waitOnFlip = False
        
        # if warning_resp is starting this frame...
        if warning_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            warning_resp.frameNStart = frameN  # exact frame index
            warning_resp.tStart = t  # local t and not account for scr refresh
            warning_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'warning_resp.started')
            # update status
            warning_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(warning_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(warning_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if warning_resp.status == STARTED and not waitOnFlip:
            theseKeys = warning_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _warning_resp_allKeys.extend(theseKeys)
            if len(_warning_resp_allKeys):
                warning_resp.keys = _warning_resp_allKeys[-1].name  # just the last key pressed
                warning_resp.rt = _warning_resp_allKeys[-1].rt
                warning_resp.duration = _warning_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=warning,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            warning.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in warning.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "warning" ---
    for thisComponent in warning.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for warning
    warning.tStop = globalClock.getTime(format='float')
    warning.tStopRefresh = tThisFlipGlobal
    thisExp.addData('warning.stopped', warning.tStop)
    # check responses
    if warning_resp.keys in ['', [], None]:  # No response was made
        warning_resp.keys = None
    thisExp.addData('warning_resp.keys',warning_resp.keys)
    if warning_resp.keys != None:  # we had a response
        thisExp.addData('warning_resp.rt', warning_resp.rt)
        thisExp.addData('warning_resp.duration', warning_resp.duration)
    thisExp.nextEntry()
    # the Routine "warning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "video" ---
    # create an object to store info about Routine video
    video = data.Routine(
        name='video',
        components=[],
    )
    video.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for video
    video.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    video.tStart = globalClock.getTime(format='float')
    video.status = STARTED
    thisExp.addData('video.started', video.tStart)
    video.maxDuration = None
    # keep track of which components have finished
    videoComponents = video.components
    for thisComponent in video.components:
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
    
    # --- Run Routine "video" ---
    video.forceEnded = routineForceEnded = not continueRoutine
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
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=video,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            video.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in video.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "video" ---
    for thisComponent in video.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for video
    video.tStop = globalClock.getTime(format='float')
    video.tStopRefresh = tThisFlipGlobal
    thisExp.addData('video.stopped', video.tStop)
    thisExp.nextEntry()
    # the Routine "video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "quizinstruction" ---
    # create an object to store info about Routine quizinstruction
    quizinstruction = data.Routine(
        name='quizinstruction',
        components=[textbox, quz_instruction_text],
    )
    quizinstruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # create starting attributes for quz_instruction_text
    quz_instruction_text.keys = []
    quz_instruction_text.rt = []
    _quz_instruction_text_allKeys = []
    # store start times for quizinstruction
    quizinstruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    quizinstruction.tStart = globalClock.getTime(format='float')
    quizinstruction.status = STARTED
    thisExp.addData('quizinstruction.started', quizinstruction.tStart)
    quizinstruction.maxDuration = None
    # keep track of which components have finished
    quizinstructionComponents = quizinstruction.components
    for thisComponent in quizinstruction.components:
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
    
    # --- Run Routine "quizinstruction" ---
    quizinstruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # *quz_instruction_text* updates
        waitOnFlip = False
        
        # if quz_instruction_text is starting this frame...
        if quz_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quz_instruction_text.frameNStart = frameN  # exact frame index
            quz_instruction_text.tStart = t  # local t and not account for scr refresh
            quz_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quz_instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'quz_instruction_text.started')
            # update status
            quz_instruction_text.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(quz_instruction_text.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(quz_instruction_text.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if quz_instruction_text.status == STARTED and not waitOnFlip:
            theseKeys = quz_instruction_text.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _quz_instruction_text_allKeys.extend(theseKeys)
            if len(_quz_instruction_text_allKeys):
                quz_instruction_text.keys = _quz_instruction_text_allKeys[-1].name  # just the last key pressed
                quz_instruction_text.rt = _quz_instruction_text_allKeys[-1].rt
                quz_instruction_text.duration = _quz_instruction_text_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=quizinstruction,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            quizinstruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quizinstruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "quizinstruction" ---
    for thisComponent in quizinstruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for quizinstruction
    quizinstruction.tStop = globalClock.getTime(format='float')
    quizinstruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('quizinstruction.stopped', quizinstruction.tStop)
    # check responses
    if quz_instruction_text.keys in ['', [], None]:  # No response was made
        quz_instruction_text.keys = None
    thisExp.addData('quz_instruction_text.keys',quz_instruction_text.keys)
    if quz_instruction_text.keys != None:  # we had a response
        thisExp.addData('quz_instruction_text.rt', quz_instruction_text.rt)
        thisExp.addData('quz_instruction_text.duration', quz_instruction_text.duration)
    thisExp.nextEntry()
    # the Routine "quizinstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "quiz" ---
    # create an object to store info about Routine quiz
    quiz = data.Routine(
        name='quiz',
        components=[],
    )
    quiz.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for quiz
    quiz.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    quiz.tStart = globalClock.getTime(format='float')
    quiz.status = STARTED
    thisExp.addData('quiz.started', quiz.tStart)
    quiz.maxDuration = None
    # keep track of which components have finished
    quizComponents = quiz.components
    for thisComponent in quiz.components:
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
    
    # --- Run Routine "quiz" ---
    quiz.forceEnded = routineForceEnded = not continueRoutine
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
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=quiz,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            quiz.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quiz.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "quiz" ---
    for thisComponent in quiz.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for quiz
    quiz.tStop = globalClock.getTime(format='float')
    quiz.tStopRefresh = tThisFlipGlobal
    thisExp.addData('quiz.stopped', quiz.tStop)
    thisExp.nextEntry()
    # the Routine "quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "quizending" ---
    # create an object to store info about Routine quizending
    quizending = data.Routine(
        name='quizending',
        components=[textbox_2, key_resp_quizending],
    )
    quizending.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox_2.reset()
    # create starting attributes for key_resp_quizending
    key_resp_quizending.keys = []
    key_resp_quizending.rt = []
    _key_resp_quizending_allKeys = []
    # store start times for quizending
    quizending.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    quizending.tStart = globalClock.getTime(format='float')
    quizending.status = STARTED
    thisExp.addData('quizending.started', quizending.tStart)
    quizending.maxDuration = None
    # keep track of which components have finished
    quizendingComponents = quizending.components
    for thisComponent in quizending.components:
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
    
    # --- Run Routine "quizending" ---
    quizending.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_2* updates
        
        # if textbox_2 is starting this frame...
        if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_2.frameNStart = frameN  # exact frame index
            textbox_2.tStart = t  # local t and not account for scr refresh
            textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_2.started')
            # update status
            textbox_2.status = STARTED
            textbox_2.setAutoDraw(True)
        
        # if textbox_2 is active this frame...
        if textbox_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_quizending* updates
        waitOnFlip = False
        
        # if key_resp_quizending is starting this frame...
        if key_resp_quizending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_quizending.frameNStart = frameN  # exact frame index
            key_resp_quizending.tStart = t  # local t and not account for scr refresh
            key_resp_quizending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_quizending, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_quizending.started')
            # update status
            key_resp_quizending.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_quizending.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_quizending.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_quizending.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_quizending.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_quizending_allKeys.extend(theseKeys)
            if len(_key_resp_quizending_allKeys):
                key_resp_quizending.keys = _key_resp_quizending_allKeys[-1].name  # just the last key pressed
                key_resp_quizending.rt = _key_resp_quizending_allKeys[-1].rt
                key_resp_quizending.duration = _key_resp_quizending_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=quizending,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            quizending.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quizending.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "quizending" ---
    for thisComponent in quizending.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for quizending
    quizending.tStop = globalClock.getTime(format='float')
    quizending.tStopRefresh = tThisFlipGlobal
    thisExp.addData('quizending.stopped', quizending.tStop)
    # check responses
    if key_resp_quizending.keys in ['', [], None]:  # No response was made
        key_resp_quizending.keys = None
    thisExp.addData('key_resp_quizending.keys',key_resp_quizending.keys)
    if key_resp_quizending.keys != None:  # we had a response
        thisExp.addData('key_resp_quizending.rt', key_resp_quizending.rt)
        thisExp.addData('key_resp_quizending.duration', key_resp_quizending.duration)
    thisExp.nextEntry()
    # the Routine "quizending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    likertLoop = data.TrialHandler2(
        name='likertLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('likert_items.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(likertLoop)  # add the loop to the experiment
    thisLikertLoop = likertLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLikertLoop.rgb)
    if thisLikertLoop != None:
        for paramName in thisLikertLoop:
            globals()[paramName] = thisLikertLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLikertLoop in likertLoop:
        likertLoop.status = STARTED
        if hasattr(thisLikertLoop, 'status'):
            thisLikertLoop.status = STARTED
        currentLoop = likertLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLikertLoop.rgb)
        if thisLikertLoop != None:
            for paramName in thisLikertLoop:
                globals()[paramName] = thisLikertLoop[paramName]
        
        # --- Prepare to start Routine "likert" ---
        # create an object to store info about Routine likert
        likert = data.Routine(
            name='likert',
            components=[likertText, likert_slider, nextButton],
        )
        likert.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        likertText.setText(itemText)
        likert_slider.reset()
        # reset nextButton to account for continued clicks & clear times on/off
        nextButton.reset()
        # store start times for likert
        likert.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        likert.tStart = globalClock.getTime(format='float')
        likert.status = STARTED
        thisExp.addData('likert.started', likert.tStart)
        likert.maxDuration = None
        # keep track of which components have finished
        likertComponents = likert.components
        for thisComponent in likert.components:
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
        
        # --- Run Routine "likert" ---
        likert.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLikertLoop, 'status') and thisLikertLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *likertText* updates
            
            # if likertText is starting this frame...
            if likertText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                likertText.frameNStart = frameN  # exact frame index
                likertText.tStart = t  # local t and not account for scr refresh
                likertText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(likertText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'likertText.started')
                # update status
                likertText.status = STARTED
                likertText.setAutoDraw(True)
            
            # if likertText is active this frame...
            if likertText.status == STARTED:
                # update params
                pass
            
            # *likert_slider* updates
            
            # if likert_slider is starting this frame...
            if likert_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                likert_slider.frameNStart = frameN  # exact frame index
                likert_slider.tStart = t  # local t and not account for scr refresh
                likert_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(likert_slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'likert_slider.started')
                # update status
                likert_slider.status = STARTED
                likert_slider.setAutoDraw(True)
            
            # if likert_slider is active this frame...
            if likert_slider.status == STARTED:
                # update params
                pass
            # *nextButton* updates
            
            # if nextButton is starting this frame...
            if nextButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextButton.frameNStart = frameN  # exact frame index
                nextButton.tStart = t  # local t and not account for scr refresh
                nextButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextButton, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nextButton.started')
                # update status
                nextButton.status = STARTED
                win.callOnFlip(nextButton.buttonClock.reset)
                nextButton.setAutoDraw(True)
            
            # if nextButton is active this frame...
            if nextButton.status == STARTED:
                # update params
                pass
                # check whether nextButton has been pressed
                if nextButton.isClicked:
                    if not nextButton.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextButton.timesOn.append(nextButton.buttonClock.getTime())
                        nextButton.timesOff.append(nextButton.buttonClock.getTime())
                    elif len(nextButton.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextButton.timesOff[-1] = nextButton.buttonClock.getTime()
                    if not nextButton.wasClicked:
                        # end routine when nextButton is clicked
                        continueRoutine = False
                    if not nextButton.wasClicked:
                        # run callback code when nextButton is clicked
                        pass
            # take note of whether nextButton was clicked, so that next frame we know if clicks are new
            nextButton.wasClicked = nextButton.isClicked and nextButton.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=likert,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                likert.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in likert.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "likert" ---
        for thisComponent in likert.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for likert
        likert.tStop = globalClock.getTime(format='float')
        likert.tStopRefresh = tThisFlipGlobal
        thisExp.addData('likert.stopped', likert.tStop)
        likertLoop.addData('likert_slider.response', likert_slider.getRating())
        likertLoop.addData('likert_slider.rt', likert_slider.getRT())
        likertLoop.addData('nextButton.numClicks', nextButton.numClicks)
        if nextButton.numClicks:
           likertLoop.addData('nextButton.timesOn', nextButton.timesOn)
           likertLoop.addData('nextButton.timesOff', nextButton.timesOff)
        else:
           likertLoop.addData('nextButton.timesOn', "")
           likertLoop.addData('nextButton.timesOff', "")
        # the Routine "likert" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLikertLoop as finished
        if hasattr(thisLikertLoop, 'status'):
            thisLikertLoop.status = FINISHED
        # if awaiting a pause, pause now
        if likertLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            likertLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'likertLoop'
    likertLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[ending_text],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ending_text.reset()
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
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
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ending_text* updates
        
        # if ending_text is starting this frame...
        if ending_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ending_text.frameNStart = frameN  # exact frame index
            ending_text.tStart = t  # local t and not account for scr refresh
            ending_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ending_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ending_text.started')
            # update status
            ending_text.status = STARTED
            ending_text.setAutoDraw(True)
        
        # if ending_text is active this frame...
        if ending_text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


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


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
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
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
