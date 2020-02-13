import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from machinelearning.models import UserCapabilities


def predict_user_capabilites():
    """

    :return:
    X_test
    Column 1, 2, 3 (amount column = amount user)-> user (Text),
    Column 4,5,6,7 (amount column = amount level)-> level (Integer),
    Column 8,9 -(amount column = amount helpers)> helpers (Boolean)
    array([[0., 0., 1., 0., 0., 0., 1., 0., 1.],
       [0., 0., 1., 0., 1., 0., 0., 1., 0.],
       [0., 1., 0., 0., 1., 0., 0., 1., 0.],
       [0., 1., 0., 0., 0., 1., 0., 0., 1.],
       [0., 0., 1., 0., 0., 0., 1., 1., 0.],
       [0., 0., 1., 0., 0., 0., 1., 1., 0.]])

    Y_test -> one dimmension
    Row -> points (get or not)
    array([1, 1, 1, 1, 0])

    """
    df = pd.DataFrame(list(
        UserCapabilities.objects.all().values_list(
            'user',
            'task_level',
            'task_helpers',
            'task_points'))
    )
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values

    onehotencoder = OneHotEncoder(handle_unknown='ignore')
    X = onehotencoder.fit_transform(X).toarray()

    labelendocer_Y = LabelEncoder()
    Y = labelendocer_Y.fit_transform(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=0)

    return {
        'test_X': X_test,
        'test_Y': Y_test,
        'category': onehotencoder.categories_
    }


def compute_average_from_test(test):
    category = test.get('category', None)
    test_Y = test.get('test_Y', None)
    test_X = test.get('test_X', None)

    success = {}

    user_category = category[0]
    for i in range(0, len(user_category)):
        for j in range(0, len(test_X)):
            if test_X[j][i] == 1:
                success.setdefault(user_category[i], {})
                total = success[user_category[i]].get('total', 0)
                success[user_category[i]]['total'] = total + 1
                if test_Y[j] == 1:
                    ok = success[user_category[i]].get('ok', 0)
                    success[user_category[i]]['ok'] = ok + 1

    avg_with_user = []
    for user, data in success.items():
        avg_with_user.append((data.get('ok') / data.get('total'), user))
    avg_with_user.sort(reverse=True)
    return avg_with_user
