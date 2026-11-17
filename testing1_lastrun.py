#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on November 16, 2026, at 14:09
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
        originPath='C:\\Users\\LENOVO\\Documents\\psychopyexperiments\\testing1_lastrun.py',
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
            monitor='testMonitor', color=[0.3255, 0.3255, 0.3255], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.3255, 0.3255, 0.3255]
        win.colorSpace = 'rgb'
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
    if deviceManager.getDevice('instruct_resp') is None:
        # initialise instruct_resp
        instruct_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instruct_resp',
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
    
    # --- Initialize components for Routine "instructions" ---
    instruction_header = visual.TextBox2(
         win, text='INSTRUCTIONS', placeholder='Type here...', font='Arial',
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
         depth=-1, autoLog=True,
    )
    instruction_text = visual.TextBox2(
         win, text='In this study, you will:\n\n1. Watch a short sample video.\n2. Answer sample questions.\n3. Watch an educational video.\n4. Answer a series of questions about what you watched.\n5. Answer a few questions about your experience.\n6. Answer a short form about your age, gender, and education.\n\n', placeholder='Type here...', font='Arial',
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
         name='instruction_text',
         depth=-2, autoLog=True,
    )
    instruct_resp = keyboard.Keyboard(deviceName='instruct_resp')
    nextButton_instructions = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextButton_instructions',
        depth=-4
    )
    nextButton_instructions.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "sampleVideo" ---
    samplevideo = visual.MovieStim(
        win, name='samplevideo',
        filename='3_with_jump.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.5, 0.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    nextbuttonSample = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextbuttonSample',
        depth=-1
    )
    nextbuttonSample.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "SampleQuestions" ---
    nextSampleQuestion = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextSampleQuestion',
        depth=-3
    )
    nextSampleQuestion.buttonClock = core.Clock()
    samplequestionA = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.35), draggable=False,      letterHeight=0.05,
         size=(0.6, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='samplequestionA',
         depth=-4, autoLog=True,
    )
    sampleBoxA = visual.Rect(
        win=win, name='sampleBoxA',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    samplequestionchoiceA = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.1), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='samplequestionchoiceA',
         depth=-6, autoLog=True,
    )
    sampleBoxB = visual.Rect(
        win=win, name='sampleBoxB',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.05), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    samplequestionchoiceB = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='samplequestionchoiceB',
         depth=-8, autoLog=True,
    )
    sampleBoxC = visual.Rect(
        win=win, name='sampleBoxC',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-9.0, interpolate=True)
    samplequestionchoiceC = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.20), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='samplequestionchoiceC',
         depth=-10, autoLog=True,
    )
    sampleBoxD = visual.Rect(
        win=win, name='sampleBoxD',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.35), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    samplequestionchoiceD = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='samplequestionchoiceD',
         depth=-12, autoLog=True,
    )
    sampleQuestionMouse = event.Mouse(win=win)
    x, y = [None, None]
    sampleQuestionMouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "intstructionforRealVideo" ---
    rv_text = visual.TextBox2(
         win, text='You will now watch a 15 minutes educational video.\n\nPlease click on "Next>>" button to start.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.1), draggable=False,      letterHeight=0.08,
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
         name='rv_text',
         depth=0, autoLog=True,
    )
    next_rv = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='next_rv',
        depth=-1
    )
    next_rv.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "videoAssignment" ---
    # Run 'Begin Experiment' code from progress_videoAssignment
    progressStep = 0
    progressTotal = 21
    progressBackground = visual.Rect(win=win, width=1.8, height=0.025, pos=(0, 0.94), units='norm', fillColor='white', lineColor='white', opacity=0.45, depth=-100)
    progressBar = visual.Rect(win=win, width=0.01, height=0.025, pos=(-0.895, 0.94), units='norm', fillColor='lightblue', lineColor='lightblue', depth=-101)
    progressBackground.setAutoDraw(True)
    progressBar.setAutoDraw(True)
    # Run 'Begin Experiment' code from code_10
    import csv
    import random
    
    # SETTINGS
    video_files = [
        "[Original]MultiExecutable_15min.mp4",
        "[Animated]MultiExecutable_15min.mp4",
        "Possessed_cat.mp4",
        "Jack_jet.mp4",
        "Creepy and scary cat.mp4",
        "cattransition.mp4"
    ]
    
    MAX_PER_VIDEO = 6
    
    # File used to keep track of assignments
    assignment_file = os.path.join(
        _thisDir,
        "video_assignment.csv"
    )
    
    # CREATE ASSIGNMENT FILE IF IT DOES NOT EXIST
    
    if not os.path.exists(assignment_file):
    
        with open(assignment_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["participant", "video"])
    
    
    # READ PREVIOUS ASSIGNMENTS
    
    video_counts = {video: 0 for video in video_files}
    
    with open(assignment_file, "r", newline="") as f:
    
        reader = csv.DictReader(f)
    
        for row in reader:
    
            video = row["video"]
    
            if video in video_counts:
                video_counts[video] += 1
    
    
    # FIND VIDEOS THAT STILL HAVE SPACE
    available_videos = [
        video
        for video in video_files
        if video_counts[video] < MAX_PER_VIDEO
    ]
    
    
    # RANDOMLY SELECT ONE AVAILABLE VIDEO
    if len(available_videos) == 0:
    
        raise Exception(
            "All videos have already been assigned "
            "to 6 participants each."
        )
    
    selected_video = random.choice(available_videos)
    
    
    # SAVE THE ASSIGNMENT
    participant_id = expInfo["participant"]
    
    with open(assignment_file, "a", newline="") as f:
    
        writer = csv.writer(f)
    
        writer.writerow([
            participant_id,
            selected_video
        ])
    
    
    
    # VARIABLE USED BY MOVIE COMPONENT
    video_to_play = selected_video
    thisExp.addData("assigned_video", video_to_play)
    
    # SELECT WHICH QUIZ TO RUN
    
    if selected_video in [
        "[Original]MultiExecutable_15min.mp4",
        "[Animated]MultiExecutable_15min.mp4"
    ]:
        quizA_reps = 1
        quizB_reps = 0
        quizC_reps = 0
    
    elif selected_video in [
        "Possessed_cat.mp4",
        "Jack_jet.mp4"
    ]:
        quizA_reps = 0
        quizB_reps = 1
        quizC_reps = 0
    
    elif selected_video in [
        "Creepy and scary cat.mp4",
        "cattransition.mp4"
    ]:
        quizA_reps = 0
        quizB_reps = 0
        quizC_reps = 1
    
    # --- Initialize components for Routine "video" ---
    movie = visual.MovieStim(
        win, name='movie',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(1.5, 1.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-2
    )
    nextVideo = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextVideo',
        depth=-3
    )
    nextVideo.buttonClock = core.Clock()
    rq_text_2 = visual.TextBox2(
         win, text='You will now answer a few questions related to what you have watched.\n\nPlease click on "Next>>" button to start.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.1), draggable=False,      letterHeight=0.08,
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
         name='rq_text_2',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "QuizA" ---
    nextQuizA = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextQuizA',
        depth=-3
    )
    nextQuizA.buttonClock = core.Clock()
    questionAText = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.35), draggable=False,      letterHeight=0.05,
         size=(0.6, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='questionAText',
         depth=-4, autoLog=True,
    )
    boxA = visual.Rect(
        win=win, name='boxA',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    choiceA = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.1), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceA',
         depth=-6, autoLog=True,
    )
    boxB = visual.Rect(
        win=win, name='boxB',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.05), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    choiceB = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceB',
         depth=-8, autoLog=True,
    )
    boxC = visual.Rect(
        win=win, name='boxC',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-9.0, interpolate=True)
    choiceC = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.20), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceC',
         depth=-10, autoLog=True,
    )
    boxD = visual.Rect(
        win=win, name='boxD',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.35), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    choiceD = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceD',
         depth=-12, autoLog=True,
    )
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "QuizB" ---
    nextQuizB = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextQuizB',
        depth=-3
    )
    nextQuizB.buttonClock = core.Clock()
    questionBText = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.35), draggable=False,      letterHeight=0.05,
         size=(0.6, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='questionBText',
         depth=-4, autoLog=True,
    )
    boxA_2 = visual.Rect(
        win=win, name='boxA_2',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    choiceA_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.1), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceA_2',
         depth=-6, autoLog=True,
    )
    boxB_2 = visual.Rect(
        win=win, name='boxB_2',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.05), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    choiceB_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceB_2',
         depth=-8, autoLog=True,
    )
    boxC_2 = visual.Rect(
        win=win, name='boxC_2',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-9.0, interpolate=True)
    choiceC_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.20), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceC_2',
         depth=-10, autoLog=True,
    )
    boxD_2 = visual.Rect(
        win=win, name='boxD_2',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.35), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    choiceD_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceD_2',
         depth=-12, autoLog=True,
    )
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "QuizC" ---
    nextQuizC = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextQuizC',
        depth=-3
    )
    nextQuizC.buttonClock = core.Clock()
    questionCText = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.35), draggable=False,      letterHeight=0.05,
         size=(0.6, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='questionCText',
         depth=-4, autoLog=True,
    )
    boxA_3 = visual.Rect(
        win=win, name='boxA_3',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    choiceA_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.1), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceA_3',
         depth=-6, autoLog=True,
    )
    boxB_3 = visual.Rect(
        win=win, name='boxB_3',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.05), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    choiceB_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceB_3',
         depth=-8, autoLog=True,
    )
    boxC_3 = visual.Rect(
        win=win, name='boxC_3',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-9.0, interpolate=True)
    choiceC_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.20), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceC_3',
         depth=-10, autoLog=True,
    )
    boxD_3 = visual.Rect(
        win=win, name='boxD_3',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.35), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    choiceD_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceD_3',
         depth=-12, autoLog=True,
    )
    mouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_4.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "instructionLikert" ---
    lr_text = visual.TextBox2(
         win, text='You will now answer a few questions about your experience.\n\nPlease click on "Next>>" button to start.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.1), draggable=False,      letterHeight=0.08,
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
         name='lr_text',
         depth=0, autoLog=True,
    )
    next_lr = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='next_lr',
        depth=-1
    )
    next_lr.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "likert" ---
    likertText = visual.TextStim(win=win, name='likertText',
        text='',
        font='Arial',
        pos=(0, 0.34), draggable=False, height=0.1, wrapWidth=1.5, ori=0.0, 
        color="'#000000'", colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    likert_slider = visual.Slider(win=win, name='likert_slider',
        startValue=4, size=(1.7, 0.1), pos=(0, 0.08), units=win.units,
        labels=('Strongly  disagree', 'Disagree', 'Somewhat  disagree', 'Neither  agree nor disagree', 'Somewhat  agree', 'Agree', 'Strongly  agree'), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor="'#000000'", markerColor=[0.3569, 0.6941, 0.8039], lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=0.084,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    nextButton = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextButton',
        depth=-3
    )
    nextButton.buttonClock = core.Clock()
    # Run 'Begin Experiment' code from code_7
    # Ctrl + Q to quit
    keys = event.getKeys(modifiers=True)
    
    for key, modifiers in keys:
        if key.lower() == 'q' and modifiers.get('ctrl', False):
            core.quit()
    instruction_slider = visual.TextBox2(
         win, text='"PLEASE CLICK ON THE SCALE OR INDICATION ON THE SLIDER"', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.55), draggable=False,      letterHeight=0.05,
         size=(1.2, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='instruction_slider',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "demographicQuiz" ---
    nextDemo = visual.ButtonStim(win, 
        text='Next >>', font='Arial',
        pos=(0.8, -0.75),
        letterHeight=0.05,
        size=(0.18, 0.15), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='nextDemo',
        depth=-4
    )
    nextDemo.buttonClock = core.Clock()
    questionDemo = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.35), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='questionDemo',
         depth=-5, autoLog=True,
    )
    box1 = visual.Rect(
        win=win, name='box1',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    choiceA_demo = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.1), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceA_demo',
         depth=-7, autoLog=True,
    )
    box2 = visual.Rect(
        win=win, name='box2',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.05), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    choiceB_demo = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceB_demo',
         depth=-9, autoLog=True,
    )
    box3 = visual.Rect(
        win=win, name='box3',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-10.0, interpolate=True)
    choiceC_demo = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.20), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceC_demo',
         depth=-11, autoLog=True,
    )
    box4 = visual.Rect(
        win=win, name='box4',
        width=(1, 0.12)[0], height=(1, 0.12)[1],
        ori=0.0, pos=(0, -0.35), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-12.0, interpolate=True)
    choiceD_demo = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(1.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='choiceD_demo',
         depth=-13, autoLog=True,
    )
    mouse_5 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_5.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "end" ---
    ending_text = visual.TextBox2(
         win, text='Thank you for participating in this study!\n\nYour responses have been recorded successfully.', placeholder='Type here...', font='Arial',
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
         depth=-1, autoLog=True,
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
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[instruction_header, instruction_text, instruct_resp, nextButton_instructions],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from progress_instructions
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    instruction_header.reset()
    instruction_text.reset()
    # create starting attributes for instruct_resp
    instruct_resp.keys = []
    instruct_resp.rt = []
    _instruct_resp_allKeys = []
    # reset nextButton_instructions to account for continued clicks & clear times on/off
    nextButton_instructions.reset()
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
            # update status
            instruction_text.status = STARTED
            instruction_text.setAutoDraw(True)
        
        # if instruction_text is active this frame...
        if instruction_text.status == STARTED:
            # update params
            pass
        
        # *instruct_resp* updates
        
        # if instruct_resp is starting this frame...
        if instruct_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_resp.frameNStart = frameN  # exact frame index
            instruct_resp.tStart = t  # local t and not account for scr refresh
            instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruct_resp.status = STARTED
            # keyboard checking is just starting
            instruct_resp.clock.reset()  # now t=0
            instruct_resp.clearEvents(eventType='keyboard')
        if instruct_resp.status == STARTED:
            theseKeys = instruct_resp.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _instruct_resp_allKeys.extend(theseKeys)
            if len(_instruct_resp_allKeys):
                instruct_resp.keys = _instruct_resp_allKeys[-1].name  # just the last key pressed
                instruct_resp.rt = _instruct_resp_allKeys[-1].rt
                instruct_resp.duration = _instruct_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *nextButton_instructions* updates
        
        # if nextButton_instructions is starting this frame...
        if nextButton_instructions.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            nextButton_instructions.frameNStart = frameN  # exact frame index
            nextButton_instructions.tStart = t  # local t and not account for scr refresh
            nextButton_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextButton_instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            nextButton_instructions.status = STARTED
            win.callOnFlip(nextButton_instructions.buttonClock.reset)
            nextButton_instructions.setAutoDraw(True)
        
        # if nextButton_instructions is active this frame...
        if nextButton_instructions.status == STARTED:
            # update params
            pass
            # check whether nextButton_instructions has been pressed
            if nextButton_instructions.isClicked:
                if not nextButton_instructions.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    nextButton_instructions.timesOn.append(nextButton_instructions.buttonClock.getTime())
                    nextButton_instructions.timesOff.append(nextButton_instructions.buttonClock.getTime())
                elif len(nextButton_instructions.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    nextButton_instructions.timesOff[-1] = nextButton_instructions.buttonClock.getTime()
                if not nextButton_instructions.wasClicked:
                    # end routine when nextButton_instructions is clicked
                    continueRoutine = False
                if not nextButton_instructions.wasClicked:
                    # run callback code when nextButton_instructions is clicked
                    pass
        # take note of whether nextButton_instructions was clicked, so that next frame we know if clicks are new
        nextButton_instructions.wasClicked = nextButton_instructions.isClicked and nextButton_instructions.status == STARTED
        # Run 'Each Frame' code from code
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
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
    
    # --- Prepare to start Routine "sampleVideo" ---
    # create an object to store info about Routine sampleVideo
    sampleVideo = data.Routine(
        name='sampleVideo',
        components=[samplevideo, nextbuttonSample],
    )
    sampleVideo.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset nextbuttonSample to account for continued clicks & clear times on/off
    nextbuttonSample.reset()
    # Run 'Begin Routine' code from progress_samplevideo
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    # store start times for sampleVideo
    sampleVideo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    sampleVideo.tStart = globalClock.getTime(format='float')
    sampleVideo.status = STARTED
    thisExp.addData('sampleVideo.started', sampleVideo.tStart)
    sampleVideo.maxDuration = None
    # keep track of which components have finished
    sampleVideoComponents = sampleVideo.components
    for thisComponent in sampleVideo.components:
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
    
    # --- Run Routine "sampleVideo" ---
    sampleVideo.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *samplevideo* updates
        
        # if samplevideo is starting this frame...
        if samplevideo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            samplevideo.frameNStart = frameN  # exact frame index
            samplevideo.tStart = t  # local t and not account for scr refresh
            samplevideo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(samplevideo, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'samplevideo.started')
            # update status
            samplevideo.status = STARTED
            samplevideo.setAutoDraw(True)
            samplevideo.play()
        
        # if samplevideo is stopping this frame...
        if samplevideo.status == STARTED:
            if bool(False) or samplevideo.isFinished:
                # keep track of stop time/frame for later
                samplevideo.tStop = t  # not accounting for scr refresh
                samplevideo.tStopRefresh = tThisFlipGlobal  # on global time
                samplevideo.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'samplevideo.stopped')
                # update status
                samplevideo.status = FINISHED
                samplevideo.setAutoDraw(False)
                samplevideo.stop()
        # *nextbuttonSample* updates
        
        # if nextbuttonSample is starting this frame...
        if nextbuttonSample.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            nextbuttonSample.frameNStart = frameN  # exact frame index
            nextbuttonSample.tStart = t  # local t and not account for scr refresh
            nextbuttonSample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextbuttonSample, 'tStartRefresh')  # time at next scr refresh
            # update status
            nextbuttonSample.status = STARTED
            win.callOnFlip(nextbuttonSample.buttonClock.reset)
            nextbuttonSample.setAutoDraw(True)
        
        # if nextbuttonSample is active this frame...
        if nextbuttonSample.status == STARTED:
            # update params
            pass
            # check whether nextbuttonSample has been pressed
            if nextbuttonSample.isClicked:
                if not nextbuttonSample.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    nextbuttonSample.timesOn.append(nextbuttonSample.buttonClock.getTime())
                    nextbuttonSample.timesOff.append(nextbuttonSample.buttonClock.getTime())
                elif len(nextbuttonSample.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    nextbuttonSample.timesOff[-1] = nextbuttonSample.buttonClock.getTime()
                if not nextbuttonSample.wasClicked:
                    # end routine when nextbuttonSample is clicked
                    continueRoutine = False
                if not nextbuttonSample.wasClicked:
                    # run callback code when nextbuttonSample is clicked
                    pass
        # take note of whether nextbuttonSample was clicked, so that next frame we know if clicks are new
        nextbuttonSample.wasClicked = nextbuttonSample.isClicked and nextbuttonSample.status == STARTED
        # Run 'Each Frame' code from ctlQ
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=sampleVideo,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            sampleVideo.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sampleVideo.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sampleVideo" ---
    for thisComponent in sampleVideo.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for sampleVideo
    sampleVideo.tStop = globalClock.getTime(format='float')
    sampleVideo.tStopRefresh = tThisFlipGlobal
    thisExp.addData('sampleVideo.stopped', sampleVideo.tStop)
    samplevideo.stop()  # ensure movie has stopped at end of Routine
    thisExp.nextEntry()
    # the Routine "sampleVideo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    sampleQuestionsTrials = data.TrialHandler2(
        name='sampleQuestionsTrials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('samplequestions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(sampleQuestionsTrials)  # add the loop to the experiment
    thisSampleQuestionsTrial = sampleQuestionsTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSampleQuestionsTrial.rgb)
    if thisSampleQuestionsTrial != None:
        for paramName in thisSampleQuestionsTrial:
            globals()[paramName] = thisSampleQuestionsTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisSampleQuestionsTrial in sampleQuestionsTrials:
        sampleQuestionsTrials.status = STARTED
        if hasattr(thisSampleQuestionsTrial, 'status'):
            thisSampleQuestionsTrial.status = STARTED
        currentLoop = sampleQuestionsTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisSampleQuestionsTrial.rgb)
        if thisSampleQuestionsTrial != None:
            for paramName in thisSampleQuestionsTrial:
                globals()[paramName] = thisSampleQuestionsTrial[paramName]
        
        # --- Prepare to start Routine "SampleQuestions" ---
        # create an object to store info about Routine SampleQuestions
        SampleQuestions = data.Routine(
            name='SampleQuestions',
            components=[nextSampleQuestion, samplequestionA, sampleBoxA, samplequestionchoiceA, sampleBoxB, samplequestionchoiceB, sampleBoxC, samplequestionchoiceC, sampleBoxD, samplequestionchoiceD, sampleQuestionMouse],
        )
        SampleQuestions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_SampleQuestions
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        # Run 'Begin Routine' code from code_sampleQuestions
        selectedAnswer = None
        mouseWasPressed = False
        sampleBoxA.fillColor = 'white'
        sampleBoxB.fillColor = 'white'
        sampleBoxC.fillColor = 'white'
        sampleBoxD.fillColor = 'white'
        nextSampleQuestion.fillColor = 'white'
        nextSampleQuestion.opacity = 0.4
        # reset nextSampleQuestion to account for continued clicks & clear times on/off
        nextSampleQuestion.reset()
        samplequestionA.reset()
        samplequestionA.setText(question)
        samplequestionchoiceA.reset()
        samplequestionchoiceA.setText(A)
        samplequestionchoiceB.reset()
        samplequestionchoiceB.setText(B)
        samplequestionchoiceC.reset()
        samplequestionchoiceC.setText(C)
        samplequestionchoiceD.reset()
        samplequestionchoiceD.setText(D)
        # setup some python lists for storing info about the sampleQuestionMouse
        sampleQuestionMouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for SampleQuestions
        SampleQuestions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        SampleQuestions.tStart = globalClock.getTime(format='float')
        SampleQuestions.status = STARTED
        thisExp.addData('SampleQuestions.started', SampleQuestions.tStart)
        SampleQuestions.maxDuration = None
        # keep track of which components have finished
        SampleQuestionsComponents = SampleQuestions.components
        for thisComponent in SampleQuestions.components:
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
        
        # --- Run Routine "SampleQuestions" ---
        SampleQuestions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisSampleQuestionsTrial, 'status') and thisSampleQuestionsTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_sampleQuestions
            buttons = sampleQuestionMouse.getPressed()
            mouseDown = buttons[0]
            
            # Respond only once per mouse click
            if mouseDown and not mouseWasPressed:
            
                if sampleQuestionMouse.isPressedIn(sampleBoxA):
                    selectedAnswer = 'A'
            
                elif sampleQuestionMouse.isPressedIn(sampleBoxB):
                    selectedAnswer = 'B'
            
                elif sampleQuestionMouse.isPressedIn(sampleBoxC):
                    selectedAnswer = 'C'
            
                elif sampleQuestionMouse.isPressedIn(sampleBoxD):
                    selectedAnswer = 'D'
            
                # Reset all answer colors
                sampleBoxA.fillColor = 'white'
                sampleBoxB.fillColor = 'white'
                sampleBoxC.fillColor = 'white'
                sampleBoxD.fillColor = 'white'
            
                # Highlight the selected answer
                if selectedAnswer == 'A':
                    sampleBoxA.fillColor = 'lightblue'
                elif selectedAnswer == 'B':
                    sampleBoxB.fillColor = 'lightblue'
                elif selectedAnswer == 'C':
                    sampleBoxC.fillColor = 'lightblue'
                elif selectedAnswer == 'D':
                    sampleBoxD.fillColor = 'lightblue'
                    
                # Proceed only if an answer has been selected
                if sampleQuestionMouse.isPressedIn(nextSampleQuestion):
                    if selectedAnswer is not None:
                        continueRoutine = False
            
            
            mouseWasPressed = mouseDown
            nextSampleQuestion.opacity = 0.4 if selectedAnswer is None else 1.0
            # Run 'Each Frame' code from cq_sampleQuestions
            # Ctrl + Q to quit
            keys = event.getKeys(modifiers=True)
            
            for key, modifiers in keys:
                if key.lower() == 'q' and modifiers.get('ctrl', False):
                    core.quit()
            # *nextSampleQuestion* updates
            
            # if nextSampleQuestion is starting this frame...
            if nextSampleQuestion.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextSampleQuestion.frameNStart = frameN  # exact frame index
                nextSampleQuestion.tStart = t  # local t and not account for scr refresh
                nextSampleQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextSampleQuestion, 'tStartRefresh')  # time at next scr refresh
                # update status
                nextSampleQuestion.status = STARTED
                win.callOnFlip(nextSampleQuestion.buttonClock.reset)
                nextSampleQuestion.setAutoDraw(True)
            
            # if nextSampleQuestion is active this frame...
            if nextSampleQuestion.status == STARTED:
                # update params
                pass
                # check whether nextSampleQuestion has been pressed
                if nextSampleQuestion.isClicked:
                    if not nextSampleQuestion.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextSampleQuestion.timesOn.append(nextSampleQuestion.buttonClock.getTime())
                        nextSampleQuestion.timesOff.append(nextSampleQuestion.buttonClock.getTime())
                    elif len(nextSampleQuestion.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextSampleQuestion.timesOff[-1] = nextSampleQuestion.buttonClock.getTime()
                    if not nextSampleQuestion.wasClicked:
                        # run callback code when nextSampleQuestion is clicked
                        pass
            # take note of whether nextSampleQuestion was clicked, so that next frame we know if clicks are new
            nextSampleQuestion.wasClicked = nextSampleQuestion.isClicked and nextSampleQuestion.status == STARTED
            
            # *samplequestionA* updates
            
            # if samplequestionA is starting this frame...
            if samplequestionA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                samplequestionA.frameNStart = frameN  # exact frame index
                samplequestionA.tStart = t  # local t and not account for scr refresh
                samplequestionA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(samplequestionA, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'samplequestionA.started')
                # update status
                samplequestionA.status = STARTED
                samplequestionA.setAutoDraw(True)
            
            # if samplequestionA is active this frame...
            if samplequestionA.status == STARTED:
                # update params
                pass
            
            # *sampleBoxA* updates
            
            # if sampleBoxA is starting this frame...
            if sampleBoxA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleBoxA.frameNStart = frameN  # exact frame index
                sampleBoxA.tStart = t  # local t and not account for scr refresh
                sampleBoxA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleBoxA, 'tStartRefresh')  # time at next scr refresh
                # update status
                sampleBoxA.status = STARTED
                sampleBoxA.setAutoDraw(True)
            
            # if sampleBoxA is active this frame...
            if sampleBoxA.status == STARTED:
                # update params
                pass
            
            # *samplequestionchoiceA* updates
            
            # if samplequestionchoiceA is starting this frame...
            if samplequestionchoiceA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                samplequestionchoiceA.frameNStart = frameN  # exact frame index
                samplequestionchoiceA.tStart = t  # local t and not account for scr refresh
                samplequestionchoiceA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(samplequestionchoiceA, 'tStartRefresh')  # time at next scr refresh
                # update status
                samplequestionchoiceA.status = STARTED
                samplequestionchoiceA.setAutoDraw(True)
            
            # if samplequestionchoiceA is active this frame...
            if samplequestionchoiceA.status == STARTED:
                # update params
                pass
            
            # *sampleBoxB* updates
            
            # if sampleBoxB is starting this frame...
            if sampleBoxB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleBoxB.frameNStart = frameN  # exact frame index
                sampleBoxB.tStart = t  # local t and not account for scr refresh
                sampleBoxB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleBoxB, 'tStartRefresh')  # time at next scr refresh
                # update status
                sampleBoxB.status = STARTED
                sampleBoxB.setAutoDraw(True)
            
            # if sampleBoxB is active this frame...
            if sampleBoxB.status == STARTED:
                # update params
                pass
            
            # *samplequestionchoiceB* updates
            
            # if samplequestionchoiceB is starting this frame...
            if samplequestionchoiceB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                samplequestionchoiceB.frameNStart = frameN  # exact frame index
                samplequestionchoiceB.tStart = t  # local t and not account for scr refresh
                samplequestionchoiceB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(samplequestionchoiceB, 'tStartRefresh')  # time at next scr refresh
                # update status
                samplequestionchoiceB.status = STARTED
                samplequestionchoiceB.setAutoDraw(True)
            
            # if samplequestionchoiceB is active this frame...
            if samplequestionchoiceB.status == STARTED:
                # update params
                pass
            
            # *sampleBoxC* updates
            
            # if sampleBoxC is starting this frame...
            if sampleBoxC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleBoxC.frameNStart = frameN  # exact frame index
                sampleBoxC.tStart = t  # local t and not account for scr refresh
                sampleBoxC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleBoxC, 'tStartRefresh')  # time at next scr refresh
                # update status
                sampleBoxC.status = STARTED
                sampleBoxC.setAutoDraw(True)
            
            # if sampleBoxC is active this frame...
            if sampleBoxC.status == STARTED:
                # update params
                pass
            
            # *samplequestionchoiceC* updates
            
            # if samplequestionchoiceC is starting this frame...
            if samplequestionchoiceC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                samplequestionchoiceC.frameNStart = frameN  # exact frame index
                samplequestionchoiceC.tStart = t  # local t and not account for scr refresh
                samplequestionchoiceC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(samplequestionchoiceC, 'tStartRefresh')  # time at next scr refresh
                # update status
                samplequestionchoiceC.status = STARTED
                samplequestionchoiceC.setAutoDraw(True)
            
            # if samplequestionchoiceC is active this frame...
            if samplequestionchoiceC.status == STARTED:
                # update params
                pass
            
            # *sampleBoxD* updates
            
            # if sampleBoxD is starting this frame...
            if sampleBoxD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleBoxD.frameNStart = frameN  # exact frame index
                sampleBoxD.tStart = t  # local t and not account for scr refresh
                sampleBoxD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleBoxD, 'tStartRefresh')  # time at next scr refresh
                # update status
                sampleBoxD.status = STARTED
                sampleBoxD.setAutoDraw(True)
            
            # if sampleBoxD is active this frame...
            if sampleBoxD.status == STARTED:
                # update params
                pass
            
            # *samplequestionchoiceD* updates
            
            # if samplequestionchoiceD is starting this frame...
            if samplequestionchoiceD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                samplequestionchoiceD.frameNStart = frameN  # exact frame index
                samplequestionchoiceD.tStart = t  # local t and not account for scr refresh
                samplequestionchoiceD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(samplequestionchoiceD, 'tStartRefresh')  # time at next scr refresh
                # update status
                samplequestionchoiceD.status = STARTED
                samplequestionchoiceD.setAutoDraw(True)
            
            # if samplequestionchoiceD is active this frame...
            if samplequestionchoiceD.status == STARTED:
                # update params
                pass
            # *sampleQuestionMouse* updates
            
            # if sampleQuestionMouse is starting this frame...
            if sampleQuestionMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sampleQuestionMouse.frameNStart = frameN  # exact frame index
                sampleQuestionMouse.tStart = t  # local t and not account for scr refresh
                sampleQuestionMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleQuestionMouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                sampleQuestionMouse.status = STARTED
                sampleQuestionMouse.mouseClock.reset()
                prevButtonState = sampleQuestionMouse.getPressed()  # if button is down already this ISN'T a new click
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=SampleQuestions,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                SampleQuestions.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SampleQuestions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SampleQuestions" ---
        for thisComponent in SampleQuestions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for SampleQuestions
        SampleQuestions.tStop = globalClock.getTime(format='float')
        SampleQuestions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('SampleQuestions.stopped', SampleQuestions.tStop)
        # store data for sampleQuestionsTrials (TrialHandler)
        x, y = sampleQuestionMouse.getPos()
        buttons = sampleQuestionMouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([sampleBoxA, sampleBoxB, sampleBoxC, sampleBoxD], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(sampleQuestionMouse):
                    gotValidClick = True
                    sampleQuestionMouse.clicked_name.append(obj.name)
            if not gotValidClick:
                sampleQuestionMouse.clicked_name.append(None)
        sampleQuestionsTrials.addData('sampleQuestionMouse.x', x)
        sampleQuestionsTrials.addData('sampleQuestionMouse.y', y)
        sampleQuestionsTrials.addData('sampleQuestionMouse.leftButton', buttons[0])
        sampleQuestionsTrials.addData('sampleQuestionMouse.midButton', buttons[1])
        sampleQuestionsTrials.addData('sampleQuestionMouse.rightButton', buttons[2])
        if len(sampleQuestionMouse.clicked_name):
            sampleQuestionsTrials.addData('sampleQuestionMouse.clicked_name', sampleQuestionMouse.clicked_name[0])
        # Run 'End Routine' code from recordSampleQuestion
        if selectedAnswer is None:
            participant_answer = "No answer"
        else:
            participant_answer = selectedAnswer
        
        thisExp.addData("participant_answer", participant_answer)
        thisExp.addData("correct_answer", correct)
        thisExp.addData(
            "is_correct",
            int(participant_answer == correct)
            if participant_answer != "No answer"
            else 0
        )
        # the Routine "SampleQuestions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisSampleQuestionsTrial as finished
        if hasattr(thisSampleQuestionsTrial, 'status'):
            thisSampleQuestionsTrial.status = FINISHED
        # if awaiting a pause, pause now
        if sampleQuestionsTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            sampleQuestionsTrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'sampleQuestionsTrials'
    sampleQuestionsTrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if sampleQuestionsTrials.trialList in ([], [None], None):
        params = []
    else:
        params = sampleQuestionsTrials.trialList[0].keys()
    # save data for this loop
    sampleQuestionsTrials.saveAsExcel(filename + '.xlsx', sheetName='sampleQuestionsTrials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "intstructionforRealVideo" ---
    # create an object to store info about Routine intstructionforRealVideo
    intstructionforRealVideo = data.Routine(
        name='intstructionforRealVideo',
        components=[rv_text, next_rv],
    )
    intstructionforRealVideo.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    rv_text.reset()
    # reset next_rv to account for continued clicks & clear times on/off
    next_rv.reset()
    # Run 'Begin Routine' code from progress_rv
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    # store start times for intstructionforRealVideo
    intstructionforRealVideo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    intstructionforRealVideo.tStart = globalClock.getTime(format='float')
    intstructionforRealVideo.status = STARTED
    thisExp.addData('intstructionforRealVideo.started', intstructionforRealVideo.tStart)
    intstructionforRealVideo.maxDuration = None
    # keep track of which components have finished
    intstructionforRealVideoComponents = intstructionforRealVideo.components
    for thisComponent in intstructionforRealVideo.components:
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
    
    # --- Run Routine "intstructionforRealVideo" ---
    intstructionforRealVideo.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rv_text* updates
        
        # if rv_text is starting this frame...
        if rv_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rv_text.frameNStart = frameN  # exact frame index
            rv_text.tStart = t  # local t and not account for scr refresh
            rv_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rv_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            rv_text.status = STARTED
            rv_text.setAutoDraw(True)
        
        # if rv_text is active this frame...
        if rv_text.status == STARTED:
            # update params
            pass
        # *next_rv* updates
        
        # if next_rv is starting this frame...
        if next_rv.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_rv.frameNStart = frameN  # exact frame index
            next_rv.tStart = t  # local t and not account for scr refresh
            next_rv.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_rv, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_rv.status = STARTED
            win.callOnFlip(next_rv.buttonClock.reset)
            next_rv.setAutoDraw(True)
        
        # if next_rv is active this frame...
        if next_rv.status == STARTED:
            # update params
            pass
            # check whether next_rv has been pressed
            if next_rv.isClicked:
                if not next_rv.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    next_rv.timesOn.append(next_rv.buttonClock.getTime())
                    next_rv.timesOff.append(next_rv.buttonClock.getTime())
                elif len(next_rv.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    next_rv.timesOff[-1] = next_rv.buttonClock.getTime()
                if not next_rv.wasClicked:
                    # end routine when next_rv is clicked
                    continueRoutine = False
                if not next_rv.wasClicked:
                    # run callback code when next_rv is clicked
                    pass
        # take note of whether next_rv was clicked, so that next frame we know if clicks are new
        next_rv.wasClicked = next_rv.isClicked and next_rv.status == STARTED
        # Run 'Each Frame' code from cq_rv
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=intstructionforRealVideo,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            intstructionforRealVideo.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intstructionforRealVideo.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intstructionforRealVideo" ---
    for thisComponent in intstructionforRealVideo.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for intstructionforRealVideo
    intstructionforRealVideo.tStop = globalClock.getTime(format='float')
    intstructionforRealVideo.tStopRefresh = tThisFlipGlobal
    thisExp.addData('intstructionforRealVideo.stopped', intstructionforRealVideo.tStop)
    thisExp.nextEntry()
    # the Routine "intstructionforRealVideo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "videoAssignment" ---
    # create an object to store info about Routine videoAssignment
    videoAssignment = data.Routine(
        name='videoAssignment',
        components=[],
    )
    videoAssignment.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from progress_videoAssignment
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    # store start times for videoAssignment
    videoAssignment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    videoAssignment.tStart = globalClock.getTime(format='float')
    videoAssignment.status = STARTED
    thisExp.addData('videoAssignment.started', videoAssignment.tStart)
    videoAssignment.maxDuration = None
    # keep track of which components have finished
    videoAssignmentComponents = videoAssignment.components
    for thisComponent in videoAssignment.components:
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
    
    # --- Run Routine "videoAssignment" ---
    videoAssignment.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from ctrlQ
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=videoAssignment,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            videoAssignment.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in videoAssignment.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "videoAssignment" ---
    for thisComponent in videoAssignment.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for videoAssignment
    videoAssignment.tStop = globalClock.getTime(format='float')
    videoAssignment.tStopRefresh = tThisFlipGlobal
    thisExp.addData('videoAssignment.stopped', videoAssignment.tStop)
    thisExp.nextEntry()
    # the Routine "videoAssignment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "video" ---
    # create an object to store info about Routine video
    video = data.Routine(
        name='video',
        components=[movie, nextVideo, rq_text_2],
    )
    video.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from progress_video
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    movie.setMovie(video_to_play)
    # reset nextVideo to account for continued clicks & clear times on/off
    nextVideo.reset()
    rq_text_2.reset()
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
        # Run 'Each Frame' code from code_3
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
        
        # *movie* updates
        
        # if movie is starting this frame...
        if movie.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            # update status
            movie.status = STARTED
            movie.setAutoDraw(True)
            movie.play()
        
        # if movie is stopping this frame...
        if movie.status == STARTED:
            if bool(False) or movie.isFinished:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.tStopRefresh = tThisFlipGlobal  # on global time
                movie.frameNStop = frameN  # exact frame index
                # update status
                movie.status = FINISHED
                movie.setAutoDraw(False)
                movie.stop()
        if movie.isFinished:  # force-end the Routine
            continueRoutine = False
        # *nextVideo* updates
        
        # if nextVideo is starting this frame...
        if nextVideo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            nextVideo.frameNStart = frameN  # exact frame index
            nextVideo.tStart = t  # local t and not account for scr refresh
            nextVideo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextVideo, 'tStartRefresh')  # time at next scr refresh
            # update status
            nextVideo.status = STARTED
            win.callOnFlip(nextVideo.buttonClock.reset)
            nextVideo.setAutoDraw(True)
        
        # if nextVideo is active this frame...
        if nextVideo.status == STARTED:
            # update params
            pass
            # check whether nextVideo has been pressed
            if nextVideo.isClicked:
                if not nextVideo.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    nextVideo.timesOn.append(nextVideo.buttonClock.getTime())
                    nextVideo.timesOff.append(nextVideo.buttonClock.getTime())
                elif len(nextVideo.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    nextVideo.timesOff[-1] = nextVideo.buttonClock.getTime()
                if not nextVideo.wasClicked:
                    # end routine when nextVideo is clicked
                    continueRoutine = False
                if not nextVideo.wasClicked:
                    # run callback code when nextVideo is clicked
                    pass
        # take note of whether nextVideo was clicked, so that next frame we know if clicks are new
        nextVideo.wasClicked = nextVideo.isClicked and nextVideo.status == STARTED
        
        # *rq_text_2* updates
        
        # if rq_text_2 is starting this frame...
        if rq_text_2.status == NOT_STARTED and movie.isFinished:
            # keep track of start time/frame for later
            rq_text_2.frameNStart = frameN  # exact frame index
            rq_text_2.tStart = t  # local t and not account for scr refresh
            rq_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rq_text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            rq_text_2.status = STARTED
            rq_text_2.setAutoDraw(True)
        
        # if rq_text_2 is active this frame...
        if rq_text_2.status == STARTED:
            # update params
            pass
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
    movie.stop()  # ensure movie has stopped at end of Routine
    thisExp.nextEntry()
    # the Routine "video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=quizA_reps, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('questionA.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "QuizA" ---
        # create an object to store info about Routine QuizA
        QuizA = data.Routine(
            name='QuizA',
            components=[nextQuizA, questionAText, boxA, choiceA, boxB, choiceB, boxC, choiceC, boxD, choiceD, mouse_2],
        )
        QuizA.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_QuizA
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        # Run 'Begin Routine' code from code_11
        if video_to_play not in [
            "[Original]MultiExecutable_15min.mp4",
            "[Animated]MultiExecutable_15min.mp4"
        ]:
            continueRoutine = False
        
        selectedAnswer = None
        mouseWasPressed = False
        
        boxA.fillColor = 'white'
        boxB.fillColor = 'white'
        boxC.fillColor = 'white'
        boxD.fillColor = 'white'
        
        nextQuizA.fillColor = 'white'
        nextQuizA.opacity = 0.4
        # reset nextQuizA to account for continued clicks & clear times on/off
        nextQuizA.reset()
        questionAText.reset()
        questionAText.setText(question)
        choiceA.reset()
        choiceA.setText(A)
        choiceB.reset()
        choiceB.setText(B)
        choiceC.reset()
        choiceC.setText(C)
        choiceD.reset()
        choiceD.setText(D)
        # setup some python lists for storing info about the mouse_2
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for QuizA
        QuizA.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        QuizA.tStart = globalClock.getTime(format='float')
        QuizA.status = STARTED
        thisExp.addData('QuizA.started', QuizA.tStart)
        QuizA.maxDuration = None
        # keep track of which components have finished
        QuizAComponents = QuizA.components
        for thisComponent in QuizA.components:
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
        
        # --- Run Routine "QuizA" ---
        QuizA.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_11
            buttons = mouse_2.getPressed()
            mouseDown = buttons[0]
            
            # Respond only once per mouse click
            if mouseDown and not mouseWasPressed:
            
                if mouse_2.isPressedIn(boxA):
                    selectedAnswer = 'A'
            
                elif mouse_2.isPressedIn(boxB):
                    selectedAnswer = 'B'
            
                elif mouse_2.isPressedIn(boxC):
                    selectedAnswer = 'C'
            
                elif mouse_2.isPressedIn(boxD):
                    selectedAnswer = 'D'
            
                # Reset all answer colors
                boxA.fillColor = 'white'
                boxB.fillColor = 'white'
                boxC.fillColor = 'white'
                boxD.fillColor = 'white'
            
                # Highlight the selected answer
                if selectedAnswer == 'A':
                    boxA.fillColor = 'lightblue'
                elif selectedAnswer == 'B':
                    boxB.fillColor = 'lightblue'
                elif selectedAnswer == 'C':
                    boxC.fillColor = 'lightblue'
                elif selectedAnswer == 'D':
                    boxD.fillColor = 'lightblue'
                    
                # Proceed only if an answer has been selected
                if mouse_2.isPressedIn(nextQuizA):
                    if selectedAnswer is not None:
                        continueRoutine = False
            
            
            mouseWasPressed = mouseDown
            nextQuizA.opacity = 0.4 if selectedAnswer is None else 1.0
            # Run 'Each Frame' code from cq
            # Ctrl + Q to quit
            keys = event.getKeys(modifiers=True)
            
            for key, modifiers in keys:
                if key.lower() == 'q' and modifiers.get('ctrl', False):
                    core.quit()
            # *nextQuizA* updates
            
            # if nextQuizA is starting this frame...
            if nextQuizA.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextQuizA.frameNStart = frameN  # exact frame index
                nextQuizA.tStart = t  # local t and not account for scr refresh
                nextQuizA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextQuizA, 'tStartRefresh')  # time at next scr refresh
                # update status
                nextQuizA.status = STARTED
                win.callOnFlip(nextQuizA.buttonClock.reset)
                nextQuizA.setAutoDraw(True)
            
            # if nextQuizA is active this frame...
            if nextQuizA.status == STARTED:
                # update params
                pass
                # check whether nextQuizA has been pressed
                if nextQuizA.isClicked:
                    if not nextQuizA.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextQuizA.timesOn.append(nextQuizA.buttonClock.getTime())
                        nextQuizA.timesOff.append(nextQuizA.buttonClock.getTime())
                    elif len(nextQuizA.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextQuizA.timesOff[-1] = nextQuizA.buttonClock.getTime()
                    if not nextQuizA.wasClicked:
                        # run callback code when nextQuizA is clicked
                        pass
            # take note of whether nextQuizA was clicked, so that next frame we know if clicks are new
            nextQuizA.wasClicked = nextQuizA.isClicked and nextQuizA.status == STARTED
            
            # *questionAText* updates
            
            # if questionAText is starting this frame...
            if questionAText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionAText.frameNStart = frameN  # exact frame index
                questionAText.tStart = t  # local t and not account for scr refresh
                questionAText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionAText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'questionAText.started')
                # update status
                questionAText.status = STARTED
                questionAText.setAutoDraw(True)
            
            # if questionAText is active this frame...
            if questionAText.status == STARTED:
                # update params
                pass
            
            # *boxA* updates
            
            # if boxA is starting this frame...
            if boxA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxA.frameNStart = frameN  # exact frame index
                boxA.tStart = t  # local t and not account for scr refresh
                boxA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxA, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxA.status = STARTED
                boxA.setAutoDraw(True)
            
            # if boxA is active this frame...
            if boxA.status == STARTED:
                # update params
                pass
            
            # *choiceA* updates
            
            # if choiceA is starting this frame...
            if choiceA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceA.frameNStart = frameN  # exact frame index
                choiceA.tStart = t  # local t and not account for scr refresh
                choiceA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceA, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceA.status = STARTED
                choiceA.setAutoDraw(True)
            
            # if choiceA is active this frame...
            if choiceA.status == STARTED:
                # update params
                pass
            
            # *boxB* updates
            
            # if boxB is starting this frame...
            if boxB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxB.frameNStart = frameN  # exact frame index
                boxB.tStart = t  # local t and not account for scr refresh
                boxB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxB, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxB.status = STARTED
                boxB.setAutoDraw(True)
            
            # if boxB is active this frame...
            if boxB.status == STARTED:
                # update params
                pass
            
            # *choiceB* updates
            
            # if choiceB is starting this frame...
            if choiceB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceB.frameNStart = frameN  # exact frame index
                choiceB.tStart = t  # local t and not account for scr refresh
                choiceB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceB, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceB.status = STARTED
                choiceB.setAutoDraw(True)
            
            # if choiceB is active this frame...
            if choiceB.status == STARTED:
                # update params
                pass
            
            # *boxC* updates
            
            # if boxC is starting this frame...
            if boxC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxC.frameNStart = frameN  # exact frame index
                boxC.tStart = t  # local t and not account for scr refresh
                boxC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxC, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxC.status = STARTED
                boxC.setAutoDraw(True)
            
            # if boxC is active this frame...
            if boxC.status == STARTED:
                # update params
                pass
            
            # *choiceC* updates
            
            # if choiceC is starting this frame...
            if choiceC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceC.frameNStart = frameN  # exact frame index
                choiceC.tStart = t  # local t and not account for scr refresh
                choiceC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceC, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceC.status = STARTED
                choiceC.setAutoDraw(True)
            
            # if choiceC is active this frame...
            if choiceC.status == STARTED:
                # update params
                pass
            
            # *boxD* updates
            
            # if boxD is starting this frame...
            if boxD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxD.frameNStart = frameN  # exact frame index
                boxD.tStart = t  # local t and not account for scr refresh
                boxD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxD, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxD.status = STARTED
                boxD.setAutoDraw(True)
            
            # if boxD is active this frame...
            if boxD.status == STARTED:
                # update params
                pass
            
            # *choiceD* updates
            
            # if choiceD is starting this frame...
            if choiceD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceD.frameNStart = frameN  # exact frame index
                choiceD.tStart = t  # local t and not account for scr refresh
                choiceD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceD, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceD.status = STARTED
                choiceD.setAutoDraw(True)
            
            # if choiceD is active this frame...
            if choiceD.status == STARTED:
                # update params
                pass
            # *mouse_2* updates
            
            # if mouse_2 is starting this frame...
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=QuizA,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                QuizA.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuizA.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "QuizA" ---
        for thisComponent in QuizA.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for QuizA
        QuizA.tStop = globalClock.getTime(format='float')
        QuizA.tStopRefresh = tThisFlipGlobal
        thisExp.addData('QuizA.stopped', QuizA.tStop)
        # store data for trials (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([boxA, boxB, boxC, boxD], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_2):
                    gotValidClick = True
                    mouse_2.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_2.clicked_name.append(None)
        trials.addData('mouse_2.x', x)
        trials.addData('mouse_2.y', y)
        trials.addData('mouse_2.leftButton', buttons[0])
        trials.addData('mouse_2.midButton', buttons[1])
        trials.addData('mouse_2.rightButton', buttons[2])
        if len(mouse_2.clicked_name):
            trials.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
        # Run 'End Routine' code from record
        if selectedAnswer is None:
            participant_answer = "No answer"
        else:
            participant_answer = selectedAnswer
        
        thisExp.addData("participant_answer", participant_answer)
        thisExp.addData("correct_answer", correct)
        thisExp.addData(
            "is_correct",
            int(participant_answer == correct)
            if participant_answer != "No answer"
            else 0
        )
        # the Routine "QuizA" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed quizA_reps repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler2(
        name='trials_2',
        nReps=quizB_reps, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('questionB.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_2 in trials_2:
        trials_2.status = STARTED
        if hasattr(thisTrial_2, 'status'):
            thisTrial_2.status = STARTED
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "QuizB" ---
        # create an object to store info about Routine QuizB
        QuizB = data.Routine(
            name='QuizB',
            components=[nextQuizB, questionBText, boxA_2, choiceA_2, boxB_2, choiceB_2, boxC_2, choiceC_2, boxD_2, choiceD_2, mouse_3],
        )
        QuizB.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_QuizB
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        # Run 'Begin Routine' code from code_12
        if video_to_play not in [
            "Possessed_cat.mp4",
            "Jack_jet.mp4"
        ]:
            continueRoutine = False
            
        selectedAnswer = None
        mouseWasPressed = False
        
        boxA_2.fillColor = 'white'
        boxB_2.fillColor = 'white'
        boxC_2.fillColor = 'white'
        boxD_2.fillColor = 'white'
        
        nextQuizB.fillColor = 'white'
        nextQuizB.opacity = 0.4
        # reset nextQuizB to account for continued clicks & clear times on/off
        nextQuizB.reset()
        questionBText.reset()
        questionBText.setText(question)
        choiceA_2.reset()
        choiceA_2.setText(A)
        choiceB_2.reset()
        choiceB_2.setText(B)
        choiceC_2.reset()
        choiceC_2.setText(C)
        choiceD_2.reset()
        choiceD_2.setText(D)
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for QuizB
        QuizB.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        QuizB.tStart = globalClock.getTime(format='float')
        QuizB.status = STARTED
        thisExp.addData('QuizB.started', QuizB.tStart)
        QuizB.maxDuration = None
        # keep track of which components have finished
        QuizBComponents = QuizB.components
        for thisComponent in QuizB.components:
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
        
        # --- Run Routine "QuizB" ---
        QuizB.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_12
            buttons = mouse_3.getPressed()
            mouseDown = buttons[0]
            
            # Respond only once per mouse click
            if mouseDown and not mouseWasPressed:
            
                if mouse_3.isPressedIn(boxA_2):
                    selectedAnswer = 'A'
            
                elif mouse_3.isPressedIn(boxB_2):
                    selectedAnswer = 'B'
            
                elif mouse_3.isPressedIn(boxC_2):
                    selectedAnswer = 'C'
            
                elif mouse_3.isPressedIn(boxD_2):
                    selectedAnswer = 'D'
            
                # Reset all answer colors
                boxA_2.fillColor = 'white'
                boxB_2.fillColor = 'white'
                boxC_2.fillColor = 'white'
                boxD_2.fillColor = 'white'
            
                # Highlight the selected answer
                if selectedAnswer == 'A':
                    boxA_2.fillColor = 'lightblue'
                elif selectedAnswer == 'B':
                    boxB_2.fillColor = 'lightblue'
                elif selectedAnswer == 'C':
                    boxC_2.fillColor = 'lightblue'
                elif selectedAnswer == 'D':
                    boxD_2.fillColor = 'lightblue'
            
                # Proceed only if an answer has been selected
                if mouse_3.isPressedIn(nextQuizB):
                    if selectedAnswer is not None:
                        continueRoutine = False
            
            mouseWasPressed = mouseDown
            nextQuizB.opacity = 0.4 if selectedAnswer is None else 1.0
            # Run 'Each Frame' code from cq_2
            # Ctrl + Q to quit
            keys = event.getKeys(modifiers=True)
            
            for key, modifiers in keys:
                if key.lower() == 'q' and modifiers.get('ctrl', False):
                    core.quit()
            # *nextQuizB* updates
            
            # if nextQuizB is starting this frame...
            if nextQuizB.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextQuizB.frameNStart = frameN  # exact frame index
                nextQuizB.tStart = t  # local t and not account for scr refresh
                nextQuizB.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextQuizB, 'tStartRefresh')  # time at next scr refresh
                # update status
                nextQuizB.status = STARTED
                win.callOnFlip(nextQuizB.buttonClock.reset)
                nextQuizB.setAutoDraw(True)
            
            # if nextQuizB is active this frame...
            if nextQuizB.status == STARTED:
                # update params
                pass
                # check whether nextQuizB has been pressed
                if nextQuizB.isClicked:
                    if not nextQuizB.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextQuizB.timesOn.append(nextQuizB.buttonClock.getTime())
                        nextQuizB.timesOff.append(nextQuizB.buttonClock.getTime())
                    elif len(nextQuizB.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextQuizB.timesOff[-1] = nextQuizB.buttonClock.getTime()
                    if not nextQuizB.wasClicked:
                        # run callback code when nextQuizB is clicked
                        pass
            # take note of whether nextQuizB was clicked, so that next frame we know if clicks are new
            nextQuizB.wasClicked = nextQuizB.isClicked and nextQuizB.status == STARTED
            
            # *questionBText* updates
            
            # if questionBText is starting this frame...
            if questionBText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionBText.frameNStart = frameN  # exact frame index
                questionBText.tStart = t  # local t and not account for scr refresh
                questionBText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionBText, 'tStartRefresh')  # time at next scr refresh
                # update status
                questionBText.status = STARTED
                questionBText.setAutoDraw(True)
            
            # if questionBText is active this frame...
            if questionBText.status == STARTED:
                # update params
                pass
            
            # *boxA_2* updates
            
            # if boxA_2 is starting this frame...
            if boxA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxA_2.frameNStart = frameN  # exact frame index
                boxA_2.tStart = t  # local t and not account for scr refresh
                boxA_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxA_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxA_2.status = STARTED
                boxA_2.setAutoDraw(True)
            
            # if boxA_2 is active this frame...
            if boxA_2.status == STARTED:
                # update params
                pass
            
            # *choiceA_2* updates
            
            # if choiceA_2 is starting this frame...
            if choiceA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceA_2.frameNStart = frameN  # exact frame index
                choiceA_2.tStart = t  # local t and not account for scr refresh
                choiceA_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceA_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceA_2.status = STARTED
                choiceA_2.setAutoDraw(True)
            
            # if choiceA_2 is active this frame...
            if choiceA_2.status == STARTED:
                # update params
                pass
            
            # *boxB_2* updates
            
            # if boxB_2 is starting this frame...
            if boxB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxB_2.frameNStart = frameN  # exact frame index
                boxB_2.tStart = t  # local t and not account for scr refresh
                boxB_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxB_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxB_2.status = STARTED
                boxB_2.setAutoDraw(True)
            
            # if boxB_2 is active this frame...
            if boxB_2.status == STARTED:
                # update params
                pass
            
            # *choiceB_2* updates
            
            # if choiceB_2 is starting this frame...
            if choiceB_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceB_2.frameNStart = frameN  # exact frame index
                choiceB_2.tStart = t  # local t and not account for scr refresh
                choiceB_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceB_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceB_2.status = STARTED
                choiceB_2.setAutoDraw(True)
            
            # if choiceB_2 is active this frame...
            if choiceB_2.status == STARTED:
                # update params
                pass
            
            # *boxC_2* updates
            
            # if boxC_2 is starting this frame...
            if boxC_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxC_2.frameNStart = frameN  # exact frame index
                boxC_2.tStart = t  # local t and not account for scr refresh
                boxC_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxC_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxC_2.status = STARTED
                boxC_2.setAutoDraw(True)
            
            # if boxC_2 is active this frame...
            if boxC_2.status == STARTED:
                # update params
                pass
            
            # *choiceC_2* updates
            
            # if choiceC_2 is starting this frame...
            if choiceC_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceC_2.frameNStart = frameN  # exact frame index
                choiceC_2.tStart = t  # local t and not account for scr refresh
                choiceC_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceC_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceC_2.status = STARTED
                choiceC_2.setAutoDraw(True)
            
            # if choiceC_2 is active this frame...
            if choiceC_2.status == STARTED:
                # update params
                pass
            
            # *boxD_2* updates
            
            # if boxD_2 is starting this frame...
            if boxD_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxD_2.frameNStart = frameN  # exact frame index
                boxD_2.tStart = t  # local t and not account for scr refresh
                boxD_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxD_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxD_2.status = STARTED
                boxD_2.setAutoDraw(True)
            
            # if boxD_2 is active this frame...
            if boxD_2.status == STARTED:
                # update params
                pass
            
            # *choiceD_2* updates
            
            # if choiceD_2 is starting this frame...
            if choiceD_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceD_2.frameNStart = frameN  # exact frame index
                choiceD_2.tStart = t  # local t and not account for scr refresh
                choiceD_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceD_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceD_2.status = STARTED
                choiceD_2.setAutoDraw(True)
            
            # if choiceD_2 is active this frame...
            if choiceD_2.status == STARTED:
                # update params
                pass
            # *mouse_3* updates
            
            # if mouse_3 is starting this frame...
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=QuizB,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                QuizB.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuizB.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "QuizB" ---
        for thisComponent in QuizB.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for QuizB
        QuizB.tStop = globalClock.getTime(format='float')
        QuizB.tStopRefresh = tThisFlipGlobal
        thisExp.addData('QuizB.stopped', QuizB.tStop)
        # store data for trials_2 (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([boxA_2,boxB_2, boxC_2, boxD_2], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_3.clicked_name.append(None)
        trials_2.addData('mouse_3.x', x)
        trials_2.addData('mouse_3.y', y)
        trials_2.addData('mouse_3.leftButton', buttons[0])
        trials_2.addData('mouse_3.midButton', buttons[1])
        trials_2.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            trials_2.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        # Run 'End Routine' code from recordB
        if selectedAnswer is None:
            participant_answer = "No answer"
        else:
            participant_answer = selectedAnswer
        
        thisExp.addData("participant_answer", participant_answer)
        thisExp.addData("correct_answer", correct)
        thisExp.addData(
            "is_correct",
            int(participant_answer == correct)
            if participant_answer != "No answer"
            else 0
        )
        # the Routine "QuizB" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial_2 as finished
        if hasattr(thisTrial_2, 'status'):
            thisTrial_2.status = FINISHED
        # if awaiting a pause, pause now
        if trials_2.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_2.status = STARTED
        thisExp.nextEntry()
        
    # completed quizB_reps repeats of 'trials_2'
    trials_2.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler2(
        name='trials_3',
        nReps=quizC_reps, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('questionC.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_3 in trials_3:
        trials_3.status = STARTED
        if hasattr(thisTrial_3, 'status'):
            thisTrial_3.status = STARTED
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "QuizC" ---
        # create an object to store info about Routine QuizC
        QuizC = data.Routine(
            name='QuizC',
            components=[nextQuizC, questionCText, boxA_3, choiceA_3, boxB_3, choiceB_3, boxC_3, choiceC_3, boxD_3, choiceD_3, mouse_4],
        )
        QuizC.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_QuizC
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        # Run 'Begin Routine' code from code_13
        if video_to_play not in [
            "Creepy and scary cat.mp4",
            "cattransition.mp4"
        ]:
            continueRoutine = False
            
        selectedAnswer = None
        mouseWasPressed = False
        
        boxA_3.fillColor = 'white'
        boxB_3.fillColor = 'white'
        boxC_3.fillColor = 'white'
        boxD_3.fillColor = 'white'
        
        nextQuizC.fillColor = 'white'
        nextQuizC.opacity = 0.4
        # reset nextQuizC to account for continued clicks & clear times on/off
        nextQuizC.reset()
        questionCText.reset()
        questionCText.setText(question)
        choiceA_3.reset()
        choiceA_3.setText(A)
        choiceB_3.reset()
        choiceB_3.setText(B)
        choiceC_3.reset()
        choiceC_3.setText(C)
        choiceD_3.reset()
        choiceD_3.setText(D)
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for QuizC
        QuizC.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        QuizC.tStart = globalClock.getTime(format='float')
        QuizC.status = STARTED
        thisExp.addData('QuizC.started', QuizC.tStart)
        QuizC.maxDuration = None
        # keep track of which components have finished
        QuizCComponents = QuizC.components
        for thisComponent in QuizC.components:
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
        
        # --- Run Routine "QuizC" ---
        QuizC.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_13
            buttons = mouse_4.getPressed()
            mouseDown = buttons[0]
            
            # Respond only once per mouse click
            if mouseDown and not mouseWasPressed:
            
                if mouse_4.isPressedIn(boxA_3):
                    selectedAnswer = 'A'
            
                elif mouse_4.isPressedIn(boxB_3):
                    selectedAnswer = 'B'
            
                elif mouse_4.isPressedIn(boxC_3):
                    selectedAnswer = 'C'
            
                elif mouse_4.isPressedIn(boxD_3):
                    selectedAnswer = 'D'
            
                # Reset all answer colors
                boxA_3.fillColor = 'white'
                boxB_3.fillColor = 'white'
                boxC_3.fillColor = 'white'
                boxD_3.fillColor = 'white'
            
                # Highlight the selected answer
                if selectedAnswer == 'A':
                    boxA_3.fillColor = 'lightblue'
                elif selectedAnswer == 'B':
                    boxB_3.fillColor = 'lightblue'
                elif selectedAnswer == 'C':
                    boxC_3.fillColor = 'lightblue'
                elif selectedAnswer == 'D':
                    boxD_3.fillColor = 'lightblue'
            
                # Proceed only if an answer has been selected
                if mouse_4.isPressedIn(nextQuizC):
                    if selectedAnswer is not None:
                        continueRoutine = False
            
            mouseWasPressed = mouseDown
            nextQuizC.opacity = 0.4 if selectedAnswer is None else 1.0
            # Run 'Each Frame' code from cq_3
            # Ctrl + Q to quit
            keys = event.getKeys(modifiers=True)
            
            for key, modifiers in keys:
                if key.lower() == 'q' and modifiers.get('ctrl', False):
                    core.quit()
            # *nextQuizC* updates
            
            # if nextQuizC is starting this frame...
            if nextQuizC.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextQuizC.frameNStart = frameN  # exact frame index
                nextQuizC.tStart = t  # local t and not account for scr refresh
                nextQuizC.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextQuizC, 'tStartRefresh')  # time at next scr refresh
                # update status
                nextQuizC.status = STARTED
                win.callOnFlip(nextQuizC.buttonClock.reset)
                nextQuizC.setAutoDraw(True)
            
            # if nextQuizC is active this frame...
            if nextQuizC.status == STARTED:
                # update params
                pass
                # check whether nextQuizC has been pressed
                if nextQuizC.isClicked:
                    if not nextQuizC.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextQuizC.timesOn.append(nextQuizC.buttonClock.getTime())
                        nextQuizC.timesOff.append(nextQuizC.buttonClock.getTime())
                    elif len(nextQuizC.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextQuizC.timesOff[-1] = nextQuizC.buttonClock.getTime()
                    if not nextQuizC.wasClicked:
                        # run callback code when nextQuizC is clicked
                        pass
            # take note of whether nextQuizC was clicked, so that next frame we know if clicks are new
            nextQuizC.wasClicked = nextQuizC.isClicked and nextQuizC.status == STARTED
            
            # *questionCText* updates
            
            # if questionCText is starting this frame...
            if questionCText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionCText.frameNStart = frameN  # exact frame index
                questionCText.tStart = t  # local t and not account for scr refresh
                questionCText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionCText, 'tStartRefresh')  # time at next scr refresh
                # update status
                questionCText.status = STARTED
                questionCText.setAutoDraw(True)
            
            # if questionCText is active this frame...
            if questionCText.status == STARTED:
                # update params
                pass
            
            # *boxA_3* updates
            
            # if boxA_3 is starting this frame...
            if boxA_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxA_3.frameNStart = frameN  # exact frame index
                boxA_3.tStart = t  # local t and not account for scr refresh
                boxA_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxA_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxA_3.status = STARTED
                boxA_3.setAutoDraw(True)
            
            # if boxA_3 is active this frame...
            if boxA_3.status == STARTED:
                # update params
                pass
            
            # *choiceA_3* updates
            
            # if choiceA_3 is starting this frame...
            if choiceA_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceA_3.frameNStart = frameN  # exact frame index
                choiceA_3.tStart = t  # local t and not account for scr refresh
                choiceA_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceA_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceA_3.status = STARTED
                choiceA_3.setAutoDraw(True)
            
            # if choiceA_3 is active this frame...
            if choiceA_3.status == STARTED:
                # update params
                pass
            
            # *boxB_3* updates
            
            # if boxB_3 is starting this frame...
            if boxB_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxB_3.frameNStart = frameN  # exact frame index
                boxB_3.tStart = t  # local t and not account for scr refresh
                boxB_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxB_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxB_3.status = STARTED
                boxB_3.setAutoDraw(True)
            
            # if boxB_3 is active this frame...
            if boxB_3.status == STARTED:
                # update params
                pass
            
            # *choiceB_3* updates
            
            # if choiceB_3 is starting this frame...
            if choiceB_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceB_3.frameNStart = frameN  # exact frame index
                choiceB_3.tStart = t  # local t and not account for scr refresh
                choiceB_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceB_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceB_3.status = STARTED
                choiceB_3.setAutoDraw(True)
            
            # if choiceB_3 is active this frame...
            if choiceB_3.status == STARTED:
                # update params
                pass
            
            # *boxC_3* updates
            
            # if boxC_3 is starting this frame...
            if boxC_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxC_3.frameNStart = frameN  # exact frame index
                boxC_3.tStart = t  # local t and not account for scr refresh
                boxC_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxC_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxC_3.status = STARTED
                boxC_3.setAutoDraw(True)
            
            # if boxC_3 is active this frame...
            if boxC_3.status == STARTED:
                # update params
                pass
            
            # *choiceC_3* updates
            
            # if choiceC_3 is starting this frame...
            if choiceC_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceC_3.frameNStart = frameN  # exact frame index
                choiceC_3.tStart = t  # local t and not account for scr refresh
                choiceC_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceC_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceC_3.status = STARTED
                choiceC_3.setAutoDraw(True)
            
            # if choiceC_3 is active this frame...
            if choiceC_3.status == STARTED:
                # update params
                pass
            
            # *boxD_3* updates
            
            # if boxD_3 is starting this frame...
            if boxD_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                boxD_3.frameNStart = frameN  # exact frame index
                boxD_3.tStart = t  # local t and not account for scr refresh
                boxD_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(boxD_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                boxD_3.status = STARTED
                boxD_3.setAutoDraw(True)
            
            # if boxD_3 is active this frame...
            if boxD_3.status == STARTED:
                # update params
                pass
            
            # *choiceD_3* updates
            
            # if choiceD_3 is starting this frame...
            if choiceD_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceD_3.frameNStart = frameN  # exact frame index
                choiceD_3.tStart = t  # local t and not account for scr refresh
                choiceD_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceD_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceD_3.status = STARTED
                choiceD_3.setAutoDraw(True)
            
            # if choiceD_3 is active this frame...
            if choiceD_3.status == STARTED:
                # update params
                pass
            # *mouse_4* updates
            
            # if mouse_4 is starting this frame...
            if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_4.frameNStart = frameN  # exact frame index
                mouse_4.tStart = t  # local t and not account for scr refresh
                mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_4.status = STARTED
                mouse_4.mouseClock.reset()
                prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=QuizC,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                QuizC.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuizC.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "QuizC" ---
        for thisComponent in QuizC.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for QuizC
        QuizC.tStop = globalClock.getTime(format='float')
        QuizC.tStopRefresh = tThisFlipGlobal
        thisExp.addData('QuizC.stopped', QuizC.tStop)
        # store data for trials_3 (TrialHandler)
        x, y = mouse_4.getPos()
        buttons = mouse_4.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([boxA_3, boxB_3, boxC_3, boxD_3], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_4):
                    gotValidClick = True
                    mouse_4.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_4.clicked_name.append(None)
        trials_3.addData('mouse_4.x', x)
        trials_3.addData('mouse_4.y', y)
        trials_3.addData('mouse_4.leftButton', buttons[0])
        trials_3.addData('mouse_4.midButton', buttons[1])
        trials_3.addData('mouse_4.rightButton', buttons[2])
        if len(mouse_4.clicked_name):
            trials_3.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
        # Run 'End Routine' code from recordC
        if selectedAnswer is None:
            participant_answer = "No answer"
        else:
            participant_answer = selectedAnswer
        
        thisExp.addData("participant_answer", participant_answer)
        thisExp.addData("correct_answer", correct)
        thisExp.addData(
            "is_correct",
            int(participant_answer == correct)
            if participant_answer != "No answer"
            else 0
        )
        # the Routine "QuizC" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial_3 as finished
        if hasattr(thisTrial_3, 'status'):
            thisTrial_3.status = FINISHED
        # if awaiting a pause, pause now
        if trials_3.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_3.status = STARTED
        thisExp.nextEntry()
        
    # completed quizC_reps repeats of 'trials_3'
    trials_3.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_3.trialList[0].keys()
    # save data for this loop
    trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "instructionLikert" ---
    # create an object to store info about Routine instructionLikert
    instructionLikert = data.Routine(
        name='instructionLikert',
        components=[lr_text, next_lr],
    )
    instructionLikert.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    lr_text.reset()
    # reset next_lr to account for continued clicks & clear times on/off
    next_lr.reset()
    # Run 'Begin Routine' code from progress_lr
    progressStep = min(progressStep + 1, progressTotal)
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
    # store start times for instructionLikert
    instructionLikert.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructionLikert.tStart = globalClock.getTime(format='float')
    instructionLikert.status = STARTED
    thisExp.addData('instructionLikert.started', instructionLikert.tStart)
    instructionLikert.maxDuration = None
    # keep track of which components have finished
    instructionLikertComponents = instructionLikert.components
    for thisComponent in instructionLikert.components:
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
    
    # --- Run Routine "instructionLikert" ---
    instructionLikert.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lr_text* updates
        
        # if lr_text is starting this frame...
        if lr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lr_text.frameNStart = frameN  # exact frame index
            lr_text.tStart = t  # local t and not account for scr refresh
            lr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lr_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            lr_text.status = STARTED
            lr_text.setAutoDraw(True)
        
        # if lr_text is active this frame...
        if lr_text.status == STARTED:
            # update params
            pass
        # *next_lr* updates
        
        # if next_lr is starting this frame...
        if next_lr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_lr.frameNStart = frameN  # exact frame index
            next_lr.tStart = t  # local t and not account for scr refresh
            next_lr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_lr, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_lr.status = STARTED
            win.callOnFlip(next_lr.buttonClock.reset)
            next_lr.setAutoDraw(True)
        
        # if next_lr is active this frame...
        if next_lr.status == STARTED:
            # update params
            pass
            # check whether next_lr has been pressed
            if next_lr.isClicked:
                if not next_lr.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    next_lr.timesOn.append(next_lr.buttonClock.getTime())
                    next_lr.timesOff.append(next_lr.buttonClock.getTime())
                elif len(next_lr.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    next_lr.timesOff[-1] = next_lr.buttonClock.getTime()
                if not next_lr.wasClicked:
                    # end routine when next_lr is clicked
                    continueRoutine = False
                if not next_lr.wasClicked:
                    # run callback code when next_lr is clicked
                    pass
        # take note of whether next_lr was clicked, so that next frame we know if clicks are new
        next_lr.wasClicked = next_lr.isClicked and next_lr.status == STARTED
        # Run 'Each Frame' code from cq_lr
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructionLikert,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructionLikert.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionLikert.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructionLikert" ---
    for thisComponent in instructionLikert.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructionLikert
    instructionLikert.tStop = globalClock.getTime(format='float')
    instructionLikert.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructionLikert.stopped', instructionLikert.tStop)
    thisExp.nextEntry()
    # the Routine "instructionLikert" was not non-slip safe, so reset the non-slip timer
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
            components=[likertText, likert_slider, nextButton, instruction_slider],
        )
        likert.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_likert
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        likertText.setText(itemText)
        likert_slider.reset()
        # reset nextButton to account for continued clicks & clear times on/off
        nextButton.reset()
        # Run 'Begin Routine' code from code_7
        nextButton.opacity = 0.4
        instruction_slider.reset()
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
            # Run 'Each Frame' code from code_7
            nextButton.opacity = 0.4 if likert_slider.getRT() is None else 1.0
            if nextButton.isClicked and likert_slider.getRT() is None:
                continueRoutine = True
            
            # *instruction_slider* updates
            
            # if instruction_slider is starting this frame...
            if instruction_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instruction_slider.frameNStart = frameN  # exact frame index
                instruction_slider.tStart = t  # local t and not account for scr refresh
                instruction_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_slider.started')
                # update status
                instruction_slider.status = STARTED
                instruction_slider.setAutoDraw(True)
            
            # if instruction_slider is active this frame...
            if instruction_slider.status == STARTED:
                # update params
                pass
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
    # get names of stimulus parameters
    if likertLoop.trialList in ([], [None], None):
        params = []
    else:
        params = likertLoop.trialList[0].keys()
    # save data for this loop
    likertLoop.saveAsExcel(filename + '.xlsx', sheetName='likertLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler2(
        name='trials_4',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('DQ.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            globals()[paramName] = thisTrial_4[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_4 in trials_4:
        trials_4.status = STARTED
        if hasattr(thisTrial_4, 'status'):
            thisTrial_4.status = STARTED
        currentLoop = trials_4
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        # --- Prepare to start Routine "demographicQuiz" ---
        # create an object to store info about Routine demographicQuiz
        demographicQuiz = data.Routine(
            name='demographicQuiz',
            components=[nextDemo, questionDemo, box1, choiceA_demo, box2, choiceB_demo, box3, choiceC_demo, box4, choiceD_demo, mouse_5],
        )
        demographicQuiz.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from progress_demographicQuiz
        progressStep = min(progressStep + 1, progressTotal)
        progressWidth = 1.8 * progressStep / progressTotal
        progressBar.setSize((progressWidth, 0.025))
        progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
        # Run 'Begin Routine' code from code_14
        selectedAnswer = None
        mouseWasPressed = False
        
        box1.fillColor = 'white'
        box2.fillColor = 'white'
        box3.fillColor = 'white'
        box4.fillColor = 'white'
        
        nextDemo.fillColor = 'white'
        nextDemo.opacity = 0.4
        # reset nextDemo to account for continued clicks & clear times on/off
        nextDemo.reset()
        questionDemo.reset()
        questionDemo.setText(question)
        choiceA_demo.reset()
        choiceA_demo.setText(A)
        choiceB_demo.reset()
        choiceB_demo.setText(B)
        choiceC_demo.reset()
        choiceC_demo.setText(C)
        choiceD_demo.reset()
        choiceD_demo.setText(D)
        # setup some python lists for storing info about the mouse_5
        mouse_5.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for demographicQuiz
        demographicQuiz.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        demographicQuiz.tStart = globalClock.getTime(format='float')
        demographicQuiz.status = STARTED
        thisExp.addData('demographicQuiz.started', demographicQuiz.tStart)
        demographicQuiz.maxDuration = None
        # keep track of which components have finished
        demographicQuizComponents = demographicQuiz.components
        for thisComponent in demographicQuiz.components:
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
        
        # --- Run Routine "demographicQuiz" ---
        demographicQuiz.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_4, 'status') and thisTrial_4.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_14
            buttons = mouse_5.getPressed()
            mouseDown = buttons[0]
            
            # Respond only once per mouse click
            if mouseDown and not mouseWasPressed:
            
                if mouse_5.isPressedIn(box1):
                    selectedAnswer = 'A'
            
                elif mouse_5.isPressedIn(box2):
                    selectedAnswer = 'B'
            
                elif mouse_5.isPressedIn(box3):
                    selectedAnswer = 'C'
            
                elif mouse_5.isPressedIn(box4):
                    selectedAnswer = 'D'
            
                # Reset all answer colors
                box1.fillColor = 'white'
                box2.fillColor = 'white'
                box3.fillColor = 'white'
                box4.fillColor = 'white'
            
                # Highlight the selected answer
                if selectedAnswer == 'A':
                    box1.fillColor = 'lightblue'
                elif selectedAnswer == 'B':
                    box2.fillColor = 'lightblue'
                elif selectedAnswer == 'C':
                    box3.fillColor = 'lightblue'
                elif selectedAnswer == 'D':
                    box4.fillColor = 'lightblue'
                    
                # Proceed only if an answer has been selected
                if mouse_5.isPressedIn(nextDemo):
                    if selectedAnswer is not None:
                        continueRoutine = False
            
            
            mouseWasPressed = mouseDown
            nextDemo.opacity = 0.4 if selectedAnswer is None else 1.0
            # Run 'Each Frame' code from cq5
            # Ctrl + Q to quit
            keys = event.getKeys(modifiers=True)
            
            for key, modifiers in keys:
                if key.lower() == 'q' and modifiers.get('ctrl', False):
                    core.quit()
            # *nextDemo* updates
            
            # if nextDemo is starting this frame...
            if nextDemo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                nextDemo.frameNStart = frameN  # exact frame index
                nextDemo.tStart = t  # local t and not account for scr refresh
                nextDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextDemo, 'tStartRefresh')  # time at next scr refresh
                # update status
                nextDemo.status = STARTED
                win.callOnFlip(nextDemo.buttonClock.reset)
                nextDemo.setAutoDraw(True)
            
            # if nextDemo is active this frame...
            if nextDemo.status == STARTED:
                # update params
                pass
                # check whether nextDemo has been pressed
                if nextDemo.isClicked:
                    if not nextDemo.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        nextDemo.timesOn.append(nextDemo.buttonClock.getTime())
                        nextDemo.timesOff.append(nextDemo.buttonClock.getTime())
                    elif len(nextDemo.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        nextDemo.timesOff[-1] = nextDemo.buttonClock.getTime()
                    if not nextDemo.wasClicked:
                        # run callback code when nextDemo is clicked
                        pass
            # take note of whether nextDemo was clicked, so that next frame we know if clicks are new
            nextDemo.wasClicked = nextDemo.isClicked and nextDemo.status == STARTED
            
            # *questionDemo* updates
            
            # if questionDemo is starting this frame...
            if questionDemo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                questionDemo.frameNStart = frameN  # exact frame index
                questionDemo.tStart = t  # local t and not account for scr refresh
                questionDemo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(questionDemo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'questionDemo.started')
                # update status
                questionDemo.status = STARTED
                questionDemo.setAutoDraw(True)
            
            # if questionDemo is active this frame...
            if questionDemo.status == STARTED:
                # update params
                pass
            
            # *box1* updates
            
            # if box1 is starting this frame...
            if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box1.frameNStart = frameN  # exact frame index
                box1.tStart = t  # local t and not account for scr refresh
                box1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
                # update status
                box1.status = STARTED
                box1.setAutoDraw(True)
            
            # if box1 is active this frame...
            if box1.status == STARTED:
                # update params
                pass
            
            # *choiceA_demo* updates
            
            # if choiceA_demo is starting this frame...
            if choiceA_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceA_demo.frameNStart = frameN  # exact frame index
                choiceA_demo.tStart = t  # local t and not account for scr refresh
                choiceA_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceA_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceA_demo.status = STARTED
                choiceA_demo.setAutoDraw(True)
            
            # if choiceA_demo is active this frame...
            if choiceA_demo.status == STARTED:
                # update params
                pass
            
            # *box2* updates
            
            # if box2 is starting this frame...
            if box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box2.frameNStart = frameN  # exact frame index
                box2.tStart = t  # local t and not account for scr refresh
                box2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box2, 'tStartRefresh')  # time at next scr refresh
                # update status
                box2.status = STARTED
                box2.setAutoDraw(True)
            
            # if box2 is active this frame...
            if box2.status == STARTED:
                # update params
                pass
            
            # *choiceB_demo* updates
            
            # if choiceB_demo is starting this frame...
            if choiceB_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceB_demo.frameNStart = frameN  # exact frame index
                choiceB_demo.tStart = t  # local t and not account for scr refresh
                choiceB_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceB_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceB_demo.status = STARTED
                choiceB_demo.setAutoDraw(True)
            
            # if choiceB_demo is active this frame...
            if choiceB_demo.status == STARTED:
                # update params
                pass
            
            # *box3* updates
            
            # if box3 is starting this frame...
            if box3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box3.frameNStart = frameN  # exact frame index
                box3.tStart = t  # local t and not account for scr refresh
                box3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box3, 'tStartRefresh')  # time at next scr refresh
                # update status
                box3.status = STARTED
                box3.setAutoDraw(True)
            
            # if box3 is active this frame...
            if box3.status == STARTED:
                # update params
                pass
            
            # *choiceC_demo* updates
            
            # if choiceC_demo is starting this frame...
            if choiceC_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceC_demo.frameNStart = frameN  # exact frame index
                choiceC_demo.tStart = t  # local t and not account for scr refresh
                choiceC_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceC_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceC_demo.status = STARTED
                choiceC_demo.setAutoDraw(True)
            
            # if choiceC_demo is active this frame...
            if choiceC_demo.status == STARTED:
                # update params
                pass
            
            # *box4* updates
            
            # if box4 is starting this frame...
            if box4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box4.frameNStart = frameN  # exact frame index
                box4.tStart = t  # local t and not account for scr refresh
                box4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box4, 'tStartRefresh')  # time at next scr refresh
                # update status
                box4.status = STARTED
                box4.setAutoDraw(True)
            
            # if box4 is active this frame...
            if box4.status == STARTED:
                # update params
                pass
            
            # *choiceD_demo* updates
            
            # if choiceD_demo is starting this frame...
            if choiceD_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choiceD_demo.frameNStart = frameN  # exact frame index
                choiceD_demo.tStart = t  # local t and not account for scr refresh
                choiceD_demo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choiceD_demo, 'tStartRefresh')  # time at next scr refresh
                # update status
                choiceD_demo.status = STARTED
                choiceD_demo.setAutoDraw(True)
            
            # if choiceD_demo is active this frame...
            if choiceD_demo.status == STARTED:
                # update params
                pass
            # *mouse_5* updates
            
            # if mouse_5 is starting this frame...
            if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_5.frameNStart = frameN  # exact frame index
                mouse_5.tStart = t  # local t and not account for scr refresh
                mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_5.status = STARTED
                mouse_5.mouseClock.reset()
                prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=demographicQuiz,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                demographicQuiz.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in demographicQuiz.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "demographicQuiz" ---
        for thisComponent in demographicQuiz.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for demographicQuiz
        demographicQuiz.tStop = globalClock.getTime(format='float')
        demographicQuiz.tStopRefresh = tThisFlipGlobal
        thisExp.addData('demographicQuiz.stopped', demographicQuiz.tStop)
        # Run 'End Routine' code from demo_record
        if selectedAnswer is None:
            participant_answer = "No answer"
        else:
            participant_answer = selectedAnswer
        
        thisExp.addData("participant_answer", participant_answer)
        
        # store data for trials_4 (TrialHandler)
        x, y = mouse_5.getPos()
        buttons = mouse_5.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([boxA, boxB, boxC, boxD], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_5):
                    gotValidClick = True
                    mouse_5.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_5.clicked_name.append(None)
        trials_4.addData('mouse_5.x', x)
        trials_4.addData('mouse_5.y', y)
        trials_4.addData('mouse_5.leftButton', buttons[0])
        trials_4.addData('mouse_5.midButton', buttons[1])
        trials_4.addData('mouse_5.rightButton', buttons[2])
        if len(mouse_5.clicked_name):
            trials_4.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
        # the Routine "demographicQuiz" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial_4 as finished
        if hasattr(thisTrial_4, 'status'):
            thisTrial_4.status = FINISHED
        # if awaiting a pause, pause now
        if trials_4.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_4.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    trials_4.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_4.trialList in ([], [None], None):
        params = []
    else:
        params = trials_4.trialList[0].keys()
    # save data for this loop
    trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[ending_text],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from progress_end
    progressStep = progressTotal
    progressWidth = 1.8 * progressStep / progressTotal
    progressBar.setSize((progressWidth, 0.025))
    progressBar.setPos((-0.9 + progressWidth / 2, 0.94))
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
            # update status
            ending_text.status = STARTED
            ending_text.setAutoDraw(True)
        
        # if ending_text is active this frame...
        if ending_text.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_8
        # Ctrl + Q to quit
        keys = event.getKeys(modifiers=True)
        
        for key, modifiers in keys:
            if key.lower() == 'q' and modifiers.get('ctrl', False):
                core.quit()
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
