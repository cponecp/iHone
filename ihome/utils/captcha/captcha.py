from PIL import Image
# 再图片上写东西
from PIL import ImageDraw
# 生成字体对象
from PIL import ImageFont
import random
from io import BytesIO


def get_random_color():
    return (random.randint(0, 256), random.randint(0, 255), random.randint(0, 255))

# def generate_captcha():
    #     new_img = Image.new('RGB', (400, 40), color=get_random_color())
    #     # 把图片放到ImageDraw内
    #     draw = ImageDraw.Draw(new_img)
    #
    #     # 构造出字体对象
    #     # 第一个参数,是字体文件(ttf格式字体文件),第二个参数,字体大小
    #     # font = ImageFont.truetype('fonts/Arial.ttf', 30)
    #     font = ImageFont.truetype('fonts/kumo.ttf',size=30)
    #     # draw.text((0,5),'python',get_random_color(),font=font)
    #     valid_code = ''
    #     for i in range(4):
    #         num_str = str(random.randint(0, 9))
    #         upper_str = chr(random.randint(65, 90))
    #         low_str = chr(random.randint(97, 122))
    #         random_str = random.choice([num_str, upper_str, low_str])
    #
    #         draw.text((i * 30 + 40, 5), random_str, get_random_color(), font=font)
    #         valid_code += random_str
    #
    #     # print(valid_code)
    #
    #     # 打开一个内存管理器,保存进去
    #     img = BytesIO()
    #     new_img.save(img, 'png')
    #     # 从内存管理器中取出img
    #     data = img.getvalue()
    #     name = "cpp"
    return name, valid_code, data


def generate_captcha():
    valid_code = 'vc6e'
    with open('ihome/utils/captcha/verfiy_code.jpg', 'rb') as f:
        data = f.read()

    name = "cpp"
    return name, valid_code, data


if __name__ == '__main__':
    print(generate_captcha())
