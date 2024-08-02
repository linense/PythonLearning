*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Keyword Test Case
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Log    ${Res}
    Input Text    name:fld_username    ${Res}