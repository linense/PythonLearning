# Install Robot Corder Chrome Extenstion

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}=    firefox


*** Test Cases ***

TC_001 Recorded Test Case
    Open Browser    https://www.thetestingworld.com/testings/    ${BROWSER}
    Input Text    //input[@name="fld_username"]    testing
    Input Text    //input[@name="fld_email"]    testing@thetestingwordl.com
        Input Text    //input[@name="phone"]    123456789
    Click Element    //input[@name="add_type"]
    Select From List By Value    //select[@name="sex"]    1
    Select From List By Value    //select[@name="country"]    15
    Click Element    //input[@name="terms"]
    Input Text    //input[@name="zip"]    45678
    Click Element    xpath=(//input)[14]