# Hostinger Router Cookbook

This cookbook demonstrates how to use Hostinger Router with the Agno framework. Hostinger Router
is an OpenAI-compatible gateway to models from OpenAI, Anthropic, Google and others
(`https://router.hostinger.com/v1`).

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `HOSTINGER_ROUTER_API_KEY`

```shell
export HOSTINGER_ROUTER_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai ddgs agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/hostinger_router/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/hostinger_router/tool_use.py
```

### 6. Run Agent that returns structured output

```shell
python cookbook/90_models/hostinger_router/structured_output.py
```

## Model Ids

Model ids have no vendor prefix, for example `gpt-5-mini`, `claude-sonnet-5` and
`gemini-3.5-flash`. Some models also have regional variants with an `-eu` or `-us` suffix,
such as `gpt-5-mini-eu` or `claude-sonnet-5-eu`.

The default is `gpt-5-mini`. The examples use `gpt-5-mini` (basic), `claude-sonnet-5`
(tool use) and `gemini-3.5-flash` (structured output) to show that one key and one base URL
reach several vendors. `GET /v1/models` is public and lists the current models with their
context length, pricing and supported endpoints:

```shell
curl https://router.hostinger.com/v1/models
```

The router also serves `/v1/embeddings` (`text-embedding-3-small`, `text-embedding-3-large`
and regional variants), which works with `OpenAIEmbedder`:

```python
from os import getenv

from agno.knowledge.embedder.openai import OpenAIEmbedder

embedder = OpenAIEmbedder(
    id="text-embedding-3-small",
    base_url="https://router.hostinger.com/v1",
    api_key=getenv("HOSTINGER_ROUTER_API_KEY"),
)
```

## Resources & Support

### API Reference
- **Base URL**: `https://router.hostinger.com/v1`
- **Models Endpoint**: `https://router.hostinger.com/v1/models`
