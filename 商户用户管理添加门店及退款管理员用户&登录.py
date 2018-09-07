# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：创建一个门店
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


# 添加用户
def add_user():
    # 点击商户用户管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[3]',
        '商户用户管理标签'
    )
    # 点击添加用户按钮
    tool.click_action(
        'addbtn',
        '添加用户按钮',
        locator=By.ID
    )
    # 用户名输入框：
    tool.fill_action(
        'username',
        'md_user',
        '用户名输入框',
        locator=By.ID
    )
    # 所属商户下拉列表：
    tool.click_action(
        'chooseResult',
        '所属商户下拉列表',
        locator=By.ID
    )
    # 点击展开商户树图标
    tool.click_action(
        '//ul[@id="resultValue"]/li/span',
        '展开商户树图标'
    )
    # 点击展开门店树图标
    tool.click_action(
        '//ul[@id="resultValue"]/li/ul/li/span',
        '展开门店树图标'
    )
    # 选择所属商户：门店for新增用户测试
    tool.click_action(
        '//ul[@id="resultValue"]/li/ul/li/ul/li/a',
        '门店for新增用户测试',
    )
    # 删除默认角色
    tool.click_action(
        '//span[@id="roleChooseResult"]/i',
        '角色下拉列表'
    )
    # 角色下拉列表：
    tool.click_action(
        'roleChooseResult',
        '角色下拉列表',
        locator=By.ID
    )
    # 点击角色树展开按钮
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[1]/span',
        '角色树展开按钮'
    )
    # 角色下拉列表：选择门店
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[1]/ul/li[2]/a',
        '门店'
    )
    # 角色下拉列表：
    tool.click_action(
        'roleChooseResult',
        '角色下拉列表',
        locator=By.ID
    )
    # 角色下拉列表：退款管理员
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[3]/a',
        '退款管理员'
    )
    # 密码输入框：123456
    tool.fill_action(
        'password',
        '123456',
        '密码输入框',
        locator=By.ID
    )
    # 确认密码输入框：123456
    tool.fill_action(
        'passwordRepeat',
        '123456',
        '确认密码输入框',
        locator=By.ID
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '已成功添加用户',
        end='@结束@'
    )


def user_login():
    time.sleep(3)
    # 点击退出图标
    tool.click_action(
        '//div[@class="topTitle"]/span[3]/span',
        '退出图标',
        response_time=5
    )
    # 用户名输入框：sh_user
    tool.fill_action(
        'username',
        'md_user',
        '用户名输入框',
        locator=By.ID
    )
    # 密码输入框：123456
    tool.fill_action(
        'password',
        '123456',
        '密码输入框',
        locator=By.ID
    )
    # 点击登录按钮
    tool.click_action(
        'loginSubmit',
        '登录按钮',
        locator=By.ID
    )
    time.sleep(5)
    # 断言
    tool.contained_text_assert(
        'leftNav',
        '菜单列表',
        [
            '账单管理', '支付汇总', '支付明细',
            '退款明细', '账单图表', '系统设置',
        ],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    add_user()
    user_login()
    tool.mark_status()
    tool.finished()
    # 清理环境
    try:
        del_sp_user(get_sp_user_info('md_user')[0]['id'])
    except:
        pass
    del_merchant(m_id)
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
