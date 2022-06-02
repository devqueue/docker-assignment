from flask import Flask, request
import hashlib

app = Flask(__name__)

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json = request.json
        file = json['file']
        json['checksum'] = hash_file(f"/data/{file}")
        return json
    else:
        return 'Welcome to the container 2'

        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000')