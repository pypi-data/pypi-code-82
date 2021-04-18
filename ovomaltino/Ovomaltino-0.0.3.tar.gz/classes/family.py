import random as r
import typing as tp
import operator as op
from classes.social_fact import SocialFact
from utils.list_functions import inputs_outputs
from utils.influence_type import Influence


class Family(SocialFact):

    def shape(self, input_value: tp.Any, output_value: tp.Any) -> tp.NoReturn:

        outputs = list(dict.fromkeys(output_value))
        new_morals = list(map(
            lambda out: {'inputValue': input_value, 'outputValue': out},
            outputs
        ))

        for moral in iter(new_morals):
            self.data['moral'] = op.add(self.data['moral'], [moral])

    def influence(self, input_value: tp.Any) -> tp.Union[Influence, None]:

        filter_list = list(x['outputValue'] for x in filter(
            lambda x: x if x['inputValue'] == input_value else False,
            self.data['moral']
        ))

        if len(filter_list) > 0:
            [inputs, outputs] = inputs_outputs(filter_list)
            max_value = max(outputs)
            action = list(set(list(filter(
                lambda x: outputs[inputs.index(x)] == max_value,
                filter_list
            ))))

            ret = action[0] if len(action) == 1 else action[r.choice(
                range(0, len(action) - 1)
            )]

            suggestion = ret
            coersion = max_value / len(filter_list)
            return (suggestion, coersion)

        else:
            return None
