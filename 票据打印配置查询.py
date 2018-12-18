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
    # 配置名称输入框：查询配置2
    tool.fill_action(
        'configName',
        '查询配置1',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        '//div[@class="collect"]/span',
        'list count',
        '1',
        end='@结束@'
    )
    # 配置名称输入框：查询配置2
    tool.fill_action(
        'configName',
        '',
        '配置名称输入框',
        locator=By.ID
    )
    tool.fill_action(
        'customerName',
        'testSP_平台服务商',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        '//div[@class="collect"]/span',
        'list count',
        '1',
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


