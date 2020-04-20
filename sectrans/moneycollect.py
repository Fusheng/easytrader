import easytrader

user = easytrader.use('ht_client')

user.prepare(user='用户名', password='雪球、银河客户端为明文密码', comm_password='华泰通讯密码，其他券商不用')

user.balance

user.position

user.auto_ipo()

user.refresh()


