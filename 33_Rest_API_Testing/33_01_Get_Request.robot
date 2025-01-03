*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${App_Base_URL}    https://thetestingworldapi.com/
${StudentID}    10508257


*** Test Cases ***
TC_001_FetchStudentDetailsByID
    Create Session    FetchData    ${App_Base_URL}
    ${Response}=  Get Request    FetchData    api/studentsDetails/${StudentID}
    ${actual_code}=    Convert To String    ${Response.status_code}
    Should Be Equal    ${actual_code}    200
    ${json_res}=    To Json    ${Response.content}
    @{first_name_list}=    Get Value From Json     ${json_res}    data.first_name
    ${first_name}=    Get From List    ${first_name_list}    0
    Log To Console    ${first_name}