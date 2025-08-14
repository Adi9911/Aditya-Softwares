# Windows Deployment Guide for Aditya Softwares Website

This guide provides step-by-step instructions for deploying the Aditya Softwares website on Windows machines.

## Prerequisites

### System Requirements
- Windows 10 or Windows 11
- At least 4GB RAM
- 1GB free disk space
- Internet connection for initial setup

### Software Requirements
- Python 3.8 or higher
- Web browser (Chrome, Firefox, Edge)

## Installation Methods

### Method 1: Automated Installation (Easiest)

1. **Download the Project**
   - Extract the project files to a folder (e.g., `C:\aditya_softwares_enhanced\`)

2. **Run Setup**
   - Double-click `setup_windows.bat`
   - Wait for the installation to complete
   - You should see "Setup completed successfully!"

3. **Start the Website**
   - Double-click `run_windows.bat`
   - Wait for "Website is running!" message
   - Your default browser should open automatically

4. **Access the Website**
   - If browser doesn't open automatically, go to: `http://localhost:5000`

### Method 2: Manual Installation

1. **Install Python**
   - Download Python from https://python.org/downloads/
   - During installation, check "Add Python to PATH"
   - Verify installation: Open Command Prompt and type `python --version`

2. **Install Dependencies**
   ```cmd
   cd C:\path\to\aditya_softwares_enhanced
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```cmd
   python app.py
   ```

4. **Access the Website**
   - Open browser and go to `http://localhost:5000`

## Configuration

### Email Configuration

1. **Gmail Setup** (Recommended)
   - Enable 2-factor authentication on your Gmail account
   - Generate an App Password:
     - Go to Google Account settings
     - Security → 2-Step Verification → App passwords
     - Generate password for "Mail"

2. **Update Email Settings**
   - Open `app.py` in a text editor
   - Find the email configuration section:
   ```python
   EMAIL_USER = 'your-email@gmail.com'
   EMAIL_PASSWORD = 'your-app-password'
   RECIPIENT_EMAIL = 'your-email@gmail.com'
   ```
   - Replace with your actual email and app password

### YouTube Integration Setup

1. **Get YouTube API Key**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable "YouTube Data API v3"
   - Create credentials → API Key
   - Copy the API key

2. **Find Your Channel ID**
   - Go to your YouTube channel
   - Right-click → View page source
   - Search for "channelId" (Ctrl+F)
   - Copy the channel ID (starts with "UC")

3. **Update YouTube Settings**
   - Open `app.py` in a text editor
   - Find and update:
   ```python
   YOUTUBE_CHANNEL_ID = "YOUR_ACTUAL_CHANNEL_ID"
   YOUTUBE_API_KEY = "YOUR_ACTUAL_API_KEY"
   ```

## Running the Website

### Development Mode (For Testing)
```cmd
set FLASK_DEBUG=True
python app.py
```
- Enables auto-reload when files change
- Shows detailed error messages
- Access at `http://localhost:5000`

### Production Mode
```cmd
set FLASK_DEBUG=False
python app.py
```
- Uses Waitress WSGI server
- Better performance and security
- Access at `http://localhost:5000`

### Custom Port
```cmd
set PORT=8080
python app.py
```
- Runs on port 8080 instead of 5000
- Access at `http://localhost:8080`

## Troubleshooting

### Common Issues and Solutions

#### 1. "Python is not recognized"
**Problem**: Python not found in PATH
**Solution**:
- Reinstall Python with "Add to PATH" checked
- Or manually add Python to PATH:
  - Control Panel → System → Advanced → Environment Variables
  - Add Python installation directory to PATH

#### 2. "Port 5000 is already in use"
**Problem**: Another application is using port 5000
**Solutions**:
- Kill the process using port 5000:
  ```cmd
  netstat -ano | findstr :5000
  taskkill /PID [PID_NUMBER] /F
  ```
- Or use a different port:
  ```cmd
  set PORT=8080
  python app.py
  ```

#### 3. "Module not found" errors
**Problem**: Dependencies not installed
**Solution**:
```cmd
pip install -r requirements.txt
```

#### 4. Email not working
**Problem**: Email configuration issues
**Solutions**:
- Verify Gmail app password is correct
- Check if 2-factor authentication is enabled
- Ensure "Less secure app access" is enabled (if not using app password)

#### 5. Images not loading
**Problem**: Static files not found
**Solutions**:
- Ensure all files are in correct directories
- Check that `static/images/` folder contains all PNG files
- Restart the application

#### 6. YouTube videos not showing
**Problem**: YouTube API issues
**Solutions**:
- Verify API key is valid
- Check if YouTube Data API v3 is enabled
- Ensure channel ID is correct
- Check API quota limits

### Performance Issues

#### Slow Loading
- Check internet connection
- Restart the application
- Clear browser cache
- Use production mode instead of debug mode

#### High Memory Usage
- Close unnecessary applications
- Restart the application
- Check for memory leaks in custom code

## Security Best Practices

### For Production Use

1. **Change Secret Key**
   - Generate a new secret key
   - Update `SECRET_KEY` in `app.py`

2. **Environment Variables**
   - Store sensitive data in environment variables
   - Don't commit passwords to version control

3. **Firewall Configuration**
   - Only allow necessary ports
   - Consider using HTTPS in production

4. **Regular Updates**
   - Keep Python and dependencies updated
   - Monitor for security vulnerabilities

## Backup and Maintenance

### Regular Backups
- Backup the entire project folder
- Export email configurations
- Save YouTube API credentials securely

### Updates
- Check for Python updates monthly
- Update dependencies: `pip install -r requirements.txt --upgrade`
- Test thoroughly after updates

### Monitoring
- Check application logs regularly
- Monitor email delivery
- Verify YouTube integration functionality

## Advanced Configuration

### Custom Domain (Optional)
1. Purchase a domain name
2. Configure DNS to point to your server
3. Set up port forwarding on your router
4. Consider using a reverse proxy (nginx)

### SSL/HTTPS Setup
1. Obtain SSL certificate
2. Configure Flask for HTTPS
3. Update all links to use HTTPS

### Database Integration (Future Enhancement)
- Consider adding SQLite or PostgreSQL
- Store contact form submissions
- Track website analytics

## Support and Resources

### Getting Help
- Check this guide first
- Review error messages carefully
- Search online for specific error messages
- Contact technical support if needed

### Useful Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/)
- [YouTube API Documentation](https://developers.google.com/youtube/v3)

### Contact Information
- Email: singhaditya.singh22@gmail.com
- YouTube Channel: [Your Channel Link]

---

**Note**: This guide assumes basic computer literacy. If you're not comfortable with command line operations, consider asking for technical assistance during setup.

