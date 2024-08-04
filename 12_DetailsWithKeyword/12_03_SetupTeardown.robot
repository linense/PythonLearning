*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resources4.robot
Documentation   This file uses Setup and Teardown functionality
Test Setup  Start Browser and Maximize
Test Teardown   Close Browser Window


*** Variables ***
${Browser}    Firefox
${URL}    http://www.thetestingworld.com/testings

*** Test Cases ***
Setup Test Case
    Input Text  name:fld_username   testings
    Input Text  name:fld_email  testingworldindia@gmail.com
    Input Text  name:fld_password   123456

Second Setup Test Case
    Select Radio Button     add_type    office