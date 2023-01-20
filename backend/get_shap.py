import shap

def create_shap_vals(data, model):
    explainer = shap.Explainer(model, data, feature_names=data.columns, model_output='probability')
    shap_values = explainer(data)

    # create classifier params
    param1 = [1-shap_values.base_values[0], shap_values.base_values[0]]
    param2 = [(shap_values.values)-1, shap_values.values]

    return [param1, param2]