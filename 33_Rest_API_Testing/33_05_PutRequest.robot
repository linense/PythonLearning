*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_URL}    https://thetestingworldapi.com/


*** Test Cases ***
TC_005 Update resource
    Create Session    EditData    ${base_URL}
    &{body}=    Create Dictionary    id=1818  first_name=Testing  middle_name=8743913121  last_name=World  date_of_birth=12/12/1990
    &{header}=    Create Dictionary    Content-Type=application/json
    ${response}=    PUT On Session    EditData    /api/studentsDetails/1818    data=${body}    headers=${header}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    ${response1}=    Get Request    EditData    /api/studentsDetails/1818
    Log To Console    ${response1.content}
