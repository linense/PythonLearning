*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
TC_06_01 Variable Test
    ${Var1}=    Set Variable    HelloWorld
    Log To Console    ${Var1}


*** Keywords ***