# -*- coding: utf-8 -*-
"""
更新cdn证书(可配合let's encrypt 等完成自动证书更新)
"""
import qiniu
from qiniu import DomainManager
import os
import time

# 账户ak，sk
access_key = os.getenv('ACCESS_KEY', '')
secret_key = os.getenv('SECRET_KEY', '')
domain_name = os.getenv('DOMAIN', '')

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

cert_path = os.path.join(os.getcwd(), "out")

privatekey = os.path.join(
    cert_path, "{}/{}.key".format(domain_name, domain_name))
ca = os.path.join(cert_path, "{}/fullchain.cer".format(domain_name))

assert os.path.isfile(privatekey),\
    "Private Key file: '%s' does not exist!" % privatekey
assert os.path.isfile(ca), "CA file '%s' does not exist!" % ca

print("Deploying to Qiniu...")

with open(privatekey, 'r') as f:
    privatekey_str = f.read()

with open(ca, 'r') as f:
    ca_str = f.read()

ret, _ = domain_manager.create_sslcert(
    "{}/{}".format(domain_name, time.strftime("%Y-%m-%d", time.localtime())),
    domain_name, privatekey_str, ca_str)

ret, info = domain_manager.put_httpsconf(domain_name, ret['certID'], False)

print("Deployed to Qiniu successfully!")
