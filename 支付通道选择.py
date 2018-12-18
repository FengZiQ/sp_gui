# coding=utf-8
from gui_test_tool import *
from dataForTest import *

tool = GUITestTool()


# 直连通道选择
def straight_channel_choice():
    # 点击支付配置管理标签
    tool.click_action(
        '//ul[@id="leftNav"]/li[4]',
        '支付配置管理标签'
    )
    # 点击支付配置管理二级标签
    tool.click_action(
        '//a[@data-menucode="channelChoose"]',
        '支付通道选择二级标签',
        response_time=5
    )
    # 选择直连通道
    tool.click_action(
        '//label[@for="straight"]',
        '直连通道label',
        response_time=1
    )
    # 点击确认保存按钮
    tool.click_action(
        'saveSwiftpayBtn',
        '确认保存按钮',
        locator=By.ID,
        response_time=1
    )
    # 断言: 提示配置信息保存成功
    tool.equal_text_assert(
        'msValue',
        '消息提示',
        '配置信息保存成功',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    time.sleep(3)


# 威富通通道选择
def swift_gallery_channel_choice():
    # 选择威富通
    tool.click_action(
        '//label[@for="swiftGallery"]',
        '威富通label',
        response_time=1
    )
    # 使用威富通间连通道的同时使用直连通道:支付宝
    tool.click_action(
        '//label[@for="switfBase2"]',
        '支付宝复选框',
        response_time=1
    )
    # 点击确认保存按钮
    tool.click_action(
        'saveSwiftpayBtn',
        '确认保存按钮',
        locator=By.ID,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        'msValue',
        '消息提示',
        '配置信息保存成功',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    time.sleep(3)


# 网商银行通道选择
def mybank_channel_choice():
    # 选择网商银行
    tool.click_action(
        '//label[@for="mybank"]',
        '网商银行label',
        response_time=1
    )
    # 点击确认保存按钮
    tool.click_action(
        'saveSwiftpayBtn',
        '确认保存按钮',
        locator=By.ID,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        'msValue',
        '消息提示',
        '配置信息保存成功',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    time.sleep(3)


# 腾讯云支付通道选择
def tencentcloud_channel_choice():
    # 腾讯云支付
    tool.click_action(
        '//label[@for="tencentcloud"]',
        '腾讯云支付label',
        response_time=1
    )
    # 点击确认保存按钮
    tool.click_action(
        'saveSwiftpayBtn',
        '确认保存按钮',
        locator=By.ID,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        'msValue',
        '消息提示',
        '配置信息保存成功',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    time.sleep(3)


if __name__ == "__main__":
    straight_channel_choice()
    swift_gallery_channel_choice()
    mybank_channel_choice()
    tencentcloud_channel_choice()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([d['id'] for d in device_info])
    delete_customer(customer_info['id'])




