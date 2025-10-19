// Reno Family Events Web App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Update last updated time
    updateLastUpdatedTime();
    
    // Set up auto-refresh every 30 minutes
    setInterval(updateLastUpdatedTime, 30 * 60 * 1000);
});

function updateLastUpdatedTime() {
    const lastUpdatedElement = document.getElementById('lastUpdated');
    if (lastUpdatedElement) {
        const now = new Date();
        lastUpdatedElement.textContent = now.toLocaleString();
    }
}

function refreshEvents() {
    const modal = new bootstrap.Modal(document.getElementById('loadingModal'));
    modal.show();
    
    fetch('/api/refresh')
        .then(response => response.json())
        .then(data => {
            modal.hide();
            if (data.success) {
                showAlert('success', data.message);
                // Reload the page after a short delay
                setTimeout(() => {
                    window.location.reload();
                }, 2000);
            } else {
                showAlert('danger', data.message);
            }
        })
        .catch(error => {
            modal.hide();
            console.error('Error:', error);
            showAlert('danger', 'Error refreshing events. Please try again.');
        });
}

function showAlert(type, message) {
    const alertContainer = document.querySelector('main .container');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    
    const icon = type === 'success' ? 'check-circle' : 'exclamation-triangle';
    alert.innerHTML = `
        <i class="fas fa-${icon} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.insertBefore(alert, alertContainer.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    }, 5000);
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + R to refresh events
    if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
        e.preventDefault();
        refreshEvents();
    }
    
    // Number keys for timeframe navigation
    if (e.key >= '1' && e.key <= '4') {
        const timeframes = ['today', 'this_week', 'next_week', 'all'];
        const timeframe = timeframes[parseInt(e.key) - 1];
        if (timeframe) {
            window.location.href = `?timeframe=${timeframe}`;
        }
    }
});

// Add loading state to buttons
function setButtonLoading(button, loading = true) {
    if (loading) {
        button.disabled = true;
        button.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Loading...';
    } else {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-sync-alt me-1"></i>Refresh';
    }
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add click tracking for external links
document.querySelectorAll('a[target="_blank"]').forEach(link => {
    link.addEventListener('click', function() {
        // You could add analytics tracking here
        console.log('External link clicked:', this.href);
    });
});

// Add copy to clipboard functionality for event details
function copyEventDetails(eventElement) {
    const title = eventElement.querySelector('.card-title').textContent.trim();
    const time = eventElement.querySelector('.fa-clock')?.parentElement?.textContent.trim() || '';
    const location = eventElement.querySelector('.fa-map-marker-alt')?.parentElement?.textContent.trim() || '';
    const link = eventElement.querySelector('.card-title a')?.href || '';
    
    const details = `${title}\n${time}\n${location}\n${link}`;
    
    navigator.clipboard.writeText(details).then(() => {
        showAlert('success', 'Event details copied to clipboard!');
    }).catch(() => {
        showAlert('warning', 'Could not copy to clipboard. Please copy manually.');
    });
}

// Add share functionality
function shareEvent(eventElement) {
    const title = eventElement.querySelector('.card-title').textContent.trim();
    const link = eventElement.querySelector('.card-title a')?.href || '';
    
    if (navigator.share) {
        navigator.share({
            title: title,
            url: link
        }).catch(console.error);
    } else {
        // Fallback to copying link
        navigator.clipboard.writeText(link).then(() => {
            showAlert('success', 'Event link copied to clipboard!');
        }).catch(() => {
            showAlert('warning', 'Could not copy link. Please copy manually.');
        });
    }
}
