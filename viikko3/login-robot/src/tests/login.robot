*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Credentials
    Input Credentials  testi  testi
    Output Should Contain  Invalid username or password

Login With Nonexistent Password
    Input Credentials  testi  \
    Output Should Contain  Username and password are required

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
