#!/bin/bash

# Export Twilio secrets/read secrets from keyvault

## Check bank holiday
export TZ="/usr/share/zoneinfo/US/Eastern"

# Run script when market is open/about to open and it's not the weekend
date=$(date "+%Y-%m-%d %H:%M:%S")
now=$(date +%H%M | sed 's/^0*//')
hours=$(date +%H | sed 's/^0*//')
minutes=$(date +%M)
day=$(date +%u)

echo "$date: Entering Dockerfile entrypoint - startup.sh."

# Sleep if markets are not open, then start program

# Case. 1 - It is a Friday after 21:00 / 16:00
if [[ $day -eq 5 && now -gt 1600 ]]; then

  sleep_time=$((((24 - hours) * 60 - minutes) + ((24 * 60) * 2) + ((9 * 60) + 30)))
  echo "$date : Sleeping for $((sleep_time / 60)) hours and $((sleep_time % 60)) minutes"
  sleep $((sleep_time * 60))

# Case 2. - It is a Saturday
elif [[ $day -eq 6 ]]; then

  sleep_time=$((((24 - hours) * 60 - minutes) + (24 * 60) + ((9 * 60) + 30)))
  echo "$date : Sleeping for $((sleep_time / 60)) hours and $((sleep_time % 60)) minutes"
  sleep $((sleep_time * 60))

# Case 3. - It is a Sunday
elif [[ $day -eq 7 ]]; then

  sleep_time=$((((24 - hours) * 60 - minutes) + ((9 * 60) + 30)))
  echo "$date : Sleeping for $((sleep_time / 60)) hours and $((sleep_time % 60)) minutes"
  sleep $((sleep_time * 60))

# Case 4. - It is a Mon, Tues, Wed, Thu, or Friday and before 09:30
elif [[ $now -lt 930 && $day -lt 6 ]]; then

  sleep_time=$((((9 * 60) + 30) - ((hours * 60) + minutes)))
  echo "$date : Sleeping for $((sleep_time / 60)) hours and $((sleep_time % 60)) minutes"
  sleep $((sleep_time * 60))

# Case 5. It is a Mon, Tues, Wed or Thu after 16:00
elif [[ $now -gt 1600 && $day -lt 5 ]]; then
  sleep_time=$((((24 - hours) * 60 - minutes) + ((9 * 60) + 30)))
  echo "$date : Sleeping for $((sleep_time / 60)) hours and $((sleep_time % 60)) minutes"
  sleep $((sleep_time * 60))
fi

# todo: check bank holidays

echo "$date: Beginning program..."

python3 main.py
