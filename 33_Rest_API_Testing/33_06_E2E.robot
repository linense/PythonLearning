*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***

${base_URL}    https://thetestingworldapi.com/
${original_first_name}    Hello
${update_first_name}    Testing

*** Test Cases ***
TC_006_End_to_End_TestCase
    Create Session    E2E    ${base_URL}
    &{header}=    Create Dictionary    Content-Type=application/json
    &{body}=    Create Dictionary    first_name=${original_first_name}    middle_name=A    last_name=World    date_of_birth=12/12/1985
    ${post_response}=    POST On Session    api/studentsDetails    headers=${header}    data=${body}
    Log To Console    ${post_response.status_code}
