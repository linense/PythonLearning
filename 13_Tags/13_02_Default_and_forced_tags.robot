*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources3.robot
Documentation   This Suite shows how to apply tags
Default Tags     DFLT    # will be applied if no tag is applied
Force Tags  ALL_TC  # will be applied to all test cases

*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Keyword Test Case
    [Tags]  Smoke   Regression
    [Documentation]     This is the first test case of the suite
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Log    ${Res}
    Input Text    name:fld_username    ${Res}
    Close Browser

Second Test Case
    # To be started with robot -i Sanity .\13_01_Tags_at_Testcases.robot so that only this test case is started
    [Tags]  Sanity  Regression
    [Documentation]     This is the second test case of the suite
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Select Radio Button     add_type    office
    Close Browser

Third Test Case
    # To be started with robot -i Sanity .\13_01_Tags_at_Testcases.robot so that only this test case is started
    # [Tags]  Sanity  Regression
    # This test case only has the default tag
    [Documentation]     This is the third test case of the suite
    ${Res}=    Start Browser and Maximize    ${URL}    ${Browser}
    Select Radio Button     add_type    office
    Close Browser