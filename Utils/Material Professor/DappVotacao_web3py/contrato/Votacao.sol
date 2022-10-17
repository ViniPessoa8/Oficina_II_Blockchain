// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Votacao {
   
    address internal admin;
    
    struct Eleitor {
        address idEleitor;
        bool statusDoVoto;              
    }

     struct Candidato {
        string nome;
        uint256 qtDeVotos;              
    }
    Candidato[]  public candidatos;

    mapping(address => Eleitor) public eleitores;    
   
    constructor() {
        candidatos.push(Candidato("Pedro", 0));
        candidatos.push(Candidato("Maria", 0));
        candidatos.push(Candidato("Jose", 0));
        candidatos.push(Candidato("Ana", 0));        
        candidatos.push(Candidato("Paulo", 0));
        candidatos.push(Candidato("Soraya", 0));
                 
        admin = msg.sender;      
    }

    function registrarEleitor(address _eleitor) public  {
        require(
            msg.sender == admin,
            "Somenente o admin pode dar a permissao para votar."
        );
        eleitores[_eleitor].statusDoVoto = false;
        eleitores[_eleitor].idEleitor = _eleitor;
    }

    function votar(string memory _candidato) public {
        
        require(eleitores[msg.sender].idEleitor == msg.sender, "Voce nao tem permissao para votar");
        
        bool candidatoEncontrado = false;

        Eleitor storage eleitor = eleitores[msg.sender];
        require(!eleitor.statusDoVoto, "Voce ja votou");

        for(uint256 i = 0; i < candidatos.length; i++){            
            if (keccak256(abi.encodePacked(candidatos[i].nome)) == keccak256(abi.encodePacked(_candidato))){
                  candidatos[i].qtDeVotos = candidatos[i].qtDeVotos + 1;
                  eleitor.statusDoVoto = true; 
                  candidatoEncontrado = true;
                  break;   
            }else{
                 candidatoEncontrado = false;
            } 
        }
        if(candidatoEncontrado == false){
             revert("Candidado nao existe.");
        }           
                        
    }  