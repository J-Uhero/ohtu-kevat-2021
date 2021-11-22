*** Settings ***
Resource resource.robot

***Keywords***
Go To Register Page
    Go To  ${REGISTER URL}

Register Page Should Be Open
    Title Should Be  Register