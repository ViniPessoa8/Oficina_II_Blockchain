import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, previousHash, data):
        self.__index = index
        self.__timestamp = datetime.timestamp(datetime.now())
        self.__previousHash = previousHash
        self.__data = data
        self.nonce = 0
        self.hash = Block.calculateHash(self)
        
    def getIndex(self):
        return self.__index

    def getTimeStamp(self):
        return self.__timestamp
    
    def getPreviousHash(self):
        return self.__previousHash
    
    def getData(self):
        return self.__data
    
    def getHash(self):
        return self.hash

    def toString(self):
        return "Block #" + str(self.__index) + " [previousHash : " + str(self.__previousHash) + ", " + "timestamp : " + str(self.__timestamp) + ", " + "data : " + str(self.__data) + ", Nonce:" + str(self.nonce) + "]"

    def calculateHash(self):
        h = ""
        txt = self.toString()
        hl = hashlib.sha256()
        hl.update(txt.encode("utf-8"))
        
        # generate 0's
        for byte in hl.digest():
            hexNum = hex(0xff & byte)
            
            if len(hexNum) == 1:
                h += "0"
        
        return h + hl.hexdigest()
    
    def proofOfWork(self, difficulty):
        self.nonce = 0
        
        while (difficulty * "0") != self.hash[:difficulty]:
            print((difficulty * "0") + " | " + self.hash[:difficulty] + " | " + str(self.nonce) + " | " + self.hash)
            self.nonce += 1
            self.hash = self.calculateHash()

if __name__ == "__main__":
    # Block Creation
    block = Block(0, 0, "texto")
    print(block.toString())
    print(block.hash)
    block.proofOfWork(1)
    print(block.nonce)
    print(block.hash)
    