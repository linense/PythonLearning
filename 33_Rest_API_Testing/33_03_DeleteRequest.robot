*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_URL}    https://thetestingworldapi.com/


*** Test Cases ***
TC_003 Validate Delete Request
    Create Session    AppAccess    ${base_URL}
    ${response}=    Delete Request    AppAccess    api/studentsDetails/28
    ${code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${code}    200
    ${jsonresponse}=    To Json    ${response.content}
    @{status_list}=    Get Value From Json    ${jsonresponse}    status
    ${status}=    Get From List   ${status_list}     0
    Should Be Equal    ${status}    false
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}