# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 前置条件：
# 给“testSP_平台服务商”服务商创建商户“商户for新增用户测试”
# 给该商户分别添加微信、支付宝、百度、银联、和包、翼支付、威富通、网商、腾讯云、收钱吧支付配置

def precondition():
    try:
        c_info = get_merchant_info('testSP_平台服务商')
        sh_id = add_merchant('商户for新增用户测试', c_info[0]['id'], 2)
    except Exception as e:
        print(e)
    else:
        return sh_id


s_id = precondition()
# 微信配置
add_pay_configuration(s_id, 'wxpayConfig', {
    "configName": "wx",
    "type": "1",
    "appId": "AppID",
    "appSecret": "appSecret",
    "mchNum": "1269310601",
    "appidKey": "APIKey",
    "certLocalPath": upload_cer(config_data['file_path'] + 'wx.p12'),
    "subMchNum": "",
    "subAppid": ""
})
# 支付宝配置
add_pay_configuration(s_id, 'alipayConfig', {
    "type": "2",
    "signType": "1",
    "configName": "zfb",
    "appId": "AppID",
    "partner": "id",
    "timeExpress": "1",
    "alipayPrivateKey": "T+key"*100
})
# 百度配置
add_pay_configuration(s_id, 'bfbpayConfig', {
    "configName": "baidu_pay",
    "merchantId": "商户号test1",
    "baifubaoKey": "baifubaoKey",
    "timeExpress": "1"
})
# 银联配置
add_pay_configuration(s_id, 'unionpayConfig', {
    "configName": "unionpayConfig",
    "acqinsCode": "收单机构test1",
    "merchantId": "商户号test1",
    "unionPayKey": "123456",
    "timeExpress": "1",
    "certLocalPath": upload_cer(config_data['file_path'] + 'yl.pfx')
})
# 和包配置
add_pay_configuration(s_id, 'cmpayConfig', {
    "configName": "cmpayConfig",
    "merchantId": "商户号test1",
    "cmpayKey": "123456",
    "timeExpress": "1"
})
# 翼支付配置
add_pay_configuration(s_id, 'bestpayConfig', {
    "configName": "bestpayConfig",
    "merchantId": "商户号test1",
    "merchantPwd": "123456",
    "bestpayKey": "123456"
})
# 威富通配置
add_pay_configuration(s_id, 'swiftpassConfig', {
    "configName": "swiftpassConfig",
    "signType": "1",
    "bankType": "6",
    "merchantId": "商户号test1",
    "timeExpress": "1",
    "swiftpassKey": "123456"
})
# 网商银行配置
add_pay_configuration(s_id, 'mybankConfig', {
    "appid": "2018071200000244",
    "isvOrgId": "202210000000000001274",
    "currency": "CNY",
    "merchantId": "226801000000123110252",
    "storeId": "211011000010000028300",
    "settleType": "1",
    "alipayStoreId": "",
    "sysServiceProviderId": "",
    "subAppId": "",
    "subMerchId": "",
    "channelId": "",
    "privateKey": "21232123132",
    "publicKey": "21232123132",
    "payLimitList": ""
})
# 腾讯云支付配置
add_pay_configuration(s_id, 'tencentcloudpayConfig', {
    "config_name": "腾讯云支付配置test1",
    "sp_id": "test1Num",
    "merchant_id": "merNumTest1",
    "shop_id": "storeTestNum1",
    "sign_key": "test"*10,
    "auth_key": "test"*10,
    "prefix": "sz0100molp",
    "staff_id": "100004"
})
# # 收钱吧配置
# add_pay_configuration(s_id, 'sqbConfig', {
#     "config_name": "收钱吧test",
#     "app_id": "app_id",
#     "vendor_sn": "服务商序列号",
#     "vendor_key": "AATds"*20
# })


