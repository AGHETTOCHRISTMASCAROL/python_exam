import base64

class DataCode:

    @staticmethod
    def encode64(data :str) -> bytes:
        data_b = data.encode()
        b64 = base64.b64encode(data_b)
        return b64

    @staticmethod
    def decode64(b64 :bytes) -> str:
        data = base64.b64decode(b64)
        return data.decode()