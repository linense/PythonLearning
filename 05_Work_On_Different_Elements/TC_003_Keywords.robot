*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${Browser}    Firefox
${URL}    http://thetestingworld.com/testings

*** Test Cases ***
Use own keyword
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    Enter Username Email Password    Testing    testingworldindia@gmail.com    123456

*** Keywords ***
Enter Username Email Password
    [Arguments]    ${username}    ${email}    ${password}
    Input Text    name:fld_username    ${username}
    Input Text    name:fld_email    ${email}
    Input Text    name:fld_password    ${password}
