#tratando uma api
usuario = {
    'nome':'João',
    'redes':[{
        'nome':'facebook',
        'imagem_profile':"",
        'imagem_capa':"imagem1",
    }, {
        'nome':"twitter",
        "imagem_profile":"imagem2",
        "imagem_capa":""
    }]
}

#retorna imagem do profile
def get_imagem_profile(usario):
    for rede in usario['redes']:
        if rede[imagem_profile]:
            return rede['imagem_profile']
    return 'default'

#retorna imagem de capa
def get_imagem_capa(usuario):
    for rede in usuario['redes']:
        if rede[imagem_capa]:
            return rede["imagem_capa"]
    return "default"

#utilizando partial
from functools import partial
def get_imagem(qual_imagem,usuario):
    for rede in usuario["redes"]:
        if rede[qual_imagem]:
            return rede[qual_imagem]
    return "default"

get_imagem_profile = partial(get_imagem,"imagem_profile")
get_imagem_capa = partial(get_imagem, "imagem_capa")

print("\nsaida partial final")
print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario))