*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This file tests abc functionality

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Keyword Test Case
    [Tags]  Smoke
    [Documentation]     This test case is to check registration functionality of application
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Log    ${Res}
    Input Text    name:fld_username    ${Res}

Second Setup Test Case
    [Tags]  Smoke   Sanity
    Select Radio Button     add_type    office