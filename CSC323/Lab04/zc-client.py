import sys, time, json, os, hashlib
from ecdsa import VerifyingKey, SigningKey
from p2pnetwork.node import Node
from Crypto.Cipher import AES
from Crypto import Random

SERVER_ADDR = "zachcoin.net"
SERVER_PORT = 9067

class ZachCoinClient (Node):
    
    #ZachCoin Constants
    BLOCK = 0
    TRANSACTION = 1
    BLOCKCHAIN = 2
    UTXPOOL = 3
    COINBASE = 50
    DIFFICULTY = 0x000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    #Hardcoded gensis block
    blockchain = [
        {
            "type": BLOCK,
            "id": "124059f656eb6b016ce36583b5d6e9fdaf82420355454a4e436f4ee2ff17dba7",
            "nonce": "5052bfab11df236c43a4d877d93e42a3",
            "pow": "000000be01b9e4b6fdd73985083174007c30a98dc0801eaa830e27bbbea0d705",
            "prev": "124059f656eb6b016ce36583b5d6e9fdaf82420355454a4e436f4ee2ff17dba7",
            "tx": {
                "type": TRANSACTION,
                "input": {
                    "id": "0000000000000000000000000000000000000000000000000000000000000000",
                    "n": 0
                },
                "sig": "33399ed9ba1cc40eb1395ef8826955398446badb9c7c84113d545806714809a013c73d71b3326041853638b1190443af",
                "output": [
                    {
                        "value": 50,
                        "pub_key": "c26cfef538dd15b6f52593262403de16fa2dc7acb21284d71bf0a28f5792581b4a6be89d2a7ec1d4f7849832fe7b4daa"
                    }
                ]
            }
        }
    ]
    utx = []
  
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(ZachCoinClient, self).__init__(host, port, id, callback, max_connections)

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)
        
    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + json.dumps(data,indent=2))

        if data != None:
            if 'type' in data:
                if data['type'] == self.TRANSACTION:
                    self.utx.append(data)
                elif data['type'] == self.BLOCKCHAIN:
                    self.blockchain = data['blockchain']
                elif data['type'] == self.UTXPOOL:
                    self.utx = data['utxpool']
                #TODO: Validate blocks
                elif data['type'] == self.BLOCK:
                    #Check all required fields
                    fields = ["type", "id", "nonce", "pow", "prev", "tx"]
                    fields_is_valid = True
                    for key in data.keys():
                        if key not in fields:
                            fields_is_valid = False
                    

                    #Validate block ID
                    id_is_valid = (hashlib.sha256(json.dumps(data['tx'], sort_keys=True).encode('utf8')).hexdigest() == data['id'])

                    #TODO: Verify prev block ID
                    prev_is_valid = False
                    if self.blockchain[-1]["id"] == data["prev"]:
                        prev_is_valid = True

                    #Compare pow with difficulty
                    pow_is_valid = int(data['pow'], 16) <= self.DIFFICULTY

                    #Verify transaction in block
                    tx_fields = ["type", "input", "sig", "output"]
                    trans_is_valid = True
                    for key in data["tx"].keys():
                        if not key in tx_fields:
                            trans_is_valid = False
                    for key in data["tx"]["input"]:
                        if not key in ["id", "n"]:
                            trans_is_valid = False
                    for key in data["tx"]["output"]:
                        if not key in ["value", "pubkey"]:
                            trans_is_valid = False
                    if int(data["tx"]["input"]["n"]) < len(data["tx"]["output"]):
                        trans_is_valid = False

                    #TODO: If all valid, then add to end of blockchain
                    if fields_is_valid & id_is_valid & prev_is_valid & pow_is_valid & trans_is_valid:
                        #Add to blockchain
                        self.blockchain = {**self.blockchain, **data}


    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop!")

#Code from Google Docs - Mining and Proof of Work
def mine_transaction(utx):
    nonce = Random.new().read(AES.block_size).hex()
    while( int( hashlib.sha256(json.dumps(utx, sort_keys=True).encode('utf8') + nonce.encode('utf-8')).hexdigest(), 16) > 0x000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
        nonce = Random.new().read(AES.block_size).hex()
    pow = hashlib.sha256(json.dumps(utx, sort_keys=True).encode('utf8') + nonce.encode('utf-8')).hexdigest()
   
    return pow, nonce

def main():

    if len(sys.argv) < 3:
        print("Usage: python3", sys.argv[0], "CLIENTNAME PORT")
        quit()

    #Load keys, or create them if they do not yet exist
    keypath = './' + sys.argv[1] + '.key'
    if not os.path.exists(keypath):
        sk = SigningKey.generate()
        vk = sk.verifying_key
        with open(keypath, 'w') as f:
            f.write(sk.to_string().hex())
            f.close()
    else:
        with open(keypath) as f:
            try:
                sk = SigningKey.from_string(bytes.fromhex(f.read()))
                vk = sk.verifying_key
            except Exception as e:
                print("Couldn't read key file", e)

    #Create a client object
    client = ZachCoinClient("127.0.0.1", int(sys.argv[2]), sys.argv[1])
    client.debug = False

    time.sleep(1)

    client.start()

    time.sleep(1)

    #Connect to server 
    client.connect_with_node(SERVER_ADDR, SERVER_PORT)
    print("Starting ZachCoin™ Client:", sys.argv[1])
    time.sleep(2)

    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        slogan = " You can't spell \"It's a Ponzi scheme!\" without \"ZachCoin\" "
        print("=" * (int(len(slogan)/2) - int(len(' ZachCoin™')/2)), 'ZachCoin™', "=" * (int(len(slogan)/2) - int(len('ZachCoin™ ')/2)))
        print(slogan)
        print("=" * len(slogan),'\n')
        x = input("\t0: Print keys\n\t1: Print blockchain\n\t2: Print UTX pool\n\t3: Create UTX\n\t4: Mine block\n\t5: Exit client\n\nEnter your choice -> ")
        try:
            x = int(x)
        except:
            print("Error: Invalid menu option.")
            input()
            continue
        if x == 0:
            print("sk: ", sk.to_string().hex())
            print("vk: ", vk.to_string().hex())
        elif x == 1:
            print(json.dumps(client.blockchain, indent=1))
            #print(client.blockchain[-1]["tx"]["output"][1])
        elif x == 2:
            count = 1
            for b in client.utx:
                print("------------------------------------------------------")
                print("UTX: ", count)
                print(json.dumps(b, indent=1))
                count += 1
            #print(json.dumps(client.utx, indent=1))
        # TODO: Add options for creating and mining transactions
        # as well as any other additional features
        elif x == 3:
            print("Enter block id: ")
            id = input()
            
            target = None
            for block in client.blockchain:
                if block["id"] == id:
                    target = block
            print(json.dumps(target["tx"]["output"], indent=1))

            print("Enter output: ")
            output = input()
            print(json.dumps(target["tx"]["output"][int(output) - 1], indent=1))
            bal = target["tx"]["output"][int(output) - 1]["value"]

            print("Enter amount: ")
            amount = input()
            if int(amount) > int(bal):
                print("Not enough coins.")
                break
            change = str(int(bal) - int(amount))

            print("Who to send to: ")
            ecdsa_pub_key = input()
            utx = None
            utx_input = {
                'input': {
                        'id': id,
                        'n': output
                    }
            }
            if int(change) > 0:
                print("Adding coinbase transaction...")
                utx = {
                    "type": 1,
                    'input': {  
                        'id': id,       #My block: 36a93fd20020f3382572f6e49eeb3cbbfafcbbbdcd3bf5e0fc4ad238003da416
                        'n': int(output)
                    },
                    'sig': sk.sign(json.dumps(utx_input['input'], sort_keys=True).encode('utf8')).hex(),
                    'output': [
                        {
                            'value': int(amount),
                            'pub_key': ecdsa_pub_key 
                        },
                        {
                            'value': int(change),
                            'pub_key': vk.to_string().hex() #7f5717b778615c1c1c4b1a63e171da6c5f6d5862a562cf5b98c124926414fc7f484f3478862b667bce82afc883c5e316
                        }
                    ]
                }
            else:
                print("Adding coinbase transaction...")
                utx = {
                    "type": 1,
                    'input': {
                        'id': id,
                        'n': int(output)
                    },
                    'sig': sk.sign(json.dumps(utx_input['input'], sort_keys=True).encode('utf8')).hex(),
                    'output': [
                        {
                            'value': int(amount),
                            'pub_key': ecdsa_pub_key
                        }
                    ]
                }

            print(json.dumps(utx, indent=1))

            print("Create transaction? (y/n)")
            answer = input()
            if answer  == 'y':
                client.send_to_nodes(utx)
            else:
                print("Canceling transaction...")

        elif x == 4:
            count = 1
            for b in client.utx:
                print("------------------------------------------------------")
                print("UTX: ", count)
                print(json.dumps(b, indent=1))
                count += 1

            print("Select UTX: ")
            index = int(input()) - 1
            u = client.utx[int(index)]

            u["output"].append({
                'value': client.COINBASE,
                'pub_key': vk.to_string().hex()
            })

            print("Mining block...")
            print(json.dumps(u, indent=1))
            pow, nonce = mine_transaction(u)
            #Get key using utx block id and 'n'
            tx = None
            n = int(u['input']['n'])
            for block in client.blockchain:
                if block["id"] == u['input']['id']:
                    tx = block['tx']
            pub_key = tx['output'][n]['pub_key']
            vk = VerifyingKey.from_string(bytes.fromhex(pub_key))
            assert vk.verify(bytes.fromhex(tx['sig']), json.dumps(tx['input'], sort_keys=True).encode('utf8'))
        
            #If valid, create a block from utx and append to blockchain
            new_tx = {"tx": u}
            print("NEW TX: ", new_tx)
            new_block = {
                "type": 0,
                "id": hashlib.sha256(json.dumps(new_tx['tx'], sort_keys=True).encode('utf8')).hexdigest(),
                "nonce": nonce,
                "pow": pow,
                "prev": client.blockchain[-1]["id"] #6833f475ffbc66704dbdc7bf2b8892c67107e680f4f3c6985362e8dd7303515a
            }

            new_block = {**new_block, **new_tx}
            client.send_to_nodes(new_block)
            client.blockchain.append(new_block)
            #print(json.dumps(new_block, indent=1))

            #Delete utx used from utx pool
            del client.utx[int(index)]
            client.send_to_nodes(client.utx)
            
            print("Finished.")

        elif x == 5:
            client.stop()
            break

        input()
        
if __name__ == "__main__":
    main()