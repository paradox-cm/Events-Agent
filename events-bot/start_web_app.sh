#!/bin/bash

# Reno Family Events Web App Startup Script

echo "🌐 Starting Reno Family Events Web App..."
echo "📱 The app will be available at: http://localhost:5000"
echo "🔄 Press Ctrl+C to stop the server"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "❌ Flask is not installed. Installing..."
    pip3 install flask
fi

# Start the web app
python3 app.py
