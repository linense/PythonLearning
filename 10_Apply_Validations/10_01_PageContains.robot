* Settings ***
Library    SeleniumLibrary

*** Variables ***
${var1}    https://thetestingworld.com

*** Test Cases ***
TC_10_01_01 Check Open Browser
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Page Should Contain    VIDEOS
    Page Should Not Contain    VIDEOS11
    Click Element    xpath://a[text()='Quick Demo']
    Sleep    2 seconds
    Close Browser
TC_10_01_02 Should contain textfield
    Open Browser    ${var1}    Firefox
    Maximize Browser Window
    Click Element    xpath://a[text()='Quick Demo']
    Page Should Contain Textfield    name:wdform_1_element_first2
    Input Text    name:wdform_1_element_first2    Greg
    Close Browser

