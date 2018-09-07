# coding=utf-8
from login_dm import login_api
from login_sp import login_sp_api
from configuration_file import config_data
import json
import random
import xlwt

dm_server = config_data['dmServer']
sp_server = config_data['spServer']
dm_session = login_api()
sp_session = login_sp_api()


# 在设备未销售列表中获得15台设备
def get_unsold_device_info():
    try:
        res = dm_session.get(
            dm_server + 'device/pageList?pageSize=15&baseType=2&modelType=4&func=unbindDevices'
        )
        temp0 = json.loads(res.text)
        unsold_d_info = temp0['data']['list']
        return unsold_d_info
    except Exception as e:
        print(e)
        print('获取未销售设备号失败')


# 传一个服务商的全称获取服务商的信息
def customer_info(customer_name):
    cus_info = {}
    try:
        res = dm_session.get(
            dm_server + 'customer/pageList?salesName=sadmin&pageIndex=1&pageSize=5&name=' + customer_name
        )
        temp0 = json.loads(res.text)
        temp1 = temp0['data']['list']
        cus_info = temp1[0]
    except Exception as e:
        print(e)
        print('获取服务商信息失败')

    return cus_info


# 创建一个服务商
def new_customer(customer_name, role_id=54, tp='1'):
    try:
        res = dm_session.post(
            dm_server + 'customer/add',
            json={
                "parentId": "-1",
                "name": customer_name,
                "abb": "for_testing" + str(random.randint(0, 100)),
                "token": "",
                "userName": "for_sp_test",
                "password": "123456",
                "contact": "测试账户",
                "mobile": "11111111111",
                "mail": "test@cn.com",
                "address": "北京海淀",
                "sales_id": "1087",
                "type": tp,
                "platform": "1",
                "locale": "CN",
                "enableStatus": "1",
                "roleIds": [role_id]
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except Exception as e:
        print(e)
        print('服务商信息新增失败')


# 删除一个服务商
def delete_customer(customer_id):
    try:
        dm_session.post(
            dm_server + 'customer/deletes',
            json=[int(customer_id)]
        )
    except Exception as e:
        print(e)
        print('删除服务商信息失败')


# 绑定设备，传服务商ID，服务商tree id，设备id组成的数组
def bind_device(customer_id, tree_id, device_id_list=list()):
    try:
        dm_session.post(
            dm_server + 'device/modify',
            json={
                "deviceIdList": device_id_list,
                "customerId": customer_id,
                "treeId": tree_id,
                "operateType": "bindCustomer"
            }
        )
    except Exception as e:
        print(e)
        print('解绑设备失败')


# 解绑设备
def unbind_device(device_id_list=list()):
    try:
        dm_session.post(
            dm_server + 'device/modify',
            json={
                "deviceIdList": device_id_list,
                "operateType": "unbindCustomer"
            }
        )
    except Exception as e:
        print(e)
        print('解绑设备失败')


# 生成一个用于批量上传的Excel文件
def upload_excel_file(device_no, file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    for i in range(len(device_no)):
        worksheet.write(i + 1, 0, device_no[i])
    workbook.save(file_name)


# 新增参数配置
def add_para_config(cus_id, is_default='1'):
    try:
        res = dm_session.post(
                dm_server + 'payChannelConfig/add',
                json={
                    "description": "selenium_test_SP平台",
                    "customerId": cus_id,
                    "isDefault": is_default,
                    "channelType": "2",
                    "fixationMoney": "1",
                    "signKey": "123456",
                    "queryOrderUrl": config_data['paydm_server']+"api/query/order",
                    "refundUrl": config_data['paydm_server']+"api/refund",
                    "cancelUrl": config_data['paydm_server']+"api/cancel/order",
                    "queryBillUrl": config_data['paydm_server']+"api/v2/billQuery",
                    "couponUrl": "",
                    "scannedPayUrl": config_data['paydm_server']+"api/scannedCode",
                    "generateOrderUrl": "",
                    "timeOut": "50"
                }
            )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 给非默认参数配置绑定设备
def bind_device_for_para_config(pay_channel_id, device_id, device_no):
    try:
        dm_session.post(
            dm_server + 'editDeviceBindChannel/modify',
            json={
                "payChannelId": pay_channel_id,
                "deviceIds": [device_id],
                "deviceNos": [device_no]
            }
        )
    except Exception as e:
        print(e)


# 参数配置下发
def para_config_issue(pc_id, cus_id, d_id=list, d_no=list):
    try:
        dm_session.post(
            dm_server + 'editDeviceUnBindChannel/modify',
            json={
                "payChannelId": str(pc_id),
                "deviceIds": d_id,
                "deviceNos": d_no,
                "operateType": "singleEdit",
                "customerId": str(cus_id)
            }
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    pass



