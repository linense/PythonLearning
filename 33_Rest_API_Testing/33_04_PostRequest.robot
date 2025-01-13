*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_URL}    https://thetestingworldapi.com/


*** Test Cases ***
TC_004 Create new resource
    Create Session    AddData    ${base_URL}
    &{body}=    Create Dictionary    first_name=Testing    middle_name=A    last_name=World    date_of_birth=12/12/1990
    ${response}=    Post Request    AddData    /api/studentsDetails    data=${body}
    Log To Console    message    ${response.status_code}
    Log To Console    message    ${response.content}