from redis import Redis

# TODO: 初始化redis实例变量
cache = Redis(host='192.168.184.128', port=6379, password='ceshi1')

# TODO: 1.对字符串操作
print('对字符串操作.....')
cache.set(name='username', value='zhiliao')
print(cache.get('username'))
cache.delete('username')
cache.set(name='read_count', value=1)
cache.incr(name='read_count', amount=5)  # TODO: 递增5
cache.decr(name='read_count', amount=3)  # TODO: 递增3
print(cache.get('read_count'))

# TODO: 2.对列表的操作
print('对列表的操作....')
cache.lpush('languges', 'python')
cache.lpush('languges', 'javascript')
print(cache.lrange('languges', 0, -1))  # TODO: 读取列表所有数据

# TODO: 3.对集合的操作
print('对集合的操作....')
cache.sadd('teams', 'python')
cache.sadd('teams', 'javscript')
print(cache.smembers('teams'))

# TODO: 4.对哈希(hash)的操作
print('对哈希(hash)的操作....')
cache.hset(name='website', key='baidu', value='https://www.baidu.com')
cache.hset(name='website', key='google', value='https://www.google.com')
print(cache.hgetall('website'))

# TODO: 5.对事务(管道)操作
print('对事务(管道)操作....')
pip = cache.pipeline()  # TODO: 定义一个管道实例
pip.set(name='height', value=170)
pip.set(name='weight', value=120)
pip.execute()

# TODO: 6.发布与订阅功能
print('发布与订阅功能....')
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        if item.get('type') == 'message':
            print(item.get('data'))
