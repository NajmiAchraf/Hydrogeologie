# Hydrogéologie
### Hydrologie des eaux souterraines Livre de David Keith Todd

## Sommaire
Cette application est une solution pour les relations d'hydrologie et de processus de contamination avec différentes utilisations en travaillant simplement dessus avec une navigation fluide.

## Fonctionnalités
### Chapitre Ⅳ: Hydraulique des puits, pompage d'essai et étude des rabattements

##### 1. ECOULEMENT UNIDIRECTIONNEL STABLE
1. Aquifère confiné:
    
    - ![h=-\frac{vx}{K}](https://latex.codecogs.com/svg.latex?\Large&space;h=-\frac{vx}{K})

2. Aquifère non confiné:
    
    - ![q=\frac{K}{2x}\left({h_0^2-h^2}\right)](https://latex.codecogs.com/svg.latex?\Large&space;q=\frac{K}{2x}\left({h_0^2-h^2}\right))

3. Débit de base vers un cours d'eau:

    - ![q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)](https://latex.codecogs.com/svg.latex?\Large&space;q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right))

    - ![d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}](https://latex.codecogs.com/svg.latex?\Large&space;d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L})

    - ![h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d](https://latex.codecogs.com/svg.latex?\Large&space;h^{2}_{max}={h^{2}_{1}}-\frac{\left({h^{2}_{1}-h^{2}_{2}}\right){d}}{L}+\frac{W}{K}\left(L-d\right){d})

    - ![h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}](https://latex.codecogs.com/svg.latex?\Large&space;h_{max}=\sqrt{{h^{2}_{1}}-\frac{\left({h^{2}_{1}-h^{2}_{2}}\right){d}}{L}+\frac{W}{K}\left(L-d\right){d}})

##### 2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS
1. Aquifère confiné:
    1. Débit de pompage:
    
        - ![Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)})

        - ![T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right))
        
    2. Conductivité hydraulique:
    
        - ![K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right))
        
    3. Niveau d'eau dans le puits pompé:
    
        - ![h_w=h_2-\frac{Q}{2\pi{Kb}}\ln{\frac{r_2}{r_1}}](https://latex.codecogs.com/svg.latex?\Large&space;h_w=h_2-\frac{Q}{2\pi{Kb}}\ln{\frac{r_2}{r_1}})
        
    4. Rayon d'influence:
    
        - ![R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)})

2. Aquifère non confiné:
    1. Débit de pompage:
    
        - ![Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;Q=\pi{K}\frac{h^{2}_{2}-h^{2}_{1}}{ln\left(\frac{r_2}{r_1}\right)})

        - ![T\cong{K}\frac{h_1+h_2}{2}](https://latex.codecogs.com/svg.latex?\Large&space;T\cong{K}\frac{h_1+h_2}{2})
    
    2. Conductivité hydraulique:
    
        - ![K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{Q}{\pi\left(h^{2}_{2}-h^{2}_{1}\right)}ln\left(\frac{r_2}{r_1}\right))

        - ![T\cong{K}\frac{h_1+h_2}{2}](https://latex.codecogs.com/svg.latex?\Large&space;T\cong{K}\frac{h_1+h_2}{2})
        
    3. Niveau d'eau dans le puits pompé:
    
        - ![h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}\ln{\frac{r_2}{r_1}}}](https://latex.codecogs.com/svg.latex?\Large&space;h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}\ln{\frac{r_2}{r_1}}})
        
    4. Rayon d'influence:
    
        - ![R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)})
    
3. Aquifère non confiné avec recharge uniforme:
    1. Équation de la courbe de rabattement:
    
        - ![h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)](https://latex.codecogs.com/svg.latex?\Large&space;h^{2}_{0}-h^{2}=\frac{W}{2K}\left(r^{2}-r^{2}_{0}\right)+\frac{Q_{w}}{\pi{K}}ln\left(\frac{r_{0}}{r}\right))
        
    2. Débit de pompage:
    
        - ![Q_w=\pi{r_{0}^{2}}W](https://latex.codecogs.com/svg.latex?\Large&space;Q_{w}=\pi{r^{2}_{0}}{W})
        
##### 3. PUIT DANS UN ECOULEMENT UNIFORME
1. Conductivité hydraulique (K):

    - ![K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)})
    
