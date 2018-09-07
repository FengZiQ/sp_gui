# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        sh_id1 = add_merchant('查询测试1', c_info[0]['id'], 2)
        sh_id2 = add_merchant('查询测试2', c_info[0]['id'], 2)
    except Exception as e:
        print(e)
    else:
        return sh_id1, sh_id2


def query():
    # 前置条件：创建名为“查询测试1”、“查询测试2”的两个商户
    sh_id1, sh_id2 = precondition()

    # 客户全称输入框：查询测试1
    tool.fill_action(
        'merchantName',
        '查询测试1',
        '客户全称输入框',
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
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )

    tool.mark_status()
    tool.finished()
    # 清理环境
    del_merchant(sh_id1)
    del_merchant(sh_id2)


if __name__ == "__main__":
    query()
    # 清理环境
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])

