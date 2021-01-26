from cryptography.fernet import Fernet 

class encryptor(object):
    def create_key(self):
        self.key = Fernet.generate_key()
        return self.key 

    def write_key(self, key, key_name):
        try:
            with open (key_name, 'xb') as self.mykey:
                self.mykey.write(key)
        except FileExistsError:
            None 
        
    def load_key(self, key_name):
        with open (key_name, 'rb') as self.mykey:
            self.key=self.mykey.read()
        return self.key
    
    def file_encrypt(self, key, original_file, encrypted_file):
        self.f=Fernet(key)

        with open(original_file, 'rb')as self.file:
            self.original= self.file.read()

        self.encrypted= self.f.encrypt(self.original) 
        
        with open(encrypted_file, 'wb')as self.file:
            self.file.write(self.encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        self.f=Fernet(key)   

        with open(encrypted_file, 'rb') as self.file:
            self.encrypted=self.file.read()
        
        self.decrypted = self.f.decrypt(self.encrypted)

        with open(decrypted_file, 'wb') as self.file:
            self.file.write(self.decrypted)
    
a = encryptor()
mykey = a.create_key()
a.write_key(mykey, 'mykey.key')
loaded_key = a.load_key('mykey.key')
a.file_encrypt(loaded_key,'test.txt','enc_test.txt')
a.file_decrypt(loaded_key,'enc_test.txt', 'dec_test.txt')


