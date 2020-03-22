import memcache

mc = memcache.Client(['192.168.184.128:11211', '192.168.184.130:11211'], debug=True)

# TODO: 设置数据
# mc.set('username', 'zhiliao', time=60 * 5)
# mc.set_multi({'address': 'zhejianghangzhou', 'age': 20, 'country': 'china', 'job': 'IT developer', 'sex': 'man'},
#              time=60 * 5)


# TODO: 读取数据
# username = mc.get('username')
# address = mc.get('address')
# country = mc.get('country')
# print(username)  # TODO: zhiliao
# print(address)  # TODO: zhejianghangzhou
# print(country)  # TODO: china


# TODO: 删除数据
# mc.delete('username')
# username = mc.get('username')
# print(username)  # TODO: None

# TODO: 自增长
# mc.set('total', 1, time=60 * 5)
# TODO: 默认自增长1
# mc.incr('total', delta=5)
# print(mc.get('total'))  # TODO: 6

# TODO: 自减少，默认自减少1
mc.decr('total', delta=3)
print(mc.get('total'))  # TODO: 3
