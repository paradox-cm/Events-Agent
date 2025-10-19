# Reno Family Events Agent

An automated event-scouting agent that aggregates family and teen-friendly events for Reno, Sparks, Carson City, and Lake Tahoe areas. The project includes both a command-line agent and a beautiful web interface.

## 🌟 Features

- **20+ Event Sources**: Scans local websites, museums, libraries, and community calendars
- **Family-Friendly Filtering**: Automatically excludes adult-only venues and activities
- **Web Interface**: Beautiful, responsive web app to browse events
- **Email Digest**: Daily email notifications with new events
- **Facebook Integration**: Optional Facebook events from local pages
- **Real-time Updates**: Refresh button to collect latest events
- **Smart Deduplication**: Prevents duplicate events across runs

## 📁 Project Structure

```
Events-Agent/
├── events-bot/                 # Main application directory
│   ├── event_agent.py         # Core event collection agent
│   ├── app.py                 # Flask web application
│   ├── .env                   # Configuration (not in git)
│   ├── templates/             # Web app HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── about.html
│   ├── static/                # Web app assets
│   │   ├── css/style.css
│   │   └── js/app.js
│   ├── start_web_app.sh       # Web app startup script
│   ├── README.md              # Detailed setup guide
│   ├── WEB_APP_README.md      # Web app documentation
│   └── FACEBOOK_PAGES_GUIDE.md # Facebook integration guide
├── Script.txt                 # Original agent script
├── env.txt                    # Environment template
└── README.md                  # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install beautifulsoup4 requests python-dateutil python-dotenv flask
```

### 2. Configure Environment
Copy the environment template and configure your settings:
```bash
cd events-bot
cp ../env.txt .env
# Edit .env with your email settings and preferences
```

### 3. Run the Agent
```bash
# Command line agent
python3 event_agent.py

# Web interface
python3 app.py
# Then open http://localhost:3001
```

## 📱 Web Interface

The web app provides a beautiful interface to browse events:

- **Event Cards**: Clean, organized display of all events
- **Time Filters**: Today, This Week, Next Week, All Events
- **Real-time Refresh**: Click to collect fresh events
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Direct Links**: Click events to visit original sources

### Access the Web App
```bash
cd events-bot
python3 app.py
```
Then open: http://localhost:3001

## 📧 Email Configuration

Configure your email settings in `events-bot/.env`:

```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.email@gmail.com
SMTP_PASSWORD=your_app_password
RECIPIENT=christopher.mena@icloud.com
SENDER_NAME=Reno Family Events Bot
```

**For Gmail users**: Generate an App Password in your Google Account settings.

## 📅 Event Sources

The agent scans 20+ local sources:

### Core Sources
- Visit Carson City
- PBS Reno Kids Club
- Lake Tahoe Travel

### Reno/Sparks Area
- This Is Reno
- Reno News & Review
- City of Reno
- City of Sparks
- Washoe County Library
- Nevada Moms
- Macaroni KID
- KUNR Community Calendar
- Reno Public Market

### Museums & Venues
- The Discovery (Nevada Discovery Museum)
- Nevada Museum of Art

### Lake Tahoe
- Visit Reno Tahoe
- Tahoe.com
- Visit Lake Tahoe

### Aggregators
- Eventbrite
- Facebook Events (optional)

## 🔧 Configuration

### Source Toggles
Enable/disable sources in `events-bot/.env`:
```bash
SOURCE_VISIT_CARSON_CITY=1
SOURCE_PBS_RENO=1
SOURCE_LAKE_TAHOE_TRAVEL=1
# ... etc
```

### Facebook Integration
Add your Facebook access token and page IDs:
```bash
FACEBOOK_ACCESS_TOKEN=your_token_here
FACEBOOK_PAGE_IDS=page_id_1,page_id_2,page_id_3
```

## 📅 Scheduling

### Daily Email Digest
Set up a cron job to run daily:
```bash
# Add to crontab (crontab -e)
0 7 * * * /usr/bin/env python3 /path/to/events-bot/event_agent.py
```

### macOS LaunchAgent
Create `~/Library/LaunchAgents/com.reno.eventsbot.plist` for daily runs.

## 🛠️ Development

### Running in Development
```bash
cd events-bot
python3 app.py  # Web app with debug mode
```

### API Endpoints
- `GET /` - Main web interface
- `GET /about` - About page
- `GET /api/events?timeframe=this_week` - Events as JSON
- `GET /api/refresh` - Refresh events data

## 📊 Event Filtering

Events are automatically filtered for family-friendliness:
- Excludes adult-only venues (bars, nightclubs, etc.)
- Includes general events unless clearly adult-only
- Focuses on events suitable for children and teenagers

## 🔍 Troubleshooting

### Common Issues
1. **No events showing**: Click "Refresh" button in web app
2. **Email not sending**: Check SMTP credentials in `.env`
3. **Port conflicts**: App automatically finds available ports
4. **Source errors**: Some sites may be temporarily down (normal)

### Logs
Check the console output for detailed logging of the collection process.

## 📄 License

This project is open source. Feel free to modify and adapt for your local area.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the detailed README files in `events-bot/`
3. Check console logs for error messages

---

**Built with ❤️ for the Reno/Sparks community**
