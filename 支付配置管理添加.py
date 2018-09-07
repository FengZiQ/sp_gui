# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：
# 给“testSP_平台服务商”服务商创建商户“商户for新增用户测试”、门店“门店for新增用户测试”

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


# 服务商添加支付配置：微信、支付宝
def provider_add_config():
    # 点击支付配置管理标签(一级)
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]',
        '支付配置管理标签(一级)'
    )
    # 点击支付配置管理标签(二级)
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]/ul/li[1]',
        '支付配置管理标签(二级)'
    )
    # 点击微信按钮
    tool.click_action(
        'wxPayBtn',
        '微信按钮',
        locator=By.ID
    )
    # 微信配置名称输入框：微信配置test1
    tool.fill_action(
        'wxConfigName',
        '微信配置test1',
        '微信配置名称输入框',
        locator=By.ID
    )
    # 配置类型单选radio：服务商商户
    tool.click_action(
        '//form[@id="wxpayConfigForm"]/div[2]/div/label[1]',
        '配置类型单选radio'
    )
    # 公共账号AppID输入框：AppID测试1
    tool.fill_action(
        'wxappId',
        'AppID测试1',
        '公共账号AppID输入框',
        locator=By.ID
    )
    # 公共账号应用秘钥输入框：
    tool.fill_action(
        'wxappSecret',
        'test1公共账号应用秘钥',
        '公共账号应用秘钥输入框',
        locator=By.ID
    )
    # 微信商户号输入框：test1微信商户号
    tool.fill_action(
        'wxmchNum',
        'test1微信商户号',
        '微信商户号输入框',
        locator=By.ID
    )
    # 微信商户API秘钥输入框：test1微信商户API秘钥
    tool.fill_action(
        'wxappidKey',
        'test1微信商户API秘钥',
        '微信商户API秘钥输入框',
        locator=By.ID
    )
    # 证书选择框：选择wx.p12文件
    tool.fill_action(
        'file',
        config_data['file_path'] + 'wx.p12',
        '证书选择框',
        locator=By.ID
    )
    # 点击上传图标
    tool.click_action(
        '//button[@title="Upload file"]',
        '上传图标',
        response_time=10
    )
    # 点击确认修改按钮
    tool.click_action(
        'saveConfigBtn',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增微信支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击支付宝/口碑按钮
    tool.click_action(
        'aliPayBtn',
        '支付宝/口碑按钮',
        locator=By.ID
    )
    # 配置类型radio：选择服务商ISV账号
    tool.click_action(
        '//form[@id="alipayConfigForm"]/div[1]/div/label[1]',
        '配置类型radio'
    )
    # 签名类型radio：选择SHA256withRsa
    tool.click_action(
        '//div[@id="aliParent"]/div[1]/div/label[2]',
        '签名类型radio'
    )
    # 支付宝配置名称输入框：test1支付宝配置
    tool.fill_action(
        'aliConfigName',
        'test1支付宝配置',
        '支付宝配置名称输入框',
        locator=By.ID
    )
    # 支付宝AppID输入框：AppID测试1
    tool.fill_action(
        'aliappId',
        'AppID测试1',
        '支付宝AppID输入框',
        locator=By.ID
    )
    # 合作者身份ID输入框：合作者身份ID测试1
    tool.fill_action(
        'aliPartner',
        'AppID测试1',
        '合作者身份ID测试1',
        locator=By.ID
    )
    # 订单有效时间输入框：1
    tool.fill_action(
        'alitimeExpress',
        '1',
        '订单有效时间输入框',
        locator=By.ID
    )
    # 应用私钥输入框：STzaW*100
    tool.fill_action(
        'alipayPrivateKey',
        'STzaW'*100,
        '应用私钥输入框',
        locator=By.ID
    )
    # 支付宝公钥输入框：STzaW*100
    tool.fill_action(
        'alipayPublicKey',
        'STzaW'*100,
        '支付宝公钥输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        'saveConfigBtn',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增支付宝支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)


# 商户添加支付配置：百度钱包、银联钱包、和包、翼支付
def sh_add_config():
    # 点击商户树展开图标
    tool.click_action(
        '//ul[@id="listTree"]/li/span',
        '商户树展开图标'
    )
    # 点击商户名称：商户for新增用户测试
    tool.click_action(
        '//ul[@id="listTree"]/li/ul/li/a',
        '商户名称'
    )
    # 点击百度钱包按钮
    tool.click_action(
        'bfbPayBtn',
        '百度钱包按钮',
        locator=By.ID
    )
    # 百付宝配置名称输入框：百付宝配置test1
    tool.fill_action(
        'bfbConfigName',
        '百付宝配置test1',
        '百付宝配置名称输入框',
        locator=By.ID
    )
    # 商户号输入框：商户号test1
    tool.fill_action(
        'bfbMerchantId',
        '商户号test1',
        '商户号输入框',
        locator=By.ID
    )
    # 秘钥输入框：秘钥test1
    tool.fill_action(
        'baifubaoKey',
        '秘钥test1',
        '秘钥输入框',
        locator=By.ID
    )
    # 订单有效时间输入框：1
    tool.fill_action(
        'timeExpress',
        '1',
        '订单有效时间输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        'saveConfigBtn',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增支付宝支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击银联钱包按钮
    tool.click_action(
        'unionPayBtn',
        '银联钱包按钮',
        locator=By.ID
    )
    # 银联配置名称输入框：银联配置test1
    tool.fill_action(
        'bfbConfigName',
        '银联配置test1',
        '银联配置名称输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        'saveConfigBtn',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增支付宝支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)


# 门店添加支付配置
def md_add_config():
    pass


if __name__ == "__main__":
    provider_add_config()
    sh_add_config()
    md_add_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_merchant(m_id)
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
