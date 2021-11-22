*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kallekal
    Set Password Confirmation  kallekal
    Click Button  Register
    Register Should Fail With Message  Password has to include numbers

Login After Successful Registration
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Create User And Go To Login Page
    Set Username  kaisa
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

***Keywords***
Reset And Go To Register page
    Reset Application
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
