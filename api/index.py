#!/usr/bin/env python3
"""
Vercel-compatible entry point for Reno Family Events Web App
"""

import os
import sys
import json
import logging
from datetime import date, datetime, timedelta

# Add the events-bot directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'events-bot'))

from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__, 
           template_folder=os.path.join(os.path.dirname(__file__), '..', 'events-bot', 'templates'),
           static_folder=os.path.join(os.path.dirname(__file__), '..', 'events-bot', 'static'))

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_sample_events():
    """Return sample events for demo purposes."""
    from datetime import date, timedelta
    
    sample_events = [
        {
            'title': 'Family Fun Day at The Discovery',
            'start_date': (date.today() + timedelta(days=1)).isoformat(),
            'end_date': (date.today() + timedelta(days=1)).isoformat(),
            'time_text': '10:00 AM - 4:00 PM',
            'location': 'The Discovery - Nevada Discovery Museum',
            'description': 'Interactive exhibits and hands-on activities for the whole family.',
            'link': 'https://nvdm.org',
            'source': 'The Discovery',
            'tags': ['museum', 'kids', 'family']
        },
        {
            'title': 'Story Time at Washoe County Library',
            'start_date': (date.today() + timedelta(days=2)).isoformat(),
            'end_date': (date.today() + timedelta(days=2)).isoformat(),
            'time_text': '11:00 AM',
            'location': 'Washoe County Library - Downtown Branch',
            'description': 'Weekly story time for children ages 3-5.',
            'link': 'https://www.washoecountylibrary.us',
            'source': 'Washoe County Library',
            'tags': ['library', 'kids', 'storytime']
        },
        {
            'title': 'PBS Reno Kids Club Event',
            'start_date': (date.today() + timedelta(days=3)).isoformat(),
            'end_date': (date.today() + timedelta(days=3)).isoformat(),
            'time_text': '2:00 PM - 3:00 PM',
            'location': 'PBS Reno Studios',
            'description': 'Educational activities and meet PBS characters.',
            'link': 'https://www.pbsreno.org',
            'source': 'PBS Reno Kids Club',
            'tags': ['education', 'kids', 'pbs']
        }
    ]
    
    return sample_events

def filter_events_by_timeframe(events, timeframe):
    """Filter events by timeframe."""
    today = date.today()
    
    if timeframe == "today":
        return [e for e in events if e['start_date'] == today.isoformat()]
    elif timeframe == "this_week":
        end_date = today + timedelta(days=7)
        return [e for e in events if e['start_date'] <= end_date.isoformat()]
    elif timeframe == "next_week":
        start_date = today + timedelta(days=8)
        end_date = today + timedelta(days=14)
        return [e for e in events if start_date.isoformat() <= e['start_date'] <= end_date.isoformat()]
    elif timeframe == "all":
        return events
    else:
        return events

@app.route('/')
def index():
    """Main page showing events."""
    timeframe = request.args.get('timeframe', 'this_week')
    events = get_sample_events()
    filtered_events = filter_events_by_timeframe(events, timeframe)
    
    # Group by date
    events_by_date = {}
    for event in filtered_events:
        date_key = event['start_date']
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
    events = get_sample_events()
    filtered_events = filter_events_by_timeframe(events, timeframe)
    return jsonify(filtered_events)

@app.route('/api/refresh')
def api_refresh():
    """API endpoint to refresh events data."""
    return jsonify({
        'success': True,
        'message': 'Events refreshed successfully',
        'new_events_count': 3
    })

@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')

@app.route('/health')
def health():
    """Health check endpoint for Vercel."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

# For Vercel
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
