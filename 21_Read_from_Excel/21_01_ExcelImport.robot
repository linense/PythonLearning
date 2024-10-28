*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://thetestingworld.com/testings/

*** Test Cases ***
TC_001 Login Logout functionality
    Open Browser    ${var1}
    #Maximize Browser Window
    Click Element    xpath:/html/body/div[4]/section/ul/li[2]/label
    Input Text    name:_txtUserName    testing
    Input Password    name:_txtPassword    testing
    Click Button    xpath:/html/body/div[4]/section/ul/li[2]/div/form/div/input[2]
    Sleep    5 seconds