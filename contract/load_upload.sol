pragma solidity ^0.4.18;
contract download_upload {

    address addr1;
    uint public dataIndex;
    mapping(address => mapping(uint => Data)) stores;
    mapping(uint => address) dataInStore;

    struct Data{//fangwu房屋duixiang房屋对象
        uint  id;   //fanmgwu房屋 ID
        string name;
        string imageLink;//tupian图片 HASH
        address ad;
    }
function upload(string name,string imageLink) public {
       dataIndex += 1 ;
       Data memory data_ = Data(dataIndex,name,imageLink,addr1) ;
       stores[msg.sender][dataIndex]=data_;
       dataInStore[dataIndex] = msg.sender;
}

//提取出来
       function download(uint id) view public returns(uint,string,string,address){
       Data memory data_ = stores[dataInStore[id]][id];
       return(data_.id,data_.name,data_.imageLink,addr1);
    }
}