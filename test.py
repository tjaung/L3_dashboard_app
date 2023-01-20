import backend.s3_pull as s3_pull
import backend.generate_dashes as generate_dashes

import os

service = 'msk'
pals = []
for dir in s3_pull.list_s3_subdirectories(f'signal_based_models/{service}/by_PAL/'):
    pals.append(os.path.basename(os.path.normpath(dir)))
#[print(p) for p in pals]
info = generate_dashes.get_dash_info('msk', pals[0])
print(info['data']['y_test'])
#print(info['data']['X_test'].index)
#print(info['data']['y_test'].index)