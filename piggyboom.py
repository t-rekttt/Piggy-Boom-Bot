import requests, json, time
url = 'http://d2fd20abim5npz.cloudfront.net/planetpigth/m/'
login_url = url+'gameNew/login/'
play_url = url+'zhuanpan/play/'

def check(arr):
    if arr['_d']['ret']==0:
        return True
    else:
        return False
    
def steal(sid,data):
    try:
        data['id'] = sid
        steal_result = requests.post(url+'userweapon/steal/',data=data).json()
        if check(steal_result):
            return (steal_result)
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
def get_info(puid,data):
    try:
        data['puid'] = puid
        info = requests.post(url+'userplanet/get/',data=data).json()
        if check(info):
            return info
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
def get_frlist(data):
    try:
        flist = requests.post(url+'userfriend/list/',data=data)
        flist = flist.json()
        if check(flist):
            return flist['_d']
        else:
            return False
    except Exception as e:
        print(e)
        return False

def l(access_token):
    try:
        login = requests.post(login_url,data={'access_token':access_token, 'loginType':'1'}).json()
        if check(login):
            l_data = login['_d']
            return_code = l_data['ret']
            t = login['_t']
            return [l_data,t,l_data['name']]
        else:
            return [False]
    except Exception as e:
        print(e)
        return [False]

def s(data):
    try:
        p = requests.post(play_url,data=data)
        play = p.json()
        if check(play):
            p_data = play['_d']['data']
            reward_type = p_data['rewardType']
            tili = p_data['tili']
            return [p_data,reward_type,str(tili),data]
        else:
            return [False]
    except Exception as e:
        print(e)
        return [False]

def start(access_token):
    login = l(access_token)
    if login[0]:
        print "Logged in as "+login[2]
        while (1>0):           
            login = l(access_token)
            l_data = login[0]
            if not login[0]:
                break
            count_down = l_data['zhuanpan']['time']
            mtkey = l_data['mtkey']
            skey = l_data['skey']
            uid = l_data['uid']
            status = l_data['status']
            
            data = {
            '_mtkey':mtkey,
            '_skey':skey,
            '_uid':uid,
            '_version':'2.5.0',
            'time':time.time(),
            }
            
            if status == '':
                time.sleep(2)
                spin = s(data)
                if spin[0]:
                    print('Reward: '+spin[1]+'. Spin left: '+spin[2])
                else:
                    print('Out of spin, sleeping '+str(count_down))
                    time.sleep(count_down)
                    
            elif status == 'fire':
                print('Got '+status+', sleeping 10s')
                time.sleep(10)
            
            elif status == 'steal':
                fbpic = l_data['zhuanpan']['stealTarget']['fbpic']
                if fbpic != '':
                    target_id = fbpic.split('/')[3]
                    targets = l_data['stealTarget']
                    fr_list = get_frlist(data)                
                    target_uid = -1
                    for i in fr_list['list']:
                        if target_id == i['siteuid']:
                            target_uid = i['uid']
                    if target_uid != -1:
                        target_info = get_info(target_uid,data)
                        target_star = target_info['planet']['star']
                        for z in range(0,len(targets)):
                            if targets[z]['planet']['star']==target_star:
                                status = steal(z,data)
                    else:
                        status = steal(1,data)
                else:
                    status = steal(1,data)

                if status: 
                    if status['_d']['data']['king']=='true':
                        print('Found the king')
                    else:
                        print('Didn\'t got the king, sorry')
                else:
                    print('Steal error')
    else:
        print('Login error')

if __name__ == '__main__':
    f = open('token.txt')
    #token = raw_input('Token: ')
    token = f.read().strip('\n')
    f.close()
    while (1>0):
        start(token)
