*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_URL}    https://thetestingworldapi.com/


*** Test Cases ***
TC_004 Create new resource
    Create Session    AddData    ${base_URL}
    &{body}=    Create Dictionary    first_name=Testing  middle_name=A  last_name=World  date_of_birth=12/12/1990
    &{header}=    Create Dictionary    Content-Type=application/json
    ${response}=    POST On Session    AddData    /api/studentsDetails    data=${body}    headers=${header}
    ${code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${code}    201
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}