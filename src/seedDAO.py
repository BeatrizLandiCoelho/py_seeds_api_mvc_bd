# ❤__________________________OMR___________________________________________ ❤

from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, declarative_base

# ❤____________________________CLASSE SEMENETE___________________________________________ ❤

from Seed import Semente

# ❤___________________________________CONEXAO___________________________________________ ❤

# Cria a conexão com o banco de dados
engine = create_engine('mysql+mysqldb://root:ubermensch@localhost/db_green_world?charset=utf8mb4&local_infile=1')

# Cria uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Cria a base declarativa
Base = declarative_base()

# Define a classe para a tabela


# Cria a tabela no banco de dados
Base.metadata.create_all(bind=engine)

# ❤________________________________________INSERT SMENTE_______________________________________ ❤

def inserir_semente(nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes):
    try:
        semente = Semente(
            nome=nome,
            quantidade_agua_por_regada=quantidade_agua,
            regadas_por_semana=regadas_por_semana,
            tempo_cultivo=tempo_cultivo,
            recomendacoes=recomendacoes
        )
        session.add(semente)
        session.commit()

        # Retorna os dados da semente em um dicionário
        dados_semente = {
            'id': semente.id,
            'nome': semente.nome,
            'quantidade_agua': semente.quantidade_agua_por_regada,
            'regadas_por_semana': semente.regadas_por_semana,
            'tempo_cultivo': semente.tempo_cultivo,
            'recomendacoes': semente.recomendacoes
        }

        return dados_semente

    except Exception as e:
        
        return None


#inserir_semente('Tomate', '2 litros', '2', 10, 'ficar longe do sol')

# ❤_______________________________DELETE BY ID_________________________________________________ ❤

def deletar_semente(id):

    try:
        # Encontra a semente pelo ID
        semente = session.get(Semente, id)
        
        if semente:
            # Remove a semente da sessão
            session.delete(semente)
            session.commit()

            return True
        
        else:
           return True
            
    except Exception as e:
       
        return False

 
#print(deletar_semente(106))
#❤______________________________________________UPDATE__________________________________________❤

def atualizar_semente(id, nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes):
    try:
        # Busca a semente pelo ID
        semente = session.get(Semente, id)

        if semente is None:
            # Caso a semente não seja encontrada, retorne False ou faça alguma tratativa de erro
            return False

        # Atualiza os atributos da semente
        semente.nome = nome
        semente.quantidade_agua_por_regada = quantidade_agua
        semente.regadas_por_semana = regadas_por_semana
        semente.tempo_cultivo = tempo_cultivo
        semente.recomendacoes = recomendacoes

        # Realiza o commit para salvar as alterações no banco de dados
        session.commit()

        # Cria um dicionário com os dados atualizados da semente
        semente_atualizada = {
            'id': semente.id,
            'nome': semente.nome,
            'quantidade_agua': semente.quantidade_agua_por_regada,
            'regadas_por_semana': semente.regadas_por_semana,
            'tempo_cultivo': semente.tempo_cultivo,
            'recomendacoes': semente.recomendacoes
        }

        # Retorna o dicionário com os dados atualizados
        return semente_atualizada

    except Exception as e:
        return False


#atualizar_semente(8, 'camomila', '3 litros', '3', 12, 'Nova recomendação')

#❤__________________________________BY ID__________________________________________________❤

def pegar_semente(id):
    try:
        # Busca a semente pelo ID
        semente = session.get(Semente, id)

        if semente is None:
            # Caso a semente não seja encontrada, retorne None ou faça alguma tratativa de erro
            return None

        # Cria um dicionário com os dados da semente
        dados_semente = {
            'id': semente.id,
            'nome': semente.nome,
            'quantidade_agua': semente.quantidade_agua_por_regada,
            'regadas_por_semana': semente.regadas_por_semana,
            'tempo_cultivo': semente.tempo_cultivo,
            'recomendacoes': semente.recomendacoes
        }

        # Retorna o dicionário com os dados da semente
        return dados_semente

    except Exception as e:
     
        return False

#print(pegar_semente(10))

#❤________________________________________TODAS SEMNETES________________________________________❤

def pegar_todas_sementes():
    try:
        # Consulta todas as instâncias da classe Semente
        todas_sementes = session.query(Semente).all()

        # Cria uma lista para armazenar os dados de todas as sementes
        lista_sementes = []

        # Itera sobre as instâncias da classe Semente e cria um dicionário com os dados de cada semente
        for semente in todas_sementes:
            dados_semente = {
                'id': semente.id,
                'nome': semente.nome,
                'quantidade_agua': semente.quantidade_agua_por_regada,
                'regadas_por_semana': semente.regadas_por_semana,
                'tempo_cultivo': semente.tempo_cultivo,
                'recomendacoes': semente.recomendacoes
            }
            lista_sementes.append(dados_semente)

        # Retorna a lista de sementes
        return lista_sementes

    except Exception as e:
        
        return False

#print(pegar_todas_sementes())

# ❤________________________________________GET SEMENETE BY NAME___________________________________________________ ❤

def pegar_semente_por_nome(nome):
    try:
        # Query the seed by name
        semente = session.query(Semente).filter_by(nome=nome).first()

        if semente is None:
            # If the seed is not found, return None or handle the error accordingly
            return None

        # Create a dictionary with the seed data
        dados_semente = {
            'id': semente.id,
            'nome': semente.nome,
            'quantidade_agua': semente.quantidade_agua_por_regada,
            'regadas_por_semana': semente.regadas_por_semana,
            'tempo_cultivo': semente.tempo_cultivo,
            'recomendacoes': semente.recomendacoes
        }

        # Return the dictionary with the seed data
        return dados_semente

    except Exception as e:
        return None

#print(pegar_semente_por_nome('Tomate'))



