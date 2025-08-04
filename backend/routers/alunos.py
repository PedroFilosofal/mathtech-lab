from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import database
from backend.crud import alunos as crud_alunos 

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)

# Dependência para obter o banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{aluno_id}")
def obter_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud_alunos.obter_aluno_por_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.put("/{aluno_id}")
def atualizar_aluno(aluno_id: int, nome: str, email: str, turma: str, db: Session = Depends(get_db)):
    aluno = crud_alunos.atualizar_aluno(db, aluno_id, nome, email, turma)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado para atualização")
    return aluno

@router.delete("/{aluno_id}")
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud_alunos.deletar_aluno(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado para exclusão")
    return {"detail": "Aluno deletado com sucesso"}