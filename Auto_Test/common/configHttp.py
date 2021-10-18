# 这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。
import requests
import json


class RunMain():

    def send_post(self, url, data):
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '111'})
    result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=1112')
    result3 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
    print(result1)
    print(result2)
    print(result3)
