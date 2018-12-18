# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def query_receipt_config():
    # 前置条件：创建无开发能力服务商；创建一个票据打印配置
    add_receipt_printer_config('删除票据打印配置测试')
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
    # 点击删除图标
    tool.click_action(
        '//a[@title="刪除"]/i',
        '删除图标'
    )
    # 点击确认按钮
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
        '删除成功',
        end='@结束@',
        locator=By.CLASS_NAME
    )


if __name__ == '__main__':
    query_receipt_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    try:
        config_id = get_receipt_printer_config_info('删除票据打印配置测试').get('id')
        del_receipt_printer_config(config_id)
    except:
        pass
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])


