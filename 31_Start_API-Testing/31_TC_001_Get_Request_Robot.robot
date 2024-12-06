*** Settings ***
Library    RequestsLibrary

*** Variables ***
${Base_URL}    https://thetestingworldapi.com/


*** Test Cases ***
TC_001_Get_Request
    Create Session    Get_Student_Details    ${Base_URL}
    ${response}=    GET On Session    Get_Student_Details    api/studentsDetails
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}