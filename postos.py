from fastapi import APIRouter, HTTPException
from typing import List
from Vacinacao.models import PostoVacinacao
from fastapi.responses import JSONResponse



router = APIRouter(prefix="/postos-vacinacao", tags=["Postos de Vacinação"])

postos_vacinacao = [
    {
        "id": 1,
        "cidade": "Maceió",
        "nome": "Posto A",
        "endereco": "Av. Brasil, 123",
        "horario": "08:00 - 17:00",
        "vacinas": ["BCG", "Hepatite B"],
    },
    {
        "id": 2,
        "cidade": "Arapiraca",
        "nome": "Posto B",
        "endereco": "Av. Asa Branca, 321",
        "horario": "09:00 - 16:00",
        "vacinas": ["Febre Amarela", "Gripe"],
    },
    {
        "id": 3,
        "cidade": "Rio Largo",
        "nome": "Posto C",
        "endereco": "Praça da República, 999",
        "horario": "07:00 - 15:00",
        "vacinas": ["COVID-19", "HPV"],
    }
]

# listar postos
@router.get("/", response_model=List[PostoVacinacao])
def listar_postos():
        return JSONResponse(content=postos_vacinacao, media_type="application/json; charset=utf-8")


# criar novos postos
@router.post("/", response_model=PostoVacinacao)
def criar_posto(posto: PostoVacinacao):
    novo_posto = posto.model_dump()  
    novo_posto["id"] = len(postos_vacinacao) + 1  
    postos_vacinacao.append(novo_posto)
    return PostoVacinacao(**novo_posto)

# deletar postos por ID
@router.delete("/{id}", response_model=dict)
def deletar_posto(id: int):
    global postos_vacinacao
    posto = next((posto for posto in postos_vacinacao if posto["id"] == id), None)
    if not posto:
        raise HTTPException(status_code=404, detail="Posto não encontrado")
    postos_vacinacao = [p for p in postos_vacinacao if p["id"] != id]
    return {"message": f"Posto com ID {id} foi removido com sucesso"}

# pesquisar por cidade
@router.get("/cidade/{cidade}", response_model=List[PostoVacinacao])
def listar_postos_por_cidade(cidade: str):
    resultado = [posto for posto in postos_vacinacao if posto["cidade"].lower() == cidade.lower()]
    if not resultado:
        raise HTTPException(status_code=404, detail="Nenhum posto encontrado")
    return resultado

# pesquisar pelo ID
@router.get("/{id}", response_model=PostoVacinacao)
def obter_posto_por_id(id: int):
    posto = next((posto for posto in postos_vacinacao if posto["id"] == id), None)
    if not posto:
        raise HTTPException(status_code=404, detail="Nenhum posto encontrado")
    return posto
