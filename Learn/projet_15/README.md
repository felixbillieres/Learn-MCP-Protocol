# Project 15: Elicitation with JSON schemas

## Objective

Learn to create detailed JSON schemas for elicitation, with validation and constraints.

## Concepts to learn

### JSON schemas for elicitation

Schemas allow you to precisely define the structure of requested data:
- Data types (string, number, boolean, enum)
- Constraints (minLength, maxLength, pattern, minimum, maximum)
- Formats (email, uri, date, date-time)
- Default values
- Required vs optional fields

### Schema structure

An elicitation schema is a JSON Schema object with:
- `type: "object"` for the root
- `properties`: Field definitions
- `required`: List of required fields

### Supported types

1. **String**: with minLength, maxLength, pattern, format
2. **Number/Integer**: with minimum, maximum
3. **Boolean**: true/false
4. **Enum**: list of possible values (with `enum` or `oneOf`)

## What you will create

In this project, you will create complex elicitation schemas with validation.

## Next steps

Read `INSTRUCTIONS.md` to see exactly what you need to do!
