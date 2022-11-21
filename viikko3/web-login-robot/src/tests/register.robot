*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Reset Application
    Set Username  kalle
    Set Password  kalle456
    Set Password_confirmation  kalle456
    Submit Credentials
    Ohtu Page Should Be Open

Register With Too Short Username And Valid Password
    Reset Application
    Set Username  k
    Set Password  kalle456
    Set Password_confirmation  kalle456
    Submit Credentials
    Registering Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Reset Application
    Set Username  kkhvkjgfv
    Set Password  k4
    Set Password_confirmation  k4
    Submit Credentials
    Registering Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Reset Application
    Set Username  kjhkjfkewg
    Set Password  kalle456
    Set Password_confirmation  khfgfr09
    Submit Credentials
    Registering Should Fail With Message  Passwords do not match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Press Logout
    Clock Button  Logout

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
