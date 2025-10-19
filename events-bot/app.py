#!/usr/bin/env python3
"""
Reno Family Events Web App
A simple Flask web interface to display events collected by the agent.
"""

import os
import json
from datetime import date, timedelta
from flask import Flask, render_template, jsonify, request
from event_agent import Event, EventDB, collect_events

app = Flask(__name__)

def get_events_data():
    """Get events data from the agent's database and live collection."""
    # Load existing events from database
    db_path = os.path.join(os.path.dirname(__file__), "events_sent.json")
    db = EventDB(db_path)
    
    # Also collect fresh events
    fresh_events = collect_events()
    
    # Combine and deduplicate
    all_events = db.events.copy()
    for event in fresh_events:
        if not db.has(event):
            all_events.append(event)
    
    return all_events

def filter_events_by_timeframe(events, timeframe):
    """Filter events by timeframe."""
    today = date.today()
    
    if timeframe == "today":
        return [e for e in events if e.start_date == today]
    elif timeframe == "this_week":
        end_date = today + timedelta(days=7)
        return [e for e in events if e.occurs_within(today, end_date)]
    elif timeframe == "next_week":
        start_date = today + timedelta(days=8)
        end_date = today + timedelta(days=14)
        return [e for e in events if e.occurs_within(start_date, end_date)]
    elif timeframe == "all":
        return events
    else:
        return events

@app.route('/')
def index():
    """Main page showing events."""
    timeframe = request.args.get('timeframe', 'this_week')
    events = get_events_data()
    filtered_events = filter_events_by_timeframe(events, timeframe)
    
    # Sort by start date
    filtered_events.sort(key=lambda x: x.start_date)
    
    # Group by date
    events_by_date = {}
    for event in filtered_events:
        date_key = event.start_date.strftime('%Y-%m-%d')
        if date_key not in events_by_date:
            events_by_date[date_key] = []
        events_by_date[date_key].append(event)
    
    return render_template('index.html', 
                         events_by_date=events_by_date,
                         current_timeframe=timeframe,
                         total_events=len(filtered_events))

@app.route('/api/events')
def api_events():
    """API endpoint to get events as JSON."""
    timeframe = request.args.get('timeframe', 'this_week')
    events = get_events_data()
    filtered_events = filter_events_by_timeframe(events, timeframe)
    
    # Convert to serializable format
    events_data = []
    for event in filtered_events:
        events_data.append({
            'title': event.title,
            'start_date': event.start_date.isoformat(),
            'end_date': event.end_date.isoformat(),
            'time_text': event.time_text,
            'location': event.location,
            'description': event.description,
            'link': event.link,
            'source': event.source,
            'tags': event.tags or []
        })
    
    return jsonify(events_data)

@app.route('/api/refresh')
def api_refresh():
    """API endpoint to refresh events data."""
    try:
        # Collect fresh events
        fresh_events = collect_events()
        
        # Save to database
        db_path = os.path.join(os.path.dirname(__file__), "events_sent.json")
        db = EventDB(db_path)
        db.add_all(fresh_events)
        db.save()
        
        return jsonify({
            'success': True,
            'message': f'Collected {len(fresh_events)} new events',
            'new_events_count': len(fresh_events)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error refreshing events: {str(e)}'
        }), 500

@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')

# For Vercel deployment
if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # Create static directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    print("🌐 Starting Reno Family Events Web App...")
    print("📱 Open your browser to: http://localhost:3001")
    print("🔄 Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=3001)

# For Vercel
app = app
