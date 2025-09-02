from contextlib import AsyncExitStack

import anyio
from agents import Agent
from agents.mcp import MCPServerStdio

from utils.llm_models import mistral_nemon_model

INSTRUCTIONS = (
    "You are a competitive intelligence agent. Given a company name or product keyword, "
    "search the web for the most recent and relevant updates (news, blog posts, press releases, social media)."
    "Produce a concise summary of notable developments in the last 7 days."
    "Include product launches, funding events, hiring trends, strategic partnerships, or controversies."
    "Summarize in 2-3 paragraphs (max 300 words). Do not include your own opinion. Avoid generic company descriptions."
)


async def search_agent() -> Agent:
    mcp_server = MCPServerStdio(
        params={"command": "uvx", "args": ["mcp-server-fetch"]},
        client_session_timeout_seconds=60,
    )
    await mcp_server.connect()
    return Agent(
        name="investigator",
        instructions=INSTRUCTIONS,
        model=mistral_nemon_model(),
        mcp_servers=[mcp_server],
    )
