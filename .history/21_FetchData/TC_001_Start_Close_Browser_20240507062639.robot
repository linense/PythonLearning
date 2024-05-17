*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${Browser}    Firefox
${URL}    https://www.t-systems.com/de/en/contact

*** Test Cases ***
TC_001 Browser Start Close
    Open Browser    ${URL}    ${Browser}
    Close Browser
TC_002 Robot First Test Case
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    Input Text    name:TextField_1032367938    Donald Duck
    