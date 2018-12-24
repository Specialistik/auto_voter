from models import Proxy
from main_proxy import proxy_generator

for proxy in proxy_generator():
    proxy = Proxy(host_port=proxy)
    proxy.save()
