# Hydrogéologie
#### Hydrologie des eaux souterraines Livre de David Keith Todd

## Sommaire
Cette application est une solution pour les relations d'hydrologie et de processus de contamination avec différentes utilisations en travaillant simplement dessus avec une navigation fluide.

## Fonctionnalités
#### Écoulement Permanent Unidirectionnel:

Nappe Captive: 

![v=\frac{hk}{x}](https://latex.codecogs.com/svg.latex?\Large&space;v=\frac{hk}{x})

Nappe Libre: 
    
![q=\frac{k}{2x}({h_0^2-h^2})](https://latex.codecogs.com/svg.latex?\Large&space;q=\frac{k}{2x}({h_0^2-h^2}))
    
#### Étiage:

Localisation de la ligne de partage d'eau souterraine (d):

![d=\frac{L}{2}-\frac{K}{W}\frac{({h_0^2-h^2})}{2L}](https://latex.codecogs.com/svg.latex?\Large&space;d=\frac{L}{2}-\frac{K}{W}\frac{({h_0^2-h^2})}{2L})
    
Hauteur Pièzometrique maximale au niveau de la ligne de partage d'eau ![h_{max}](https://latex.codecogs.com/svg.latex?\Large&space;h_{max}):

![h_{max}=\sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{K}{W}(L-d)d}](https://latex.codecogs.com/svg.latex?\Large&space;h_{max}=\sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{K}{W}(L-d)d})
    
Temps de déplacement a partir la ligne de partage d'eau souterraine vers les deux rivières (t):

![t_a=\frac{L_a}{v_a}=\frac{L_a}{(\frac{k}{n})(\frac{\Delta{h}}{\Delta{x}})}](https://latex.codecogs.com/svg.latex?\Large&space;t_a=\frac{L_a}{v_a}=\frac{L_a}{(\frac{k}{n})(\frac{\Delta{h}}{\Delta{x}})})
    
Débit quotidien par Kilométrer de la nappe vers les deux rivières (q):

![q=\frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x)](https://latex.codecogs.com/svg.latex?\Large&space;q=\frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x))

## Langage de Programmation :: [Python](https://www.python.org/)
1. [Python :: 3.7](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.7)
2. [Python :: 3.8](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.8)

## Comment Démarrer
### Modules Requis :: [pypi](https://pypi.org/) 

    pip install -r requirements.txt

# Notes de Version
### [version 1.0.0.1 RC](https://github.com/DeepEastWind/Hydrogeologie/releases/tag/df6af02)
1. Release Candidate contient deux parties:
    1. Écoulement Permanent Unidirectionnel
    
    2. Étiage
   
2. GUi d'application se compose de deux interfaces:
    1. la premiers interface contient des boutons de navigation et de control, des entree et des cadres des noms et des unités
    
    2. la deuxième interface contient la feuille du calcul

### version 2.0.0.1 RC
1. switcher l'interface graphique vers le Notebook

2. amélioration du script