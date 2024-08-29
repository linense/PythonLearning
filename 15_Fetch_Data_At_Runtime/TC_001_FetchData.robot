Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This Suite shows how to apply tags

*** Settings ***
#Test Setup  Start Browser and Maximize

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Robot Fetch Data
    [Documentation]     This is the Robot Fetch Data test case
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    testingworldindia@gmail.com
    Input Text    name:fld_password  123456
    
    Close Browser