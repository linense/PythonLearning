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
    [Documentation]     This test case fetches data from various parts
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Select From List By Index    name:sex    1
    ${ActualURL}=    Get Location
    Log    ${ActualURL}
    ${PageHTML}=    Get Source
    Log    ${PageHTML}
    ${Attr}=    Get Element Attribute    name:fld_username    class
    Log    ${Attr}
    ${cnt}=    Get Element Count    class:field
    Log    ${cnt}
    Close Browser