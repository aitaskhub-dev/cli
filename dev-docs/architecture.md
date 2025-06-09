# Architecture Overview

## Problem Statement

AI development tools like GitHub Copilot provide general coding assistance, but enterprises face specific challenges:

- **Complex internal guidelines** scattered across documentation
- **Compliance requirements** that developers struggle to locate  
- **Context overload** - too many rules reduce AI performance
- **Lack of task-specific optimization** for enterprise workflows

## Solution: Task-Specific AI Agent Platform

A CLI tool that creates, manages, and shares task-specific AI configurations for Cursor AI, enabling teams to build specialized AI agents for different development scenarios.

## Core Concept

Cursor AI behavior is controlled by two configuration types:
- **Rules** (`.cursor/rules/*.md`) - Prompt engineering for specific guidelines
- **MCP Servers** (`.cursor/mcp-server.json`) - Function tools for automation

Our platform manages these configurations as reusable, shareable "tasks."

## Architecture Components

### 1. CLI Core (`taskhub`)

```bash
taskhub init my-task          # Create new task structure
taskhub list                  # Show saved tasks
taskhub load my-task          # Import task to current project
taskhub unload my-task          # Unload my-task
taskhub release my-task       # github에 version까지 tagging
taskhub clone user/task-name  # Download from repository
```

**Task Structure:**
```
my-task/
├── rules/
│   └── guidelines.md
├── mcp-servers/
│   └── automation.py
└── README.md
```

### 2. MCP Integration

- Auto-launch MCP servers without manual configuration
- Leverage existing libraries (e.g., instant-mcp)
- Seamless integration with Cursor AI workflow

### 3. Web Marketplace

**Domain:** `taskhub.microwiseai.dev`

**Features:**
- GitHub OAuth authentication
- Task publishing and discovery
- Simple search functionality
- Download compressed task packages

**Stack:**
- Frontend: Storybook + Cloudflare Pages
- Backend: Cloudflare Workers
- Search: MongoDB (free tier)

## Implementation Strategy

### MVP Scope (2-day hackathon)

**Day 1:**
- CLI basic commands (init, load, export)
- MCP server auto-launching
- Simple web interface setup

**Day 2:**  
- Task marketplace integration
- Demo task creation
- End-to-end workflow demonstration

### Advanced Features (Future)

- Semantic versioning (`>=0.1.3`)
- Advanced search with filters
- Task collaboration and forking
- Enterprise deployment tools

## Demo Scenarios

### Scenario 1: Internal Guidelines
1. Load company compliance task: `taskhub load datev-compliance`
2. AI automatically applies internal guidelines to code
3. Generate compliance reports and documentation

### Scenario 2: Documentation Automation  
1. Switch to documentation task: `taskhub export doc-generator`
2. AI creates standardized project documentation
3. Maintains changelog and contribution guidelines

## Technical Dependencies

```yaml
# requirements.txt
cleo      # CLI framework (Poetry side project)
appdirs   # Cross-platform app directories
mcp       # Model Context Protocol
requests  # Web API communication
```

## Success Metrics

- **Developer Productivity:** Reduced time finding compliance requirements
- **Code Quality:** Consistent application of internal guidelines  
- **Knowledge Sharing:** Reusable AI configurations across teams
- **Scalability:** Easy onboarding of new compliance rules

## Key Differentiator

Unlike general-purpose AI tools, this platform creates **specialized AI experts** for specific enterprise contexts, ensuring both high performance and strict compliance.
