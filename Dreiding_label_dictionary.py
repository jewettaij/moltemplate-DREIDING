# Dictionary of all possible labels
# Index [0] - mass; [1] - bond data (R0); [2] - nonbond LJ where [2][0] is
# R0 and [2][1] is D0; [3] - dihedral data

labelDict= {
    "H": [1.008, 0.330, [2.846421, 0.0152], 0],
    "H_HB": [1.008, 0.330, [2.846421, 0.0001], 0],
    "C_3": [12.011, 0.770, [3.472990, 0.0951], 3],
    "C_34": [16.043, 0.770, [3.774738, 0.3016], 3],
    "C_33": [15.035, 0.770, [3.699368, 0.2500], 3],
    "C_32": [14.027, 0.770, [3.623909, 0.1984], 3],
    "C_31": [13.019, 0.770, [3.548450, 0.1467], 3],
    "C_R": [12.011, 0.700, [3.472990, 0.0951], 2],
    "C_R1": [13.019, 0.700, [3.768502, 0.1356], 2],
    "C_R_b1": [12.011, 0.700, [3.472990, 0.0951], 2],
    "C_R1_b1": [13.019, 0.700, [3.768502, 0.1356], 2],
    "C_2": [12.011, 0.670, [3.472990, 0.0951], 2],
    "C_2_b1": [12.011, 0.670, [3.472990, 0.0951], 2],
    "C_2_b2": [12.011, 0.670, [3.472990, 0.0951], 2],
    "C_1": [12.011, 0.602, [3.472990, 0.0951], 0],
    "C_1_b1": [12.011, 0.602, [3.472990, 0.0951], 0],
    "N_3": [14.007, 0.702, [3.262560, 0.0774], 2],
    "N_3_ha": [14.007, 0.702, [3.262560, 0.0774], 2],
    "N_3_hd": [14.007, 0.702, [3.262560, 0.0774], 2],
    "N_R_d1": [14.007, 0.650, [3.262560, 0.0774], 1],
    "N_R_d1_ha": [14.007, 0.650, [3.262560, 0.0774], 1],
    "N_R_d2": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_R_d2_ha": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_R_d2_hd": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_R_b1_d2": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_R_b1_d2_ha": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_R_b1_d2_hd": [14.007, 0.650, [3.262560, 0.0774], 2],
    "N_2_d1": [14.007, 0.615, [3.262560, 0.0774], 1],
    "N_2_d1_ha": [14.007, 0.615, [3.262560, 0.0774], 1],
    "N_2_d1_hd": [14.007, 0.615, [3.262560, 0.0774], 1],
    "N_2_b1_d1": [14.007, 0.615, [3.262560, 0.0774], 1],
    "N_2_b1_d1_ha": [14.007, 0.615, [3.262560, 0.0774], 1], # hd equivalent doesn't exist, can't need b1 specifying and be hd
    "N_2_b2_d1": [14.007, 0.615, [3.262560, 0.0774], 1],
    "N_2_b2_d1_ha": [14.007, 0.615, [3.262560, 0.0774], 1], # hd equivalent doesn't exist, can't need b1 specifying and be hd
    "N_2_d2": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_d2_hd": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_d2_ha": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b1_d2": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b1_d2_hd": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b1_d2_ha": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b2_d2": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b2_d2_hd": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_2_b2_d2_ha": [14.007, 0.615, [3.262560, 0.0774], 2],
    "N_1": [14.007, 0.556, [3.262560, 0.0774], 0],
    "N_1_ha": [14.007, 0.556, [3.262560, 0.0774], 0],
    "O_3": [15.999, 0.660, [3.033153, 0.0957], 1],
    "O_3_hd": [15.999, 0.660, [3.033153, 0.0957], 1],
    "O_3_ha": [15.999, 0.660, [3.033153, 0.0957], 1],
    "O_R": [15.999, 0.660, [3.033153, 0.0957], 1],
    "O_R_ha": [15.999, 0.660, [3.033153, 0.0957], 1],
    "O_2": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_ha": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_b1": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_b1_ha": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_b1_hd": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_b2": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_2_b2_ha": [15.999, 0.560, [3.033153, 0.0957], 1],
    "O_1": [15.999, 0.528, [3.033153, 0.0957], 0],
    "O_1_ha": [15.999, 0.528, [3.033153, 0.0957], 0],

    # Second Wave additions
    "H_B": [1.008, 0.510, [2.846421, 0.0152], 1],
    "B_3": [10.810, 0.880, [3.581513, 0.095], 3],
    "B_2_d1": [10.810, 0.790, [3.581513, 0.095], 1],
    "B_2_d2": [10.810, 0.790, [3.581513, 0.095], 2],
    "B_2_b1_d1": [10.810, 0.790, [3.581513, 0.095], 1],
    "B_2_b1_d2": [10.810, 0.790, [3.581513, 0.095], 2],
    "B_2_b2_d1": [10.810, 0.790, [3.581513, 0.095], 1],
    "B_2_b2_d2": [10.810, 0.790, [3.581513, 0.095], 2],
    "F": [18.998, 0.611, [3.093200, 0.0725], 0],
    "F_hd": [18.998, 0.611, [3.093200, 0.0725], 0],
    "F_ha": [18.998, 0.611, [3.093200, 0.0725], 0],
    "Cl": [34.450, 0.997, [3.519317, 0.2833], 0],
    "Br": [79.904, 1.167, [3.519050, 0.37], 0],
    "I": [126.904, 1.360, [3.697230, 0.51], 0],
    "Al_3_d1": [26.982, 1.047, [3.893227, 0.31], 1],
    "Al_3_d2": [26.982, 1.047, [3.893227, 0.31], 2],
    "Si_3": [28.085, 0.937, [3.804138, 0.31], 3],
    "P_3_d2": [30.974, 0.890, [3.697230, 0.32], 2],
    "P_3_d3": [30.974, 0.890, [3.697230, 0.32], 3],
    "P_3_d4": [30.974, 0.890, [3.697230, 0.32], 4],
    "S_3": [32.060, 1.040, [3.590322, 0.32], 1],
    "Ga_3": [69.723, 1.210, [3.911045, 0.40], 2],
    "Ge_3_d1": [72.630, 1.210, [3.804138, 0.40], 1],
    "Ge_3_d2": [72.630, 1.210, [3.804138, 0.40], 2],
    "Ge_3_d3": [72.630, 1.210, [3.804138, 0.40], 3],
    "As_3_d1": [74.922, 1.210, [3.697230, 0.41], 1],
    "As_3_d2": [74.922, 1.210, [3.697230, 0.41], 2],
    "As_3_d3": [74.922, 1.210, [3.697230, 0.41], 3],
    "As_3_d4": [74.922, 1.210, [3.697230, 0.41], 4],
    "Se_3_d1": [78.971, 1.210, [3.590321, 0.43], 1],
    "Se_3_d2": [78.971, 1.210, [3.590321, 0.43], 2],
    "Se_3_d3": [78.971, 1.210, [3.590321, 0.43], 3],
    "Se_3_d5": [78.971, 1.210, [3.590321, 0.43], 5],
    "In_3_d1": [114.818, 1.390, [4.089225, 0.55], 1],
    "In_3_d2": [114.818, 1.390, [4.089225, 0.55], 2],
    "Sn_3_d2": [118.710, 1.373, [3.982317, 0.55], 2],
    "Sn_3_d3": [118.710, 1.373, [3.982317, 0.55], 3],
    "Sb_3_d2": [121.760, 1.432, [3.875409, 0.55], 2],
    "Sb_3_d3": [121.760, 1.432, [3.875409, 0.55], 3],
    "Sb_3_d4": [121.760, 1.432, [3.875409, 0.55], 4],
    "Te_3_d1": [127.600, 1.280, [3.768502, 0.57], 1],
    "Te_3_d2": [127.600, 1.280, [3.768502, 0.57], 2],
    "Te_3_d3": [127.600, 1.280, [3.768502, 0.57], 3],
    "Te_3_d5": [127.600, 1.280, [3.768502, 0.57], 5],
    "Na": [22.990, 1.860, [2.800986, 0.50], 0],
    "Ca": [40.078, 1.940, [3.093200, 0.050], 0],
    "Fe": [55.845, 1.285, [4.044680, 0.055], 0],
    "Zn": [65.380, 1.330, [4.044680, 0.055], 0],
}
