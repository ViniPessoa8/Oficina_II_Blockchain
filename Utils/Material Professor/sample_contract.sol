pragma solidity ^0.8.17;

contract simpleStorage{
    uint data;

    function set(uint parameter) public{
        data = parameter;
    }

    function get() public returns(uint) {
        return data;
    }
}
