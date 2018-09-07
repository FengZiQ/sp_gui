# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def query_by_p_n():
    # 点击设备管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[2]',
        '设备管理标签'
    )
    # 点击未销售设备标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[2]/ul/li[1]',
        '未销售设备标签'
    )
    # 所属部门输入框：testSP_平台服务商
    tool.fill_action(
        'queryCustomerName',
        'testSP_平台服务商',
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
        '15',
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
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])