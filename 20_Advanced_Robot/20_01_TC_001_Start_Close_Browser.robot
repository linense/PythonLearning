*** Settings ***

Library    SeleniumLibrary
Library    Locators.py

*** Variables ***
${Browser}    Firefox
${URL}    http://thetestingworld.com/testings

*** Test Cases ***
Robot First Test Case
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    ${username}=    Read Element Locator    Registration.username_textbox_name
    ${email}=    Read Element Locator    Registration.email_textbox_name
     Input Text    name:${username}    TestingWorld
    Input Text    name:${email}   testingworldindia@gmail.com
 
*** Keywords ***
Read Element Locator
    [Arguments]    ${JsonPath}
    ${result}=    read_locator_from_json    ${JsonPath}
    RETURN    ${result}
