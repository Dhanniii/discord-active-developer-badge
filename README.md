- Discord Active Developer Badge Bot - Setup Guide
- Before starting, make sure you have:

 - Python 3.8 or newer installed
- A Discord account
- A Discord server with Community features enabled
- A text editor (VS Code recommended)

- Discord Server Setup

* Enable Community Features:

* Go to your Discord server
* Click Server Settings > Enable Community
* Follow the setup steps:

* Enable verification level
* Enable explicit media content filter
* Create rules and community updates channels

* Server Requirements:
* Server must be a Community server
* You need to have "Manage Server" permissions
* Server must have rules and community updates channels

 - Bot Creation
* Create Application:
* Visit Discord Developer Portal
* Click "New Application"
* Name your application
* Save the changes

- Configure Bot Settings:
* Go to "Bot" section
* Click "Add Bot"
* Bot settings to enable:

✅ Presence Intent
✅ Server Members Intent
✅ Message Content Intent

* Reset Token and save it securely
* Under "Bot Permissions":

✅ Send Messages
✅ Embed Links
✅ Use Slash Commands

* Create Invite Link:
* Go to OAuth2 > URL Generator
* Select scopes:

* bot
* applications.commands

- Select permissions:
* Send Messages
* Embed Links
* Use Slash Commands

* Copy the generated URL

- Invite Bot:
* Open the generated URL in a new tab
* Select your server
* Click "Authorize"
* Complete the captcha
