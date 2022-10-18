pragma solidity ^0.8.17;

contract Pokemon {

    string name;
    uint8 life;
    uint8 attack;
    uint8 defense;
    address owner;

    constructor (string memory _name, uint8 _attack, uint8 _defense) {
        life = 100;
        name = _name;
        attack = _attack;
        defense = _defense;
        owner = msg.sender;
    }

    

}