# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        s_id1 = add_merchant('已销售设备测试1', c_info[0]['id'], 2)
        s_id2 = add_merchant('已销售设备测试2', c_info[0]['id'], 2)
    except Exception as e:
        print(e)
    else:
        return s_id1, s_id2


# 创建两个商户“已销售设备测试1”、“已销售设备测试2”并分别绑定5台设备
sh_id1, sh_id2 = precondition()
bind_device_to_mer(sh_id1, [d['id'] for d in device_info][:5])
bind_device_to_mer(sh_id2, [d['id'] for d in device_info][5:10])


# 通过所属部门查询
def query_by_p_n():
    # 点击设备管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[2]',
        '设备管理标签'
    )
    # 点击已销售设备标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[2]/ul/li[2]',
        '已销售设备标签'
    )
    # 所属部门输入框：已销售设备测试1
    tool.fill_action(
        'queryCustomerName',
        '已销售设备测试1',
        '所属部门输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '5',
        end='@结束@',
        locator=By.CLASS_NAME
    )


# 通过设备编号查询
def query_by_device_no():
    # 设备编号输框输入要查询的设备编号
    tool.fill_action(
        'queryDeviceId',
        device_info[0]['serialNum'],
        '设备编号输框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )


if __name__ == "__main__":
    query_by_p_n()
    query_by_device_no()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device_to_mer([d['id'] for d in device_info][:10])
    del_merchant(sh_id1)
    del_merchant(sh_id2)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
