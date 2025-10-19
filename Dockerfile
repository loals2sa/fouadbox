FROM kalilinux/kali-rolling:latest

LABEL maintainer="Fouad Zulof <zalaffouad37@gmail.com>"
LABEL description="Fouad Box - Advanced Security Toolkit"
LABEL version="1.0.0"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV FOUADBOX_PATH=/opt/fouadbox

# Update and install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    curl \
    nano \
    vim \
    net-tools \
    iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /opt/fouadbox

# Copy project files
COPY . /opt/fouadbox/

# Install Python requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Make scripts executable
RUN chmod +x fouadbox.py install.py

# Create symbolic link
RUN ln -sf /opt/fouadbox/fouadbox.py /usr/local/bin/fouadbox

# Set default installation path
RUN echo "/opt/fouadbox-tools/" > /root/fouadboxpath.txt

# Expose common ports (if needed for tools)
EXPOSE 8080 8443 4444 5555

# Set entrypoint
ENTRYPOINT ["/bin/bash"]

# Default command
CMD ["--help"]
