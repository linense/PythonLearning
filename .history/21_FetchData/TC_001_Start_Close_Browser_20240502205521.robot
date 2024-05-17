*** Settings ***

#Documentation    This file having testcase of testing ABC functionality
#Test Setup    Start Browser and Maximize
#Test Teardown    Close Browser Window
#Suite Setup    Before Each Test Suite
#suite teardown    After Each Test Suite
#default tags    DFLT
#force tags    ALL_TC

Library    SeleniumLibrary

*** Variables ***
${Browser}    chrome
#${URL}    https://www.thetestingworld.com/testings

*** Test Cases ***
TC_001 Browser Start and Close
    Open Browser  ${Browser}
