*** Settings ***

Library    SeleniumLibrary

*** Test Cases ***
TC_08_01 Set Timeout
    Open Browser    https://thetestingworld.com/testings    Firefox
    Maximize Browser Window
    Input Text    name:fld_username    Testing
    Input Text    name:fld_email    TestingworldIndia@gmail.com
    Input Text    name:fld_password    abcd
    Capture Page Screenshot    C:/Users/a315707/OneDrive - Deutsche Telekom AG/Schulungen/Programmierung/Python/PythonLearning/08_MiscellaneousKeywords/TC_08_01.png
    Close All Browsers    #closes all browsers that have been opened by the script
    