# Stacks Docs Development Makefile
# Helpful commands for working with the Stacks documentation repository

.PHONY: help lint lint-md spellcheck links format serve docker-build docker-run docker-stop setup env-setup info

help: ## Show this help message
	@echo "Stacks Docs Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Setup local tooling (optional)
	@echo "No local dependencies required. Use make lint or make serve."

lint: lint-md ## Run all lint checks

lint-md: ## Lint markdown files using markdownlint-cli
	@command -v npx >/dev/null 2>&1 || (echo "npx not found. Install Node.js." && exit 1)
	npx --yes markdownlint-cli '**/*.md' --ignore node_modules

spellcheck: ## Spellcheck markdown files (optional)
	@command -v npx >/dev/null 2>&1 || (echo "npx not found. Install Node.js." && exit 1)
	npx --yes cspell '**/*.md' --no-progress

links: ## Check markdown links (optional)
	@command -v npx >/dev/null 2>&1 || (echo "npx not found. Install Node.js." && exit 1)
	npx --yes markdown-link-check **/*.md -q

format: ## Format markdown files (optional)
	@command -v npx >/dev/null 2>&1 || (echo "npx not found. Install Node.js." && exit 1)
	npx --yes prettier --write "**/*.md"

serve: ## Serve the repository over a local static server
	@command -v python3 >/dev/null 2>&1 || (echo "python3 not found." && exit 1)
	python3 -m http.server 8000

docker-build: ## Build Docker image for linting
	docker build -t stacks-docs .

docker-run: ## Run markdown lint in Docker
	docker run --rm -v $$PWD:/app -w /app stacks-docs

docker-stop: ## No-op for local dev (placeholder)
	@echo "Nothing to stop."

env-setup: ## Create .env template
	@echo "Creating .env file..."
	@echo "# Stacks docs env" > .env
	@echo "DOCS_BASE_URL=http://localhost:8000" >> .env

info: ## Show project information
	@echo "Stacks Docs Repository"
	@echo "Content: Markdown documentation"