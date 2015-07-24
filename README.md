# easygo_python
"宜出行"SDK

使用python setup.py install 进行安装

## Example
```python
from easygo import EasygoClient

easygoClient = EasygoClient()
data = easygoClient.get_heatmap_data.get(lng0=118.298895,lat0=32.261379,lng1=118.31489499999999,lat1=32.277379)
```
data的数据就是此接口的数据:
http://easygo.qq.com/get_heatmap_data?openid=ot5aas1gv5RQ1dOFrlqBp4HcvKqM&lng0=118.298895&lat0=32.261379&lng1=118.31489499999999&lat1=32.277379

SDK是定制类原理,提前设置好url,通过__getattr__将属性填写进访问地址。
