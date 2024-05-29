** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://www.thetestingworld.com/testings/

*** Test Cases ***
TC_08_06_01 Enter text
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Click Element    xpath://html/body/div[4]/section/ul/li[2]/label
    Press Key    name:_txtUserName    hello
    Press Key    xpath://html/body/div[4]/section/ul/li[2]/div/form/div/input[2]    \\13
    Sleep    2 seconds
    Close Browser