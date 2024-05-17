*** Settings ***

Documentation    This file having testcase of testing ABC functionality
Test Setup    Start Browser and Maximize
Test Teardown    Close Browser Window
Suite Setup    Before Each Test Suite
suite teardown    After Each Test Suite
default tags    DFLT
force tags    ALL_TC

*** Variables ***
${Browser}    Chrome
${URL}    https://www.thetestingworld.com/testings

*** Test Cases ***
Robot First Test Case
    [Tags]    Smoke
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    testingworldindia@gmail.com
    Input Text    name:fld_password    123456

Robot Next Test Case
    Select Radio Button    add_type    office