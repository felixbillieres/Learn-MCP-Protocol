from mcp.server.fastmcp import FastMCP, Context
from typing import Any, Set

# TODO: Crée le serveur avec support des subscriptions
mcp_server = FastMCP(
    "MonServeurSubscriptions",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
    # TODO: Ajoute capabilities={"resources": {"subscribe": True}}
)

# État de la resource status
status_content = {"status": "running", "uptime": 0}

# TODO: Gère les subscriptions (URI -> set de clients)
# subscriptions: dict[str, Set] = {}

# TODO: Implémente list_resources
@mcp_server.list_resources()
async def list_resources() -> list[dict[str, Any]]:
    """
    Liste les resources disponibles.
    """
    pass

# TODO: Implémente read_resource
@mcp_server.read_resource()
async def read_resource(uri: str) -> dict[str, Any]:
    """
    Lit une resource.
    """
    if uri == "status://app/current":
        return {
            "contents": [{
                "uri": uri,
                "mimeType": "application/json",
                "text": str(status_content)
            }]
        }
    raise ValueError(f"Resource not found: {uri}")

# TODO: Crée un outil pour modifier le status
@mcp_server.tool()
async def update_status(
    status: str,
    uptime: int,
    ctx: Context
) -> dict[str, Any]:
    """
    Met à jour le status de l'application et notifie les abonnés.

    Args:
        status: Nouveau status
        uptime: Nouveau uptime
        ctx: Context MCP

    Returns:
        Confirmation de la mise à jour
    """
    global status_content
    # TODO: Met à jour status_content
    # TODO: Notifie les abonnés avec ctx ou le serveur
    # Note: FastMCP peut avoir des limitations, l'important est le concept
    pass


def main():
    print("Mon serveur MCP avec subscriptions démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()