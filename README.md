# CelsiusToFahrenheitExceptionHandlingTests
A Python Exception Handling UnitTest Challenge

**Goal:**
----------
You will write  write a function titled, celsiusToFahrenheit() that...
* receives a number (celsius) - could be a string, float, or int
* calculates fahrenheit
* catches a ValueError if input cannot be converted to a number
  * If so, it will return -9999
* returns a floating point number (fahrenheit)

**Inputs:**
----------
* `celsiusToFahrenheit()` receives 1 input: an integer, float, or string (celsius)
* `celsiusToFahrenheit()` will try to convert the input to a float and *if it is unable to convert a string to a float, it will return -9999 to indicate there was an error*
* `celsiusToFahrenheit()` calculates area using the following formula: `area * 247.10538`

**Notes/Challenge Opportunity**
-------------
* Your function needs to check to make sure the inputs can be converted to a number
* Your function needs to handle incorrect input (e.g. strings that can't be converted to numbers)
* Your function will need to incorporate Exception Handling in addition to performing the expected function

**Examples:**
inputs => output/s
--------------------------------
* divisibilty:
  * 10 2 => "divides evenly"
  * 7 2 => "doesn't divide evenly"
  * 20 0 => "error"
  * "five" / "two" => "error"
* fahrenheitToCelsius:
  * "ten" => -9999
  * 212 => 100.0
  * 32 => 0.0
  * 5 => -15.0
* celsiusToFahrenheit:
  * "twenty" => -9999
  * 0 => 32.0
  * 100 => 212.0
  * 55 => 131.0
