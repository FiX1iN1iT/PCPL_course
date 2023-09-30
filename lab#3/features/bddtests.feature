Feature: Testing biquadrate equation solution
  Scenario: Test 0 roots
    Given main is ran
    When a = 1, b = 0, c = 10
    Then we get 0 roots
  Scenario: Test 2 roots
    Given main is ran
    When a = 1, b = 0, c = -4
    Then we get 2 roots
  Scenario: Test 3 roots
    Given main is ran
    When a = -4, b = 16, c = 0
    Then we get 3 roots
  Scenario: Test 4 roots
    Given main is ran
    When a = 1, b = -13, c = 36
    Then we get 4 roots