from seedDAO import inserir_semente,pegar_semente,pegar_todas_sementes,atualizar_semente,deletar_semente, pegar_semente_por_nome
from tools import ERRROR_INTERANL_ERRO, ERROR_BAD_REQUEST,NOT_FOUND,SUCESS

# ❤_________________________________INSERT___________________________________________________________ ❤


def add_nova_semente(nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes):
    try:
        # Verifica se os campos quantidade_agua, regadas_por_semana e tempo_cultivo são números
        if (
            not quantidade_agua.isdigit() or
            not regadas_por_semana.isdigit() or
            not tempo_cultivo.isdigit() or

            nome == '' or
            len(nome) > 89 or

            len(recomendacoes) > 700

              ):
            return 400, ERROR_BAD_REQUEST

        # Converte as strings para números
        quantidade_agua = int(quantidade_agua)
        regadas_por_semana = int(regadas_por_semana)
        tempo_cultivo = int(tempo_cultivo)

        #nome lower
        nome = nome.lower()
        recomendacoes = recomendacoes.lower()


        semente = inserir_semente(nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes)
        
        if semente is not None:
            return 201, semente
        else:
            return 500, ERRROR_INTERANL_ERRO

    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO
 
#inserir_semente('Tomate', '2 litros', '2', 10, 'ficar longe do sol')
#print(add_nova_semente('AMENDOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAljnvjwnwnvjrnvkjnwrbrwfkvwkjrnrkkrkjv hw ihwc kwrchhk', '2', '2', '10', 'ficar longe do sol'))
#print(inserir_semente('AMENDOA', '2 litros', '2', 10, 'ficar longe do sol'))

nome = 'AMENDOA'



# ❤________________________________________GET SEMENETE ID___________________________________________________ ❤

def get_semente(id):
    if id.isdigit() == False:
        return 400, ERROR_BAD_REQUEST

    try:
        semente = pegar_semente(id)
        if semente is not None:
            # Concatenate "ml" to water quantity
            semente['quantidade_agua'] = str(semente['quantidade_agua']) + " ml"

            # Concatenate "dias" to cultivation time
            semente['tempo_cultivo'] = str(semente['tempo_cultivo']) + " dias"

            return 200, semente
        
        else:
            return 404, NOT_FOUND
        
    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO

#print(get_semente('16'))
    
# ❤________________________________________GET TODAS SEMENTES___________________________________________________ ❤

def get_todas_sementes():
    try:
        sementes = pegar_todas_sementes()

        if sementes is not None:
            # Iterate over the list of seeds and concatenate "ml" and "dias" to the respective fields
            for semente in sementes:
                semente['quantidade_agua'] = str(semente['quantidade_agua']) + " ml"
                semente['tempo_cultivo'] = str(semente['tempo_cultivo']) + " dias"

            return 200, sementes
       
        else:
            return 500, ERRROR_INTERANL_ERRO

    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO

#print(get_todas_sementes())

# ❤________________________________________UPDATE SEMENTE BY ID___________________________________________________ ❤

#
def update_semente(id, nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes):
    try:
        if not id.isdigit():
            return 400, ERROR_BAD_REQUEST
        
        if not quantidade_agua.isdigit() or not regadas_por_semana.isdigit() or not tempo_cultivo.isdigit():
            return 400, ERROR_BAD_REQUEST
        
        id = int(id)
        quantidade_agua = int(quantidade_agua)
        regadas_por_semana = int(regadas_por_semana)
        tempo_cultivo = int(tempo_cultivo)

        if pegar_semente(id) is None:
            return 404, NOT_FOUND

        semente = atualizar_semente(id, nome, quantidade_agua, regadas_por_semana, tempo_cultivo, recomendacoes)

        if semente is not None:
            # Concatenate "ml" and "dias" to the respective fields
            semente['quantidade_agua'] = str(semente['quantidade_agua']) + " ml"
            semente['tempo_cultivo'] = str(semente['tempo_cultivo']) + " dias"

            return 200, semente
        else:
            return 404, NOT_FOUND

    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO



#print(update_semente('17', 'banana', '300', '3', '15', 'New recommendation'))

# ❤________________________________________DELETE SEMENTE BY ID___________________________________________________ ❤
#status, result = 
def delete_semente_por_id(id):
    try:
        if not id.isdigit():
            return 400, ERROR_BAD_REQUEST
   
   
        id = int(id)

        if pegar_semente(id)== None:
           return 404, NOT_FOUND
        
        success = deletar_semente(id)

        if success == True:
            return 200, SUCESS
        else:
            return 404, NOT_FOUND

    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO
    
#print(delete_semente_por_id("11")) 

# ❤________________________________________DELETE SEMENTE BY NAME___________________________________________________ ❤

def get_semente_nome(nome):

    if nome == '' or len(nome)>89:
        return 400, ERROR_BAD_REQUEST

    try:
        nome =nome.lower()
        semente = pegar_semente_por_nome(nome)
        if semente is not None:
            # Concatenate "ml" to water quantity
            semente['quantidade_agua'] = str(semente['quantidade_agua']) + " ml"

            # Concatenate "dias" to cultivation time
            semente['tempo_cultivo'] = str(semente['tempo_cultivo']) + " dias"

            return 200, semente
        
        else:
            return 404, NOT_FOUND
        
    except Exception as e:
        return 500, ERRROR_INTERANL_ERRO

#print(get_semente_nome('bananaaaaaijfoiawjoijcwoocfnuerhviueqhrnuhnveverejrh 3ugjj gic 3u4hivhwfgiurgwrfhiruvnsirfvnrvnoervriejgiajrliajglienl'))
