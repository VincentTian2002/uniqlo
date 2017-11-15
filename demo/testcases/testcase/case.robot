*** Settings ***
Library     demo.workflow.baseworkflow.BaseWorkFlow
Library     demo.workflow.baseworkflow.BaseWorkFlow
*** Test Cases ***
case1
    [Documentation]     add one product into cart and assert product details in cart.
    [Tags]  CART
    [Setup]  Get Test Data  'abc'
    Open Uniqlo
    Select Product
