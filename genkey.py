import os
import rsa
import win32api


def keygen():
    try:
        local = os.path.expanduser("~")
        try:
            os.mkdir(r"%s\.ssh" % local)
        except:
            pass
        # 512，1024位的密钥已经过时了，2048位的比较常用，但是……老子喜欢3072的
        (pub, pri) = rsa.newkeys(3072)

        prikey = pri.save_pkcs1()
        file_id = (r"%s\.ssh\id_rsa.pem" % local)
        with open(file_id, 'wb') as file_obj:
            file_obj.write(prikey)

        pubkey = pub.save_pkcs1()
        file_pub = (r"%s\.ssh\id_rsa_pub.pem" % local)
        with open(file_pub, 'wb') as file_obj:
            file_obj.write(pubkey)
    except:
        win32api.MessageBox(0, "未知错误，请联系管理员", "错误", 0)


if __name__ == "__main__":
    keygen()
