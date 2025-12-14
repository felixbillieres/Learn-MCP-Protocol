# Instructions - Project 05

## Your mission

Create a tool with robust error handling and data validation.

## Steps to follow

1. **Create a `calculate_division` tool** that:
   - Takes two parameters: `dividend` (float) and `divisor` (float)
   - Also takes `ctx: Context`
   - Divides the dividend by the divisor

2. **Validations to implement**:
   - If `dividend` is None or not provided → `ctx.error()` + `raise ValueError("Dividend is required")`
   - If `divisor` is None or not provided → `ctx.error()` + `raise ValueError("Divisor is required")`
   - If `divisor == 0` → `ctx.error()` + `raise ValueError("Division by zero is impossible")`
   - If the result is infinite → `ctx.warning()` (but still return the result)

3. **Logging**:
   - At the start: `ctx.info()`: "Calculating {dividend} / {divisor}"
   - On success: `ctx.info()`: "Result: {result}"
   - On error: log with `ctx.error()` before raising the exception

4. **Returns**: a float (the division result)

## Hints

- Validate parameters **before** doing the calculation
- Use `math.isinf()` to check if the result is infinite
- Error messages must be clear and informative
- Always log with `ctx.error()` before raising an exception

## Test

Use `python test.py` to verify that:
- Validations work
- Errors are properly handled
- Messages are clear

## Expected result

- Normal division: returns the result
- Division by zero: raises ValueError with clear message
- Missing parameters: raises ValueError with clear message
- All cases are logged in the Context
