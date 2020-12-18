import base64
import rsa
from rsa import common


class RsaUtil(object):
    # 初始化key
    def __init__(self, pub_key_dir="0", pri_key_dir="0"):
        """初始化的时候要给出公钥和私钥的地址
        :param pri_key_dir：私钥
        :param pub_key_dir：公钥
        """
        if pub_key_dir:
            self.company_public_key = rsa.PublicKey.load_pkcs1(open(pub_key_dir, 'rb').read())
        if pri_key_dir:
            self.company_private_key = rsa.PrivateKey.load_pkcs1(open(pri_key_dir, 'rb').read())

    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n)
        reserve_size = 11  # 预留位为11，具体为啥我在我的报告里说
        if not encrypt:  # 解密时不需要考虑预留位
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    # 加密
    def encrypt_by_public_key(self, message):
        """使用公钥加密.
            :param message: 需要加密的内容.
            加密之后需要对接过进行base64转码
        """
        try:
            encrypt_result = b''
            max_length = self.get_max_length(self.company_public_key)
            while message:
                input = message[:max_length]
                message = message[max_length:]
                out = rsa.encrypt(input, self.company_public_key)
                encrypt_result += out
            encrypt_result = base64.b64encode(encrypt_result)
            return encrypt_result
        except:
            pass

    # 解密
    def decrypt_by_private_key(self, message):
        """使用私钥解密.
            :param message: 需要加密的内容.
            解密之后的内容直接是字符串，不需要在进行转义
        """
        try:
            decrypt_result = b""
            max_length = self.get_max_length(self.company_private_key, False)
            decrypt_message = base64.b64decode(message)
            while decrypt_message:
                input = decrypt_message[:max_length]
                decrypt_message = decrypt_message[max_length:]
                out = rsa.decrypt(input, self.company_private_key)
                decrypt_result += out
            return decrypt_result
        except:
            pass

    def sign_by_private_key(self, data):
        """私钥签名.
            :param data: 需要签名的内容.
            使用SHA-256 方法进行签名（也可以使用MD5）
            签名之后，需要转义后输出
        """
        signature = rsa.sign(data, priv_key=self.company_private_key, hash_method='SHA-256')
        return base64.b64encode(signature)

    def verify_by_public_key(self, message, signature):
        """公钥验签.
            :param message: 验签的内容.
            :param signature: 对验签内容签名的值（签名之后，会进行b64encode转码，所以验签前也需转码）.
        """
        signature = base64.b64decode(signature)
        return rsa.verify(message, signature, self.company_public_key)
