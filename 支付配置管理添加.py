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
        '//form[@id="wxpayConfigForm"]/div[5]/button',
        '确认修改按钮',
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
        '//div[@id="aliParent"]/div[8]/button',
        '确认修改按钮',
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
        '//form[@id="bfbConfigForm"]/div[5]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增百付宝支付配置信息成功',
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
        'unionConfigName',
        '银联配置test1',
        '银联配置名称输入框',
        locator=By.ID
    )
    # 收单机构输入框：收单机构test1
    tool.fill_action(
        'acqinsCode',
        '收单机构test1',
        '收单机构输入框',
        locator=By.ID
    )
    # 商户号输入框：商户号test1
    tool.fill_action(
        'unionMerchantId',
        '商户号test1',
        '商户号输入框',
        locator=By.ID
    )
    # 秘钥输入框：秘钥test1
    tool.fill_action(
        'unionPayKey',
        '秘钥test1',
        '秘钥输入框',
        locator=By.ID
    )
    # 订单有效时间输入框：1
    tool.fill_action(
        'unionTimeExpress',
        '1',
        '订单有效时间输入框',
        locator=By.ID
    )
    # 证书选择框：选择yl.pfx文件
    tool.fill_action(
        'unionFile',
        config_data['file_path'] + 'yl.pfx',
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
        '//form[@id="unionConfigForm"]/div[7]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增银联支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击和包按钮
    tool.click_action(
        'cmPayBtn',
        '和包按钮',
        locator=By.ID
    )
    # 和包配置名称输入框：和包配置test1
    tool.fill_action(
        'cmConfigName',
        '和包配置test1',
        '和包配置名称输入框',
        locator=By.ID
    )
    # 商户号输入框：商户号test1
    tool.fill_action(
        'cmMerchantId',
        '商户号test1',
        '商户号输入框',
        locator=By.ID
    )
    # 秘钥输入框：秘钥test1
    tool.fill_action(
        'cmpayKey',
        '秘钥test1',
        '秘钥输入框',
        locator=By.ID
    )
    # 订单有效时间输入框：1
    tool.fill_action(
        'cmTimeExpress',
        '1',
        '订单有效时间输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="cmConfigForm"]/div[5]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增和包支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击翼支付按钮
    tool.click_action(
        'bestPayBtn',
        '翼支付按钮',
        locator=By.ID
    )
    # 翼支付配置名称输入框：翼支付配置名称test1
    tool.fill_action(
        'bestConfigName',
        '翼支付配置名称test1',
        '翼支付配置名称输入框',
        locator=By.ID
    )
    # 商户号输入框：商户号test1
    tool.fill_action(
        'bestMerchantId',
        '商户号test1',
        '商户号输入框',
        locator=By.ID
    )
    # 退款密码输入框：退款密码test1
    tool.fill_action(
        'bestMerchantPwd',
        '退款密码test1',
        '退款密码输入框',
        locator=By.ID
    )
    # 秘钥输入框：秘钥TWETest233
    tool.fill_action(
        'bestpayKey',
        '秘钥TWETest233',
        '秘钥输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="bestConfigForm"]/div[5]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增翼支付支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)


# 门店添加支付配置：威富通、网商银行、腾讯云支付、收钱吧
def md_add_config():
    # 点击门店树展开图标
    tool.click_action(
        '//ul[@id="listTree"]/li/ul/li/span',
        '门店树展开图标'
    )
    # 点击门店名称：门店for新增用户测试
    tool.click_action(
        '//ul[@id="listTree"]/li/ul/li/ul/li/a',
        '门店名称'
    )
    # 点击威富通按钮
    tool.click_action(
        'swiftPayBtn',
        '威富通按钮',
        locator=By.ID
    )
    # 威富通配置名称输入框：威富通配置test1
    tool.fill_action(
        'swiftConfigName',
        '威富通配置test1',
        '威富通配置名称输入框',
        locator=By.ID
    )
    # 签名类型radio：RSA_256
    tool.click_action(
        '//form[@id="swiftConfigForm"]/div[2]/div/label[2]',
        '签名类型radio'
    )
    # 银行通道下拉列表：兴业银行
    tool.click_action(
        '//select[@id="swiftBankType"]/option[2]',
        '银行通道下拉列表'
    )
    # 商户号输入框：商户号test1
    tool.fill_action(
        'swiftMerchantId',
        '商户号test1',
        '商户号输入框',
        locator=By.ID
    )
    # 订单有效时间输入框：1
    tool.fill_action(
        'swiftpastimeExpress',
        '1',
        '订单有效时间输入框',
        locator=By.ID
    )
    # 秘钥输入框：'PASSk'*100
    tool.fill_action(
        'swiftpassKey',
        'PASSk'*100,
        '秘钥输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="swiftConfigForm"]/div[7]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增威富通支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击网上银行按钮
    tool.click_action(
        'mybankPayBtn',
        '点击网上银行按钮',
        locator=By.ID
    )
    # 网商银行分配的APPID输入框：APPidTest1
    tool.fill_action(
        'mybankbestAppid',
        'APPidTest1',
        '网商银行分配的APPID输入框',
        locator=By.ID
    )
    # 合作方机构号输入框：合作方机构号test1
    tool.fill_action(
        'mybankIsvOrgId',
        '合作方机构号test1',
        '合作方机构号输入框',
        locator=By.ID
    )
    # 币种下拉列表：人民币
    tool.click_action(
        '//select[@id="mybankCurrency"]/option[1]',
        '币种下拉列表'
    )
    # 商户ID输入框：商户IDTest1
    tool.fill_action(
        'mybankMerchantId',
        '商户IDTest1',
        '商户ID输入框',
        locator=By.ID
    )
    # 门店ID输入框：门店IDTest1
    tool.fill_action(
        'mybankStoreId',
        '门店IDTest1',
        '门店ID输入框',
        locator=By.ID
    )
    # 支付宝店铺编号输入框：BH2518
    tool.fill_action(
        'mybankAlipayStoreId',
        'BH2518',
        '支付宝店铺编号输入框',
        locator=By.ID
    )
    # 支付宝系统服务商ID输入框：SystemId2018
    tool.fill_action(
        'mybankSysServiceProviderId',
        'SystemId2018',
        '支付宝系统服务商ID输入框',
        locator=By.ID
    )
    # 微信公众号APPid输入框：APPid123456
    tool.fill_action(
        'mybankSubAppId',
        'APPid123456',
        '微信公众号APPid输入框',
        locator=By.ID
    )
    # 微信支付指定子商户号radio：是
    tool.click_action(
        '//form[@id="mybankConfigForm"]/div[12]/div/div[1]/ins',
        '微信支付指定子商户号radio'
    )
    # 微信交易子商户号输入框：SubNum123
    tool.fill_action(
        'mybankSubMerchId',
        'SubNum123',
        '微信交易子商户号输入框',
        locator=By.ID
    )
    # 微信支付渠道号输入框：PayChId123456
    tool.fill_action(
        'mybankChannelId',
        'PayChId123456',
        '微信支付渠道号输入框',
        locator=By.ID
    )
    # 商户私钥输入框：PrKey*100
    tool.fill_action(
        'mybankPrivateKey',
        'PrKey'*100,
        '商户私钥输入框',
        locator=By.ID
    )
    # 网商银行公钥输入框：PubKe*100
    tool.fill_action(
        'mybankPublicKey',
        'PubKe'*100,
        '网商银行公钥输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="mybankConfigForm"]/div[17]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增网商支付配置信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击腾讯云支付按钮
    tool.click_action(
        'tencentcloudpayBtn',
        '腾讯云支付按钮',
        locator=By.ID
    )
    # 腾讯云支付配置名称输入框：腾讯云支付配置test1
    tool.fill_action(
        'TencentcloudConfig_name',
        '腾讯云支付配置test1',
        '腾讯云支付配置名称输入框',
        locator=By.ID
    )
    # 服务商账号输入框：test1Num
    tool.fill_action(
        'TencentcloudSp_id',
        'test1Num',
        '服务商账号输入框',
        locator=By.ID
    )
    # 商户账号输入框：merNumTest1
    tool.fill_action(
        'TencentcloudMerchant_id',
        'merNumTest1',
        '商户账号输入框',
        locator=By.ID
    )
    # 门店账号输入框：storeTestNum1
    tool.fill_action(
        'Tencentcloudshop_id',
        'storeTestNum1',
        '门店账号输入框',
        locator=By.ID
    )
    # 商户签名秘钥输入框：SignK*10
    tool.fill_action(
        'TencentcloudSign_key',
        'SignK'*10,
        '商户签名秘钥输入框',
        locator=By.ID
    )
    # 商户认证秘钥输入框：AuthK*10
    tool.fill_action(
        'TencentcloudAuth_key',
        'AuthK'*10,
        '商户认证秘钥输入框',
        locator=By.ID
    )
    # 商户单号前缀输入框：Test122
    tool.fill_action(
        'TencentcloudPrefix',
        'Test122',
        '商户单号前缀输入框',
        locator=By.ID
    )
    # 员工编号输入框：1255233
    tool.fill_action(
        'TencentcloudStaff_id',
        '1255233',
        '员工编号输入框',
        locator=By.ID
    )
    # 点击确认修改按钮
    tool.click_action(
        '//form[@id="TencentcloudConfigForm"]/div[9]/button',
        '确认修改按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增腾讯云支付配置信息成功',
        end='@结束@'
    )
    # time.sleep(3)
    # # 收钱吧按钮
    # tool.click_action(
    #     'sqbpayBtn',
    #     '收钱吧按钮',
    #     locator=By.ID
    # )
    # # 收钱吧支付配置名称输入框：收钱吧支付配置test1
    # tool.fill_action(
    #     'sqbpayConfig_name',
    #     '收钱吧支付配置test1',
    #     '收钱吧支付配置名称输入框',
    #     locator=By.ID
    # )
    # # 收钱吧appId输入框：收钱吧appIdTest1
    # tool.fill_action(
    #     'sqbpayApp_id',
    #     '收钱吧appIdTest1',
    #     '收钱吧appId输入框',
    #     locator=By.ID
    # )
    # # 服务商序列号输入框：服务商序列号Test1
    # tool.fill_action(
    #     'sqbpayVendor_sn',
    #     '服务商序列号Test1',
    #     '服务商序列号输入框',
    #     locator=By.ID
    # )
    # # 服务商秘钥输入框：服务商秘钥Test1
    # tool.fill_action(
    #     'sqbpayVendor_key',
    #     '服务商秘钥Test1',
    #     '服务商秘钥输入框',
    #     locator=By.ID
    # )
    # # 点击确认修改按钮
    # tool.click_action(
    #     'saveConfigBtn',
    #     '确认修改按钮',
    #     locator=By.CLASS_NAME,
    #     response_time=1
    # )
    # # 断言
    # tool.equal_text_assert(
    #     '/html/body/div/div/span/p',
    #     '提示消息',
    #     '新增收钱吧支付配置信息成功',
    #     end='@结束@'
    # )


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
