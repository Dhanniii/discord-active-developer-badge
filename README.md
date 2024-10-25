# Discord Active Developer Badge Bot - Setup Guide

A step-by-step guide to setting up your Discord bot for earning the Active Developer Badge.

---

## Prerequisites

Before starting, make sure you have:

- **Python**: Version 3.8 or newer installed
- **Discord Account**: A registered Discord account
- **Discord Server**: A server with Community features enabled
- **Text Editor**: (VS Code recommended)

---

## Discord Server Setup

To prepare your server:

### 1. Enable Community Features

1. Open **Server Settings** in your Discord server.
2. Click on **Enable Community** and follow the setup steps:
   - Enable **Verification Level**
   - Enable **Explicit Media Content Filter**
   - Create **Rules** and **Community Updates** channels

### 2. Server Requirements

- The server must be a **Community Server**.
- You must have **Manage Server** permissions.
- Rules and community updates channels are required.

---

## Bot Creation

To create and configure your bot:

### 1. Create a Discord Application

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application**.
3. Give your application a name and save the changes.

### 2. Configure Bot Settings

1. In your application, go to the **Bot** section.
2. Click **Add Bot** to create a bot user for your application.
3. Enable the following bot settings:
   - ✅ **Presence Intent**
   - ✅ **Server Members Intent**
   - ✅ **Message Content Intent**
4. **Reset the Token** and save it securely.
5. Under **Bot Permissions**, enable:
   - ✅ **Send Messages**
   - ✅ **Embed Links**
   - ✅ **Use Slash Commands**

### 3. Create an Invite Link

1. Go to **OAuth2** > **URL Generator**.
2. Select the following scopes:
   - `bot`
   - `applications.commands`
3. Under **Permissions**, select:
   - ✅ **Send Messages**
   - ✅ **Embed Links**
   - ✅ **Use Slash Commands**
4. Copy the generated invite link.

### 4. Invite the Bot to Your Server

1. Open the invite link in a new browser tab.
2. Select the server you wish to add the bot to.
3. Click **Authorize** and complete the captcha.

---

## Getting the Badge

### Requirements

To be eligible for the Active Developer Badge:

- The bot must be in a **Community Server**.
- The server must have **Community features enabled**.
- You must run at least **one slash command**.
- Wait **24 hours** after running the command.

### Claiming the Badge

1. Wait **24 hours** after using the command.
2. Visit the **Active Developer Page**.
3. Click **Claim Badge**.
4. The badge should appear on your profile.

---

You are now ready to run your bot and begin using it for your Active Developer Badge!
