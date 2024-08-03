*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This file tests abc functionality
test Timeout    50s  # Timeout can be set on suite level, added in 12_02

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Keyword Test Case
    [Documentation]     This test case is to check registration functionality of application
    #[Timeout]   2mins 50s; Timeouts are normally set on test case level
    [Timeout]   50s 
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Log    ${Res}
    Input Text    name:fld_username    ${Res}