*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources2.robot

*** Variables ***


*** Test Cases ***
Keyword Test Case
    Start Browser and Maximize    http://www.thetestingworld.com/testings    Firefox
    Input Text    name:fld_username    HelloWorld