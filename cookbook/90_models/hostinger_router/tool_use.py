"""
Hostinger Router Tool Use
=========================

Cookbook example for Hostinger Router, OpenAILike model provider, with tools.
"""

import asyncio

from agno.agent import Agent
from agno.models.hostinger_router import HostingerRouter
from agno.tools.websearch import WebSearchTools

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(
    model=HostingerRouter(id="claude-sonnet-5"),
    tools=[WebSearchTools()],
    markdown=True,
)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("What's the latest news about AI?")

    # --- Sync + Streaming ---
    agent.print_response("What's the current weather in Tokyo?", stream=True)

    # --- Async and Async + Streaming ---
    # Both calls share one event loop, because the model caches its async client and that
    # client is bound to the loop it was created in.
    async def main():
        # --- Async ---
        await agent.aprint_response("What are the top stories on Hacker News today?")

        # --- Async + Streaming ---
        await agent.aprint_response(
            "Search for the latest developments in quantum computing and summarize them",
            stream=True,
        )

    asyncio.run(main())
