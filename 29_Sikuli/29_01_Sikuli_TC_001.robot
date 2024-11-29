*** Settings ***
Library    SikuliLibrary    mode=NEW
Library    SeleniumLibrary



*** Variables ***



*** Test Cases ***
TC_001 Start Browser on Windows
    Start Sikuli Process
    Add Image Path    C:/Users/a315707/OneDrive - Deutsche Telekom AG/Schulungen/Programmierung/Python/PythonLearning/29_Sikuli/
    Click    Sikuli_StartButton.png
    Click    Sikuli_Chrome.png
    