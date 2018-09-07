# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：
# 给“testSP_平台服务商”服务商创建商户“商户for新增用户测试”、门店“”门店for新增用户测试
# 给商户创建sh_user1、sh_user2用户，给门店创建md_user1、md_user2用户
def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        sh_id = add_merchant('商户for新增用户测试', c_info[0]['id'], 2)
        md_id = add_merchant('门店for新增用户测试', sh_id, 1)
    except Exception as e:
        print(e)
    else:
        return sh_id, md_id


s_id, m_id = precondition()
sh_user1 = add_sp_user(s_id, [60], 'sh_user1')
sh_user2 = add_sp_user(s_id, [60], 'sh_user2')
md_user1 = add_sp_user(m_id, [61], 'md_user1')
md_user2 = add_sp_user(m_id, [61], 'md_user2')


def query_user():
    # 点击商户用户管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[3]',
        '商户用户管理标签'
    )
    # 用户名输入框：sh_user1
    tool.fill_action(
        'queryUser',
        'sh_user1',
        '用户名输入框',
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
    # 用户名输入框：
    tool.fill_action(
        'queryUser',
        '',
        '用户名输入框',
        locator=By.ID
    )
    # 商户名称输入框：门店for新增用户测试
    tool.fill_action(
        'customerName',
        '门店for新增用户测试',
        '商户名称输入框',
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
        '2',
        end='@结束@',
        locator=By.CLASS_NAME
    )


if __name__ == "__main__":
    query_user()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_sp_user(sh_user1)
    del_sp_user(sh_user2)
    del_sp_user(md_user1)
    del_sp_user(md_user2)
    del_merchant(m_id)
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
