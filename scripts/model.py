from joblib import PrintTime

import scripts.source as scr
import typing
import pandas
import sklearn.model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


class ModelClassification:
    """ ModelClassification

    # attributes:

    #  name: name of the dataset. Type: str.
    #   - Possible values: 'iris', 'diabetes', 'digits', 'wine', 'linnerud', 'breast_cancer'
    #  clf: classifier. Type: str.
    #  - Possible values: 'Logistic', 'GBoost'
    #  scaler: scaler. Type: str.
    #  - Possible values: 'MinMax', 'Standard'
    #  scaler function.
    #  - Possible values: MinMaxScaler, StandardScaler
    #  dataset. Type: sklearn.utils.Bunch.
    #  - Includes: data, target, target_names, feature_names, filename, description
    #  data. Type: dict.
    #  - Includes: dataframe (df), map (dictionary for target values translation),
    # split dataset(x_data, y_data), train dataset(xtrn, ytrn), cross-validation dataset (xcv, ycv),
    # test dataset (xtst, ytst)
    #  model: Classifier methodology/function
    #  - Possible values: LogisticRegression(), GradientBoostingClassifier()
    #  data_flag: data flag. Type: bool.
    #  target_flag: target flag. Type: bool.
    #  target_names_flag: target_names flag. Type: bool.
    #  feature_names_flag: feature_names flag. Type: bool.
    #  filename_flag: filename flag. Type: bool.
    #  description_flag: description flag. Type: bool.
    # flags: flags related to functions to be checked. Type: list


    # methods:

    #  __init__: constructor.
    #  __add_attributes: update attributes (private).
    #  __dataset_info: print attribute from dataset if flag is True. (private).
    #  __dataset2df: data and target from dataset to dataframe (Alternative to - load_X(as_frame = True)) (private).
    #  __dataset_split: create x_data and y_data from dataframe and includes __train_test(private).
    #  __train_test: split x_data and y_data into train dataset (and cross-validation dataset) and test_dataset(private).
    #  __model_fit: train the model (private).
    #  __model_predict: get predictions (private).
    #  set_model: includes  __add_attributes, __dataset_info, __dataset2df, __dataset_split, __model_fit,
    # __model_predict (public).

    # return: -
    """

    def __init__(self):
        self.name = None
        self.clf = None
        self.scaler = None
        self.scaler_fcn = None
        self.dataset = None
        self.data = dict()
        self.model = None
        self.data_flag = False
        self.target_flag = False
        self.target_names_flag = False
        self.feature_names_flag = False
        self.filename_flag = False
        self.description_flag = False
        self.flags = [False]*6


    def __add__attributes(
            self,
            name: typing.Optional[str] = None,
            clf: typing.Optional[str] = None,
            scaler: typing.Optional[str] = None,
            data_flag: typing.Optional[bool] = False,
            target_flag: typing.Optional[bool] = False,
            target_names_flag: typing.Optional[bool] = False,
            feature_names_flag: typing.Optional[bool] = False,
            filename_flag: typing.Optional[bool] = False,
            description_flag: typing.Optional[bool] = False):
        """  __add__attributes: update attributes.

        # parameters:
        #  self: class.
        #  name: name of the dataset. Type: str.
        #  clf: classifier. Type: str.
        #  scaler: scaler. Type: str.
        #  data_flag: data flag. Type: bool.
        #  target_flag: target flag. Type: bool.
        #  target_names_flag: target_names flag. Type: bool.
        #  feature_names_flag: feature_names flag. Type: bool.
        #  filename_flag: filename flag. Type: bool.
        #  description_flag: description flag. Type: bool.


        # return: IF success: Update attributes. ELSE: -
        """


        self.name = scr.check_instance(name, str, None)

        try:

            if name not in ['iris', 'diabetes', 'digits', 'wine', 'linnerud', 'breast_cancer']:

                self.name = None
                raise ValueError

        except(Exception, ValueError, TypeError):

            print(f'Invalid dataset name - {name} - (__add__attributes)')

        self.clf = scr.check_instance(clf, str, None)

        try:

            if clf not in ['Logistic', 'GBoost']:

                self.clf = None
                raise ValueError

        except(Exception, ValueError, TypeError):

            print(f'Invalid classifier - {clf} - (__add__attributes)')

        self.scaler = scr.check_instance(scaler, str, None)

        try:

            if scaler not in ['MinMax', 'Standard']:

                self.scaler = None
                raise ValueError

        except(Exception, ValueError, TypeError):

            print(f'Invalid scalling method - {scaler} - (__add__attributes)')

        self.data_flag = scr.check_instance(data_flag, bool, False)
        self.feature_names_flag = scr.check_instance(feature_names_flag, bool, False)
        self.target_flag = scr.check_instance(target_flag, bool, False)
        self.target_names_flag = scr.check_instance(target_names_flag, bool, False)
        self.filename_flag = scr.check_instance(filename_flag, bool, False)
        self.description_flag = scr.check_instance(description_flag, bool, False)

        if all(elem is not None for elem in [self.scaler, self.name, self.clf]):
            self.flags[0] = True
        else:
            print(f'Invalid parameters - (__add__attributes)')

    def __dataset_info(self):
        """ Print attribute from dataset if flag is True.

        # parameters:
        #  self: class.

        # return: -
        """

        if (
                (self.flags[0] is True) and
                any(elem is True for elem in [self.data_flag, self.filename_flag, self.target_flag, self.target_names_flag, self.description_flag, self.feature_names_flag])
        ):
            self.flags[1] = True
            self.dataset = scr.load_dataset(self.name)


        if (self.flags[1] is True) and (self.dataset is not None):

            print('\n\tDATA DESCRIPTION:\n')


            if (hasattr(self.dataset, 'data')) and (self.data_flag is True):
                print('The data matrix:\n', self.dataset['data'])


            if (hasattr(self.dataset, 'target')) and (self.target_flag is True):
                print('The classification target:\n', self.dataset['target'])

            if (hasattr(self.dataset, 'feature_names')) and (self.feature_names_flag is True):
                print('The names of the dataset columns:\n', self.dataset['feature_names'])

            if (hasattr(self.dataset, 'target_names')) and (self.target_names_flag is True):
                print('The names of target classes:\n', self.dataset['target_names'])

            if (hasattr(self.dataset, 'DESCR')) and (self.description_flag is True):
                print('The full description of the dataset:\n', self.dataset['DESCR'])

            if (hasattr(self.dataset, 'filename')) and (self.filename_flag is True):
                print('The path to the location of the data:\n', self.dataset['filename'])

    def __dataset2df(self):
        """ Data and Target from dataset to dataframe (Alternative to - load_X(as_frame = True)).

        # parameters:
        #  self: class.

        # return: Update self.dataset, and self.data
        """

        if self.flags[0] is True:
            self.flags[2] = True
            self.dataset = scr.load_dataset(self.name)

        if self.flags[2] is True and (self.dataset is not None):

            print('\n\tDATA CLEANING:\n')

            if (
                    hasattr(self.dataset, 'data') and
                    hasattr(self.dataset, 'target') and
                    hasattr(self.dataset, 'target_names') and
                    hasattr(self.dataset, 'feature_names')
               ):

                data_df = None
                target_df = None
                d_map = None
                df_new = None

                data_df = pandas.DataFrame(data=self.dataset['data'],
                                           columns=self.dataset['feature_names'])

                target_df = pandas.DataFrame(data=self.dataset['target'])
                target_df = target_df.rename(columns={0: 'target'})

                df_new = pandas.concat([data_df, target_df], axis=1)
                df_new.dropna(how='any', axis=0, inplace=True)

                d_map = scr.create_map_dict(df_new['target'].unique(), self.dataset['target_names'])
                df_new = df_new.replace({"target": d_map}, inplace=False)

                self.data['df'] = df_new
                self.data['map'] = d_map

                print('\nFirst values of the data:\n', df_new.head())
                print('\nUnique features:\n', df_new['target'].unique())

                del data_df
                del target_df
                del df_new
                del d_map
        else:
            self.flags[2]  = False
            print(f'Invalid dataset - {self.name} (dataset2df)')

    def __train_test(self):
        """ Split x_data and y_data into train dataset (and cross-validation dataset) and test_dataset.

        # parameters:
        #  self: class.

        # return: Update self.data and self.scaler_fcn
        """
        if (
                (self.flags[2] is True) and
                (all(idKey in self.data.keys() for idKey in ['x_data', 'y_data']))
        ):

            aux_xtrain = None
            aux_ytrain = None

            aux_xtrain, self.data['xtst'], aux_ytrain, self.data['ytst'] = sklearn.model_selection.train_test_split(
                self.data['x_data'],
                self.data['y_data'],
                train_size=0.80,
                random_state=1)

            self.data['xtrn'], self.data['xcv'], self.data['ytrn'], self.data[
                'ycv'] = sklearn.model_selection.train_test_split(aux_xtrain,
                                                                  aux_ytrain,
                                                                  train_size=0.75,
                                                                  random_state=1)

            match self.scaler:
                case 'MinMax':
                    self.scaler_fcn = sklearn.preprocessing.MinMaxScaler()
                case 'Standard':
                    self.scaler_fcn = sklearn.preprocessing.StandardScaler()

            self.data['xtrn'] = pandas.DataFrame(self.scaler_fcn.fit_transform(self.data['xtrn']),
                                                 columns=self.data['xtrn'].columns)
            self.data['xtst'] = pandas.DataFrame(self.scaler_fcn.transform(self.data['xtst']),
                                                 columns=self.data['xtst'].columns)
            self.data['xcv'] = pandas.DataFrame(self.scaler_fcn.transform(self.data['xcv']),
                                                columns=self.data['xcv'].columns)

            print(f'\n\txtrn: {self.data['xtrn'].shape} \n')

            print(f'\n\tytrn: {self.data['ytrn'].shape}\n')

            print(f'\n\txtst: {self.data['xtst'].shape}\n')

            print(f'\n\tytst: {self.data['ytst'].shape}\n')

            print(f'\n\txcv:{self.data['xcv'].shape}\n')

            print(f'\n\tycv: {self.data['ycv'].shape}\n')

            del aux_xtrain
            del aux_ytrain
        else:
            print(f'Invalid parameters (__train_test)')  # alterado

    def __dataset_split(self):
        """ Create x_data and y_data from dataframe and includes __train_test.

        # parameters:
        #  self: class.

        # return: Update self.data.
        """

        count_list = list()

        if (
                (self.flags[2] is True) and
                (all(idKey in ['df', 'map'] for idKey in self.data.keys()))
           ):
            self.flags[3] = True
            invert_map = scr.inv_map(self.data['map'])
            aux_df = self.data['df'].replace({"target": invert_map}, inplace=False)

            self.data['x_data'] = aux_df.copy()
            self.data['y_data'] = aux_df.pop('target')
            self.data['x_data'] = self.data['x_data'].drop(['target'], axis=1)
            count_list = self.data['y_data'].value_counts(normalize=True).unique()

            del invert_map
            del aux_df

        if len(count_list) == 1:

            print('BALANCED DATASET')
            self.__train_test()

        else:
            self.flags[3] = False
            print(f'Invalid parameters (dataset_split)')

        del count_list

    def __model_fit(self):
        """ Train the model.

        # parameters:
        #  self: class.

        # return: Update self.model
        """

        if (
                (self.flags[3] is True) and
                (all(idKey in self.data.keys() for idKey in ['xtrn', 'ytrn']))
        ):
            self.model = scr.model_fit(self.clf, self.data['xtrn'], self.data['ytrn'])
            self.flags[4] = True
        else:
            print(f'Invalid parameters (__model_fit)')



    def __model_predict(self):
        """Get predictions.

        # parameters:
        #  self: class.

        # return: -
        """

        if (
                (self.flags[4] is True) and
                (all(idKey in self.data.keys() for idKey in ['xcv', 'ycv','xtst','ytst']))
        ):
            scr.model_predict(self.model, self.data['xcv'], self.data['ycv'], "CV")
            scr.model_predict(self.model, self.data['xtst'], self.data['ytst'], "Test")
            self.flags[5] = True
        else:
            print(f'Invalid parameters (__model_predict)')

    def set_model(
            self,
            name: typing.Optional[str] = None,
            clf: typing.Optional[str] = None,
            scaler: typing.Optional[str] = None,
            data_flag: typing.Optional[bool] = False,
            target_flag: typing.Optional[bool] = False,
            target_names_flag: typing.Optional[bool] = False,
            feature_names_flag: typing.Optional[bool] = False,
            filename_flag: typing.Optional[bool] = False,
            description_flag: typing.Optional[bool] = False):

        """ set_model: includes  __add_attributes, __dataset_info, __dataset2df, __dataset_split, __model_fit,__model_predict.

        # parameters:
        #  self: class.
        #  name: name of the dataset. Type: str.
        #  clf: classifier. Type: str.
        #  scaler: scaler. Type: str.
        #  data_flag: data flag. Type: bool.
        #  target_flag: target flag. Type: bool.
        #  target_names_flag: target_names flag. Type: bool.
        #  feature_names_flag: feature_names flag. Type: bool.
        #  filename_flag: filename flag. Type: bool.
        #  description_flag: description flag. Type: bool.

        # return: -
        """

        self.__add__attributes(
            name,
            clf,
            scaler,
            data_flag,
            target_flag,
            target_names_flag,
            feature_names_flag,
            filename_flag,
            description_flag)

        self.__dataset_info()
        self.__dataset2df()
        self.__dataset_split()
        self.__model_fit()
        self.__model_predict()

