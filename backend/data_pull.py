# get list from s3 and pull relevant data list and files
# for now manually create list

MODELS_BY_PAL = {
    'Foot Surgeries Bunionectomy and Hammertoe': {
        'version': "0.1",
        'pickle_file': "l3_foot_surgeries_bunionectomy_and_hammertoe_elasticnet_log_reg_l1_ratio02_rfe_v0_1_2022_12_22.pkl",
        'author': "Tim Jaung"
    }
}

MODELS_BY_PAL_full = {
    'Epidural Steroid Injections (Outpatient Only)': {
        'version': "0.1",
        'pickle_file': 'l3_epidural_injections_outpatient_only_logistic_regression_v0_1_2022_12_09.pkl'
    },
    'Facet Injections': {
        'version': "0.1",
        'pickle_file': 'l3_facet_injections_logistic_regression_v0_1_2022_12_09.pkl'
    },
    'Orthopedic surgeries: hip, knee and shoulder arthroscopy': {
        'version': "0.1",
        'pickle_file': 'l3_orthopedic_surgeries_hip_knee_and_shoulder_arthroscopy_l1_log_reg_v0_1_2022_12_09.pkl'
    },
    'Orthopedic surgeries: hip, knee and shoulder arthroplasty': {
        'version': "0.1",
        'pickle_file': 'l3_orthopedic_surgeries_hip_knee_and_shoulder_arthroplasty_l2_log_reg_v0_1_2022_12_08.pkl'
    },
    'SI joint injections': {
        'version': "0.1.1",
        'pickle_file': 'l3_si_joint_injections_random_forest_v0_1_1_2022_12_15.pkl'
    },
    'Spinal cord stimulators': {
        'version': "0.1",
        'pickle_file': 'l3_spinal_cord_stimulators_l1_log_reg_v0_1_2022_12_08.pkl'
    },
    'Spine Surgeries; Spinal fusion, decompression, kyphoplasty and vertebroplasty': {
        'version': "0.1",
        'pickle_file': 'l3_spinal_fusion_decompression_kyphoplasty_and_vertebroplasty_elasticnet_log_reg_l1_ratio0_5_v0_1_2022_12_08.pkl'
    },
    'Physical, occupational and speech therapy (excludes Alabama)': {
        'version': "0.1",
        'pickle_file': "l3_therapy_physical_occupational_and_speech_elasticnet_log_reg_l1_ratio02_rfe_v0_1_2022_12_15.pkl"
    },
    'Pain infusion pump': {
        'version': "0.1",
        'pickle_file': "l3_pain_infusion_pump_logistic_regression_v0_1_2022_12_14.pkl"
    },
    'Varicose vein: surgical treatment and sclerotherapy': {
        'version': "0.1",
        'pickle_file': "l3_varicose_vein_surgical_treatment_and_sclerotherapy_elasticnet_log_reg_l1_ratio05_v0_1_2022_12_22.pkl"
    },
    'Decompression of peripheral nerve (i.e., carpal tunnel surgery)': {
        'version': "0.1",
        'pickle_file': "l3_decompression_of_peripheral_nerve_ie_carpal_tunnel_surgery_l1_log_reg_v0_1_2022_12_22.pkl"
    },
    'Blepharoplasty': {
        'version': "0.1",
        'pickle_file': "l3_blepharoplasty_l2_log_reg_v0_1_2022_12_23.pkl"
    },
    'Foot Surgeries Bunionectomy and Hammertoe': {
        'version': "0.1",
        'pickle_file': "l3_foot_surgeries_bunionectomy_and_hammertoe_elasticnet_log_reg_l1_ratio02_rfe_v0_1_2022_12_22.pkl"
    }
}