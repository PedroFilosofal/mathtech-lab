from sqlalchemy.orm import Session
from backend import models  # ajuste conforme o nome da sua pasta

# Criar aluno
def criar_aluno(db: Session, nome: str, email: str, turma: str):
    novo_aluno = models.Student(name=nome, email=email, turma=turma)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

# Listar todos os alunos
def listar_alunos(db: Session):
    return db.query(models.Student).all()

# Obter aluno por ID
def obter_aluno_por_id(db: Session, aluno_id: int):
    return db.query(models.Student).filter(models.Student.id == aluno_id).first()

# Atualizar aluno
def atualizar_aluno(db: Session, aluno_id: int, nome: str, email: str, turma: str):
    aluno = db.query(models.Student).filter(models.Student.id == aluno_id).first()
    if aluno:
        aluno.name = nome
        aluno.email = email
        aluno.turma = turma
        db.commit()
        db.refresh(aluno)
    return aluno

# Deletar aluno
def deletar_aluno(db: Session, aluno_id: int):
    aluno = db.query(models.Student).filter(models.Student.id == aluno_id).first()
    if aluno:
        db.delete(aluno)
        db.commit()
    return aluno