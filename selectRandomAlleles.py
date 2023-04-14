import random

names = ['Earb_J.0', 'Earb_J.1', 'Earb_SC3.0', 'Earb_SC3.1', 'Earb_SC4.0', 'Earb_SC4.1', 'Ebic_15R1.0', 'Ebic_15R1.1', 'Ebic_15R3.0', 'Ebic_15R3.1', 'Ebic_f.0', 
         'Ebic_f.1', 'Ehyb_BB1.0', 'Ehyb_BB1.1', 'Ehyb_BB2.0', 'Ehyb_BB2.1', 'Ehyb_DH1.0', 'Ehyb_DH1.1', 'Ekur_20R2.0', 'Ekur_20R2.1', 'Ekur_20R3.0', 'Ekur_20R3.1',
         'Ekur_25R5.0', 'Ekur_25R5.1', 'Emax_DH3.0', 'Emax_DH3.1', 'Emax_KM1.0', 'Emax_KM1.1', 'Emax_KM2.0', 'Emax_KM2.1', 'Erad_BB1.0', 'Erad_BB1.1', 'Erad_BB2.0',
         'Erad_BB2.1', 'Erad_BH1.0', 'Erad_BH1.1', 'Erad_BH2.0', 'Erad_BH2.1', 'Erad_BiS3.0', 'Erad_BiS3.1', 'Erad_BiS4.0', 'Erad_BiS4.1', 'Erad_CBS1.0', 'Erad_CBS1.1',
         'Erad_CBS14.0', 'Erad_CBS14.1', 'Erad_CR1.0', 'Erad_CR1.1', 'Erad_CR2.0', 'Erad_CR2.1', 'Erad_CW1.0', 'Erad_CW1.1', 'Erad_CW17.0', 'Erad_CW17.1', 
         'Erad_DH1.0', 'Erad_DH1.1', 'Erad_DW1.0', 'Erad_DW1.1', 'Erad_DW3.0', 'Erad_DW3.1', 'Erad_f.0', 'Erad_f.1', 'Erad_FB1.0', 'Erad_FB1.1', 'Erad_FB2.0', 
         'Erad_FB2.1', 'Erad_G1.0', 'Erad_G1.1', 'Erad_G15.0', 'Erad_G15.1', 'Erad_HB15.0', 'Erad_HB15.1', 'Erad_HB65.0', 'Erad_HB65.1', 'Erad_J.0', 'Erad_J.1',
         'Erad_M19.0', 'Erad_M19.1', 'Erad_M9.0', 'Erad_M9.1', 'Erad_MK1.0', 'Erad_MK1.1', 'Erad_MK2.0', 'Erad_MK2.1', 'Erad_PA2.0', 'Erad_PA2.1', 'Erad_PA3.0',
         'Erad_PA3.1', 'EradSS_DH1.0', 'EradSS_DH1.1', 'EradSS_DH3.0', 'EradSS_DH3.1', 'Erad_TK.0', 'Erad_TK.1']

# Create a set to keep track of the selected names
selected_names = set()

# Iterate until all names have been selected
while len(selected_names) < len(names):
# Shuffle the remaining names and select the first name that meets the conditions
    random.shuffle(names)
    for name in names:
        if name not in selected_names and ((name.endswith('0') and not any(n.startswith(name[:-1]) and n.endswith('1') for n in selected_names)) or (name.endswith('1') and not any(n.startswith(name[:-1]) and n.endswith('0') for n in selected_names))):
            print(name)
            selected_names.add(name)
            names.remove(name)
            break