#python -m venv venv
#.\venv\Scripts\activate

#❤❤❤framework flask he is just like express❤❤❤
from flask import Flask, make_response, request,jsonify


#❤❤❤camila❤❤❤

from seed_controller import get_todas_sementes,get_semente_nome,get_semente,update_semente,delete_semente_por_id

#instance the framework
app = Flask(__name__)

#❤________________________________________________________________❤#


@app.route("/v2/greens-world/bring-all-seeds",methods=['GET'])
def bring_all_seeds():

    operatio_status, seed_data =get_todas_sementes()

    return make_response(

        jsonify(
            data= seed_data,
            status= operatio_status
        )
    )

#❤_________________________________name_______________________________❤#

@app.route("/v2/greens-world/bring-seeds-by-name",methods=['POST'])
def bring_seed_by_name():

    seed_name = request.json['nome_seed']
    operatio_status, seed_data = get_semente_nome(seed_name)

    return make_response(

        jsonify(
            data= seed_data,
            status= operatio_status
        )
    )

#❤_________________________________id_______________________________❤#

@app.route("/v2/greens-world/bring-seeds-by-id",methods=['POST'])
def bring_seed_by_id():

    id = request.json['id_semente']
    operatio_status, seed_data = get_semente(id)

    return make_response(

        jsonify(
            data= seed_data,
            status= operatio_status
        )
    )
#❤_________________________________id_______________________________❤#

@app.route("/v2/greens-world/update-seed",methods=['POST'])
def update_seed_by_id():

    id = request.json['id']
    name = request.json['novo_nome']
    water = request.json['nova_quantidade_agua']
    watering = request.json['novas_regadas_por_semana']
    time = request.json['novo_tempo_cultivo']
    recomendation = request.json['novas_recomendacoes']
    
    operatio_status, seed_data = update_semente(id, name, water, watering, time, recomendation)

    return make_response(

        jsonify(
            data= seed_data,
            status= operatio_status
        )
    )
#❤_________________________________update_______________________________❤#

@app.route("/v2/greens-world/delete-seeds-by-id",methods=['DELETE'])
def delete_seed_by_id():

    id = request.json['id_semente']
    operatio_status, seed_data = delete_semente_por_id(id)

    return make_response(

        jsonify(
            data= seed_data,
            status= operatio_status
        )
    )
app.run(debug=True, port=8181)

 #pip freeze > "requirements.txt"