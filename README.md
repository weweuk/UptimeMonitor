# Mini Uptime Monitor

A lightweight, zero-dependency Python script to monitor the uptime of your personal servers and services. It checks specific host/port combinations and logs the results into a local SQLite database for easy tracking of 30-day online rates.

## Features
- Port-level TCP ping to verify service availability.
- Persistent logging using built-in SQLite.
- Zero external dependencies (uses only Python standard libraries).

## Usage
1. Clone the repository.
2. Edit the `SERVICES` list in `monitor.py` to add your own endpoints.
3. Run the script:
   ```bash
   python3 monitor.py
