from flask import Flask
from flask import request
from flask import render_template		#including flask
from bccore import Block
from bccore import BlockChain

app = Flask(__name__)

fbl1 = Block(1,"BootStrapBlock",'000000000000000000000000000000000000000000000000000000000000')		#first block
bc = BlockChain( fbl1 )
@app.route('/')
def my_form():						#functions accessing bccore and html file
    return render_template("blockchain.html",bc=bc)
@app.route('/addblock', methods=['GET','POST'])
def add_block():	
	bc.addBlock(request.args['addblocktext'])
	return render_template("blockchain.html",bc=bc)
@app.route('/modifyblock', methods=['GET','POST'])
def modify_block():	
	bc.modifyBlock(int(request.args['blockIndex']),request.args['editblocktext'])
	return render_template("blockchain.html",bc=bc)
@app.route('/mineblock/<int:blockIndex>', methods=['GET','POST'])
def mine_block(blockIndex):	
	bc.mineTheBlock(blockIndex)
	return render_template("blockchain.html",bc=bc)
if __name__ == '__main__':
    app.run()
