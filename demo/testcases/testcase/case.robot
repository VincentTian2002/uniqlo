*** Settings ***
Library     demo.workflow.baseworkflow.BaseWorkFlow
Library     demo.workflow.baseworkflow.BaseWorkFlow
*** Test Cases ***
case1
    [Documentation]     add one product into cart and assert product details in cart.
    [Tags]  CART
    [Setup]  Get Test Data  test.properties
    Customer Open Uniqlo
    Customer Select Product
    Customer Edit Product Details