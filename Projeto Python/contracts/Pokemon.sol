// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Pokemon {

    // ATTRIBUTES
    string name;
    uint8 life;
    uint8 attack;
    uint8 defense;
    address owner;

    // MODIFIERS
    modifier isOwner{
        require(owner == msg.sender);
        _;
    }

    // EVENTS
    event ownerChanged(address oldOwner, address newOwner);

    // FUNCTIONS
    constructor (string memory _name, uint8 _attack, uint8 _defense) {
        life = 100;
        name = _name;
        attack = _attack;
        defense = _defense;
        owner = msg.sender;
    }

    function changeOwner(address newOwner) public isOwner {
        address oldOwner = owner;
        owner = newOwner;
        emit ownerChanged(oldOwner, newOwner);
    }

    function takeDamage(uint8 damage) public {
        life -= damage;
        if (life < 0) life = 0;
    }

    function getName() view public returns(string memory) {
        return name;
    }
    
    function getOwner() view public returns(address) {
        return owner;
    }
    
    function getLife() view public returns(uint8) {
        return life;
    }

    function getAttack() view public returns(uint8) {
        return attack;
    }

    function getDefense() view public returns(uint8) {
        return defense;
    }


}