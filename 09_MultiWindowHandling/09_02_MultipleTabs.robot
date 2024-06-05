** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://robotframework.org
*** Test Cases ***
TC_09_01_01 Open multiple browsers
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Click Element    //a[text()='robotic process automation (RPA)']
    # Abgebrochen wegen geänderter Webseite
