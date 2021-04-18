#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe de wrapping Scikit-Learn pour PyTorch, base classifier.

Created on Mon Oct 21 14:42:57 2019

@author: Cyrile Delestre
"""
from typing import Union, Dict, List, Tuple, Any, Optional, Iterable

import numpy as np
from pandas.core.frame import DataFrame
from sklearn.base import ClassifierMixin
from torch import no_grad
from torch.utils.data import Dataset

from ._base import BaseEnvironnement
from . import check_tensor_dict, check_tensor

class BaseClassifier(BaseEnvironnement, ClassifierMixin):
    r"""
    Classe d'implémentation des Classifier pour être compatible Scikit-Learn.
    Elle hérite de BaseEnvironnement et ClassifierMixin.
    
    Notes
    -----
    Les méthodes constituant BaseClassifier :
        predict :
            méthode de prédiction compatible avec le prototypage Scikit-Learn 
            predict(X, rnn_hidden_state, **kargs) retournant la classe 
            d'appartenance.
        predict_proba : méthode de prédiction compatible avec le prototypage
            Scikit-Learn predict_proba(X, rnn_hidden_state, **kargs) 
            retournant la probabilité d'appartenir à chaque classe.
    """
    _estimator_type = 'classifier'
    def predict(self,
                X: Union[Dataset,
                         np.ndarray,
                         DataFrame,
                         List[Dict[str, Any]],
                         Tuple[Dict[str, Any]],
                         Dict[str, Any]],
                treat_nan_inf: bool=True,
                fill_nan: float=0,
                **kargs):
        r"""
        Méthode de prédiction de la classe compatible Scikit-Learn.
        
        Parameters
        ----------
        X : Union[Dataset, np.ndarray, DataFrame, List[Dict[str, Any]], Tuple[Dict[str, Any]], Dict[str, Any]]
            Features du modèle, pour le bon fonctionnement via Scikit-Learn et
            de son utilisation classique, X peut être de différents types
                - Dataset: Classe Dataset de PyTorch, doit sortir un 
                    dictionnaire contenant tous les arguments indispensables au
                    calcul du modèle de la fonction forward.
                - list: liste de dictionnaire contenant tous les arguments
                    indispensables au calcul du modèle de la fonction forward.
            Attention : La première dimension doit être consacrée à celle du
            batch. Si qu'une seule observation alors la première dimension sera
            de dimension 1.
        treat_nan_inf : bool
            traitre les NaN si l'algorithme à divergé et met les valeurs inf 
            à la plus grande valeur possible du type du numpy array.
        fill_nan : float
            valeur de remplacement des NaN.
        Returns
        -------
        res : np.ndarray
            retourne le résultat au format numpy array de l'argument du max 
            la fonction de classification forward
        """
        self.eval()
        with no_grad():
            if isinstance(X, Dataset):
                res = []
                for data in X:
                    data = check_tensor_dict(data)
                    out = self.forward(**data).detach().numpy()
                    if treat_nan_inf:
                        out = np.nan_to_num(out, nan=fill_nan)
                    res.append(np.argmax(out, axis=1).reshape(-1, 1))
                res = np.concatenate(res, axis=0)
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
            elif isinstance(X, (list, tuple,)):
                res = []
                for data in X:
                    data = check_tensor_dict(data)
                    out = self.forward(**data).detach().numpy()
                    if treat_nan_inf:
                        out = np.nan_to_num(out, nan=fill_nan)
                    res.append(np.argmax(out, axis=1).reshape(-1, 1))
                res = np.concatenate(res, axis=0)
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
            elif isinstance(X, np.ndarray):
                res = self.forward(check_tensor(X), **kargs).detach().numpy()
                if treat_nan_inf:
                    res = np.nan_to_num(res, nan=fill_nan)
                return np.argmax(res, axis = 1).reshape(-1, 1)
            elif isinstance(X, dict):
                X = check_tensor_dict(X)
                res = self.forward(**X).detach().numpy()
                if treat_nan_inf:
                    res = np.nan_to_num(res, nan=fill_nan)
                return np.argmax(res, axis=1).reshape(-1, 1)
        return None

    def predict_proba(self,
                      X: Union[Dataset,
                               np.ndarray,
                               DataFrame,
                               List[Dict[str, Any]],
                               Tuple[Dict[str, Any]],
                               Dict[str, Any]],
                      treat_nan_inf: bool=True,
                      fill_nan: float=0,
                      **kargs):
        r"""
        Fonction de prédiction de la probabilité d'appartenance à chaque 
        classe compatible Scikit-Learn.
        
        Parameters
        ----------
        X : Union[Dataset, np.ndarray, DataFrame, List[Dict[str, Any]], Tuple[Dict[str, Any]], Dict[str, Any]]
            Features du modèle, pour le bon fonctionnement via Scikit-Learn 
            et de son utilisation classique, X peut être de différents types
                - Dataset: Classe Dataset de PyTorch, doit sortir un 
                    dictionnaire contenant tous les arguments indispensables 
                    au  calcul du modèle de la fonction forward.
                - list: liste de dictionnaires contenant tous les arguments
                    indispensables au calcul du modèle de la fonction forward.
            Attention : La première dimension doit être consacrée à celle du
            batch. Si qu'une seule observation alors la première dimension 
            sera de dimension 1.
        treat_nan_inf : bool
            traitre les NaN si l'algorithme à divergé et met les valeurs inf 
            à la plus grande valeur possible du type du numpy array.
        fill_nan : float
            valeur de remplacement des NaN.
        
        Returns
        -------
        res : np.ndarray
            retourne le résultat au format numpy array de la fonction de 
            classification forward
        """
        self.eval()
        with no_grad():
            if isinstance(X, Dataset):
                res = []
                for data in X:
                    data = check_tensor_dict(data)
                    res.append(self.forward(**data).detach().numpy())
                res = np.concatenate(res, axis=0)
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
            elif isinstance(X, (list, tuple,)):
                res = []
                for data in X:
                    data = check_tensor_dict(data)
                    res.append(self.forward(**data).detach().numpy())
                res = np.concatenate(res, axis=0)
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
            elif isinstance(X, np.ndarray):
                res = self.forward(check_tensor(X), **kargs).detach().numpy()
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
            elif isinstance(X, dict):
                X = check_tensor_dict(X)
                res = self.forward(**X).detach().numpy()
                if treat_nan_inf:
                    return np.nan_to_num(res, nan=fill_nan)
                else:
                    return res
        return None

class BaseClassifierOnline(BaseClassifier):
    r"""
    Classe d'implémentation des Classifier dans un contexte online pour être 
    compatible à Scikit-Learn. Elle hérite de BaseClassifier.
    
    Notes
    -----
    Les méthodes constituant BaseClassifierOnline :
        save_weights :
            surchage de la méthode save_weights de BaseEnvironnement afin de 
            coller au contexte online.
        fit :
            surcharge de la méthode fit de BaseEnvironnement afin de coller au
            context online.
        fit_online :
            implémentation de l'apprentissage online avec possibilité de 
            réaliser une prédiction à la volée.
    """
    def save_weights(self, path: Optional[str]=None, **kargs_dump):
        r"""
        Méthode permettant de sauvegarder simplement les paramètres et les
        poids du modèle (sans la structure de réseau) ainsi que l'état de 
        l'optimizer pour une utilisation online. Utilise Pickle.
        
        Parameters
        ----------
        path : Optional[str]
            path directory du modèle, si None retourne les données binaires de 
            Pickle.dumps()
        **kargs_dump : 
            paramètres attachés à Pickle.dump(obj, file, **kargs_dump) si 
            path est un chemin ou a Pickles.dump(obj, **kargs_dump) si None.
        """
        return super(BaseClassifier, self).save_weights(
            path=path,
            save_optimizer_state=True,
            **kargs_dump
        )

    def fit(self, X: Iterable, y: Optional[Iterable]=None, **kargs):
        r"""
        Méthode de fit (wrapper vers Scikit-learn). Pour l'apprentissage la
        partie preprocessing doit être faite au préalable. La fonction est
        conçue pour fonctionner avec du multiprocessing. Donc un identifiant
        unique est donné à chaque session d'entrainement via uuid avec pour
        protocole 1.
        
        Parameters
        ----------
        X : Iterable
            Dataset PyTorch contenant dans un dictionnaire les infos 
            nécessaires pour l'apprentissage du modèle.
                - Attention :
                    à la sortie du DataLoader (donc via collate_fn ou 
                    directement via DataSet de PyTorch), il faut que le 
                    dictionnaire possède les noms présents dans le forward de 
                    la sous-classe du modèle.
        y : Optional[Iterable]
            Pour être ISO avec Scikit-learn. L'ensemble de l'apprentissage 
            passera via X et le système DataSet et DataLoader de PyTorch.
        **kargs :
            le reste des arguments de la méthode fit de la classe 
            BaseEnvironnement.
        """
        super(BaseClassifier, self).fit(
            X=X,
            y=y,
            eval_set=None,
            nb_epoch=1,
            dataloader=False,
            batch_size=1,
            shuffle=False,
            drop_last=False,
            callbacks=[],
            **kargs
        )
        return self

    def fit_online(self,
                   X: Iterable,
                   y: Optional[Iterable]=None,
                   predict: bool=False,
                   needs_proba: bool=False,
                   gap: int=0,
                   treat_nan_inf: bool=True,
                   fill_nan: float=0,
                   **fit_kargs):
        r"""
        Méthode d'apprentissage online avec possibilité d'inférence à la volée.
        
        Parameters
        ----------
        X : Iterable
            Dataset PyTorch contenant dans un dictionnaire les infos
            nécessaires pour l'apprentissage du modèle.
                - Attention :
                    à la sortie du DataLoader (donc via collate_fn 
                    ou directement via DataSet de PyTorch), il faut que le 
                    dictionnaire possède les noms présents dans le forward de 
                    la sous-classe du modèle.
        y : Optional[Iterable]
            Pour être ISO avec Scikit-learn. L'ensemble de l'apprentissage 
            passera via X et le système DataSet et DataLoader de PyTorch.
        predict : bool
            permet de faire la phase d'inférence à la volée. Par défaut False.
        needs_proba : bool
            précise si la prédiction nécessite la probabilité d'appartenance 
            à chaque classe (True) ou la prédiction de la classe (False). Par 
            défaut False.
        gap : int
            Permet de définir un gap entre l'apprentissage du modèle et la 
            prédiction. Par défaut 0, aucun gap. Dans la pratique le gap 
            est à minima égal à l'horizon de prédiction
        treat_nan_inf : bool
            traitre les NaN de la prédiction si l'algorithme à divergé et met 
            les valeurs inf à la plus grande valeur possible du type du numpy 
            array.
        fill_nan : float
            valeur de remplacement des NaN pour la prédiction.
        **fit_kargs :
            le reste des arguments de la méthode fit de la classe 
            BaseEnvironnement.
        """
        if 'rebuild' in fit_kargs.keys():
            fit_kargs_ = dict(fit_kargs)
            if fit_kargs_['rebuild']:
                fit_kargs_['rebuild'] = False
                self.build()
        else:
            fit_kargs_ = dict(fit_kargs)
            fit_kargs_['rebuild'] = False
        if predict:
            res = []
        for ii, data in enumerate(X):
            self.fit(data, y=y, **fit_kargs_)
            if predict:
                if gap > 0:
                    if ii+gap < len(X):
                        data_eval = X[ii+gap]
                        if needs_proba:
                            res.append(
                                self.predict_proba(
                                    data_eval,
                                    treat_nan_inf=treat_nan_inf,
                                    fill_nan=fill_nan
                                )
                            )
                        else:
                            res.append(
                                self.predict(
                                    data_eval,
                                    treat_nan_inf=treat_nan_inf,
                                    fill_nan=fill_nan
                                )
                            )
                else:
                    if needs_proba:
                        res.append(
                            self.predict_proba(
                                data,
                                treat_nan_inf=treat_nan_inf,
                                fill_nan=fill_nan
                            )
                        )
                    else:
                        res.append(
                            self.predict(
                                data,
                                treat_nan_inf=treat_nan_inf,
                                fill_nan=fill_nan
                            )
                        )
        if predict:
            return np.concatenate(res, axis=0)
        return self
