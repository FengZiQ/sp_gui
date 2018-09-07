# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：在“testSP_平台服务商”服务商下创建一个二级服务商“二级服务商for新增用户测试”
def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        ejf_id = add_merchant('二级服务商for新增用户测试', c_info[0]['id'], 1)
    except Exception as e:
        print(e)
    else:
        return ejf_id


ef_id = precondition()


# 添加二级服务商用户
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
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 点击添加用户按钮
    tool.click_action(
        'addbtn',
        '添加用户按钮',
        locator=By.ID
    )
    # 用户名输入框：ejf_user
    tool.fill_action(
        'username',
        'ejf_user',
        '用户名输入框',
        locator=By.ID
    )
    # 所属商户下拉列表：选择二级服务商for新增用户测试
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
        '//ul[@id="resultValue"]/li/ul/li[1]/a',
        '二级服务商for新增用户测试',
    )
    # 删除默认角色
    tool.click_action(
        '//span[@id="roleChooseResult"]/i',
        '默认角色图标'
    )
    # 角色下拉列表：选择“二级服务商”
    tool.click_action(
        'roleChooseResult',
        '角色下拉列表',
        locator=By.ID
    )
    # 点击角色树展开按钮
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[1]/span',
        '角色树展开按钮',
        response_time=1
    )
    tool.click_action(
        '//ul[@id="roleResultValue"]/li[1]/a',
        '二级服务商'
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


# 二级服务商账户登录SP平台
def user_login():
    time.sleep(3)
    # 点击退出图标
    tool.click_action(
        '//div[@class="topTitle"]/span[3]/span',
        '退出图标',
        response_time=5
    )
    # 用户名输入框：ejf_user
    tool.fill_action(
        'username',
        'ejf_user',
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
            '商户管理', '设备管理', '商户用户管理',
            '支付配置管理', '账单管理', '账单图表'
        ],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    add_user()
    user_login()
    tool.mark_status()
    tool.finished()
    # 清理环境：删除创建的用户、二级服务商、商户、门店、服务商
    try:
        del_sp_user(get_sp_user_info('ejf_user')[0]['id'])
    except Exception as e:
        print(e)
    del_merchant(ef_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
