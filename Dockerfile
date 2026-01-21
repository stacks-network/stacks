# Stacks Docs Dockerfile
# Container for linting markdown files

FROM node:20-alpine

WORKDIR /app

RUN npm install -g markdownlint-cli@0.42.0 \
  && npm install -g cspell@8.18.0 \
  && npm install -g markdown-link-check@3.12.2 \
  && npm install -g prettier@3.3.3

COPY . ./

CMD ["markdownlint", "**/*.md", "--ignore", "node_modules"]