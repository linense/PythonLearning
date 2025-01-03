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
    ${response}=    Get Request    Get_Param    /api/users    params=${param}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}