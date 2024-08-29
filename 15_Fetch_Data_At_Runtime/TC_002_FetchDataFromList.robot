*** Settings ***
#Test Setup  Start Browser and Maximize
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This Suite shows how to apply tags


*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Robot Fetch Data From List
    [Documentation]     This test case fetches data from a list
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Select From List By Index    name:sex    1
    ${Val}=    Get Selected List Value    name:sex
    Log    ${Val}
    ${Text}=    Get Selected List Label    name:sex
    Log    ${Text}
    ${AllLabels}=    Get List Items    name:sex
    Log    ${AllLabels}

    Close Browser