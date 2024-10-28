*** Settings ***
Library    SeleniumLibrary
Resource    Resources/UserKeywords.robot


*** Variables ***
${var1}    https://thetestingworld.com/testings/

*** Test Cases ***
TC_001 Login Logout functionality
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    ${row}=    Read Number of Rows    Tabelle1
    FOR    ${i}    IN RANGE    1    ${row}+1
        Click Element    xpath:/html/body/div[4]/section/ul/li[2]/label
        ${username}=    Read Excel data from cell    Tabelle1    ${i}    1
        ${password}=    Read Excel data from cell    Tabelle1    ${i}    2
        Input Text    name:_txtUserName    ${username}
        Input Password    name:_txtPassword    ${password}
        Click Button    xpath:/html/body/div[4]/section/ul/li[2]/div/form/div/input[2]
        Sleep    5 seconds
    END
    Close Browser