2. La pente de la surface piézométrique dans les conditions naturelles:

    - ![i=\frac{\Delta{h}}{\Delta{x}}](https://latex.codecogs.com/svg.latex?\Large&space;i=\frac{\Delta{h}}{\Delta{x}})
    
3. Les limites longitudinales et transversales des eaux souterraines entrant dans le puits:

    - ![y_L=\pm\frac{Q}{2Kbi}](https://latex.codecogs.com/svg.latex?\Large&space;y_L=\pm\frac{Q}{2Kbi})
    
    - ![x_L=-\frac{Q}{2\pi{Kbi}}](https://latex.codecogs.com/svg.latex?\Large&space;x_L=-\frac{Q}{2\pi{Kbi}})

##### 4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
1. Équation de pompage de puits instable:
    1. La Transmisivité:
    
        - ![T=\frac{114.6Q}{s}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{114.6Q}{s}W\left(u\right))
        
        - ![T=\frac{Q}{4\pi{s}}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{Q}{4\pi{s}}W\left(u\right))
        
    2. Le coefficient de stockage:
    
        - ![S=\frac{Tt}{\frac{1}{u}1.87r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{Tt}{\frac{1}{u}1.87r^2}) (t en jours)
    
        - ![S=\frac{Tt}{\frac{1}{u}2693r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{Tt}{\frac{1}{u}2693r^2}) (t en minutes)
    
2. Méthode de solution de Theis:
    1. La Transmisivité:
    
        - ![T=\frac{Q}{4\pi{s}}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{Q}{4\pi{s}}W\left(u\right))
        
    2. Le coefficient de stockage:
    
        - ![S=\frac{4Tu}{r^2/t}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{4Tu}{r^2/t})

3. Méthode de solution de Cooper-Jacob:
    1. La Transmisivité:
    
        - ![T=\frac{2.303Q}{4\pi\Delta{s}}](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{2.303Q}{4\pi\Delta{s}})
        
    2. Le coefficient de stockage:
    
        - ![S=\frac{{2.246Tt}_0}{r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{{2.246Tt}_0}{r^2})

4. Méthode de solution de Chow:

    - ![F\left(u\right)=\frac{s}{\Delta{s}}](https://latex.codecogs.com/svg.latex?\Large&space;F\left(u\right)=\frac{s}{\Delta{s}})

##### 5. FLUX RADIAL INSTANTANE DANS UN AQUIFERE NON CONFINE

- ![s=\frac{Q}{4\pi{T}}W\left(u_a,u_y,\eta\right)](https://latex.codecogs.com/svg.latex?\Large&space;s=\frac{Q}{4\pi{T}}W\left(u_a,u_y,\eta\right))

- ![u_a=\frac{r^{2}S}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u_a=\frac{r^{2}S}{4Tt})

- ![u_y=\frac{r^{2}S_y}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u_y=\frac{r^{2}S_y}{4Tt})

- ![\eta=\frac{r^{2}K_z}{b^{2}K_h}](https://latex.codecogs.com/svg.latex?\Large&space;\eta=\frac{r^{2}K_z}{b^{2}K_h})
    
##### 6. ECOULEMENT RADIAL INSTABLE DANS UN AQUIFERE QUI FUIT

- ![s=\frac{Q}{4\pi{T}}W\left(u,\frac{r}{B}\right)](https://latex.codecogs.com/svg.latex?\Large&space;s=\frac{Q}{4\pi{T}}W\left(u,\frac{r}{B}\right))

- ![u=\frac{r^{2}S}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u=\frac{r^{2}S}{4Tt})

- ![\frac{r}{B}=\frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{r}{B}=\frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}})
    
##### 7. UN PUITS S'ECOULE PRES DES LIMITES DE L'AQUIFERE 

- ![s_b=\frac{Q}{4\pi{T}}W\left(u_p\right)+\frac{Q}{4\pi{T}}W\left(u_i\right)](https://latex.codecogs.com/svg.latex?\Large&space;s_b=\frac{Q}{4\pi{T}}W\left(u_p\right)+\frac{Q}{4\pi{T}}W\left(u_i\right))

- ![u_p=\frac{r^{2}_{p}S}{4Tt_p}](https://latex.codecogs.com/svg.latex?\Large&space;u_p=\frac{r^{2}_{p}S}{4Tt_p})

- ![u_i=\frac{r^{2}_{i}S}{4Tt_i}](https://latex.codecogs.com/svg.latex?\Large&space;u_i=\frac{r^{2}_{i}S}{4Tt_i})
---
## Langage de Programmation :: [Python](https://www.python.org/)
1. [Python :: 3.7](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.7)
2. [Python :: 3.8](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.8)

## Comment Démarrer

### [Télécharger La Dernière Commit Dans Hydrogéologie Repository](https://github.com/NajmiAchraf/Hydrogeologie/archive/main.zip)

Ou bien 

### [Télécharger La Dernière Release Dans Hydrogéologie Releases](https://github.com/NajmiAchraf/Hydrogeologie/releases/latest)

### Installation du Font

- Pour une bonne qualité d'écriture installée la police `DejaVuSans.ttf`, sa valable pour les versions inférieur à la version 4

- Depuis la version 4 on es capable de changer la police de GUI, mais la police `DejaVuSans` reste donnée par défaut

### Installation des Modules Requis :: [pypi](https://pypi.org/) 
ouvrir `cmd.exe` en tant qu'administrateur
```
C:\WINDOWS\system32>pip install -r requirements.txt
```
### Démarrer

ouvrir `cmd.exe` en tant qu'administrateur
```
C:\WINDOWS\system32>python C:\ ...(adresse)... \Hydrogeologie-main\__main__.py
```

# Notes de Version
### [version 1.0.0.1 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v1.0.0.1-RC)
1. Release Candidate contient deux parties:
    1. Écoulement Permanent Unidirectionnel
    
    2. Étiage
   
2. GUI d'application se compose de deux interfaces:
    1. la premiers interface contient des boutons de navigation et de control, des entrée et des cadres des noms et des unités
    
    2. la deuxième interface contient la feuille du calcul

### [version 2.0.0.1 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v2.0.0.1-RC)
1. switcher l'interface graphique vers le Notebook

2. amélioration du script

### [version 3.0.0.1 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.0.0.1-bêta)
1. commencer à inclure de nouvelles relations dans l'application

### [version 3.0.0.2 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.0.0.2-bêta)
1. amélioration du script et des relations

### [version 3.0.0.3 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.0.0.3-RC)
1. amélioration du script et ajoute des nouvelles tab

### [version 3.0.0.4 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.0.0.4-FV)
1. des petites améliorations au niveau du script

### [version 3.1.0.1 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.1.0.1-bêta)
1. ajout la possibilité de cliquer sur entré est afficher la résultat sur la feuille de calcul

2. corrige le lent démarrage d'application

3. amélioration l’adaptation du script

### [version 3.1.0.2 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.1.0.2-bêta)
1. colorée la feuille du calcul au couleur blanche

2. attribue les résultats par l'axe x dans la feuille du calcul

3. amélioration global du script

### [version 3.1.0.3 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.1.0.3-RC)
1. amélioration partout dans le script

### [version 3.1.0.4 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.1.0.4-FV)
1. colorée les résultats et le texte généralement dans la feuille du calcul

### [version 3.2.0.1 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.2.0.1-bêta)

1. amélioré la coloration des résultats et le texte généralement dans la feuille du calcul

2. correction de texte partout dans l'application

### [version 3.2.0.2 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.2.0.2-bêta)
1. amélioration global du script

### [version 3.2.0.3 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.2.0.3-bêta)
1. améliorer DrawLaTex dans FigureXY pour GUI en :
    1. l'affichage rapide des des résultats dans la feuille de calcul
    
    2. définir la position verticale de chaque ligne de texte en attente sur l'axe x
    
    3. améliore les couleurs pour chaque ligne de texte dans la feuille de calcul
    
### [version 3.2.0.4 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.2.0.4-RC)
1. améliorer DrawLaTex dans FigureXY par la méthode la plus rapide jamais vue pour afficher les résultats dans la feuille de calcul

### [version 3.2.0.5 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v3.2.0.5-FV)
1. améliorer à nouveau DrawLaTex dans FigureXY

### [version 4.0.0.1 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.0.0.1-bêta)
- ajouter menu bare avec deux fonctionnalités:
    - les paramétrages d'application contient:
        - changements de polices et de tailles pour la partie GUI et pour la feuille de calcul
        
        - changements de titre pour la feuille de calcul
        
    - quitté l'application

### [version 4.0.0.2 bêta](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.0.0.2-bêta)
- régler la taille de fenêtre du démarrage 

- accordée la notebook avec le style de police d'interface

- colorer les boutons de paramètres

- l'application des modifications ne nécessite plus un redémarrage de l'hydrogéologie juste l'effacement du feuille de calcul

- mettre la disposition des widgets dynamique selon son nom

### [version 4.0.0.3 RC](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.0.0.3-RC)
- réduire l'affichage de la popup pour ne s'applique qu'aux changements qui prennent en compte la feuille de calcul

- ajouter une option pur choisir un thème style

- régler l'application des modifications qui prennent en compte la feuille de calcul en cas de choisir non

- la bouton appliquer ne s'allume quand il y a un changement dans les paramètre

- des améliorations sur le script

### [version 4.0.0.4 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.0.0.4-FV)
- des corrections au niveau du texte

- a propos des calculs la modification concerne l'affichage de "ln" à là place de "log"
  
- modification de l'application du paramètre Titre ID

- au niveau du script la modification de choisir soit que changer le Titre ID ou non est manuel

### [version 4.0.1.0 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.0.1.0-FV)
- fixé le click du bouton Appliqué dans paramètre

### [version 4.1.0.0 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.1.0.0-FV)
- devise la partie 3. "Aquifére non confiné avec recharge uniforme" en deux parties:
    - Équation de la courbe de rabattement
    
    - Débit de pompage

- fixé un erreur de calcul dans l’Équation de la courbe de rabattement

### [version 4.2.0.0 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.2.0.0-FV)
- auto install du police

- des améliorations sur le script
