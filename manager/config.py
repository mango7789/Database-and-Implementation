from typing import Final
from .utils import load_json
from manager import models


AUTHEN_IMAGES: Final = load_json("static/captcha/authen_images.json")
# 下载类型和对应的文件位置
DOWNLOAD_PATH: Final = {
        1: 'static/files/order_template.csv', 
        2: 'static/files/order_record.csv'
} 
CHOICE_TYPE: Final = dict(models.goods.type_choice)  # 商品类别
MAIL_TYPE: Final = ["进货单价变动", "新建的商品信息", "商品单价变动"]   # 邮件类别   
COST_TO_GOODS: Final = 1.1  # 默认（售价/进货单价）的值
image_ver = [None] * 2     # 验证码图片信息

## 以字符串形式表示的html内容       
BUTTON_STYLE: Final = '''style="padding: 0px 8px; font-size: 12px; margin-top: 0px"'''
LIST_MODIFY_BUTTON: Final = \
        '''
        <button type="button" class="btn btn-round btn-primary" ''' + BUTTON_STYLE + ''' onclick="redirectTo({})">修改</button>
        ''' 
LIST_REDIRECT_BUTTON: Final = \
        '''
        <button type="button" class="btn btn-round btn-success" ''' + BUTTON_STYLE + ''' onclick="redirectToSub({})">查看员工</button>
        ''' 
LIST_DELETE_BUTTON: Final = \
        '''
        <a class="btn btn-round btn-danger delete-link" ''' + BUTTON_STYLE + ''' href="/shop/{}/salesman/delete">删除</a>
        ''' 
SPAN_SUCCESS: Final = \
        '''
        <span class="badge" style="background-color: green">{}</span>
        '''
SPAN_DANGER: Final = \
        '''
        <span class="badge" style="background-color: red">{}</span>
        '''
SPAN_WARNING: Final = \
        '''
        <span class="badge" style="background-color: orange">{}</span>
        '''
ARROW_DOWN_RED: Final = \
        '''
        <i class="error fa fa-long-arrow-down" style="color: red"></i>
        '''
ARROW_UP_ORANGE: Final = \
        '''
        <i class="error fa fa-long-arrow-up" style="color: orange"></i>
        '''
ARROW_DOWN_GREEN: Final = \
        '''
        <i class="error fa fa-long-arrow-down" style="color: green"></i>
        '''
ARROW_UP_RED: Final = \
        '''
        <i class="error fa fa-long-arrow-up" style="color: red"></i>
        '''
## end html

# Configuration for cache
RATE_TIME_TIMEFRAME = 1
RATE_MAX_SUBMISSION = 5