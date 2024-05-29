** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://www.thetestingworld.com/login

*** Test Cases ***
TC_08_05_01 Open Context Menu
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Open Context Menu    xpath://span[contains(text(),'VIDEOS')]
    Sleep    2 seconds
    Close Browser

TC_08_05_02 Doubleclick
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Double Click Element    xpath://a[text()='Quick Demo']
    Sleep    2 seconds
    Close Browser

TC_08_05_03 Mouse up and down
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Mouse Up    xpath://a[text()='Quick Demo']
    Sleep    1 second
    Mouse Down    xpath://a[text()='Quick Demo']
    Sleep    2 seconds
    Close Browser

TC_08_05_04 Mouse over
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Mouse Over    xpath://span[contains(text(),'VIDEOS')]
    Sleep    2 seconds
    Close Browser
    