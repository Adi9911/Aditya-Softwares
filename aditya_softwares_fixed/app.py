import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, send_from_directory, jsonify, flash, redirect, url_for
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.secret_key = os.getenv("SECRET_KEY", "W9xvZkL2sQf3pT7uXjYbA1cD9eFgHkLmNpQrStUvWxYz1234567890")

# Email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USER = 'singhaditya.singh22@gmail.com'
EMAIL_PASSWORD = 'cigq hdaw wjfw djbp'
RECIPIENT_EMAIL = 'singhaditya.singh22@gmail.com'

# YouTube Channel Configuration (Optional - only if you want to show your YouTube videos)
YOUTUBE_CHANNEL_ID = ""  # Add your YouTube channel ID here if you want YouTube integration
YOUTUBE_API_KEY = ""     # Add your YouTube API key here if you want YouTube integration

def send_email(subject, body, sender_email=None):
    """Send email notification"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        
        text = msg.as_string()
        server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

@app.route("/")
def home():
    if request.method == "HEAD":
        # Respond to HEAD requests with just headers
        return "", 200
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        email_subject = f"New Contact Form Submission - {subject}"
        email_body = f"""
        <html>
        <body>
            <h2>New Contact Form Submission</h2>
            <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Subject:</strong> {subject}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
            
            <hr>
            <p><em>This email was sent from the Aditya Softwares website contact form.</em></p>
        </body>
        </html>
        """
        
        email_sent = send_email(email_subject, email_body, email)
        
        if email_sent:
            flash('Thank you for your message! We will get back to you soon.', 'success')
        else:
            flash('There was an error sending your message. Please try again.', 'error')
        
        return render_template('contact.html', submitted=True, name=name, email=email, email_sent=email_sent)
    return render_template('contact.html', submitted=False)

@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        service = request.form['service']
        company = request.form.get('company', '')
        budget = request.form.get('budget', '')
        timeline = request.form.get('timeline', '')
        description = request.form.get('description', '')
        
        email_subject = f"New Project Enquiry - {service}"
        email_body = f"""
        <html>
        <body>
            <h2>New Project Enquiry</h2>
            <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <h3>Client Information:</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Mobile:</strong> {mobile}</p>
            <p><strong>Company:</strong> {company if company else 'Not provided'}</p>
            
            <h3>Project Details:</h3>
            <p><strong>Service Required:</strong> {service}</p>
            <p><strong>Budget Range:</strong> {budget if budget else 'Not specified'}</p>
            <p><strong>Timeline:</strong> {timeline if timeline else 'Not specified'}</p>
            
            <h3>Project Description:</h3>
            <p>{description if description else 'No description provided'}</p>
            
            <hr>
            <p><em>This email was sent from the Aditya Softwares website enquiry form.</em></p>
            <p><strong>Action Required:</strong> Please respond to the client within 24 hours.</p>
        </body>
        </html>
        """
        
        email_sent = send_email(email_subject, email_body, email)
        
        if email_sent:
            flash('Thank you for your enquiry! We will contact you within 24 hours.', 'success')
        else:
            flash('There was an error submitting your enquiry. Please try again.', 'error')
        
        return render_template('enquiry.html', submitted=True, name=name, mobile=mobile, email=email, service=service, email_sent=email_sent)
    return render_template('enquiry.html', submitted=False)

# YouTube Integration Routes
@app.route('/youtube')
def youtube_videos():
    return render_template('youtube.html')

@app.route('/api/youtube/videos')
def get_youtube_videos():
    """API endpoint to fetch YouTube videos"""
    # Sample videos data with real YouTube video IDs for demonstration
    sample_videos = [
        {
            "id": "dQw4w9WgXcQ",
            "title": "PC Hardware Troubleshooting Guide",
            "description": "Learn how to diagnose and fix common PC hardware issues step by step.",
            "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
            "url": "https://youtube.com/watch?v=dQw4w9WgXcQ"
        },
        {
            "id": "oHg5SJYRHA0", 
            "title": "Network Setup Tutorial",
            "description": "Complete guide to setting up a home or office network from scratch.",
            "thumbnail": "https://img.youtube.com/vi/oHg5SJYRHA0/maxresdefault.jpg",
            "url": "https://youtube.com/watch?v=oHg5SJYRHA0"
        },
        {
            "id": "iik25wqIuFo",
            "title": "CCTV Installation Tips",
            "description": "Professional tips for installing and configuring CCTV security cameras.",
            "thumbnail": "https://img.youtube.com/vi/iik25wqIuFo/maxresdefault.jpg", 
            "url": "https://youtube.com/watch?v=iik25wqIuFo"
        },
        {
            "id": "9bZkp7q19f0",
            "title": "Printer Setup and Troubleshooting",
            "description": "How to set up printers and solve common printing problems.",
            "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/maxresdefault.jpg",
            "url": "https://youtube.com/watch?v=9bZkp7q19f0"
        },
        {
            "id": "kJQP7kiw5Fk",
            "title": "Windows Installation Guide",
            "description": "Step-by-step Windows operating system installation tutorial.",
            "thumbnail": "https://img.youtube.com/vi/kJQP7kiw5Fk/maxresdefault.jpg",
            "url": "https://youtube.com/watch?v=kJQP7kiw5Fk"
        },
        {
            "id": "L_jWHffIx5E",
            "title": "Server Setup and Configuration",
            "description": "Complete guide to setting up and configuring servers for business use.",
            "thumbnail": "https://img.youtube.com/vi/L_jWHffIx5E/maxresdefault.jpg",
            "url": "https://youtube.com/watch?v=L_jWHffIx5E"
        }
    ]
    return jsonify(sample_videos)

@app.route('/api/youtube/upload', methods=['POST'])
def upload_video():
    """API endpoint for video upload functionality"""
    # This would handle video uploads to YouTube
    # For now, return a placeholder response
    return jsonify({
        "status": "success",
        "message": "Video upload functionality will be implemented with YouTube API integration",
        "note": "This requires YouTube Data API v3 setup and OAuth authentication"
    })

@app.route('/api/youtube/download', methods=['POST'])
def download_video():
    """API endpoint for video download functionality"""
    # This would handle video downloads
    # For now, return a placeholder response
    return jsonify({
        "status": "info",
        "message": "Video download functionality requires proper licensing and terms compliance",
        "note": "Please ensure you have permission to download the requested content"
    })

# Technical Support Routes
@app.route('/tech-support')
def tech_support():
    return render_template('tech_support.html')

@app.route('/tech-support/hardware')
def hardware_support():
    return render_template('hardware_support.html')

@app.route('/tech-support/software')
def software_support():
    return render_template('software_support.html')

@app.route('/tech-support/printers')
def printer_support():
    return render_template('printer_support.html')

@app.route('/tech-support/cctv')
def cctv_support():
    return render_template('cctv_support.html')

@app.route('/tech-support/servers')
def server_support():
    return render_template('server_support.html')

@app.route('/tech-support/windows')
def windows_support():
    return render_template('windows_support.html')

@app.route('/tech-support/ai-ml')
def ai_ml_support():
    return render_template('ai_ml_support.html')

@app.route('/tech-support/scanner')
def scanner_support():
    return render_template('scanner_support.html')

# Hardware Support Sub-routes
@app.route('/hardware-support/pc')
def pc_support():
    return render_template('pc_support.html')

@app.route('/hardware-support/laptop')
def laptop_support():
    return render_template('laptop_support.html')

@app.route('/hardware-support/pos-printer')
def pos_printer_support():
    return render_template('pos_printer_support.html')

@app.route('/hardware-support/balance-machine')
def balance_machine_support():
    return render_template('balance_machine_support.html')

# Network Support Sub-routes
@app.route('/network-support/router')
def router_support():
    return render_template('router_support.html')

@app.route('/network-support/switch')
def switch_support():
    return render_template('switch_support.html')

# Network Support Routes
@app.route('/network-support')
def network_support():
    return render_template('network_support.html')

# Static file routes
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # For Windows compatibility, use 0.0.0.0 to allow external access
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    if debug_mode:
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        serve(app, host='0.0.0.0', port=port)

