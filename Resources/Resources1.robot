*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://www.thetestingworld.com/testings
${Browser}    Firefox

*** Keywords ***
Start Browser and Maximize
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window