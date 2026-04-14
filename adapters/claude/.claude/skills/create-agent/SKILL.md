---
name: create-agent
description: Create a product-engineering agent using AgentDevFlow shared role files.
user-invocable: true
---

# create-agent

Supported types:

- team-lead
- product-manager
- architect
- engineer
- qa-engineer
- platform-sre
- pmo

Role mapping:

- `architect` -> `skills/shared/agents/architect.md`

The created agent must load its shared role file under `skills/shared/agents/` and the required source prompts under `prompts/`.

## Creation Rules

1. load the selected shared role file first
2. load the required source prompts
3. inject critical rules, responsibilities, required reading, and standard actions
4. do not create a generic fallback role for a gated delivery responsibility
5. `team-lead` is the human user themselves, not a separate agent
