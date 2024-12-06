*** Settings ***
Library    RequestsLibrary

*** Variables ***
${Base_URL}    https://thetestingworldapi.com/
${StudentID}    10508257

*** Test Cases ***
TC_001_Get_Request_Fetch_Student_Details_By_ID
    Create Session    Fetch_Data    ${Base_URL}
    ${response}=    GET On Session    Fetch_Data    api/studentsDetails/${StudentID}
    ${actual_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${actual_code}    200
    Log To Console    ${response.status_code}
    Log To Console    ${response.content} 