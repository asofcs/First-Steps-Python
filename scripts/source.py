import typing
import pandas
import sklearn.datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix


def check_instance(
        var: typing.Any,
        xtype: typing.Any,
        v_error: typing.Any) -> typing.Any:
    """ Check instance/type of variable

    # parameters:
    #  var: variable to check
    #  xtype: type expected
    #  v_error: error value

    # return: IF success: var. ELSE: v_error
    """

    try:

        if isinstance(var, xtype) is True:

            return var

        else:
            raise Exception

    except (Exception, ValueError, TypeError):
        return v_error

def load_dataset(name: typing.Optional[str] = None) -> sklearn.utils.Bunch:
    """ Load dataset from the sklearn.datasets package

    # parameters:
    #  name: name of dataset to import. Type: str.

    # return: IF success: dataset (data, target, target_names, feature_names, filename, description). ELSE: None
    """

    test_flag = False
    dt_new = None

    try:
        if isinstance(name, str) and (name in ['iris', 'diabetes', 'digits', 'wine', 'linnerud', 'breast_cancer']):

            test_flag = True

        else:
            raise Exception


    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} - (load_dataset)')

    if test_flag is True:

        match name:
            case 'iris':
                dt_new = sklearn.datasets.load_iris()
            case 'diabetes':
                dt_new = sklearn.datasets.load_diabetes()
            case 'digits':
                dt_new = sklearn.datasets.load_digits()
            case 'wine':
                dt_new = sklearn.datasets.load_wine()
            case 'linnerud':
                dt_new = sklearn.datasets.load_linnerud()
            case 'breast_cancer':
                dt_new = sklearn.datasets.load_breast_cancer()

    del test_flag
    return dt_new

def create_map_dict(
        orig_list: typing.Optional[list] = None,
        final_list: typing.Optional[list] = None, ) -> dict:
    """ Create dictionary from two lists, to map a dataframe.

    # parameters:
    #  orig_list: list of the original values (keys).
    #  final_list: list of the final values (values).

    # return: IF success: filled dictionary. ELSE: empty dictionary
    """

    d_map = None

    if (orig_list is not None) and (final_list is not None):

        if len(orig_list) == len(final_list):
            d_map = {elem: final_list[idVal] for idVal, elem in enumerate(sorted(orig_list))}

    return d_map

def inv_map(orig_map: typing.Optional[dict] = None) -> dict:
    """ Reverse a dictionary to map a dataframe.

    # parameters:
    #  origMap: original dictionary. Type: dict

    # return: IF success: reversed dictionary. ELSE: empty dictionary.
    """

    invert_map = dict()
    test_flag = False

    try:

        if (orig_map is not None) and (isinstance(orig_map, dict)) and (orig_map.keys()):

            test_flag = True
        else:
            raise Exception


    except(Exception, ValueError, TypeError):
        print(f'Invalid dictionary - (inv_map)')

    if test_flag is True:
        invert_map = {orig_map[idKey]: idKey for idKey in orig_map.keys()}

    del test_flag

    return invert_map

def model_fit(
        clf: typing.Optional[str] = None,
        x_train: typing.Optional[pandas.DataFrame] = None,
        y_train: typing.Optional[pandas.DataFrame] = None,)-> typing.Optional[typing.Union[sklearn.ensemble.GradientBoostingClassifier, sklearn.linear_model.LogisticRegression]]:
    """ Train/Fit model

    # parameters:
    #  clf: classifier. Type: str
    #  x_train: train dataset (data). Type: pandas.Dataframe
    #  y_train: train dataset (target). Type: pandas.Dataframe

    # return: IF success: classifier function/model. ELSE: None
    """

    model = None
    test_flag = False

    try:

        if (clf is not None) and (clf in ['Logistic','GBoost']) and (x_train is not None) and (y_train is not None):

            test_flag = True

        else:

            raise ValueError

    except(Exception, ValueError, TypeError):

        print(f'Invalid parameters (model_fit - {clf})')


    if test_flag is True:

        match clf:

            case 'Logistic':
                model = sklearn.linear_model.LogisticRegression()

            case 'GBoost':
                model = sklearn.ensemble.GradientBoostingClassifier()

    # fit the model on the training data
    if model is not None:

        model.fit(x_train, y_train)

    del test_flag

    return model

def model_predict(
        model: typing.Optional[typing.Union[sklearn.ensemble.GradientBoostingClassifier, sklearn.linear_model.LogisticRegression]],
        x_test: typing.Optional[pandas.DataFrame] = None,
        y_test: typing.Optional[pandas.DataFrame] = None,
        type: typing.Optional[str] = None,):

    """ Train/Fit model

    # parameters:
    #  model: model. Type: sklearn.ensemble.GradientBoostingClassifier or sklearn.linear_model.LogisticRegression
    #  x_test: test dataset (data). Type: pandas.Dataframe
    #  y_test: test dataset (target). Type: pandas.Dataframe
    #  type:: type of testing (cross-validation or standard). type: str.

    # return: IF success: classifier function/model. ELSE: None
    """


    y_pred = None
    y_true = None
    test_flag = False

    try:
        if (model is not None) and (type is not None) and (type in ['CV', 'Test']) and (x_test is not None) and (y_test is not None):
            test_flag = True
        else:
            raise ValueError
    except(Exception, ValueError, TypeError):

        print(f'Invalid parameters (model_predict - {type})')

    if test_flag is True:

        y_true = y_test.to_numpy()

        match type:
            case 'Test':
                y_pred = model.predict(x_test)

            case 'CV':
                y_pred = sklearn.model_selection.cross_val_predict(model, x_test, y_test, cv=5)


    if y_pred is not None:

        print(f'\n\t CLASSIFICATION REPORT ({type} - {model}):\n')
        print(sklearn.metrics.classification_report(y_true, y_pred))

    del y_true
    del y_pred
    del test_flag
