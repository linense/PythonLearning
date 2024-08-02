*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://thetestingworld.com/testings

*** Test Cases ***
TC_10_04_01 Validate Text
    Open Browser    ${var1}    Chrome
    Maximize Browser Window
    Element Text Should Be    xpath://div[@id='tab-content1']/p    Register now and kick start your career as a Software Testing Pro!
    Element Should Contain    xpath://div[@id='tab-content1']/p    Software Testing
    Input Text    name:fld_username    Hello
    Close Browser

TC_10_04_02 Validate Title
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Title Should Be    Login & Sign Up Forms
    Close Browser

TC_10_04_03 Element enabled
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Element Should Be Enabled    name:fld_username
    Close Browser

TC_10_04_03 Element visible
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Element Should Be Visible    name:fld_username
    Close Browser

