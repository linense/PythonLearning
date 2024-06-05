*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://thetestingworld.com

*** Test Cases ***
TC_10_03_01 Verify Checkbox
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Click Element    xpath://html/body/div[2]/div[2]/div/div/div[2]/ul/li[9]/a/span
    Select Checkbox    name:jform[contact_email_copy]
    Checkbox Should Be Selected    name:jform[contact_email_copy]
    Click Element    name:jform[contact_email_copy]
    Checkbox Should Not Be Selected    name:jform[contact_email_copy]
    Close Browser