*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${Browser}    Firefox
${URL}    http://thetestingworld.com/testings

*** Test Cases ***
Robot First Test Case
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    Input Text    name:fld_username    TestingWorld
    Input Text    xpath://input[@name='fld_email']    testingworldindia@gmail.com
    Select Radio Button    add_type    office
    Select Checkbox    name:terms
    Click Link    xpath://a[text()='Read Detail']
    
    
