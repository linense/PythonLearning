*** Settings ***
Test Setup    Start Browser and Maximize

*** Variables ***
${Browser}    Chrome
${URL}    https://www.thetestingworld.com/testings

*** Test Cases ***
Robot Fetch Data
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    testingworldindia@gmail.com
    Input Text    name:fld_password    123456

