# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：创建一个商户
def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        sh_id = add_merchant('商户for新增用户测试', c_info[0]['id'], 2)
    except Exception as e:
        print(e)
    else:
        return sh_id


s_id = precondition()


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
        'r_m_user',
        '用户名输入框',
        locator=By.ID
    )
    # 所属商户下拉列表：
    tool.click_action(
        'chooseResult',
        '所属商户下拉列表',
        locator=By.ID
    )
    # 点击商户树展开按钮
    tool.click_action(
        '//ul[@id="resultValue"]/li[1]/span',
        '商户树展开按钮'
    )
    # 选择所属商户
    tool.click_action(
        '//ul[@id="resultValue"]/li/ul/li/a',
        '商户for新增用户测试',
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
    # 角色下拉列表：退款管理员
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[3]/a',
        '退款管理员'
    )
    # 删除默认角色
    tool.click_action(
        '//span[@id="roleChooseResult"]/i[1]',
        '角色下拉列表'
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
        'r_m_user',
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
        ['账单管理', '支付明细', '系统设置'],
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
        del_sp_user(get_sp_user_info('r_m_user')[0]['id'])
    except:
        pass
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
