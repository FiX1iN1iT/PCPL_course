from behave import Given, When, Then
from main import solve_biquadrate_equation


@Given("main is ran")
def given_function(context):
    print("given func is ran")


@When("a = {a}, b = {b}, c = {c}")
def when_equation(context, a, b, c):
    context.result = len(solve_biquadrate_equation(int(a), int(b), int(c)))


@Then("we get {out} roots")
def then_result(context, out):
    assert(context.result == int(out))
