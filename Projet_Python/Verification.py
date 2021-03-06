#Vérifier les différents attributs des bases de données

#Fonction "Verification" pour vérifier si la population est inscrite sous forme numérique et vérifier si le format original
#a été conservé

def Verification(data):
    
    #Effectuer une division du nombre total de crimes pour les 4 quartiles par la population de la ville de Florence, Alabama
    try:
        reponse = ((data.loc[0]["1st quarter"]+data.loc[0]["2nd quarter"]+data.loc[0]["3rd quarter"]+
                    data.loc[0]["4th quarter"])/(data.loc[0][-1]))*100
    
    #Si la division est impossible, l'erreur est retournée et la population n'est donc pas inscrite sous forme numérique
    except Exception as e:
        print('Erreur détectée : ', e)
    
    #Sinon, le résultat de la division est calculé
    else:
        print('Le nombre de crimes représente le pourcentage suivant de la population de Florence, Alabama:', reponse)
    
    #Instruction finale pour montrer que la vérification est terminée
    finally:
        print('Exécution finale')
    
    #Si le nombre de colonnes ne correspond pas à celui du format original, l'exception est retournée
    if len(data.loc[0]) > 15:
        raise Exception ("Attention, le nombre de colonnes de la base de données a été modifié.")