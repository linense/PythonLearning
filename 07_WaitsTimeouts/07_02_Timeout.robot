*** Settings ***

Library    SeleniumLibrary

*** Test Cases ***
TC_07_02_01 Set Timeout
    Open Browser    https://thetestingworld.com/testings    Firefox
    Maximize Browser Window
    Set Selenium Timeout    20 seconds
    ${tm}=    Get Selenium Timeout
    Log To Console    ${tm}
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    TestingworldIndia@gmail.com
    Input Text    name:fld_password    abcd
    Wait Until Page Contains    Testing

    


