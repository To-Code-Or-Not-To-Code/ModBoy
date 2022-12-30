# Wenevieve Gang
A entertainment discord bot. Also functions as a moderation bot. The name started as a meme name by my brother. 
Files for discord bot

Please don't mind all the pull requests that I made. I protected the master branch so I have to make them, well, I accidently enabled prevent admins from force committing. Anyways it's gone, and some other requests are just for getting used to github.

## How to self host

### Requirements
- This repo
- Python

### Step 1
Download or clone from this repo with one of the following commands. You could also download the ZIP file. If you had downloaded the ZIP file, extract it.
```
git clone https://github.com/To-Code-Or-Not-To-Code/Wenevieve-Gang.git
gh repo clone To-Code-Or-Not-To-Code/Wenevieve-Gang
git@github.com:To-Code-Or-Not-To-Code/Wenevieve-Gang.git
```
### Step 2
Navigate to the folder you just downloaded or extracted. After that create a file called secrets.env. After your finished, open it in any text editor.

You could use the following commands to create it.

In Windows:

```
cd <wherever-you-downloaded-it>
type nul > secrets.env
```

In Linux or Mac

```
cd <wherever-you-downloaded-it>
touch secrets.env
```

### Step 3
Navigate to https://www.discord.com/developers/applications/
Create a new applicaton, and name it whatever you want. Select the checkbox and select Create

### Step 4
Navigate to bot and create a new bot. Click yes on the confirmation modal.

### Step 5
Select reset token and confirm. Copy the token. After that, enable all intents.

### Step 6
Scroll down to Bot Permissions and select your permissions. Copy this integer and save it for later.

### Step 7
Navigate to OAuth2 and copy your client ID, save this for later

### Step 8
Put your client ID and permission integer into this URL. Go into the page.
https://discordapp.com/oauth2/authorize?client_id=<CLIENTID>&scope=bot&permissions=<PERMISSIONINT>

### Step 9
Invite your bot to your server

### Step 10
Hey, remember the token? You'll need it now. Go back into secrets.env and type:
```
token=<yourtoken>
```

### Step 11
Go back into your terminal in the folder and run:

In Windows:
```
pip install -r requirements.txt
```

In Linux and Mac
```
sudo pip3 install -r requirements.txt
```

### Step 12
Run main.py, and your done!
