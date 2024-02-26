# Use stable-slim version of Debian
FROM debian:stable-slim AS latex

# Update package list and install LaTeX
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    latexmk \
    make \
    texlive-full && \
    rm -rf /var/lib/apt/lists/*

# Create latex directory
WORKDIR /report/

# Build the report
CMD ["make", "report"]
