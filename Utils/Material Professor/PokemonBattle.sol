//Autor: Prof. Fabio Santos (fssilva@uea.edu.br)
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract PokemonBattle {
    
    struct Pokemon{
       string name;
       uint LifeLevel;
       uint attackEnergy;
       uint defenseEnergy;
       address owner;
       string uri;
    }

    Pokemon[] private pokemonList; 
    address gameOwner;

    event winner(uint256 pokemon_1, uint256 pokemon_2);

    constructor() {
        gameOwner = msg.sender;       
    }
    
    modifier onlyOwnerOf(uint _pokemonId) {
        require(pokemonList[_pokemonId].owner == msg.sender, "Deve ser o proprietario do Pokemon para batalhar");
        _;
    }

    function createPokemon(string memory _name, address _owner, string memory _uri) public {
       //uint pokemeoneId = pokemeList.length;
       pokemonList.push(Pokemon(_name, 1, 100, 100, _owner, _uri));
       
    }

    function battle(uint _pokemonId_1, uint _pokemonId_2) onlyOwnerOf(_pokemonId_1) public {

       Pokemon storage pokemon_1 =  pokemonList[_pokemonId_1];
       Pokemon storage pokemon_2 =  pokemonList[_pokemonId_2];

       if (pokemon_1.attackEnergy >= pokemon_2.defenseEnergy) {
           pokemon_1.LifeLevel +=1;
           pokemon_1.attackEnergy +=10; 
           pokemon_2.LifeLevel -=1; 
           pokemon_2.defenseEnergy -=10;         
       } else {
            pokemon_2.LifeLevel +=1;            
            pokemon_2.defenseEnergy +=10;
            pokemon_1.LifeLevel -=1; 
            pokemon_1.attackEnergy -=10;  
       }

       emit winner(pokemon_1.LifeLevel, pokemon_2.LifeLevel);
    }

    
    function getListPokemon() view public returns (Pokemon[] memory) {
        return pokemonList;
    }

    function gePokemon(uint _pokemonId) view public returns (Pokemon memory) {
        return pokemonList[_pokemonId];
    }
}