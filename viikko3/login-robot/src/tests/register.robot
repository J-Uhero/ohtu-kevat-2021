*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kaisa  kaisa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kaisa123
    Run Application
    Output Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kaisa  kais123
    Run Application
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaisa  kaisakai
    Run Application
    Output Should Contain  Password has to include numbers

***Keywords***
Create User And Input New
    Create User  kalle  kalle123
    Input New Command