*** Settings ***
Library  SeleniumLibrary


*** Variables ***
# ${Browser}    Chrome
${URL}    https://www.mozilla.org/de/

*** Test Cases ***
TC_001 Browser Start Close
    Open Browser    ${URL}    Chrome
    Close Browser
