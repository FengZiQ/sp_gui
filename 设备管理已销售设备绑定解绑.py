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


# 创建两个商户“已销售设备测试1”、“已销售设备测试2”
sh_id1, sh_id2 = precondition()


# 绑定设备
def bind_d_to_s():
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
    # 点击展开商户树
    tool.click_action(
        '//ul[@id="listTree"]/li/span',
        '商户树',
        response_time=5
    )
    # 点击商户“已销售设备测试1”
    tool.click_action(
        '//ul[@class="treemenu"]/li[1]/a',
        '已销售设备测试1'
    )
    # 点击设备绑定按钮
    tool.click_action(
        'addbtn',
        '设备绑定按钮',
        locator=By.ID
    )
    # 查询要绑定的设备
    tool.fill_action(
        'queryDeviceId',
        device_info[0]['serialNum'],
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 选中设备
    tool.click_action(
        '//table[@id="addDevicesTable"]/tbody/tr/td[1]/div/ins',
        '选择设备复选框'
    )
    # 点击确认绑定按钮
    tool.click_action(
        'addDeviceBtn',
        '确认绑定按钮',
        locator=By.CLASS_NAME
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言提示消息
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '已成功绑定1台设备',
        end='@结束@'
    )


# 解绑设备
def unbind_d_from_s():
    time.sleep(3)
    # 选择解绑设备
    tool.click_action(
        '//table[@id="merchantDevices"]/tbody/tr/td[1]/div/ins',
        '解绑设备复选框'
    )
    # 点击设备解绑按钮
    tool.click_action(
        'unwrap',
        '设备解绑按钮',
        locator=By.ID
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言提示消息
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备解绑成功',
        end='@结束@'
    )


if __name__ == "__main__":
    bind_d_to_s()
    unbind_d_from_s()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_merchant(sh_id1)
    del_merchant(sh_id2)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
