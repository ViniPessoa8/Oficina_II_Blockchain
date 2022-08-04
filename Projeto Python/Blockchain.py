import Block as b

class Blockchain:
    def __init__(self, difficulty):
        self.__difficulty = difficulty
        self.blocks = []
        
        block = b.Block(0, 0, "Genesis Block")
        block.proofOfWork(self.__difficulty)
        
        self.blocks.append(block)
        
    def getDifficulty(self):
        return self.__difficulty
    
    def latestBlock(self):
        return self.blocks[-1]
    
    def newBlock(self, data):
        latestBlock = self.latestBlock()
        newBlock = b.Block(latestBlock.getIndex() + 1, latestBlock.hash, data)
        return newBlock
    
    def addBlock(self, block):
        if block != None:
            block.proofOfWork(self.__difficulty)
            self.blocks.append(block)
    
    def isFirstBlockValid(self):
        firstBlock = self.blocks[0]
        
        if firstBlock.getIndex() != 0:
            return False

        if firstBlock.getPreviousHash() != None:
            return False

        if firstBlock.getHash() == None or not b.Block.calculateHash(firstBlock) == firstBlock.getHash():
            return False
        
        return True
    
    def isValidNewBlock(self, newBlock, previousBlock):
        if newBlock == None or previousBlock == None:
            return False
        
        if newBlock.getPreviousHash() == None or not newBlock.getPreviousHash() == previousBlock.getHash():
            return False
        
        if newBlock.getHash() == None or not b.Block.calculateHash(newBlock) == newBlock.getHash():
            return False
        
        return True
        
    def isBlockChainValid(self):
        if not self.isFirstBlockValid:
            return False
        
        for i in range(1, len(self.blocks)):
            currentBlock = self.blocks[i]
            previousBlock = self.blocks[i-1]
            
            if not self.isValidNewBlock(currentBlock, previousBlock):
                return False
            
        return True
        
    def toString(self):
        txt = ""
        
        for block in self.blocks:
            txt += block.toString() + "\n"    
            
        return txt