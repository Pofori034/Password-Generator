from cryptography.fernet import Fernet 
import base64

class encryptor(object):
    def __init__(self):
        super(encryptor, self).__init__()
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
    

    def write_key(self, key_name):
        try:
            with open (key_name, 'xb') as self.mykey:
                self.mykey.write(self.key)
        except FileExistsError:
            None 
        
    def load_key(self, key_name):
        with open (key_name, 'rb') as self.mykey:
            self.key=self.mykey.read()
        return self.key
    
    def file_encrypt(self, original):

        #with open(original_file, 'rb')as self.file:
        #self.original= original.encode()

        #self.encrypted= self.f.encrypt(self.original) 
        return self.f.encrypt(original.encode())
        #with open(encrypted_file, 'wb')as self.file:
        #    self.file.write(self.encrypted)

    def file_decrypt(self, encrypted):

        #with open(encrypted_file, 'rb') as self.file:
        #self.encrypted=encrypted
        
        self.decrypted = self.f.decrypt(encrypted)
        return self.decrypted

        #with open(decrypted_file, 'wb') as self.file:
        #    self.file.write(self.decrypted)
    
#a = encryptor()
#mykey = a.create_key()
#a.write_key(mykey, 'mykey.key')
#loaded_key = a.load_key('mykey.key')
#a.file_encrypt(loaded_key,'test.txt')
#a.file_decrypt(loaded_key,'enc_test.txt')


