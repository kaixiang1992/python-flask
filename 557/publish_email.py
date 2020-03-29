from redis import Redis

# TODO: 初始化redis实例变量
cache = Redis(host='192.168.184.128', port=6379, password='ceshi1')

for x in range(5):
    cache.publish('email', '1058628890@qq.com')