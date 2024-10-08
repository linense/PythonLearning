*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This file tests abc functionality

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Keyword Test Case
    [Tags]  Smoke   Regression
    [Documentation]     This is the first test case of the suite
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Log    ${Res}
    Input Text    name:fld_username    ${Res}
    Close Browser

Second Setup Test Case
    # To be started with robot -i Sanity .\13_01_Tags_at_Testcases.robot so that only this test case is started
    [Tags]  Sanity  Regression
    [Documentation]     This is the second test case of the suite
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Select Radio Button     add_type    office
    Close Browser