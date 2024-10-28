*** Settings ***
Resource    ../Resources/Resources4.robot
Library    ../Resources/UserKeywords.py

*** Variables ***


*** Test Cases ***
Test Case in BDD Format
    Given Start Browser and Maximize
    When Create Folder With Argument    folder    subfolder
    Then Concatenate Username and Password    Testing    World