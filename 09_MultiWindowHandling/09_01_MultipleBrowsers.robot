** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://www.thetestingworld.com/
${var2}    https:/www.google.com

*** Test Cases ***
TC_09_01_01 Open multiple browsers
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Open Browser    ${var2}    Firefox
    Maximize Browser Window
    Switch Browser    1
    ${url1}=    Get Location
    Log To Console    URL of first browser ${url1}
    Switch Browser    2
    ${url2}=    Get Location
    Log To Console    URL of second browser ${url2}

    Close All Browsers    