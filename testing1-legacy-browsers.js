/***************** 
 * Testing1 *
 *****************/


// store info about the experiment session:
let expName = 'testing1';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('#d3d3d3'),
  units: 'norm',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(demographicRoutineBegin());
flowScheduler.add(demographicRoutineEachFrame());
flowScheduler.add(demographicRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(warningRoutineBegin());
flowScheduler.add(warningRoutineEachFrame());
flowScheduler.add(warningRoutineEnd());
flowScheduler.add(videoRoutineBegin());
flowScheduler.add(videoRoutineEachFrame());
flowScheduler.add(videoRoutineEnd());
flowScheduler.add(quizinstructionRoutineBegin());
flowScheduler.add(quizinstructionRoutineEachFrame());
flowScheduler.add(quizinstructionRoutineEnd());
flowScheduler.add(sampleQuizRoutineBegin());
flowScheduler.add(sampleQuizRoutineEachFrame());
flowScheduler.add(sampleQuizRoutineEnd());
flowScheduler.add(quizRoutineBegin());
flowScheduler.add(quizRoutineEachFrame());
flowScheduler.add(quizRoutineEnd());
flowScheduler.add(quizendingRoutineBegin());
flowScheduler.add(quizendingRoutineEachFrame());
flowScheduler.add(quizendingRoutineEnd());
const likertLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(likertLoopLoopBegin(likertLoopLoopScheduler));
flowScheduler.add(likertLoopLoopScheduler);
flowScheduler.add(likertLoopLoopEnd);


flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'likert_items.xlsx', 'path': 'likert_items.xlsx'},
    {'name': 'demoForm.xlsx', 'path': 'demoForm.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var demographicClock;
var demoNext;
var form;
var consentClock;
var consentText;
var mouse;
var consentNextButton;
var instructionsClock;
var instruction_header;
var instruction_text;
var instruct_resp;
var nextButton_instructions;
var warningClock;
var warning_header;
var warning_text;
var warning_resp;
var nextButton_warning;
var videoClock;
var quizinstructionClock;
var textbox;
var quz_instruction_text;
var nextButton_quizInstruction;
var sampleQuizClock;
var quizClock;
var quizendingClock;
var textbox_2;
var key_resp_quizending;
var nextButton_2;
var likertClock;
var likertText;
var likert_slider;
var nextButton;
var endClock;
var ending_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "demographic"
  demographicClock = new util.Clock();
  demoNext = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'demoNext',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: 0,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  demoNext.clock = new util.Clock();
  
  form = new visual.Form({
    win : psychoJS.window, name:'form',
    items : 'demoForm.xlsx',
    textHeight : 0.03,
    font : 'Noto Sans',
    randomize : false,
    size : [1.6, 0.7],
    pos : [0, 0],
    style : 'custom...',
    itemPadding : 0.1,
    depth : -1
  });
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consentText = new visual.TextBox({
    win: psychoJS.window,
    name: 'consentText',
    text: 'PARTICIPANT INFORMATION AND CONSENT\n\nWho Can Take Part\n- You must be 18 years or older.\n- You must not have a vision or hearing impairment that would affect your participation.\n- You must be able to follow a lecture in English\n- You must not have been enrolled one of the competencies listed here:\n   - AIC - 505 Generative AI\n   - SEN - 210 DesktopGUI\n   - TBC\n\nHow Long It Takes\n- The whole session takes about 30 to 45 minutes.\n- Please follow the instructions on the screen.\n\nYour Rights\n- Taking part is voluntary.\n- You can stop and leave at any time. You do not have to give a reason.\n- If you leave, your data will not be stored or used.\n\nPrivacy\n- Your name will not be written in your data. You will only have a participant number.\n- Your data will be stored securely.\n- Results will only be reported for the whole group. No one will be identified.\n\nCONSENT\n- I have read this information.\n- I understand that I can stop at any time.\n- I agree to take part in this study.\n\nYou can ask the experimenter any question before you start.\n\nIf you agree, please continue to the next step by clicking the "NEXT" button.',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1.5, 0.75],  units: 'height', 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.02,
    alignment: 'top-left',
    overflow: 'scroll',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  consentNextButton = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'consentNextButton',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -3,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  consentNextButton.clock = new util.Clock();
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instruction_header = new visual.TextBox({
    win: psychoJS.window,
    name: 'instruction_header',
    text: 'Instructions',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0.65], 
    draggable: false,
    letterHeight: 0.15,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  instruction_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'instruction_text',
    text: 'In this study, you will:\n\n1. Watch a short educational video\n2. Answer a series of questions about what you watched\n3. Answer a few questions about your experience\n4. Fill in a short form about your age, gender, and education.\n\n',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, (- 0.05)], 
    draggable: false,
    letterHeight: 0.1,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'hidden',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  instruct_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nextButton_instructions = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'nextButton_instructions',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -3,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  nextButton_instructions.clock = new util.Clock();
  
  // Initialize components for Routine "warning"
  warningClock = new util.Clock();
  warning_header = new visual.TextBox({
    win: psychoJS.window,
    name: 'warning_header',
    text: 'IMPORTANT',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0.65], 
    draggable: false,
    letterHeight: 0.15,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  warning_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'warning_text',
    text: '- You will watch one video in full. \n- Please pay close attention, as you will be tested on the content \n  afterward.\n- The video and quiz cannot be repeated once completed.\n\n',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, (- 0.15)], 
    draggable: false,
    letterHeight: 0.1,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  warning_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nextButton_warning = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'nextButton_warning',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -3,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  nextButton_warning.clock = new util.Clock();
  
  // Initialize components for Routine "video"
  videoClock = new util.Clock();
  // Initialize components for Routine "quizinstruction"
  quizinstructionClock = new util.Clock();
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: 'Thank you for watching the video.\n\nYou will now answer some questions about what you just watched.\n\nPlease answer based on your own understanding.\n\nBefore the main questions, you will first complete a short sample \nquiz to help you get familiar with how the questions work.\n\n',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.1,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  quz_instruction_text = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nextButton_quizInstruction = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'nextButton_quizInstruction',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -2,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  nextButton_quizInstruction.clock = new util.Clock();
  
  // Initialize components for Routine "sampleQuiz"
  sampleQuizClock = new util.Clock();
  // Initialize components for Routine "quiz"
  quizClock = new util.Clock();
  // Initialize components for Routine "quizending"
  quizendingClock = new util.Clock();
  textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_2',
    text: "You have completed the quiz.\n\nJust a few more short questions about your experience, and then \nyou'll be finished.\n\n",
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.1,
    lineSpacing: 1.0,
    size: [1.85, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp_quizending = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nextButton_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'nextButton_2',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -2,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  nextButton_2.clock = new util.Clock();
  
  // Initialize components for Routine "likert"
  likertClock = new util.Clock();
  likertText = new visual.TextStim({
    win: psychoJS.window,
    name: 'likertText',
    text: '',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color("'#000000'"),  opacity: undefined,
    depth: 0.0 
  });
  
  likert_slider = new visual.Slider({
    win: psychoJS.window, name: 'likert_slider',
    startValue: undefined,
    size: [1.5, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: ["Strongly disagree", "Disagree", "Somewhat disagree", "Neither agree nor disagree", "Somewhat agree", "Agree", "Strongly agree"], fontSize: 0.036, ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color("'#000000'"), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  nextButton = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'nextButton',
    text: 'Next>>',
    font: 'Times New Roman',
    pos: [0.8, (- 0.75)],
    size: [0.15, 0.15],
    padding: null,
    anchor: 'center',
    ori: 0.0,
    units: psychoJS.window.units,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    fillColor: [1.0, 1.0, 1.0],
    borderColor: null,
    colorSpace: 'rgb',
    borderWidth: 0.0,
    opacity: null,
    depth: -2,
    letterHeight: 0.05,
    bold: true,
    italic: false,
  });
  nextButton.clock = new util.Clock();
  
  // Run 'Begin Experiment' code from code_7
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  ending_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'ending_text',
    text: 'Thank you for participating in this study!\n\nYour responses have been recorded successfully.',
    placeholder: 'Type here...',
    font: 'Times New Roman',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.1,
    lineSpacing: 1.0,
    size: [1.8, 0.5],  units: undefined, 
    ori: 0.0,
    color: "'#000000'", colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var demographicMaxDurationReached;
var demographicMaxDuration;
var demographicComponents;
function demographicRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'demographic' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    demographicClock.reset();
    routineTimer.reset();
    demographicMaxDurationReached = false;
    // update component parameters for each repeat
    // reset demoNext to account for continued clicks & clear times on/off
    demoNext.reset()
    psychoJS.experiment.addData('demographic.started', globalClock.getTime());
    demographicMaxDuration = null
    // keep track of which components have finished
    demographicComponents = [];
    demographicComponents.push(demoNext);
    demographicComponents.push(form);
    
    demographicComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demographicRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'demographic' ---
    // get current time
    t = demographicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoNext* updates
    if (t >= 0 && demoNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoNext.tStart = t;  // (not accounting for frame time here)
      demoNext.frameNStart = frameN;  // exact frame index
      
      demoNext.setAutoDraw(true);
    }
    
    
    // if demoNext is active this frame...
    if (demoNext.status === PsychoJS.Status.STARTED) {
    }
    
    if (demoNext.status === PsychoJS.Status.STARTED) {
      // check whether demoNext has been pressed
      if (demoNext.isClicked) {
        if (!demoNext.wasClicked) {
          // store time of first click
          demoNext.timesOn.push(demoNext.clock.getTime());
          // store time clicked until
          demoNext.timesOff.push(demoNext.clock.getTime());
        } else {
          // update time clicked until;
          demoNext.timesOff[demoNext.timesOff.length - 1] = demoNext.clock.getTime();
        }
        if (!demoNext.wasClicked) {
          // end routine when demoNext is clicked
          continueRoutine = false;
          
        }
        // if demoNext is still clicked next frame, it is not a new click
        demoNext.wasClicked = true;
      } else {
        // if demoNext is clicked next frame, it is a new click
        demoNext.wasClicked = false;
      }
    } else {
      // keep clock at 0 if demoNext hasn't started / has finished
      demoNext.clock.reset();
      // if demoNext is clicked next frame, it is a new click
      demoNext.wasClicked = false;
    }
    
    // *form* updates
    if (t >= 0.0 && form.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      form.tStart = t;  // (not accounting for frame time here)
      form.frameNStart = frameN;  // exact frame index
      
      form.setAutoDraw(true);
    }
    
    
    // if form is active this frame...
    if (form.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from code_9
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demographicComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demographicRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'demographic' ---
    demographicComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('demographic.stopped', globalClock.getTime());
    psychoJS.experiment.addData('demoNext.numClicks', demoNext.numClicks);
    psychoJS.experiment.addData('demoNext.timesOn', demoNext.timesOn);
    psychoJS.experiment.addData('demoNext.timesOff', demoNext.timesOff);
    form.addDataToExp(psychoJS.experiment, 'rows');
    // the Routine "demographic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var consentMaxDurationReached;
var gotValidClick;
var consentMaxDuration;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    consentClock.reset();
    routineTimer.reset();
    consentMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    // reset consentNextButton to account for continued clicks & clear times on/off
    consentNextButton.reset()
    psychoJS.experiment.addData('consent.started', globalClock.getTime());
    consentMaxDuration = null
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(consentText);
    consentComponents.push(mouse);
    consentComponents.push(consentNextButton);
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consentText* updates
    if (t >= 0.0 && consentText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentText.tStart = t;  // (not accounting for frame time here)
      consentText.frameNStart = frameN;  // exact frame index
      
      consentText.setAutoDraw(true);
    }
    
    
    // if consentText is active this frame...
    if (consentText.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from codeScroll
    /* Syntax Error: Fix Python code */
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse is active this frame...
    if (mouse.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    
    // *consentNextButton* updates
    if (t >= 0 && consentNextButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentNextButton.tStart = t;  // (not accounting for frame time here)
      consentNextButton.frameNStart = frameN;  // exact frame index
      
      consentNextButton.setAutoDraw(true);
    }
    
    
    // if consentNextButton is active this frame...
    if (consentNextButton.status === PsychoJS.Status.STARTED) {
    }
    
    if (consentNextButton.status === PsychoJS.Status.STARTED) {
      // check whether consentNextButton has been pressed
      if (consentNextButton.isClicked) {
        if (!consentNextButton.wasClicked) {
          // store time of first click
          consentNextButton.timesOn.push(consentNextButton.clock.getTime());
          // store time clicked until
          consentNextButton.timesOff.push(consentNextButton.clock.getTime());
        } else {
          // update time clicked until;
          consentNextButton.timesOff[consentNextButton.timesOff.length - 1] = consentNextButton.clock.getTime();
        }
        if (!consentNextButton.wasClicked) {
          // end routine when consentNextButton is clicked
          continueRoutine = false;
          
        }
        // if consentNextButton is still clicked next frame, it is not a new click
        consentNextButton.wasClicked = true;
      } else {
        // if consentNextButton is clicked next frame, it is a new click
        consentNextButton.wasClicked = false;
      }
    } else {
      // keep clock at 0 if consentNextButton hasn't started / has finished
      consentNextButton.clock.reset();
      // if consentNextButton is clicked next frame, it is a new click
      consentNextButton.wasClicked = false;
    }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('consent.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    
    psychoJS.experiment.addData('consentNextButton.numClicks', consentNextButton.numClicks);
    psychoJS.experiment.addData('consentNextButton.timesOn', consentNextButton.timesOn);
    psychoJS.experiment.addData('consentNextButton.timesOff', consentNextButton.timesOff);
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionsMaxDurationReached;
var _instruct_resp_allKeys;
var instructionsMaxDuration;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionsClock.reset();
    routineTimer.reset();
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    instruct_resp.keys = undefined;
    instruct_resp.rt = undefined;
    _instruct_resp_allKeys = [];
    // reset nextButton_instructions to account for continued clicks & clear times on/off
    nextButton_instructions.reset()
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instruction_header);
    instructionsComponents.push(instruction_text);
    instructionsComponents.push(instruct_resp);
    instructionsComponents.push(nextButton_instructions);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_header* updates
    if (t >= 0.0 && instruction_header.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_header.tStart = t;  // (not accounting for frame time here)
      instruction_header.frameNStart = frameN;  // exact frame index
      
      instruction_header.setAutoDraw(true);
    }
    
    
    // if instruction_header is active this frame...
    if (instruction_header.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *instruction_text* updates
    if (t >= 0.0 && instruction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text.tStart = t;  // (not accounting for frame time here)
      instruction_text.frameNStart = frameN;  // exact frame index
      
      instruction_text.setAutoDraw(true);
    }
    
    
    // if instruction_text is active this frame...
    if (instruction_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *instruct_resp* updates
    if (t >= 0.0 && instruct_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_resp.tStart = t;  // (not accounting for frame time here)
      instruct_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruct_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruct_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruct_resp.clearEvents(); });
    }
    
    // if instruct_resp is active this frame...
    if (instruct_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruct_resp.getKeys({keyList: 'space', waitRelease: false});
      _instruct_resp_allKeys = _instruct_resp_allKeys.concat(theseKeys);
      if (_instruct_resp_allKeys.length > 0) {
        instruct_resp.keys = _instruct_resp_allKeys[_instruct_resp_allKeys.length - 1].name;  // just the last key pressed
        instruct_resp.rt = _instruct_resp_allKeys[_instruct_resp_allKeys.length - 1].rt;
        instruct_resp.duration = _instruct_resp_allKeys[_instruct_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nextButton_instructions* updates
    if (t >= 0 && nextButton_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextButton_instructions.tStart = t;  // (not accounting for frame time here)
      nextButton_instructions.frameNStart = frameN;  // exact frame index
      
      nextButton_instructions.setAutoDraw(true);
    }
    
    
    // if nextButton_instructions is active this frame...
    if (nextButton_instructions.status === PsychoJS.Status.STARTED) {
    }
    
    if (nextButton_instructions.status === PsychoJS.Status.STARTED) {
      // check whether nextButton_instructions has been pressed
      if (nextButton_instructions.isClicked) {
        if (!nextButton_instructions.wasClicked) {
          // store time of first click
          nextButton_instructions.timesOn.push(nextButton_instructions.clock.getTime());
          // store time clicked until
          nextButton_instructions.timesOff.push(nextButton_instructions.clock.getTime());
        } else {
          // update time clicked until;
          nextButton_instructions.timesOff[nextButton_instructions.timesOff.length - 1] = nextButton_instructions.clock.getTime();
        }
        if (!nextButton_instructions.wasClicked) {
          // end routine when nextButton_instructions is clicked
          continueRoutine = false;
          
        }
        // if nextButton_instructions is still clicked next frame, it is not a new click
        nextButton_instructions.wasClicked = true;
      } else {
        // if nextButton_instructions is clicked next frame, it is a new click
        nextButton_instructions.wasClicked = false;
      }
    } else {
      // keep clock at 0 if nextButton_instructions hasn't started / has finished
      nextButton_instructions.clock.reset();
      // if nextButton_instructions is clicked next frame, it is a new click
      nextButton_instructions.wasClicked = false;
    }
    // Run 'Each Frame' code from code
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruct_resp.corr, level);
    }
    psychoJS.experiment.addData('instruct_resp.keys', instruct_resp.keys);
    if (typeof instruct_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruct_resp.rt', instruct_resp.rt);
        psychoJS.experiment.addData('instruct_resp.duration', instruct_resp.duration);
        routineTimer.reset();
        }
    
    instruct_resp.stop();
    psychoJS.experiment.addData('nextButton_instructions.numClicks', nextButton_instructions.numClicks);
    psychoJS.experiment.addData('nextButton_instructions.timesOn', nextButton_instructions.timesOn);
    psychoJS.experiment.addData('nextButton_instructions.timesOff', nextButton_instructions.timesOff);
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var warningMaxDurationReached;
var _warning_resp_allKeys;
var warningMaxDuration;
var warningComponents;
function warningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'warning' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    warningClock.reset();
    routineTimer.reset();
    warningMaxDurationReached = false;
    // update component parameters for each repeat
    warning_resp.keys = undefined;
    warning_resp.rt = undefined;
    _warning_resp_allKeys = [];
    // reset nextButton_warning to account for continued clicks & clear times on/off
    nextButton_warning.reset()
    psychoJS.experiment.addData('warning.started', globalClock.getTime());
    warningMaxDuration = null
    // keep track of which components have finished
    warningComponents = [];
    warningComponents.push(warning_header);
    warningComponents.push(warning_text);
    warningComponents.push(warning_resp);
    warningComponents.push(nextButton_warning);
    
    warningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function warningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'warning' ---
    // get current time
    t = warningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *warning_header* updates
    if (t >= 0.0 && warning_header.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning_header.tStart = t;  // (not accounting for frame time here)
      warning_header.frameNStart = frameN;  // exact frame index
      
      warning_header.setAutoDraw(true);
    }
    
    
    // if warning_header is active this frame...
    if (warning_header.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *warning_text* updates
    if (t >= 0.0 && warning_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning_text.tStart = t;  // (not accounting for frame time here)
      warning_text.frameNStart = frameN;  // exact frame index
      
      warning_text.setAutoDraw(true);
    }
    
    
    // if warning_text is active this frame...
    if (warning_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *warning_resp* updates
    if (t >= 0.0 && warning_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning_resp.tStart = t;  // (not accounting for frame time here)
      warning_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { warning_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { warning_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { warning_resp.clearEvents(); });
    }
    
    // if warning_resp is active this frame...
    if (warning_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = warning_resp.getKeys({keyList: [], waitRelease: false});
      _warning_resp_allKeys = _warning_resp_allKeys.concat(theseKeys);
      if (_warning_resp_allKeys.length > 0) {
        warning_resp.keys = _warning_resp_allKeys[_warning_resp_allKeys.length - 1].name;  // just the last key pressed
        warning_resp.rt = _warning_resp_allKeys[_warning_resp_allKeys.length - 1].rt;
        warning_resp.duration = _warning_resp_allKeys[_warning_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nextButton_warning* updates
    if (t >= 0 && nextButton_warning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextButton_warning.tStart = t;  // (not accounting for frame time here)
      nextButton_warning.frameNStart = frameN;  // exact frame index
      
      nextButton_warning.setAutoDraw(true);
    }
    
    
    // if nextButton_warning is active this frame...
    if (nextButton_warning.status === PsychoJS.Status.STARTED) {
    }
    
    if (nextButton_warning.status === PsychoJS.Status.STARTED) {
      // check whether nextButton_warning has been pressed
      if (nextButton_warning.isClicked) {
        if (!nextButton_warning.wasClicked) {
          // store time of first click
          nextButton_warning.timesOn.push(nextButton_warning.clock.getTime());
          // store time clicked until
          nextButton_warning.timesOff.push(nextButton_warning.clock.getTime());
        } else {
          // update time clicked until;
          nextButton_warning.timesOff[nextButton_warning.timesOff.length - 1] = nextButton_warning.clock.getTime();
        }
        if (!nextButton_warning.wasClicked) {
          // end routine when nextButton_warning is clicked
          continueRoutine = false;
          
        }
        // if nextButton_warning is still clicked next frame, it is not a new click
        nextButton_warning.wasClicked = true;
      } else {
        // if nextButton_warning is clicked next frame, it is a new click
        nextButton_warning.wasClicked = false;
      }
    } else {
      // keep clock at 0 if nextButton_warning hasn't started / has finished
      nextButton_warning.clock.reset();
      // if nextButton_warning is clicked next frame, it is a new click
      nextButton_warning.wasClicked = false;
    }
    // Run 'Each Frame' code from code_2
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    warningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function warningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'warning' ---
    warningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('warning.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(warning_resp.corr, level);
    }
    psychoJS.experiment.addData('warning_resp.keys', warning_resp.keys);
    if (typeof warning_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('warning_resp.rt', warning_resp.rt);
        psychoJS.experiment.addData('warning_resp.duration', warning_resp.duration);
        routineTimer.reset();
        }
    
    warning_resp.stop();
    psychoJS.experiment.addData('nextButton_warning.numClicks', nextButton_warning.numClicks);
    psychoJS.experiment.addData('nextButton_warning.timesOn', nextButton_warning.timesOn);
    psychoJS.experiment.addData('nextButton_warning.timesOff', nextButton_warning.timesOff);
    // the Routine "warning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var videoMaxDurationReached;
var videoMaxDuration;
var videoComponents;
function videoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'video' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    videoClock.reset();
    routineTimer.reset();
    videoMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('video.started', globalClock.getTime());
    videoMaxDuration = null
    // keep track of which components have finished
    videoComponents = [];
    
    videoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function videoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'video' ---
    // get current time
    t = videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_3
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    videoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function videoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'video' ---
    videoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('video.stopped', globalClock.getTime());
    // the Routine "video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quizinstructionMaxDurationReached;
var _quz_instruction_text_allKeys;
var quizinstructionMaxDuration;
var quizinstructionComponents;
function quizinstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quizinstruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    quizinstructionClock.reset();
    routineTimer.reset();
    quizinstructionMaxDurationReached = false;
    // update component parameters for each repeat
    quz_instruction_text.keys = undefined;
    quz_instruction_text.rt = undefined;
    _quz_instruction_text_allKeys = [];
    // reset nextButton_quizInstruction to account for continued clicks & clear times on/off
    nextButton_quizInstruction.reset()
    psychoJS.experiment.addData('quizinstruction.started', globalClock.getTime());
    quizinstructionMaxDuration = null
    // keep track of which components have finished
    quizinstructionComponents = [];
    quizinstructionComponents.push(textbox);
    quizinstructionComponents.push(quz_instruction_text);
    quizinstructionComponents.push(nextButton_quizInstruction);
    
    quizinstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quizinstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quizinstruction' ---
    // get current time
    t = quizinstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    
    // if textbox is active this frame...
    if (textbox.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *quz_instruction_text* updates
    if (t >= 0.0 && quz_instruction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      quz_instruction_text.tStart = t;  // (not accounting for frame time here)
      quz_instruction_text.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { quz_instruction_text.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { quz_instruction_text.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { quz_instruction_text.clearEvents(); });
    }
    
    // if quz_instruction_text is active this frame...
    if (quz_instruction_text.status === PsychoJS.Status.STARTED) {
      let theseKeys = quz_instruction_text.getKeys({keyList: 'space', waitRelease: false});
      _quz_instruction_text_allKeys = _quz_instruction_text_allKeys.concat(theseKeys);
      if (_quz_instruction_text_allKeys.length > 0) {
        quz_instruction_text.keys = _quz_instruction_text_allKeys[_quz_instruction_text_allKeys.length - 1].name;  // just the last key pressed
        quz_instruction_text.rt = _quz_instruction_text_allKeys[_quz_instruction_text_allKeys.length - 1].rt;
        quz_instruction_text.duration = _quz_instruction_text_allKeys[_quz_instruction_text_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nextButton_quizInstruction* updates
    if (t >= 0 && nextButton_quizInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextButton_quizInstruction.tStart = t;  // (not accounting for frame time here)
      nextButton_quizInstruction.frameNStart = frameN;  // exact frame index
      
      nextButton_quizInstruction.setAutoDraw(true);
    }
    
    
    // if nextButton_quizInstruction is active this frame...
    if (nextButton_quizInstruction.status === PsychoJS.Status.STARTED) {
    }
    
    if (nextButton_quizInstruction.status === PsychoJS.Status.STARTED) {
      // check whether nextButton_quizInstruction has been pressed
      if (nextButton_quizInstruction.isClicked) {
        if (!nextButton_quizInstruction.wasClicked) {
          // store time of first click
          nextButton_quizInstruction.timesOn.push(nextButton_quizInstruction.clock.getTime());
          // store time clicked until
          nextButton_quizInstruction.timesOff.push(nextButton_quizInstruction.clock.getTime());
        } else {
          // update time clicked until;
          nextButton_quizInstruction.timesOff[nextButton_quizInstruction.timesOff.length - 1] = nextButton_quizInstruction.clock.getTime();
        }
        if (!nextButton_quizInstruction.wasClicked) {
          // end routine when nextButton_quizInstruction is clicked
          continueRoutine = false;
          
        }
        // if nextButton_quizInstruction is still clicked next frame, it is not a new click
        nextButton_quizInstruction.wasClicked = true;
      } else {
        // if nextButton_quizInstruction is clicked next frame, it is a new click
        nextButton_quizInstruction.wasClicked = false;
      }
    } else {
      // keep clock at 0 if nextButton_quizInstruction hasn't started / has finished
      nextButton_quizInstruction.clock.reset();
      // if nextButton_quizInstruction is clicked next frame, it is a new click
      nextButton_quizInstruction.wasClicked = false;
    }
    // Run 'Each Frame' code from code_4
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quizinstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quizinstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quizinstruction' ---
    quizinstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quizinstruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(quz_instruction_text.corr, level);
    }
    psychoJS.experiment.addData('quz_instruction_text.keys', quz_instruction_text.keys);
    if (typeof quz_instruction_text.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('quz_instruction_text.rt', quz_instruction_text.rt);
        psychoJS.experiment.addData('quz_instruction_text.duration', quz_instruction_text.duration);
        routineTimer.reset();
        }
    
    quz_instruction_text.stop();
    psychoJS.experiment.addData('nextButton_quizInstruction.numClicks', nextButton_quizInstruction.numClicks);
    psychoJS.experiment.addData('nextButton_quizInstruction.timesOn', nextButton_quizInstruction.timesOn);
    psychoJS.experiment.addData('nextButton_quizInstruction.timesOff', nextButton_quizInstruction.timesOff);
    // the Routine "quizinstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var sampleQuizMaxDurationReached;
var sampleQuizMaxDuration;
var sampleQuizComponents;
function sampleQuizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'sampleQuiz' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    sampleQuizClock.reset();
    routineTimer.reset();
    sampleQuizMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('sampleQuiz.started', globalClock.getTime());
    sampleQuizMaxDuration = null
    // keep track of which components have finished
    sampleQuizComponents = [];
    
    sampleQuizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function sampleQuizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'sampleQuiz' ---
    // get current time
    t = sampleQuizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    sampleQuizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function sampleQuizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'sampleQuiz' ---
    sampleQuizComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('sampleQuiz.stopped', globalClock.getTime());
    // the Routine "sampleQuiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quizMaxDurationReached;
var quizMaxDuration;
var quizComponents;
function quizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    quizClock.reset();
    routineTimer.reset();
    quizMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz.started', globalClock.getTime());
    quizMaxDuration = null
    // keep track of which components have finished
    quizComponents = [];
    
    quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz' ---
    // get current time
    t = quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_5
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz' ---
    quizComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz.stopped', globalClock.getTime());
    // the Routine "quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quizendingMaxDurationReached;
var _key_resp_quizending_allKeys;
var quizendingMaxDuration;
var quizendingComponents;
function quizendingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quizending' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    quizendingClock.reset();
    routineTimer.reset();
    quizendingMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_quizending.keys = undefined;
    key_resp_quizending.rt = undefined;
    _key_resp_quizending_allKeys = [];
    // reset nextButton_2 to account for continued clicks & clear times on/off
    nextButton_2.reset()
    psychoJS.experiment.addData('quizending.started', globalClock.getTime());
    quizendingMaxDuration = null
    // keep track of which components have finished
    quizendingComponents = [];
    quizendingComponents.push(textbox_2);
    quizendingComponents.push(key_resp_quizending);
    quizendingComponents.push(nextButton_2);
    
    quizendingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quizendingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quizending' ---
    // get current time
    t = quizendingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox_2* updates
    if (t >= 0.0 && textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_2.tStart = t;  // (not accounting for frame time here)
      textbox_2.frameNStart = frameN;  // exact frame index
      
      textbox_2.setAutoDraw(true);
    }
    
    
    // if textbox_2 is active this frame...
    if (textbox_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_quizending* updates
    if (t >= 0.0 && key_resp_quizending.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_quizending.tStart = t;  // (not accounting for frame time here)
      key_resp_quizending.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_quizending.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_quizending.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_quizending.clearEvents(); });
    }
    
    // if key_resp_quizending is active this frame...
    if (key_resp_quizending.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_quizending.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_quizending_allKeys = _key_resp_quizending_allKeys.concat(theseKeys);
      if (_key_resp_quizending_allKeys.length > 0) {
        key_resp_quizending.keys = _key_resp_quizending_allKeys[_key_resp_quizending_allKeys.length - 1].name;  // just the last key pressed
        key_resp_quizending.rt = _key_resp_quizending_allKeys[_key_resp_quizending_allKeys.length - 1].rt;
        key_resp_quizending.duration = _key_resp_quizending_allKeys[_key_resp_quizending_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nextButton_2* updates
    if (t >= 0 && nextButton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextButton_2.tStart = t;  // (not accounting for frame time here)
      nextButton_2.frameNStart = frameN;  // exact frame index
      
      nextButton_2.setAutoDraw(true);
    }
    
    
    // if nextButton_2 is active this frame...
    if (nextButton_2.status === PsychoJS.Status.STARTED) {
    }
    
    if (nextButton_2.status === PsychoJS.Status.STARTED) {
      // check whether nextButton_2 has been pressed
      if (nextButton_2.isClicked) {
        if (!nextButton_2.wasClicked) {
          // store time of first click
          nextButton_2.timesOn.push(nextButton_2.clock.getTime());
          // store time clicked until
          nextButton_2.timesOff.push(nextButton_2.clock.getTime());
        } else {
          // update time clicked until;
          nextButton_2.timesOff[nextButton_2.timesOff.length - 1] = nextButton_2.clock.getTime();
        }
        if (!nextButton_2.wasClicked) {
          // end routine when nextButton_2 is clicked
          continueRoutine = false;
          
        }
        // if nextButton_2 is still clicked next frame, it is not a new click
        nextButton_2.wasClicked = true;
      } else {
        // if nextButton_2 is clicked next frame, it is a new click
        nextButton_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if nextButton_2 hasn't started / has finished
      nextButton_2.clock.reset();
      // if nextButton_2 is clicked next frame, it is a new click
      nextButton_2.wasClicked = false;
    }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quizendingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quizendingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quizending' ---
    quizendingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quizending.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_quizending.corr, level);
    }
    psychoJS.experiment.addData('key_resp_quizending.keys', key_resp_quizending.keys);
    if (typeof key_resp_quizending.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_quizending.rt', key_resp_quizending.rt);
        psychoJS.experiment.addData('key_resp_quizending.duration', key_resp_quizending.duration);
        routineTimer.reset();
        }
    
    key_resp_quizending.stop();
    psychoJS.experiment.addData('nextButton_2.numClicks', nextButton_2.numClicks);
    psychoJS.experiment.addData('nextButton_2.timesOn', nextButton_2.timesOn);
    psychoJS.experiment.addData('nextButton_2.timesOff', nextButton_2.timesOff);
    // the Routine "quizending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var likertLoop;
function likertLoopLoopBegin(likertLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    likertLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'likert_items.xlsx',
      seed: undefined, name: 'likertLoop'
    });
    psychoJS.experiment.addLoop(likertLoop); // add the loop to the experiment
    currentLoop = likertLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    likertLoop.forEach(function() {
      snapshot = likertLoop.getSnapshot();
    
      likertLoopLoopScheduler.add(importConditions(snapshot));
      likertLoopLoopScheduler.add(likertRoutineBegin(snapshot));
      likertLoopLoopScheduler.add(likertRoutineEachFrame());
      likertLoopLoopScheduler.add(likertRoutineEnd(snapshot));
      likertLoopLoopScheduler.add(likertLoopLoopEndIteration(likertLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function likertLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(likertLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function likertLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var likertMaxDurationReached;
var likertMaxDuration;
var likertComponents;
function likertRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'likert' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    likertClock.reset();
    routineTimer.reset();
    likertMaxDurationReached = false;
    // update component parameters for each repeat
    likertText.setText(itemText);
    likert_slider.reset()
    // reset nextButton to account for continued clicks & clear times on/off
    nextButton.reset()
    psychoJS.experiment.addData('likert.started', globalClock.getTime());
    likertMaxDuration = null
    // keep track of which components have finished
    likertComponents = [];
    likertComponents.push(likertText);
    likertComponents.push(likert_slider);
    likertComponents.push(nextButton);
    
    likertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function likertRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'likert' ---
    // get current time
    t = likertClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *likertText* updates
    if (t >= 0.0 && likertText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      likertText.tStart = t;  // (not accounting for frame time here)
      likertText.frameNStart = frameN;  // exact frame index
      
      likertText.setAutoDraw(true);
    }
    
    
    // if likertText is active this frame...
    if (likertText.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *likert_slider* updates
    if (t >= 0.0 && likert_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      likert_slider.tStart = t;  // (not accounting for frame time here)
      likert_slider.frameNStart = frameN;  // exact frame index
      
      likert_slider.setAutoDraw(true);
    }
    
    
    // if likert_slider is active this frame...
    if (likert_slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *nextButton* updates
    if (t >= 0 && nextButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextButton.tStart = t;  // (not accounting for frame time here)
      nextButton.frameNStart = frameN;  // exact frame index
      
      nextButton.setAutoDraw(true);
    }
    
    
    // if nextButton is active this frame...
    if (nextButton.status === PsychoJS.Status.STARTED) {
    }
    
    if (nextButton.status === PsychoJS.Status.STARTED) {
      // check whether nextButton has been pressed
      if (nextButton.isClicked) {
        if (!nextButton.wasClicked) {
          // store time of first click
          nextButton.timesOn.push(nextButton.clock.getTime());
          // store time clicked until
          nextButton.timesOff.push(nextButton.clock.getTime());
        } else {
          // update time clicked until;
          nextButton.timesOff[nextButton.timesOff.length - 1] = nextButton.clock.getTime();
        }
        if (!nextButton.wasClicked) {
          // end routine when nextButton is clicked
          continueRoutine = false;
          
        }
        // if nextButton is still clicked next frame, it is not a new click
        nextButton.wasClicked = true;
      } else {
        // if nextButton is clicked next frame, it is a new click
        nextButton.wasClicked = false;
      }
    } else {
      // keep clock at 0 if nextButton hasn't started / has finished
      nextButton.clock.reset();
      // if nextButton is clicked next frame, it is a new click
      nextButton.wasClicked = false;
    }
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    likertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function likertRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'likert' ---
    likertComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('likert.stopped', globalClock.getTime());
    psychoJS.experiment.addData('likert_slider.response', likert_slider.getRating());
    psychoJS.experiment.addData('likert_slider.rt', likert_slider.getRT());
    psychoJS.experiment.addData('nextButton.numClicks', nextButton.numClicks);
    psychoJS.experiment.addData('nextButton.timesOn', nextButton.timesOn);
    psychoJS.experiment.addData('nextButton.timesOff', nextButton.timesOff);
    // the Routine "likert" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endMaxDurationReached;
var endMaxDuration;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    endClock.reset();
    routineTimer.reset();
    endMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    endMaxDuration = null
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(ending_text);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ending_text* updates
    if (t >= 0.0 && ending_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_text.tStart = t;  // (not accounting for frame time here)
      ending_text.frameNStart = frameN;  // exact frame index
      
      ending_text.setAutoDraw(true);
    }
    
    
    // if ending_text is active this frame...
    if (ending_text.status === PsychoJS.Status.STARTED) {
    }
    
    // Run 'Each Frame' code from code_8
    /* Syntax Error: Fix Python code */
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
