# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        s_id = add_merchant('已销售设备测试1', c_info[0]['id'], 2)
    except Exception as e:
        print(e)
    else:
        return s_id


# 创建商户“已销售设备测试1”并绑定1台设备
sh_id = precondition()
bind_device_to_mer(sh_id, [device_info[0]['id']])


def set_alias():
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
    # 设备编号输框输入要操作的设备编号
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
    # 点击修改别名图标
    tool.click_action(
        '//table[@id="merchantDevices"]/tbody/tr[1]/td[5]/a/i',
        '修改别名图标'
    )
    # 点击取消按钮
    tool.click_action(
        'cancelButton',
        '取消按钮',
        locator=By.CLASS_NAME
    )
    # 点击修改别名图标
    tool.click_action(
        '//table[@id="merchantDevices"]/tbody/tr[1]/td[5]/a/i',
        '修改别名图标'
    )
    # 别名输入框：别名测试
    tool.fill_action(
        'alias',
        '别名测试',
        '别名输入框',
        locator=By.ID
    )
    # 点击确定按钮
    tool.click_action(
        'saveButton',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '别名编辑成功',
        end='@结束@'
    )


if __name__ == "__main__":
    set_alias()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device_to_mer([device_info[0]['id']])
    del_merchant(sh_id)
    unbind_device([device_info[0]['id']])
    delete_customer(customer_info['id'])
