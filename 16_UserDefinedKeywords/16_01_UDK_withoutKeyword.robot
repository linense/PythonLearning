*** Settings ***
#Test Setup  Start Browser and Maximize
Library    SeleniumLibrary
Documentation   This Suite uses User Defined Keywords in Python

Resource    ../Resources/Resources4.robot

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Robot Create Folder
    Create Folder at Runtime
    [Documentation]     This test case fetches data from various parts
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Select From List By Index    name:sex    1
    ${ActualURL}=    Get Location
    Log    ${ActualURL}
    Close Browser