*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***

*** Test Cases ***
TC_06_03_001 Test For Loop
    FOR    ${i}    IN RANGE    1    10
        log to console    ${i}
    END

TC_06_03_002 Print list values
    @{List1}    Create List    Hello    22    23.23    World    Abcd1234
    FOR    ${i}    IN    @{List1}
        Log To Console    ${i}
    END

*** Keywords ***