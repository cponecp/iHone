
from qiniu import Auth, put_data, etag
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = '87Dh5ohJ4fTY7EniBBheK0MaPnINJwmVxTrSsZMx'
secret_key = 'KTNYHIJzFU5twPQ2jA35LzTQpne5OfFE1ZSmg5VH'


def storage(file_data):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'ihome'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    ret, info = put_data(token, None, file_data)
    if info.status_code == 200:
        return ret.get('key')
    else:
        # 上传失败
        raise Exception("上传七牛失败")


if __name__ == '__main__':
    with open('1.jpg', 'rb') as f:
        data = f.read()
        storage(data)
