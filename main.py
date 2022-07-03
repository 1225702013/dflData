import numpy as np
import pickle
from pathlib import Path

if __name__ == '__main__':
    model_data_path = Path('ZIBI06_SAEHD_data.dat')
    # model_data_path = Path('DFD224F_SAEHD_data.dat')
    model_data = pickle.loads(model_data_path.read_bytes())
    print(model_data['loss_history'])
    model_data['iter'] = 1
    model_data['loss_history'] = [[4.391892433166504, 4.638905048370361]]
    # model_data['options']['batch_size'] = 4
    # model_data['options']['clipgrad'] = True
    model_data['options']['ct_mode'] = 'none'
    # model_data['options']['true_face_power'] = 0.01
    # model_data['options']['uniform_yaw'] = True
    f = open('ZIBI06_SAEHD_data.dat','wb')
    pickle.dump(model_data,f)

