# Piggy-Boom-Bot
A bot for Piggy Boom game at https://apps.facebook.com/cos_th_pig/

# Requirements
- Python 2.7.x
- Python requests (Install it by running "pip install requests"

# How to use?
1. Clone this repo
2. Go to https://developers.facebook.com/tools/debug/accesstoken/?app_id=1707883516108963
3. Copy your app token, the one in the left of the "Debug" button
4. Paste your token into token.txt and save it off
5. Open bash/cmd and navigate to your repository folder
6. Execute "python piggyboom.py"
7. Enjoy

# How it works
- The bot will login to the app with your access token and spin automatically via HTTP requests.
- If you spin onto "Fire", the bot would wait 30 seconds for you to fire.
- If you spin onto "Steal", it would try to find out and steal the king automatically if that person is in your friendlist, else it would pick the middle one.
- When you're out of spinning turn, the bot would delay until the next cool-down and repeat all the steps above.
