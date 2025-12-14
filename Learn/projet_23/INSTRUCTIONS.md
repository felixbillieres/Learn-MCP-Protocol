# Instructions - Project 23

## Your mission

Create a server that uses roots to operate in authorized directories.

## Steps

1. **Request roots**: Use `ctx.roots.list()` to get available roots

2. **Create tools that respect roots**:
   - `list_files`: Lists files in authorized roots
   - `read_file`: Reads a file if it's in an authorized root

3. **Validate paths**: Checks that the requested path is within an authorized root
