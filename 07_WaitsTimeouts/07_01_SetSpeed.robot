*** Settings ***

Library    SeleniumLibrary

*** Test Cases ***
TC_07_01_01 Set Selenium Speed
    ${speed}=    Get Selenium Speed
    Log To Console    ${speed}
    Open Browser    https://thetestingworld.com/testings    Firefox
    Maximize Browser Window
    Set Selenium Speed    2 seconds
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    TestingworldIndia@gmail.com
    Input Text    name:fld_password    abcd
    ${speed}=    Get Selenium Speed
    Log To Console    ${speed}

TC_07_01_02 Sleep command
    Open Browser    https://thetestingworld.com/testings    Firefox
    Maximize Browser Window
    Sleep    10 seconds
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    TestingworldIndia@gmail.com
    Input Text    name:fld_password    abcd

