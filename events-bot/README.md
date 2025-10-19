# Reno/Sparks Family Events Agent

An automated event-scouting agent that aggregates family and teen-friendly events for Reno, Sparks, Carson City, and Lake Tahoe areas.

## What It Does

- Scans 20+ local event sources daily
- Filters for family/teen-friendly events (excludes adult-only venues)
- Groups events by time windows: 0-3 days, 4-7 days, 8-14 days
- Sends daily email digest with event details
- Deduplicates events to avoid sending the same event twice

## Sources Included

### Core Sources
- Visit Carson City
- PBS Reno Kids Club  
- Lake Tahoe Travel

### Reno/Sparks Area
- This Is Reno
- Reno News & Review (RN&R)
- Reno Gazette Journal
- City of Reno (Special Events)
- City of Sparks
- Washoe County Library
- Nevada Moms
- Macaroni KID (Reno/Sparks)
- KUNR Community Calendar
- Reno Public Market
- The Discovery (Nevada Discovery Museum)
- Nevada Museum of Art

### Carson City
- Carson Now

### Lake Tahoe
- Visit Reno Tahoe
- Tahoe.com
- Visit Lake Tahoe

### Aggregators
- Eventbrite (with optional API token)
- Facebook Events (optional, requires API token)

## Setup

### 1. Install Dependencies
```bash
pip install beautifulsoup4 requests python-dateutil python-dotenv
```

### 2. Configure Environment
Edit `.env` file with your email settings:

```bash
# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.email@gmail.com
SMTP_PASSWORD=your_app_password
RECIPIENT=christopher.mena@icloud.com
SENDER_NAME=Reno Family Events Bot
```

**For Gmail users:** You'll need to generate an App Password:
1. Enable 2-Factor Authentication
2. Go to Google Account settings → Security → App passwords
3. Generate a password for "Mail"
4. Use that password (not your regular Gmail password)

### 3. Source Toggles
All sources are enabled by default. To disable a source, set its value to `0`:

```bash
SOURCE_VISIT_CARSON_CITY=0  # Disable Carson City events
SOURCE_RGJ=0                # Disable Reno Gazette Journal
```

### 4. Optional: Eventbrite API
To get more comprehensive Eventbrite results:
1. Get a personal OAuth token from Eventbrite
2. Add to `.env`: `EVENTBRITE_TOKEN=your_token_here`

### 5. Optional: Facebook Events
To include Facebook page events:
1. Generate a Facebook Graph API token with "events" read permission
2. Add to `.env`:
   ```bash
   FACEBOOK_ACCESS_TOKEN=your_token_here
   FACEBOOK_PAGE_IDS=page_id_1,page_id_2,page_id_3
   ```

## Running the Agent

### Manual Run
```bash
cd events-bot
python event_agent.py
```

### Expected Output
```
2024-01-15 10:30:00 INFO Collecting events from enabled sources...
2024-01-15 10:30:01 INFO Collecting from: Visit Carson City
2024-01-15 10:30:02 INFO Collecting from: PBS Reno Kids Club
...
2024-01-15 10:30:45 INFO New events: 12 (out of 45 relevant / 67 total)
2024-01-15 10:30:46 INFO Email sent; DB updated.
```

## Scheduling

### macOS/Linux: Cron
Add to crontab (`crontab -e`):
```bash
# Run daily at 7:00 AM Pacific Time
0 7 * * * /usr/bin/env python3 /ABSOLUTE/PATH/events-bot/event_agent.py >> /ABSOLUTE/PATH/events-bot/agent.log 2>&1
```

### macOS: LaunchAgent (Alternative)
Create `~/Library/LaunchAgents/com.reno.eventsbot.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.reno.eventsbot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/ABSOLUTE/PATH/events-bot/event_agent.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/ABSOLUTE/PATH/events-bot/agent.log</string>
    <key>StandardErrorPath</key>
    <string>/ABSOLUTE/PATH/events-bot/agent.log</string>
</dict>
</plist>
```

Load with: `launchctl load ~/Library/LaunchAgents/com.reno.eventsbot.plist`

## Files Created

- `event_agent.py` - Main script
- `.env` - Configuration (keep private!)
- `events_sent.json` - Event deduplication database (created automatically)
- `agent.log` - Log file (when scheduled)

## Troubleshooting

### No Events Found
- Check that sources are enabled in `.env`
- Verify internet connection
- Some sites may be temporarily down or have changed structure

### Email Not Sending
- Verify SMTP credentials in `.env`
- For Gmail, ensure you're using an App Password, not your regular password
- Check that 2FA is enabled on your Gmail account

### Permission Errors
- Ensure the script has write permissions in the events-bot directory
- Check that Python can access the internet (firewall/proxy settings)

## Notes

- The script respects website robots.txt and uses polite delays between requests
- Parsers are "best-effort" - some sites may change structure over time
- Events are filtered to exclude obvious adult-only venues
- The script only sends emails when new events are found
- All events are deduplicated by title and start date
