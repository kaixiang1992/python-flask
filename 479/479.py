from sqlalchemy import create_engine

# TODO: 数据库配置
HOSTNAME = '127.0.0.1'
PORT = 3300
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root123'

# TODO: dialect+driver://username:password@host:port/database?charset=utf8
# TODO: 示例：mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME, port=PORT,
                                                                                        db=DATABASE)
print(DB_URI)

# TODO: 创建数据库引擎
engine = create_engine(DB_URI)

# TODO: 创建链接
con = engine.connect()
# TODO: 测试查询数据
result = con.execute('SELECT 1')
value = result.fetchone()
print(value)  # TODO: (1,)
