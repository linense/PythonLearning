*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://reqres.in

*** Test Cases ***
TC_002 Validate Get Request with Parameters
    Create Session    Get_Param    ${base_url}
    &{param}=    Create Dictionary    page=2
    ${response}=    GET On Session    Get_Param    /api/users    params=${param}
    ${status_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200    
    ${jsonresponse}=    to json    ${response.content}
    @{name_list}=    Get Value From Json    ${jsonresponse}    data[0].first_name
    ${name}=    Get From List    ${name_list}    0
    Should Be Equal    ${name}    Michael
    #Log To Console    ${response.status_code}
    #Log To Console    ${response.content}