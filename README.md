# Piggy-Boom-Bot
A bot for Piggy Boom game at https://apps.facebook.com/cos_th_pig/

### VI:
# Yêu cầu hệ thống
- Python 2.7.x
- Python requests (Cài đặt qua pip bằng lệnh "pip install requests")

# Hướng dẫn sử dụng
1. Clone repo này
2. Vào trang https://developers.facebook.com/tools/debug/accesstoken/?app_id=1707883516108963
3. Copy token của app (bên trái nút "Debug")
4. Paste token vào file token.txt và lưu lại
5. Mở bash/cmd và di chuyển đến thư mục repo
6. Chạy lệnh "python piggyboom.py"
7. Tận hưởng :3

# Cách thức hoạt động
- Bot sẽ login vào app bằng access token của bạn và tự động spin qua HTTP requests.
- Nếu bạn spin vào ô "Fire", bot sẽ đợi bạn 30s để bắn.
- Nếu bạn spin vào ô "Steal", bot sẽ tự tìm king trong friendlist của bạn, nếu tìm không ra thì chọn bừa cái ở giữa (kiểu gì cũng được tiền mà :)) )
- Nếu bạn hết lượt quay thì bot sẽ đợi đến khi có thêm lượt và lặp lại những bước trên.

### EN:
# Requirements
- Python 2.7.x
- Python requests (Install it by running "pip install requests")

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
