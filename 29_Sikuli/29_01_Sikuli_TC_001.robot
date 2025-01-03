*** Settings ***
Library    SikuliLibrary    mode=NEW

*** Variables ***

*** Test Cases ***
TC_001 Start Browser on Windows
    Start Sikuli Process
    Add Image Path    C:/Users/a315707/OneDrive - Deutsche Telekom AG/Schulungen/Programmierung/Python/PythonLearning/29_Sikuli/
    Click    Sikuli_StartButton.png
    Click    Sikuli_Chrome.png

TC_002 Notepad Editing
    Start Sikuli Process
    Add Image Path    C:/Users/a315707/OneDrive - Deutsche Telekom AG/Schulungen/Programmierung/Python/PythonLearning/29_Sikuli/
    Highlight    Sikuli_StartButton.png    5   
    Click    Sikuli_StartButton.png
    Click    Sikuli_Suchfeld.png
    Input Text    Sikuli_Suchfeld    notepad++
    Click    Sikuli_Notepad++.png
    Wait Until Screen Contain    Sikuli_Notepad++.png    10
    #Click    Sikuli_Notepad++TextArea.png
    #Input Text    Sikuli_Notepad++TextArea.png    This text has been entered by Sikuli
