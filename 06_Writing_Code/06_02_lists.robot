*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***

*** Test Cases ***
TC_06_01 Variable Test
    @{List1}    Create List    Hello    22    23.23    World    Abcd1234
    ${list_length}    Get Length    ${List1}
    Log To Console    ${list_length}
    ${list_data}=    Get From List    ${List1}    3
    Log To Console    ${list_data}


*** Keywords ***