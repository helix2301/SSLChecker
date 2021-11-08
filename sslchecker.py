import ssl
import socket
import hashlib

addr = 'address of target'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
wrappedSocket = ssl.wrap_socket(sock)

try:
    wrappedSocket.connect((addr, 443))
except:
    response = False
else:
    der_cert_bin = wrappedSocket.getpeercert(True)
    pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
    print(pem_cert)

    # Thumbprint
    thumb_md5 = hashlib.md5(der_cert_bin).hexdigest()
    thumb_sha1 = hashlib.sha1(der_cert_bin).hexdigest()
    thumb_sha256 = hashlib.sha256(der_cert_bin).hexdigest()
    print("MD5: " + thumb_md5)
    print("SHA1: " + thumb_sha1)
    print("SHA256: " + thumb_sha256)

wrappedSocket.close()
