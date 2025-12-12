from mcp.server.fastmcp import FastMCP
from typing import Any, Optional

# TODO: Crée le serveur avec support des prompts ET resources
mcp_server = FastMCP(
    "MonServeurPromptsAvances",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"prompts": {}, "resources": {}}
)

# Resources
RESOURCES = {
    "doc://examples/code_sample": {
        "content": "def example_function():\n    return 'Hello, World!'"
    },
    "doc://guidelines/best_practices": {
        "content": "1. Use meaningful variable names\n2. Write docstrings\n3. Handle errors properly"
    }
}

# TODO: Implémente list_resources et read_resource
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """Liste les resources disponibles."""
    pass

@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """Lit une resource."""
    pass

# TODO: Crée list_prompts avec des prompts avancés
@mcp_server.list_prompts()
async def list_prompts() -> list[dict[str, Any]]:
    """Liste les prompts avancés."""
    pass

# TODO: Crée get_prompt avec messages multiples et resources
@mcp_server.get_prompt()
async def get_prompt(
    name: str,
    arguments: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
    """
    Récupère un prompt avancé.
    
    Pour tutorial : retourne plusieurs messages
    Pour code_analysis : inclut une référence à une resource
    """
    if arguments is None:
        arguments = {}
    
    # TODO: Implémente tutorial avec messages multiples
    # TODO: Implémente code_analysis avec référence à resource
    pass


def main():
    print("Mon serveur MCP avec prompts avancés démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

