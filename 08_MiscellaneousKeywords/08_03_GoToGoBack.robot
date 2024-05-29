*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://www.thetestingworld.com

*** Test Cases ***
TC_08_03_01 Goto    # Change URL
    Open Browser    ${var1}    Firefox
    Go To    https://www.google.com
    Sleep    2 seconds
    Close Browser

TC_08_03_02 Go Back    # Go Back in the browser history
    Open Browser    ${var1}    Firefox
    Go To    https://www.google.com
    Sleep    2 seconds
    Go Back
    Sleep    2 seconds
    Close Browser

TC_08_03_03 Get Location    # Store URL in variable
    Open Browser    ${var1}    Firefox
    ${URL1}=    Get Location
    Log To Console    ${URL1}
    Go Back
    Go To    https://www.google.com
    ${URL1}=    Get Location
    Log To Console    ${URL1}
    Close All Browsers


