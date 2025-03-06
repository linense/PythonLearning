

# Implement a python class to be derived
class Service:

  def __init__(self, host, port):
    self.host = host
    self.port = port

# Implement methods in the class
  def getService(self):
    return f'{self.host}:{self.port}'

  def getData(self):
    return ''
  
# Implement a subclass
  class Web(Service):
    def __init__(self, protocol='http', host='0.0.0.0', port=80):
        super().__init__(host, port)
        self.protocol=protocol

# Override methods in the subclass
    def getService(self):
        return f'{self.protocol}://{self.host}:{self.port}'

    def getData(self):
        return '<html>...</html>'

class Mail(Service):
  def __init__(self, method='IMAP', host='0.0.0.0', port=143):
    super().__init__(host,port)
    self.method=method

  def getData(self):
    return 'To: <steve@example.com>\nFrom: <jane@example.com>\nContent-Type: text/plain;\n\nHello, World!\n'
  
# Demonstrate use of the classes by printing results and output to the console
s = Service('0.0.0.0', 8888)
print(f'Service: {s.getService()}')
print()

http = Web()
print(f'Web Service: {http.getService()}')
print(http.getData())
print()

mail = Mail(method='POP3')
print(f'Mail Service: {mail.getService()}')
print(mail.getData())