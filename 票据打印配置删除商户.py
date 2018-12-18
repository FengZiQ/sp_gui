# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：创建无开发能力服务商；给改服务商创建一个商户；创建一个票据打印配置；将商户绑定在票据打印配置中
c_id = None
c_info = get_merchant_info('testSP_平台服务商')
add_receipt_printer_config('查询配置1')
sh_id1 = add_merchant('商户查询测试1', c_info[0]['id'], 2)
try:
    c_id = get_receipt_printer_config_info('查询配置1')['id']
    bind_device_from_receipt_config(c_id, [int(sh_id1)])
except:
    print('获取票据打印配置失败')


def query_receipt_config():
    # 点击支付配置管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]',
        '支付配置管理标签'
    )
    # 点击支付配置管理二级标签
    tool.click_action(
        '//a[@data-menucode="spReceiptPrint"]',
        '票据打印配置二级标签',
        response_time=5
    )
    # 点击列表图标
    tool.click_action(
        '//a[@title="列表"]/i',
        '列表图标'
    )
    # 商户名称输入框：商户查询测试1
    tool.fill_action(
        'customerName',
        '商户查询测试1',
        '商户名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 选择要删除的商户
    tool.click_action(
        '//table/tbody/tr/th[1]/div/ins',
        '全选复选框'
    )
    # 点击删除商户按钮
    tool.click_action(
        'batchDel',
        '删除商户按钮',
        locator=By.CLASS_NAME
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        'msValue',
        '消息提示',
        '删除商户成功',
        locator=By.CLASS_NAME
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table/tbody/tr/td',
        '查询结果',
        '暂无商户数据',
        end='@结束@'
    )


if __name__ == '__main__':
    query_receipt_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    try:
        config_id = get_receipt_printer_config_info('查询配置1').get('id')
        del_receipt_printer_config(config_id)
    except:
        pass
    del_merchant(sh_id1)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])


