# Use Node.js version 18 (slim version)
FROM node:18-slim

# Update package list and install essential build tools, Git, Make, Python 3, and update CA certificates
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    gcc \
    git \
    make \
    netcat-openbsd \
    python3 \
    python3-pymongo \
    python3-requests && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates && \
    ln -s /usr/bin/python3 /usr/bin/python

# Install global npm packages
RUN npm install -g @angular/cli typescript && \
    npm cache clean --force

# Create app directory
WORKDIR /app/

# Clone the project
RUN git clone https://github.com/feekosta/JSONSchemaDiscovery ./ && \
    git checkout 1.1.0

# Copy patches
COPY patches/ ./patches/

# Apply patches
RUN git apply patches/*

# Install project dependencies
RUN npm ci && \
    npm cache clean --force

# Build the application
RUN ["npm", "run", "build"]

# Run predev script
RUN ["npm", "run", "predev"]

# Copy scripts
COPY scripts/ ./scripts/

# Copy data
COPY data/ ./data/

# Run smoke test
RUN ["bash", "scripts/smoke.sh"]

# Set the command to run the application
CMD ["bash", "scripts/start.sh"]

# Expose port 3000
EXPOSE 3000
