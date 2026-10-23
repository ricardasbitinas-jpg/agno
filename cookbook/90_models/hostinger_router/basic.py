"""
Hostinger Router Basic
======================

Cookbook example for Hostinger Router, OpenAILike model provider.
"""

import asyncio

from agno.agent import Agent
from agno.models.hostinger_router import HostingerRouter

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(model=HostingerRouter(id="gpt-5-mini"), markdown=True)

# You can also select the provider by string, which resolves to the same class:
# agent = Agent(model="hostinger-router:gpt-5-mini", markdown=True)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("Explain quantum computing in simple terms")

    # --- Sync + Streaming ---
    agent.print_response("Explain quantum computing in simple terms", stream=True)

    # --- Async and Async + Streaming ---
    # Both calls share one event loop, because the model caches its async client and that
    # client is bound to the loop it was created in.
    async def main():
        # --- Async ---
        await agent.aprint_response("Share a 2 sentence horror story")

        # --- Async + Streaming ---
        await agent.aprint_response(
            "Write a short poem about artificial intelligence",
            stream=True,
        )

    asyncio.run(main())
