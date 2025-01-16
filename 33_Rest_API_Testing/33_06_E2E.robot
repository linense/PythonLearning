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
    # Post Request
    &{header}=    Create Dictionary    Content-Type=application/json
    &{body}=    Create Dictionary    first_name=${original_first_name}    middle_name=A    last_name=World    date_of_birth=12/12/1985
    ${post_response}=    POST On Session    E2E    api/studentsDetails    headers=${header}    data=${body}
    ${json_response}=    To Json     ${post_response.content}
    @{id_list}=    Get Value From Json    ${json_response}    id
    ${id}=    Get From List    @{id_list}    0
    Log To Console    ${post_response.status_code}
    Log To Console    ${post_response.content}
    # Put Request
    &{body1}=    Create Dictionary    id=${id}    first_name=${update_first_name}    middle_name=A    last_name=World    date_of_birth=12/12/1985
    ${put_response}=    PUT On Session    E2E    api/studentsDetails/${id}    headers=${header}    data=${body}
    Log To Console    ${post_response.content}
    Log To Console    ${post_response.status_code}
    # Get Request
    ${get_request}=    Get Request    E2E    api/studentsDetails/${id}
    ${json_response}=    To Json    ${get_request.content}
    Log To Console    ${json_response}
    @{Lfirst_name}    Get Value From Json    ${json_response}    json_path    data.first_name
    ${first_name}=    Get From List    ${Lfirst_name}    0
    Should Be Equal    ${first_name}    ${update_first_name} 
    # Delete Request
    ${delete_response}=    Delete Request    E2E    api/studentsDetails/${id}
    Log To Console    ${delete_response.status_code}
    Log To Console    ${delete_response.content}
    ${json_delete}=    To Json    ${delete_response.content}
    @{Message}=    Get Value From Json    ${json_delete}    status
    ${statusM}=    Get From List    ${Message}    0
    Should Be Equal    ${statusM}    true