run:
```shell
gunicorn --reload 'look.app:get_app()'
```

test_app.py # 单元测试

test_integration.py # 功能测试

### 学习笔记

1. 可以通过在方法请求加 `@falcon.before` 装饰器，做数据检验，或者扩展数据

2. 单元测试
```python
from falcon import testing
testing.TestClient(api)  # 可以模拟发送请求


from unittest.mock import mock_open, call, MagicMock
# mock_open, 模拟open 函数
# MagicMock 可以模拟一般的对象
```

3. web 视图 和业务逻辑解耦

例如：
`images.py` 中 `Collection` 和 `ImageStore` web 逻辑处理和业务逻辑处理
