#!/bin/bash

# Log folder
LOG_FILE="/Users/giorgio/Antigravity/Linkedin auto apply/Auto_job_applier_linkedIn/logs/daily_run.log"

echo "=== Starting Daily Run: $(date) ===" >> "$LOG_FILE"

# Navigate to the project directory
cd "/Users/giorgio/Antigravity/Linkedin auto apply/Auto_job_applier_linkedIn" || exit 1

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!" >> "$LOG_FILE"
    exit 1
fi

# Run the bot
# Assuming python3 is the correct interpreter. If using a venv, activate it here.
# source .venv/bin/activate
# Run for USA
echo "--- Running for USA ---" >> "$LOG_FILE"
/usr/bin/python3 runAiBot.py --location "United States" >> "$LOG_FILE" 2>&1

echo "--- Pausing between runs ---" >> "$LOG_FILE"
sleep 60

# Run for UK
echo "--- Running for UK ---" >> "$LOG_FILE"
/usr/bin/python3 runAiBot.py --location "United Kingdom" >> "$LOG_FILE" 2>&1

echo "=== Finished Daily Run: $(date) ===" >> "$LOG_FILE"
