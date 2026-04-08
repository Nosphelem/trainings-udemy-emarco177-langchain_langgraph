import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()



def main():
    print("Hello from langchain-course!")

    info = """
    Margaret Heafield Hamilton, née Margaret Heafield le 17 août 1936[1], est une informaticienne, ingénieure système et cheffe d'entreprise américaine. Elle était directrice du département génie logiciel (« software engineering », terme de son invention[2]) au sein du MIT Instrumentation Laboratory qui conçut le système embarqué du programme spatial Apollo[3]. En 1986, elle fonde la société Hamilton Technologies, Inc. à partir de ses travaux entrepris au MIT.
    Margaret Heafield Hamilton est née à Paoli dans l'Indiana, États-Unis ; elle est la fille de Kenneth Heafield et Ruth Esther Heafield (née Partington)[4],[5]. Après avoir fini ses études secondaires à la Hancock High School, en 1954[6], elle étudie les mathématiques à l'Université du Michigan en 1955, avant d'obtenir sa licence (Bachelor of Arts) de mathématiques au sein du Earlham College en 1958 (mineure en philosophie)[7],[8].
    Elle déménage dans l'État du Massachusetts avec l'intention de poursuivre des études de Mathématiques pures à l'Université Brandeis mais finalement choisit d'intégrer le MIT en 1959 et faire ses premiers pas d'informaticienne en développant des programmes de prévision météorologique[9]sur des ordinateurs Royal McBee LGP-30 (en)[10] et PDP-1[11],[1] pour le professeur Edward Lorenz.
    De 1961 à 1963 elle travaille sur le projet militaire SAGE au laboratoire Lincoln du MIT où elle développe des programmes de détection d'avions sur l'ordinateur géant AN/FSQ-7 (en). Elle rejoint en 1963 le Laboratoire Charles Stark Draper du MIT (en).
    Au laboratoire Draper elle travaille pour les missions du programme Apollo de la NASA sur les logiciels embarqués dans les vaisseaux spatiaux qui doivent prendre en charge la navigation et l'atterrissage sur la Lune. Elle devient responsable de l'équipe chargée du développement du logiciel embarqué utilisé par les missions Apollo puis Skylab[3]. Elle acquiert ainsi une solide expérience sur la conception des logiciels à une époque où les méthodes de gestion et de conception des projets informatiques en sont à leur balbutiement.
    Dans le cadre de ces projets informatiques, son domaine d'expertise concerne la conception de système et de développement de logiciels, la modélisation de processus, la conception de systèmes de prévention, le paradigme de développement, les systèmes formels et des langages informatiques de modélisation, la conception et de la programmation orientée objet, la gestion automatisée des cycles de vie, les méthodes de fiabilisation et de réutilisation des logiciels, l'analyse de domaine, l'exactitude de propriétés linguistiques intégrées, les techniques d'architecture ouverte pour des systèmes robustes, l'automatisation du cycle de vie complet, l'assurance qualité, l'intégration transparente, les systèmes distribués, les techniques de détection d'erreur et de récupération, les systèmes d'interface homme-machine, les systèmes d'exploitation, les techniques de test bout en bout et des techniques de gestion du cycle de vie[3].
    Elle innove dans le domaine du processus de construction des programmes de vols et de leur environnement de développement, en normalisant et en rationalisant ces processus dans toutes les phases de développement, qui sont réutilisés de version en version, ou entre les logiciels du LM (module lunaire) et du CM (module de commande), jusqu'au programme Skylab[3].
    """

    summary_template = """
    Given the information {info} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5.4-nano")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"info": info})
    print(response.content)

if __name__ == "__main__":
    main()
