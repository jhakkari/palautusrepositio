*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  aaaaa  testi1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User
    Input New Command and Create User
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  testi1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  testik  t
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testik  qwertyui
    Output Should Contain  Only characters cannot be used as a password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  testi  testi56789