FROM python:3.8

# Define username and home
ARG USERNAME=pprunty
ARG USERHOME=/home/trader

# Copy everything to $USERHOME
COPY --chown=$USERNAME:$USERNAME * $USERHOME/

# Change permissions on bash script
RUN chmod 775 $USERHOME/startup.sh

# Make time-zone Irish time
#ENV TZ=/usr/share/zoneinfo/US/Eastern

# Run environment
WORKDIR /home/trader

## Pip install requirements
RUN pip install -r requirements.txt

# Entrypoint
ENTRYPOINT ./startup.sh