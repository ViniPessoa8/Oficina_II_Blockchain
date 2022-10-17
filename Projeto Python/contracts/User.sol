pragma solidity ^0.8.17;

contract User {

    address userHash;
    string[] pokemons;

    // CONSTRUCTOR
    constructor() {
        userHash = msg.sender;
        pokemons = ["pikachu", "charizard", "squirtle"];
    }

    // MODIFIERS
    modifier isOwner{
        require(userHash == msg.sender);
        _;
    }

    modifier hasPokemon(string calldata pokemonName) {
        require(getPokemonIndex(pokemonName) >= 0, "You don't have this pokemon.");
        _;
    }

    // FUNCTIONS
    function addPokemon(string memory name) public isOwner {
        pokemons.push(name);
    }

    function getPokemons() view public isOwner returns(string[] memory) {
        return pokemons;
    }

    function getPokemonNum() view public isOwner returns(uint) {
        // DOESN'T WORK AFTER REMOVING LIST ITEM
        return pokemons.length;
    }

    function removePokemon(string calldata _name) public isOwner {
        // Check if pokemon exists
        int index = getPokemonIndex(_name); 
        if (index < 0) return;

        // remove pokemon
        delete pokemons[uint(index)];
    }

    function getPokemonIndex(string calldata pokemonName) view public isOwner returns(int){
        /* 
        Check if current user already have a given pokemon and returns it's index.
        
        Parameters
            pokemonName: string - name of the pokemon to search for on users list.

        Return
            Pokemon's index on list if found, -1 otherwise. 
        */
        for (uint i = 0; i <= pokemons.length - 1; i+=1){
            if (keccak256(bytes(pokemonName)) == keccak256(bytes(pokemons[i]))) { // Comparing strings 
                return int(i);        
            }
        }
        return -1;
    }

}