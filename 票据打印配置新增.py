# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def add_receipt_config():
    config_type = [
        '支付票据打印配置',
        '退款票据打印配置'
    ]
    values = [
        'orderNo',
        'transactionId',
        'time',
        'totalFee',
        'payFee',
        'discountFee',
        'deviceNo',
        'payType',
        'customerName'
    ]
    option = 8
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
    for ct in config_type:
        # 点击新增按钮
        tool.click_action(
            'addbtn',
            '新增按钮',
            locator=By.ID
        )
        # 配置名称输入框
        tool.fill_action(
            'configName',
            ct,
            '配置名称输入框',
            locator=By.ID
        )
        # 点击配置类型下拉列表
        tool.click_action(
            '//button[@data-id="configTypeSelector"]',
            '配置类型下拉列表',
            response_time=1
        )
        if ct == '支付票据打印配置':
            # 选择支付类型
            tool.click_action(
                '//form/div[2]/div/div/div/ul/li[1]',
                '支付类型',
                response_time=1
            )
        elif ct == '退款票据打印配置':
            # 选择退款类型
            tool.click_action(
                '//form/div[2]/div/div/div/ul/li[2]',
                '退款类型',
                response_time=1
            )
            option = 10
        for count in range(option):
            # 点击增加字段图标
            tool.click_action(
                '//form[@id="receiptPrintForm"]/div[5]/div',
                '增加字段图标',
                response_time=1
            )
        for i in range(len(values)):
            tool.click_action(
                '//table/tbody/tr['+str(i+2)+']/td[1]/select/option[@value="'+values[i]+'"]',
                '第'+str(i+2)+'行key选择'+values[i],
                response_time=1
            )
            tool.fill_action(
                '//table/tbody/tr[' + str(i + 2) + ']/td[2]/input',
                values[i],
                '第' + str(i + 2) + '行value填写框'
            )
        if ct == '退款票据打印配置':
            tool.click_action(
                '//table/tbody/tr[11]/td[1]/select/option[@value="refundFee"]',
                '第11行key选择refundFee',
                response_time=1
            )
            tool.fill_action(
                '//table/tbody/tr[11]/td[2]/input',
                '第11行value填写refundFee',
                '第11行value填写框'
            )
            tool.click_action(
                '//table/tbody/tr[12]/td[1]/select/option[@value="refundNo"]',
                '第12行key选择refundNo',
                response_time=1
            )
            tool.fill_action(
                '//table/tbody/tr[12]/td[2]/input',
                '第12行value填写refundNo',
                '第12行value填写框'
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
            '添加成功',
            end='@结束@',
            locator=By.CLASS_NAME
        )
        time.sleep(3)


if __name__ == '__main__':
    add_receipt_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    try:
        config_id1 = get_receipt_printer_config_info('支付票据打印配置').get('id')
        config_id2 = get_receipt_printer_config_info('退款票据打印配置').get('id')
        del_receipt_printer_config(config_id1)
        del_receipt_printer_config(config_id2)
    except:
        pass
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
