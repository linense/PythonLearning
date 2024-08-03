*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***
Start Browser and Maximize
    [Documentation]  This Documentation is to open a browser and maximize the browser window
    [Arguments]    ${UserURL}    ${InputBrowser}
    [Timeout]   50s  #Added in 12_02, Timeout can be set on Keyword level
    Open Browser    ${UserURL}    ${InputBrowser}
    Maximize Browser Window
    ${Title}=    Get Title
    [Return]    ${Title}