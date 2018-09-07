# coding=utf-8
from spApiCondition import *


# 获取商户信息
def get_merchant_info(cus_name, p_id='', t_id=''):
    try:
        res = sp_session.get(
            sp_server + 'customer/pageList?operateType=sp&name='+cus_name+'&parentId='+str(p_id)+'&treeId'+str(t_id)
        )
        temp = json.loads(res.text)
        m_info = temp['data']['list']
    except Exception as e:
        print(e)
        print('获取服务商信息失败')
    else:
        return m_info


# 新增商户：type={1:'服务商',2:'商户',3:'门店'}
def add_merchant(name, p_id, tp):
    try:
        res = sp_session.post(
                sp_server + 'customer/add',
                json={
                    "parentId": str(p_id),
                    "abb": name,
                    "name": name,
                    "type": str(tp),
                    "contact": "测试账户",
                    "mobile": "0"*8,
                    "mail": "test@cn.com",
                    "address": "北京海淀",
                    "enableStatus": "1"
                }
            )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 商户门店设备绑定
def bind_device_to_mer(s_id, device_id_list=list):
    try:
        sp_session.post(
            sp_server + 'device/bind/edit',
            json={
                "deviceIdList": device_id_list,
                "customerId": str(s_id)
            }
        )
    except Exception as e:
        print(e)
        print('设备绑定失败')


# 商户门店解绑设备
def unbind_device_to_mer(device_id_list=list):
    try:
        sp_session.post(
            sp_server + 'device/unbind/edit',
            json={"deviceIdList": device_id_list}
        )
    except Exception as e:
        print(e)
        print('设备解绑失败')


# 删除商户
def del_merchant(m_id):
    try:
        sp_session.post(
            sp_server + 'customer/deletes',
            json=[int(m_id)]
        )
    except Exception as e:
        print(e)
        print('删除商户失败')


def test_data():
    try:
        # 创建服务商"testSP_平台服务商"，并销售15台设备
        new_customer('testSP_平台服务商')
        # 获取设备信息
        dev_info = get_unsold_device_info()
        # 获取服务商信息
        cus_info = customer_info('testSP_平台服务商')
        # 绑定设备
        bind_device(cus_info['id'], cus_info['treeId'], [d['id'] for d in dev_info])
    except Exception as e:
        print(e)
        print('创建测试数据失败！')
    else:
        return dev_info, cus_info


# 新增SP商户：roleIds={60:'商户',61:'门店',62:'二级服务商',71:'门店无退款权限',161:'退款管理员'}
def add_sp_user(c_id, r_id, name='testUser'):
    try:
        res = sp_session.post(
                sp_server + 'user/add?operateType=customer',
                json={
                    "username": name,
                    "password": "123456",
                    "passwordRepeat": "123456",
                    "enableStatus": "1",
                    "customerId": int(c_id),
                    "roleIds": r_id
                }
            )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 删除sp用户
def del_sp_user(u_id):
    try:
        sp_session.post(
            sp_server + 'user/deletes',
            json=[int(u_id)]
        )
    except Exception as e:
        print(e)


# 获取sp用户信息
def get_sp_user_info(username):
    try:
        res = sp_session.get(
            sp_server + 'user/pageList?operateType=merchant&userName='+username
        )
        temp = json.loads(res.text)
        user_info = temp['data']['list']
    except Exception as e:
        print(e)
        print('获取服务商信息失败')
    else:
        return user_info


device_info, customer_info = test_data()


if __name__ == "__main__":
    pass
    # print(add_sp_user(4302, [60], 'tester12'))


