# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def modify_receipt_config():
    print_type = ['默认', '追加', '覆盖']
    # 前置条件
    add_receipt_printer_config('票据打印配置modifyTest')

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
    for i in range(len(print_type)):
        # 点击修改图标
        tool.click_action(
            '//a[@title="修改"]',
            '修改图标'
        )
        # 配置名称输入框
        tool.fill_action(
            'configName',
            '打印配置_' + print_type[i],
            '配置名称输入框',
            locator=By.ID
        )
        # 点击打印类型下拉列表
        tool.click_action(
            '//button[@data-id="printType"]',
            '打印类型下拉列表',
            response_time=1
        )
        # 打印类型选择
        tool.click_action(
            '//form/div[4]/div/div/div/ul/li['+str(i+1)+']',
            '打印类型',
            response_time=1
        )
        # 点击保存按钮
        tool.click_action(
            'saveBtn',
            '保存按钮',
            locator=By.CLASS_NAME,
            response_time=1
        )
        # 断言
        tool.equal_text_assert(
            'msValue',
            '消息提示',
            '修改成功',
            end='@结束@',
            locator=By.CLASS_NAME
        )
        time.sleep(3)


if __name__ == '__main__':
    modify_receipt_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    try:
        config_id = get_receipt_printer_config_info('打印配置_覆盖').get('id')
        del_receipt_printer_config(config_id)
    except:
        pass
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
