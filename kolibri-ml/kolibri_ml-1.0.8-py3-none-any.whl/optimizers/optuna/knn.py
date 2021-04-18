import numpy as np
from kolibri.errors import MetricException
import optuna

from kolibri.optimizers.metric import Metric
from sklearn.neighbors import KNeighborsClassifier

class KNNObjective:
    def __init__(
        self,
        ml_task,
        X_train,
        y_train,
        sample_weight,
        X_validation,
        y_validation,
        sample_weight_validation,
        eval_metric,
        n_jobs,
        random_state,
    ):
        self.ml_task = ml_task
        self.X_train = X_train
        self.y_train = y_train
        self.sample_weight = sample_weight
        self.X_validation = X_validation
        self.y_validation = y_validation
        self.eval_metric = Metric({"name": eval_metric})
        self.n_jobs = n_jobs
        self.seed = random_state

    def __call__(self, trial):
        try:
            params = {
                "n_neighbors": trial.suggest_int("n_neighbors", 1, 128),
                "weights": trial.suggest_categorical(
                    "weights", ["uniform", "distance"]
                ),
                "n_jobs": self.n_jobs,
            }
            Algorithm =KNeighborsClassifier

            model = Algorithm(**params)
            model.fit(self.X_train, self.y_train)
            preds = model.predict(self.X_validation)

            score = self.eval_metric(self.y_validation, preds)
            if Metric.optimize_negative(self.eval_metric.name):
                score *= -1.0

        except optuna.exceptions.TrialPruned as e:
            raise e
        except Exception as e:
            print("Exception in KNNObjective", str(e))
            return None

        return score
