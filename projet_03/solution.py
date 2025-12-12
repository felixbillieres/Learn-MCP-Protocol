from mcp.server.fastmcp import FastMCP

# TODO: Importe BaseModel et Field depuis pydantic

# Crée le serveur MCP
mcp_server = FastMCP(
    "MonPremierServeur",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée le modèle Message avec :
# - expediteur (str, obligatoire)
# - destinataire (str, obligatoire)
# - contenu (str, obligatoire)
# - priorite (str, optionnel, défaut "normale")
# Utilise Field() pour les descriptions
class Message:
    pass

# TODO: Crée le modèle MessageResponse avec :
# - message_id (int)
# - expediteur (str)
# - destinataire (str)
# - contenu (str)
# - priorite (str)
# - date_envoi (str)
class MessageResponse:
    pass

# TODO: Crée l'outil envoyer_message
# Prend un Message en paramètre
# Retourne un MessageResponse
# Génère un message_id aléatoire
# Ajoute la date d'envoi actuelle
@mcp_server.tool()
async def envoyer_message(message: Message) -> MessageResponse:
    """Envoie un message et retourne les informations complètes"""
    pass


def main():
    print("Mon serveur MCP avec modèles Pydantic démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()