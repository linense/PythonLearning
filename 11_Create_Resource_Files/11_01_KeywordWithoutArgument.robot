*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources1.robot

*** Variables ***


*** Test Cases ***
Keyword Test Case
    Start Browser and Maximize
    Input Text    name:fld_username    HelloWorld