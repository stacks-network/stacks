#!/usr/bin/env bash

# Stacks Docs Setup Script
# This script prepares a local environment for working with the docs repo

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info() {
  echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
  echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

print_info "Setting up stacks docs tooling..."

if ! command_exists npx; then
  print_warning "npx not found. Install Node.js to run lint/format tools."
else
  print_success "npx found. You can run: make lint"
fi

if ! command_exists python3; then
  print_warning "python3 not found. Install Python to serve docs locally."
else
  print_success "python3 found. You can run: make serve"
fi

if [[ ! -f ".env" ]]; then
  cat > .env << EOF
# Stacks docs env
DOCS_BASE_URL=http://localhost:8000
EOF
  print_success ".env created."
else
  print_info ".env already exists."
fi

print_success "Setup complete."
echo ""
print_info "Next steps:"
echo "  1. Lint markdown: make lint"
echo "  2. Serve docs: make serve"
echo "  3. Use Docker: docker-compose up --build"