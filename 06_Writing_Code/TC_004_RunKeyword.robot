*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***

*** Test Cases ***
TC_001 RunKeyword
    ${Key_Var}=    Set Variable    log to console
    Run Keyword    ${Key_Var}    TestingWorldIndia@gmail.com

TC_002 RunKeywordIf
    ${Var}=    Set Variable    NO
    Run Keyword If    '${Var}'=='YES'    Log To Console    Value Found
    Run Keyword If    '${Var}'=='NO'    Log To Console    Value Not Found

*** Keywords ***