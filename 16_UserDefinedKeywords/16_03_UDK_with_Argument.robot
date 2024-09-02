*** Settings ***
#Test Setup  Start Browser and Maximize
Library    SeleniumLibrary
Documentation   This Suite uses User Defined Keywords in Python

Resource    ../Resources/Resources4.robot

*** Variables ***

*** Test Cases ***
Robot Create Folder
    Create Folder With Argument    Hello1234    Testing
