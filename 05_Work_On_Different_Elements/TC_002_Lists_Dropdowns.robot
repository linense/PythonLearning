*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${Browser}    Firefox
${URL}    http://thetestingworld.com/testings

*** Test Cases ***
Select Value from List
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    #Set Selenium Speed    2seconds
    Select From List By Index    name:sex    2         #Female
    Select From List By Value    name:country    82    #Germany

    