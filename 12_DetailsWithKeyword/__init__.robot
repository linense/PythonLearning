# For chapter 12_06: A folder can be behave like a test suite


*** Settings ***
Suite Setup     Before Each Test Suite
Suite Teardown  After Each Test Suite

*** Variables ***


*** Keywords ***
Before Each Test Suite
    Log     Test Suite Started

After Each Test Suite
    Log     Test Suite Ended