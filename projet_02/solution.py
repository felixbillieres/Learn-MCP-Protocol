from mcp.server.fastmcp import FastMCP

# Crée le serveur MCP (comme dans le projet 01)
mcp_server = FastMCP(
    "MonPremierServeur",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Ajoute le décorateur et crée l'outil dire_bonjour
# Cette fonction doit :
# - Prendre un paramètre 'nom' (str)
# - Retourner un message de salutation
# - Être async
# - Avoir une docstring
def dire_bonjour(nom: str) -> str:
    pass

# TODO: Ajoute le décorateur et crée l'outil calculer_somme
# Cette fonction doit :
# - Prendre deux paramètres 'a' et 'b' (int)
# - Retourner la somme (int)
# - Être async
# - Avoir une docstring
def calculer_somme(a: int, b: int) -> int:
    pass


def main():
    print("Mon serveur MCP avec outils démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()