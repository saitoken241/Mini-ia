arv = {
    "pergunta": "febre?",
    "sim": {
        "pergunta": "febre alta?",
        "sim": {
            "pergunta": "tosse produtiva?",
            "sim": {
                "pergunta": "catarro amarelo?",
                "sim": {
                    "pergunta": "dor toracica?",
                    "sim": {"diagnostico": "DOR TORACICA -> pneumonia/bronquite"},
                    "nao": {"diagnostico": "DORES NO CORPO -> influenza/virose"}
                },
                "nao": {
                    "pergunta": "dor de garganta?",
                    "sim": {"diagnostico": "ENGOLIR -> amigdalite/abscesso"},
                    "nao": {"diagnostico": "MANCHAS NA PELE -> sarampo/infecção"}
                }
            },
            "nao": {
                "pergunta": "dor de garganta?",
                "sim": {"diagnostico": "ENGOLIR -> amigdalite/abscesso"},
                "nao": {"diagnostico": "MANCHAS NA PELE -> sarampo/infecção"}
            }
        },
        "nao": {
            "pergunta": "coriza?",
            "sim": {
                "pergunta": "olhos vermelhos?",
                "sim": {"diagnostico": "ESPIRROS -> rinite/conjuntivite"},
                "nao": {"diagnostico": "DOR NO CORPO -> resfriado/rinossinusite"}
            },
            "nao": {
                "pergunta": "fadiga?",
                "sim": {"diagnostico": "ESPIRROS -> COVID/ASTENIA"},
                "nao": {"diagnostico": "TONTURA -> pressao baixa/febre"}
            }
        }
    },
    "nao": {
        "pergunta": "tosse?",
        "sim": {
            "pergunta": "tosse seca?",
            "sim": {
                "pergunta": "piora a noite?",
                "sim": {"diagnostico": "HISTORICO DE ASMA -> ASMA/TOSSE ALERGICA"},
                "nao": {"diagnostico": "ROUQUIDAO -> laringite/tosse"}
            },
            "nao": {
                "pergunta": "catarro transparente?",
                "sim": {"diagnostico": "CHIADO -> bronquite/catarro"},
                "nao": {"diagnostico": "FUMA -> bronquite/infecção"}
            }
        },
        "nao": {
            "pergunta": "dor de garganta?",
            "sim": {
                "pergunta": "consegue engolir?",
                "sim": {"diagnostico": "PLACAS -> amigdalite/faringite"},
                "nao": {"diagnostico": "INCHAÇO -> abscesso/faringite"}
            },
            "nao": {
                "pergunta": "falta de ar?",
                "sim": {"diagnostico": "PIORA DEITADO -> cardiaco/ansiedade"},
                "nao": {"diagnostico": "DORES NO CORPO -> fadiga/saudavel"}
            }
        }
    }
}
def preorder(no):
    
    if "diagnostico" in no:
        return [f"⇒ {no['diagnostico']}"]
    pergunta = no.get("pergunta")
    atual = [pergunta] if pergunta else []
    return atual + preorder(no.get("sim")) + preorder(no.get("nao"))
def inorder(no):
    
    if "diagnostico" in no:
        return [f"⇒ {no['diagnostico']}"]
    pergunta = no.get("pergunta")
    atual = [pergunta] if pergunta else []
    return   inorder(no.get("sim"))+ atual + inorder(no.get("nao"))
def posorder(no):
    
    if "diagnostico" in no:
        return [f"⇒ {no['diagnostico']}"]
    pergunta = no.get("pergunta")
    atual = [pergunta] if pergunta else []
    return   posorder(no.get("sim")) + posorder(no.get("nao")) + atual
preordem = preorder(arv)
inordem = inorder(arv)
posordem = posorder(arv)

#• Pré-ordem: raiz → esquerda → direita
#• In-ordem: esquerda → raiz → direita
#• Pós-ordem: esquerda → direita → raiz
print("Pre-ordem:", " | ".join(preordem))
print("In-ordem:", " | ".join(inordem))
print("Pos-ordem:", " | ".join(posordem))
