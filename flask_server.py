false = 1
true = 2
a1 = [
    {
        "constant": false,
        "inputs": [],
        "name": "Datamodel",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_key",
                "type": "bytes32"
            },
            {
                "name": "timestamp",
                "type": "uint256"
            },
            {
                "name": "sender",
                "type": "address"
            },
            {
                "name": "version",
                "type": "uint256"
            },
            {
                "name": "hash",
                "type": "bytes32"
            }
        ],
        "name": "setData",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "name": "allowedMap",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_key",
                "type": "bytes32"
            },
            {
                "name": "extend",
                "type": "bytes1[512]"
            }
        ],
        "name": "setExtend",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "allowedArray",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_key",
                "type": "bytes32"
            }
        ],
        "name": "getData",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            },
            {
                "name": "",
                "type": "address"
            },
            {
                "name": "",
                "type": "uint256"
            },
            {
                "name": "",
                "type": "bytes32"
            },
            {
                "name": "",
                "type": "bytes1[512]"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_address",
                "type": "address"
            }
        ],
        "name": "denyAccess",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_address",
                "type": "address"
            }
        ],
        "name": "allowAccess",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "name": "_handler",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "_address",
                "type": "address"
            }
        ],
        "name": "AddressAllowed",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "name": "_handler",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "_address",
                "type": "address"
            }
        ],
        "name": "AddressDenied",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "_handler",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "timestamp",
                "type": "uint256"
            },
            {
                "indexed": true,
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "version",
                "type": "uint256"
            },
            {
                "indexed": false,
                "name": "hash",
                "type": "bytes32"
            }
        ],
        "name": "DataSaved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "_handler",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "extend",
                "type": "bytes1[512]"
            }
        ],
        "name": "ExtendSaved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "_handler",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "version",
                "type": "uint256"
            },
            {
                "indexed": false,
                "name": "extend",
                "type": "bytes1[512]"
            }
        ],
        "name": "ExtendNotSave",
        "type": "event"
    }
]
a2 =[
	{
		"constant": false,
		"inputs": [
			{
				"name": "a",
				"type": "uint256"
			},
			{
				"name": "b",
				"type": "uint256"
			}
		],
		"name": "multiply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
a2 =[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "greeting",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]