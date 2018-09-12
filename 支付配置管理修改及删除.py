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
wx_config = add_pay_configuration(s_id, 'wxpayConfig', {
            "configName": "wx",
            "type": "3",
            "appId": "",
            "appSecret": "",
            "mchNum": "",
            "appidKey": "",
            "certLocalPath": "",
            "subMchNum": "1455670902",
            "subAppid": "wx44c0d203361769c7"
        })
# 支付宝配置
ali_config = add_pay_configuration(s_id, 'alipayConfig', {
            "configName": "ali",
            "type": "2",
            "appId": "appId",
            "partner": "partner id",
            "timeExpress": "1",
            "alipayPrivateKey": "T+key"*100
        })
# 百度配置
bfb_config = add_pay_configuration(s_id, 'bfbpayConfig', {
            "configName": "baidu_pay",
            "merchantId": "商户号test1",
            "baifubaoKey": "baifubaoKey",
            "timeExpress": "1"
        })
# 银联配置
union_config = add_pay_configuration(s_id, 'unionpayConfig', {
            "configName": "unionpayConfig",
            "acqinsCode": "收单机构test1",
            "merchantId": "商户号test1",
            "unionPayKey": "123456",
            "timeExpress": "1",
            "certLocalPath": upload_cer(config_data['file_path'] + 'yl.pfx')
        })


if __name__ == "__main__":

    tool.mark_status()
    tool.finished()
    # 清理环境
    del_merchant(s_id)
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])
