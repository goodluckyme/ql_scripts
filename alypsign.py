'''
阿里云盘 -- 签到
抓包 www.aliyundrive.com 下的 refresh_token

变量填写:
    1: 单账号 exoprt refresh_token_ali='refresh_token'
    2: 多账号 export refresh_token_ali='refresh_token1#refresh_token2'

抓包方法:
	1: 进入网址 www.aliyundrive.com 并登录
	2: 打开 F12(开发者工具) 进入 console(控制台)
    3: 控制台输入 alert(JSON.parse(localStorage.token)['refresh_token']) 弹出的就是 refresh_token
'''

try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(b'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\n')))
except KeyboardInterrupt:
	exit()
