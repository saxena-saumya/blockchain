import hashlib as hasher

class Block:                                    #class of a block 
  def __init__(self, index, data, previous_hash):
    self.index = index
    self.data = data
    self.previous_hash = previous_hash
    self.nonce, self.hash = self.mine()
    self.legit = True

  def mine(self):                             #function to mine the edited block
    nonce = 0
    sha = hasher.sha256()
    raw = str(self.index) + str(nonce) + str(self.data) + str(self.previous_hash)
    encode = raw.encode('utf-8')
    sha.update(encode)
    while ( sha.hexdigest()[0:4] != '0000'):    #find nonce such that hash starts with '0000'
      nonce = nonce + 1
      raw = str(self.index) + str(nonce) + str(self.data) + str(self.previous_hash)
      encode = raw.encode('utf-8')
      sha.update(encode)
    return nonce, sha.hexdigest()         #return the hash value and nonce

  def print(self):                  #function to print the block
    print ("Index :" + str(self.index))
    print ("Nonce :" + str(self.nonce))
    print ("Data :" + str(self.data))
    print ("Prev Hash :" + str(self.previous_hash))
    print ("Hash :" + str(self.hash))
    print ("Legit : " + str( self.legit))



class BlockChain:
  def __init__ ( self, firstBlock ):      #initialization of first block
    self.firstBlock = firstBlock
    self.chain = []
    self.chain.append( firstBlock )

  def addBlock ( self, data ):            #function to add a block(uses function from previous class)
    prevBlk = self.chain[-1:][0]
    blk = Block(prevBlk.index + 1, data, prevBlk.hash)
    self.chain.append(blk)

  def modifyBlock ( self, index, data):     #function to modify data in a given block
    bf = False
    for bl in self.chain:
      if (bf):
        bl.legit = False
      if ( bl.index == index ):
        bl.data = data
        bl.legit = False
        bf = True

  def mineTheBlock ( self, index ):       #function to mine a given block(uses function from previous class)
    for bl in self.chain:
      if ( bl.index == index):
        bl.nonce, bl.hash = bl.mine()
        bl.legit = True


  def print( self):
    print ("Blocks in the Chain : " + str(len(self.chain))) 
    for bl in self.chain:
      print ('************************************')
      bl.print()
      print ('************************************')

if __name__ == '__main__':
  fbl1 = Block(1,"BootStrapBlock",'000000000000000000000000000000000000000000000000000000000000')
  bc = BlockChain( fbl1 )
  bc.addBlock('Saumya Saxena')
  bc.addBlock('Sameer Saxena')
  bc.print()
  bc.modifyBlock(2, 'Anju Saxena')
  bc.print()
  bc.mineTheBlock(2)
  bc.print()
  bc.mineTheBlock(3)
  bc.print()




