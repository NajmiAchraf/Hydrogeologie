# Hydrogéologie
### Hydrologie des eaux souterraines Livre de David Keith Todd

## Sommaire
Cette application est une solution pour les relations d'hydrologie et de processus de contamination avec différentes utilisations en travaillant simplement dessus avec une navigation fluide.

## Fonctionnalités
### Chapitre Ⅳ: Hydraulique des puits, pompage d'essai et étude des rabattements

##### 1. ECOULEMENT UNIDIRECTIONNEL STABLE
1. Aquifère confine:
    
    ![h=-\frac{vx}{K}](https://latex.codecogs.com/svg.latex?\Large&space;h=-\frac{vx}{K})

2. Aquifère non confine:
    
    ![q=\frac{K}{2x}\left({h_0^2-h^2}\right)](https://latex.codecogs.com/svg.latex?\Large&space;q=\frac{K}{2x}\left({h_0^2-h^2}\right))

3. Flux de base vers un flux:

    ![q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)](https://latex.codecogs.com/svg.latex?\Large&space;q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right))

    ![d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}](https://latex.codecogs.com/svg.latex?\Large&space;d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L})

    ![h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d](https://latex.codecogs.com/svg.latex?\Large&space;h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d)

    ![h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}](https://latex.codecogs.com/svg.latex?\Large&space;h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d})

##### 2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS
1. Aquifère confine:
    1. Débit de pompage:
    
        ![Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)})

        ![T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right))
        
    2. Conductivité hydraulique:
    
        ![K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right))
        
    3. Niveau d'eau dans le puits pompé:
    
        ![h_w=h_2-\frac{Q}{2\pi{Kb}}\ln{\frac{r_2}{r_1}}](https://latex.codecogs.com/svg.latex?\Large&space;h_w=h_2-\frac{Q}{2\pi{Kb}}\ln{\frac{r_2}{r_1}})
        
    4. Rayon d'influence:
    
        ![R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)})

