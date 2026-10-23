# Hostinger Router Tests

### basic.py

**Status:** PASS

**Description:** Basic Hostinger Router model cookbook with `gpt-5-mini`, covering sync, streaming, async, and async streaming agent responses.

**Result:** All four responses returned against `https://router.hostinger.com/v1` (tested 2026-10-23).

---

### tool_use.py

**Status:** PASS

**Description:** Agent with `claude-sonnet-5` and `WebSearchTools()` covering sync, streaming, async, and async streaming tool calls.

**Result:** The model called `search_news` / `web_search` in all four runs and answered from the results. Some DuckDuckGo searches returned "No results found" (a search backend result, not a model error), and the model retried with other queries.

---

### structured_output.py

**Status:** PASS

**Description:** Agent with `gemini-3.5-flash` and `output_schema=MovieScript` prompted with "New York".

**Result:** Returned a valid `MovieScript` instance with every field populated.

---

### Unit tests

`libs/agno/tests/unit/models/test_hostinger_router.py`: 7 passed, without network access.
