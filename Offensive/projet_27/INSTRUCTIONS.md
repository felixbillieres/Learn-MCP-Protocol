# Instructions - Project 27 (Payload Manager)

## Your Mission

Create a payload manager with CRUD, validation, and intelligent selection.

## Steps to Follow

1. **Create Pydantic Models**:
   - `Payload`:
     - `id`: int
     - `name`: str
     - `type`: str (enum: "exploit", "shell", "shellcode")
     - `os`: str (enum: "linux", "windows", "macos")
     - `architecture`: str (enum: "x86", "x64", "arm")
     - `description`: str | None
     - `code`: str (the payload itself)
     - `tags`: List[str]

2. **Create CRUD tools**:
   - `create_payload`: Add a new payload
   - `list_payloads`: List with filters (type, os, architecture)
   - `get_payload`: Retrieve a payload by ID
   - `delete_payload`: Delete a payload

3. **Create `select_payload` tool** with elicitation:
   - Requests context (os, architecture, type)
   - Uses elicitation to confirm the choice
   - Returns the most suitable payload

4. **Create resource `payload://list`**:
   - Exposes all available payloads

5. **Validate data**:
   - Verifies that os/architecture are compatible
   - Validates code format

## Test

Use `python test.py` to verify CRUD and selection.