2. Aquifère non confine:
    1. Débit de pompage:
    
        ![Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)})

        ![T\cong{K}\frac{h_1+h_2}{2}](https://latex.codecogs.com/svg.latex?\Large&space;T\cong{K}\frac{h_1+h_2}{2})
    
    2. Conductivité hydraulique:
    
        ![K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right))

        ![T\cong{K}\frac{h_1+h_2}{2}](https://latex.codecogs.com/svg.latex?\Large&space;T\cong{K}\frac{h_1+h_2}{2})
        
    3. Niveau d'eau dans le puits pompé:
    
        ![h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}\ln{\frac{r_2}{r_1}}}](https://latex.codecogs.com/svg.latex?\Large&space;h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}\ln{\frac{r_2}{r_1}}})
        
    4. Rayon d'influence:
    
        ![R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}](https://latex.codecogs.com/svg.latex?\Large&space;R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)})
    
3. Aquifère non confine avec recharge uniforme:
    1. Équation de la courbe de rabattement:
    
        ![h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)](https://latex.codecogs.com/svg.latex?\Large&space;h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right))
        
    2. Débit de pompage:
    
        ![Q_w=\pi{r_{0}^{2}}W](https://latex.codecogs.com/svg.latex?\Large&space;Q_w=\pi{r_{0}^{2}}W)
        
##### 3. PUIT DANS UN ECOULEMENT UNIFORME
1. Conductivité hydraulique (K):

    ![K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}](https://latex.codecogs.com/svg.latex?\Large&space;K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)})
    
2. La pente de la surface piézométrique dans les conditions naturelles:

    ![i=\frac{\Delta{h}}{\Delta{x}}](https://latex.codecogs.com/svg.latex?\Large&space;i=\frac{\Delta{h}}{\Delta{x}})
    
3. Les limites longitudinales et transversales des eaux souterraines entrant dans le puits:

    ![y_L=\pm\frac{Q}{2Kbi}](https://latex.codecogs.com/svg.latex?\Large&space;y_L=\pm\frac{Q}{2Kbi})
    
    ![x_L=-\frac{Q}{2\pi{Kbi}}](https://latex.codecogs.com/svg.latex?\Large&space;x_L=-\frac{Q}{2\pi{Kbi}})

##### 4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
1. Équation de pompage de puits instable:
    1. La Transmisivité:
    
        ![T=\frac{114.6Q}{s}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{114.6Q}{s}W\left(u\right))
        
        ![T=\frac{Q}{4\pi{s}}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{Q}{4\pi{s}}W\left(u\right))
        
    2. Le coefficient de stockage:
    
        ![S=\frac{Tt}{\frac{1}{u}1.87r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{Tt}{\frac{1}{u}1.87r^2}) (t en jours)
    
        ![S=\frac{Tt}{\frac{1}{u}2693r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{Tt}{\frac{1}{u}2693r^2}) (t en minutes)
    
2. Méthode de solution de Theis:
    1. La Transmisivité:
    
        ![T=\frac{Q}{4\pi{s}}W\left(u\right)](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{Q}{4\pi{s}}W\left(u\right))
        
    2. Le coefficient de stockage:
    
        ![S=\frac{4Tu}{r^2/t}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{4Tu}{r^2/t})

3. Méthode de solution de Cooper-Jacob:
    1. La Transmisivité:
    
        ![T=\frac{2.303Q}{4\pi\Delta{s}}](https://latex.codecogs.com/svg.latex?\Large&space;T=\frac{2.303Q}{4\pi\Delta{s}})
        
    2. Le coefficient de stockage:
    
        ![S=\frac{2.246Tt_0}{r^2}](https://latex.codecogs.com/svg.latex?\Large&space;S=\frac{2.246Tt_0}{r^2})

4. Méthode de solution de Chow:

    ![F\left(u\right)=\frac{s}{\Delta{s}}](https://latex.codecogs.com/svg.latex?\Large&space;F\left(u\right)=\frac{s}{\Delta{s}})

##### 5. FLUX RADIAL INSTANTANE DANS UN AQUIFERE NON CONFINE

![s=\frac{Q}{4\pi{T}}W\left(u_a,u_y,\eta\right)](https://latex.codecogs.com/svg.latex?\Large&space;s=\frac{Q}{4\pi{T}}W\left(u_a,u_y,\eta\right))

![u_a=\frac{r^{2}S}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u_a=\frac{r^{2}S}{4Tt})

![u_y=\frac{r^{2}S_y}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u_y=\frac{r^{2}S_y}{4Tt})

![\eta=\frac{r^{2}K_z}{b^{2}K_h}](https://latex.codecogs.com/svg.latex?\Large&space;\eta=\frac{r^{2}K_z}{b^{2}K_h})
    
##### 6. ECOULEMENT RADIAL INSTABLE DANS UN AQUIFERE QUI FUIT

![s=\frac{Q}{4\pi{T}}W\left(u,\frac{r}{B}\right)](https://latex.codecogs.com/svg.latex?\Large&space;s=\frac{Q}{4\pi{T}}W\left(u,\frac{r}{B}\right))

![u=\frac{r^{2}S}{4Tt}](https://latex.codecogs.com/svg.latex?\Large&space;u=\frac{r^{2}S}{4Tt})

![\frac{r}{B}=\frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}}](https://latex.codecogs.com/svg.latex?\Large&space;\frac{r}{B}=\frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}})
    
##### 7. UN PUITS S'ECOULE PRES DES LIMITES DE L'AQUIFERE 

![s_b=\frac{Q}{4\pi{T}}W\left(u_p\right)+\frac{Q}{4\pi{T}}W\left(u_i\right)](https://latex.codecogs.com/svg.latex?\Large&space;s_b=\frac{Q}{4\pi{T}}W\left(u_p\right)+\frac{Q}{4\pi{T}}W\left(u_i\right))

![u_p=\frac{r^{2}_{p}S}{4Tt_p}](https://latex.codecogs.com/svg.latex?\Large&space;u_p=\frac{r^{2}_{p}S}{4Tt_p})

![u_i=\frac{r^{2}_{i}S}{4Tt_i}](https://latex.codecogs.com/svg.latex?\Large&space;u_i=\frac{r^{2}_{i}S}{4Tt_i})
---
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

### [version 2.0.0.1 RC](https://github.com/DeepEastWind/Hydrogeologie/releases/tag/381b303)
1. switcher l'interface graphique vers le Notebook

2. amélioration du script

### [version 3.0.0.1 bêta](https://github.com/DeepEastWind/Hydrogeologie/releases/tag/30d8efe)
1. commencer à inclure de nouvelles relations dans l'application

### [version 3.0.0.2 bêta](https://github.com/DeepEastWind/Hydrogeologie/releases/tag/d232780)
1. amélioration du script et des relations

### [version 3.0.0.3 RC](https://github.com/DeepEastWind/Hydrogeologie/releases/tag/793787d)
1. amélioration du script et ajoute des nouvelles tab

### version 3.0.0.4 FV
1. des petites améliorations au niveau du script