# 微信支付配置修改与删除
def wx_mod_del():
    # 点击支付配置管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]',
        '支付配置管理标签'
    )
    # 点击支付配置管理二级标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]/ul/li[1]',
        '支付配置管理二级标签'
    )
    # 点击商户树展开图标
    tool.click_action(
        '//ul[@id="listTree"]/li/span',
        '商户树展开图标'
    )
    # 点击商户名称：商户for新增用户测试
    tool.click_action(
        '//ul[@id="listTree"]/li/ul/li/a',
        '商户for新增用户测试'
    )
    # 点击微信按钮
    tool.click_action(
        'wxPayBtn',
        '微信按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="wxpayConfigForm"]/div[5]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改微信支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="wxpayConfigForm"]/div[5]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 支付宝支付配置修改与删除
def ali_mod_del():
    time.sleep(3)
    # 点击支付宝按钮
    tool.click_action(
        'aliPayBtn',
        '支付宝按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//div[@id="aliParent"]/div[8]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改支付宝支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//div[@id="aliParent"]/div[8]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 百度钱包支付配置修改与删除
def bfb_mod_del():
    time.sleep(3)
    # 点击百度钱包按钮
    tool.click_action(
        'bfbPayBtn',
        '百付宝按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="bfbConfigForm"]/div[5]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改百付宝支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="bfbConfigForm"]/div[5]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 银联钱包支付配置修改与删除
def union_mod_del():
    time.sleep(3)
    # 点击银联钱包按钮
    tool.click_action(
        'unionPayBtn',
        '银联钱包按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="unionConfigForm"]/div[7]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改银联支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="unionConfigForm"]/div[7]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 和包支付配置修改与删除
def cm_mod_del():
    time.sleep(3)
    # 点击和包按钮
    tool.click_action(
        'cmPayBtn',
        '和包按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="cmConfigForm"]/div[5]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改和包支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="cmConfigForm"]/div[5]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 翼支付支付配置修改与删除
def best_mod_del():
    time.sleep(3)
    # 点击翼支付按钮
    tool.click_action(
        'bestPayBtn',
        '翼支付按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="bestConfigForm"]/div[5]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改翼支付支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="bestConfigForm"]/div[5]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 威富通支付配置修改与删除
def swift_mod_del():
    time.sleep(3)
    # 点击威富通按钮
    tool.click_action(
        'swiftPayBtn',
        '威富通按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="swiftConfigForm"]/div[7]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改威富通支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="swiftConfigForm"]/div[7]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 网商银行支付配置修改与删除
def my_bank_mod_del():
    time.sleep(3)
    # 点击网商银行按钮
    tool.click_action(
        'mybankPayBtn',
        '网商银行按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="mybankConfigForm"]/div[17]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改网商支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="mybankConfigForm"]/div[17]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 腾讯云支付配置修改与删除
def tencent_cloud_mod_del():
    time.sleep(3)
    # 点击腾讯云支付按钮
    tool.click_action(
        'tencentcloudpayBtn',
        '腾讯云支付按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="TencentcloudConfigForm"]/div[9]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改腾讯云支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="TencentcloudConfigForm"]/div[9]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


# 收钱吧支付配置修改与删除
def sqb_mod_del():
    time.sleep(3)
    # 点击收钱吧按钮
    tool.click_action(
        'sqbpayBtn',
        '收钱吧按钮',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="sqbConfigForm"]/div[5]/button',
        '确认修改按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改收钱吧支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击删除配置按钮
    tool.click_action(
        '//form[@id="sqbConfigForm"]/div[5]/div',
        '删除配置按钮'
    )
    # 点击确认修改按钮
    tool.click_action(
        'ok',
        '确认修改按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功',
        end='@结束@'
    )


if __name__ == "__main__":
    wx_mod_del()
    ali_mod_del()
    bfb_mod_del()
    union_mod_del()
    cm_mod_del()
    best_mod_del()
    swift_mod_del()
    my_bank_mod_del()
    tencent_cloud_mod_del()
    sqb_mod_del()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
