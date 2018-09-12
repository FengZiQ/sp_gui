# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 返回按钮
def return_button():
    # 点击添加客户按钮
    tool.click_action(
        'addbtn',
        '添加客户按钮',
        locator=By.ID
    )
    # 点击客户简称输入框
    tool.click_action(
        'abb',
        '客户简称输入框',
        locator=By.ID
    )
    # 客户类型：选择服务商
    tool.click_action(
        '//div[@id="userType"]/div[1]/ins',
        '服务商radio'
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '添加客户按钮',
        '添加客户',
        end='@结束@',
        locator=By.ID
    )


# 添加二级服务商和商户
def add_sub_pro_mer():
    for i in range(2):
        # 点击添加客户按钮
        tool.click_action(
            'addbtn',
            '添加客户按钮',
            locator=By.ID
        )
        if i == 0:
            # 客户简称输入框：test二级服务商
            tool.fill_action(
                'abb',
                'test二级服务商',
                '客户简称输入框',
                locator=By.ID
            )
            # 客户全称输入框：测试二级服务商
            tool.fill_action(
                'name',
                '测试二级服务商',
                '客户全称输入框',
                locator=By.ID
            )
            # 客户类型：选择服务商
            tool.click_action(
                '//div[@id="userType"]/div[1]/ins',
                '服务商radio'
            )
        elif i == 1:
            # 客户简称输入框：test商户
            tool.fill_action(
                'abb',
                'test商户',
                '客户简称输入框',
                locator=By.ID
            )
            # 客户全称输入框：test商户全称
            tool.fill_action(
                'name',
                'test商户全称',
                '客户全称输入框',
                locator=By.ID
            )
            # 客户类型：选择商户
            tool.click_action(
                '//div[@id="userType"]/div[2]/ins',
                '商户radio'
            )
        # 联系人输入框：测试
        tool.fill_action(
            'contact',
            '测试',
            '联系人输入框',
            locator=By.ID
        )
        # 电话输入框：8个0
        tool.fill_action(
            'mobile',
            '0'*8,
            '电话输入框',
            locator=By.ID
        )
        # 邮箱输入框：test@111232
        tool.fill_action(
            'mail',
            'test@111232',
            '邮箱输入框',
            locator=By.ID
        )
        # 地址输入框：test地址北京海淀
        tool.fill_action(
            'address',
            'test地址北京海淀',
            '地址输入框',
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
            '新增客户信息成功',
            end='@结束@'
        )
        time.sleep(3)


# 添加门店
def add_store():
    # 点击展开商户树
    tool.click_action(
        '//ul[@id="listTree"]/li/span',
        '商户树',
        response_time=5
    )
    # 点击商户“test商户”
    tool.click_action(
        '//ul[@class="treemenu"]/li[2]/a',
        'test商户'
    )
    # 点击添加客户按钮
    tool.click_action(
        'addbtn',
        '添加客户按钮',
        locator=By.ID
    )
    # 客户简称输入框：test门店
    tool.fill_action(
        'abb',
        'test门店',
        '客户简称输入框',
        locator=By.ID
    )
    # 客户全称输入框：test门店全称
    tool.fill_action(
        'name',
        'test门店全称',
        '客户全称输入框',
        locator=By.ID
    )
    # 客户类型：选择门店
    tool.click_action(
        '//div[@id="userType"]/div[2]/ins',
        '门店radio'
    )
    # 联系人输入框：测试
    tool.fill_action(
        'contact',
        '测试',
        '联系人输入框',
        locator=By.ID
    )
    # 电话输入框：8个0
    tool.fill_action(
        'mobile',
        '0' * 8,
        '电话输入框',
        locator=By.ID
    )
    # 邮箱输入框：test@111232
    tool.fill_action(
        'mail',
        'test@111232',
        '邮箱输入框',
        locator=By.ID
    )
    # 地址输入框：test地址北京海淀
    tool.fill_action(
        'address',
        'test地址北京海淀',
        '地址输入框',
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
        '新增客户信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    add_sub_pro_mer()
    add_store()
    tool.mark_status()
    tool.finished()
    # 清理环境
    c_info = get_merchant_info('testSP_平台服务商')
    sh_info = get_merchant_info('', c_info[0]['id'], c_info[0]['treeId'])
    md_info = get_merchant_info('', sh_info[1]['id'], sh_info[1]['treeId'])
    try:
        del_merchant(md_info[0]['id'])
    except:
        print('门店删除失败')
    try:
        del_merchant(sh_info[0]['id'])
    except:
        print('商户删除失败')
    try:
        del_merchant(sh_info[1]['id'])
    except:
        print('商户删除失败')
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
