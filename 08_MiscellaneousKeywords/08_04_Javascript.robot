*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://www.thetestingworld.com

*** Test Cases ***
TC_08_04_01 execute Javascript
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Execute Javascript    window.scrollTo(0,1000)
    sleep    3 seconds
    