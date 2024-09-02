*** Settings ***
#Test Setup  Start Browser and Maximize
Library    SeleniumLibrary
Documentation   This Suite uses User Defined Keywords in Python

Resource    ../Resources/Resources4.robot

*** Variables ***

*** Test Cases ***
Robot Concatenate Values
    Concatenate Username and Password   myUser    myPassword
