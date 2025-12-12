from mcp.server.fastmcp import FastMCP, Context

# TODO: Crée le serveur MCP
mcp_server = FastMCP(
    "MonServeurSampling",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True
)

# TODO: Crée l'outil poser_question
@mcp_server.tool()
async def poser_question(
    question: str,
    ctx: Context
) -> str:
    """
    Pose une question au LLM via sampling.
    
    Args:
        question: La question à poser
        ctx: Context MCP
        
    Returns:
        La réponse du LLM
    """
    # TODO: Utilise ctx.sampling.create_message() avec :
    # - messages: [{"role": "user", "content": {"type": "text", "text": question}}]
    # - max_tokens: 200 (optionnel)
    # 
    # La réponse a .content.text qui contient le texte
    
    # TODO: Retourne la réponse
    pass

# TODO: Crée l'outil generer_resume
@mcp_server.tool()
async def generer_resume(
    texte: str,
    ctx: Context
) -> str:
    """
    Génère un résumé d'un texte via le LLM.
    
    Args:
        texte: Le texte à résumer
        ctx: Context MCP
        
    Returns:
        Le résumé généré
    """
    # TODO: Utilise ctx.sampling.create_message() avec :
    # - messages: [{"role": "user", "content": {"type": "text", "text": f"Résume ce texte : {texte}"}}]
    # - system_prompt: "Tu es un assistant qui crée des résumés concis"
    # - max_tokens: 150
    
    # TODO: Retourne le résumé
    pass


def main():
    print("Mon serveur MCP avec sampling démarre !")
    print("URL: http://127.0.0.1:8000/mcp")
    mcp_server.run(transport="streamable-http")


if __name__ == "__main__":
    main()

