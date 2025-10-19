# Reno Family Events Web App

A beautiful, modern web interface for viewing family-friendly events in the Reno/Sparks area.

## Features

- 📅 **Event Display**: View events organized by date
- 🔍 **Time Filters**: Filter by Today, This Week, Next Week, or All Events
- 🔄 **Real-time Refresh**: Click refresh to get the latest events
- 📱 **Responsive Design**: Works great on desktop, tablet, and mobile
- 🎨 **Modern UI**: Clean, Bootstrap-based interface
- 🔗 **Direct Links**: Click events to visit the original source

## Quick Start

### Option 1: Use the Startup Script
```bash
./start_web_app.sh
```

### Option 2: Run Directly
```bash
python3 app.py
```

### Option 3: Run in Background
```bash
nohup python3 app.py > web_app.log 2>&1 &
```

## Access the App

Once started, open your browser to:
- **Local**: http://localhost:5000
- **Network**: http://YOUR_IP:5000 (accessible from other devices on your network)

## Features Overview

### Main Page
- **Event Cards**: Each event is displayed in a clean card format
- **Date Grouping**: Events are grouped by date for easy browsing
- **Source Tags**: See which source each event came from
- **Direct Links**: Click any event to visit the original page

### Time Filters
- **Today**: Events happening today
- **This Week**: Events in the next 7 days
- **Next Week**: Events 8-14 days from now
- **All Events**: All available events

### Refresh Function
- **Manual Refresh**: Click the "Refresh" button to collect new events
- **Real-time**: Shows loading modal while collecting
- **Success/Error**: Displays status messages

### About Page
- **Source List**: See all 20+ event sources
- **How It Works**: Explanation of the filtering system
- **Tips**: Helpful usage tips

## API Endpoints

The web app also provides API endpoints:

- `GET /api/events?timeframe=this_week` - Get events as JSON
- `GET /api/refresh` - Refresh events data
- `GET /` - Main web interface
- `GET /about` - About page

## Keyboard Shortcuts

- **Ctrl/Cmd + R**: Refresh events
- **1-4**: Quick timeframe switching (Today, This Week, Next Week, All)

## Customization

### Styling
Edit `static/css/style.css` to customize colors, fonts, and layout.

### Templates
Edit files in `templates/` to modify the HTML structure.

### JavaScript
Edit `static/js/app.js` to add new functionality.

## Troubleshooting

### App Won't Start
1. Check if Python 3 is installed: `python3 --version`
2. Check if Flask is installed: `python3 -c "import flask"`
3. Install Flask: `pip3 install flask`

### No Events Showing
1. Click the "Refresh" button to collect events
2. Check the agent's `.env` file configuration
3. Verify internet connection

### Port Already in Use
If port 5000 is busy, edit `app.py` and change the port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001
```

## Production Deployment

For production use, consider:

1. **Use a WSGI server** like Gunicorn:
   ```bash
   pip3 install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Set up a reverse proxy** with Nginx

3. **Use environment variables** for configuration

4. **Set up SSL/HTTPS** for secure connections

## Integration with Agent

The web app automatically:
- Reads events from the agent's database (`events_sent.json`)
- Uses the same event collection functions
- Respects the same filtering rules
- Updates when you refresh

## Support

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Ensure the agent's `.env` file is properly configured
4. Check that the events database file exists and is readable
