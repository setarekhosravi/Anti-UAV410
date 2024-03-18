import numpy as np
"""

mode 1 means the results is formatted by (x,y,w,h)
mode 2 means the results is formatted by (x1,y1,x2,y2)

Default_Trackers indicates results trained without the AntiUAV410 dataset
Trained_Trackers indicates results trained with the AntiUAV410 dataset

"""

Default_Trackers=[
{'name': 'DSST', 'path': './Tracking_results/Defaults/DSST', 'mode': 1},
{'name': 'KCF', 'path': './Tracking_results/Defaults/KCF', 'mode': 1},
{'name': 'SRDCF', 'path': './Tracking_results/Defaults/SRDCF', 'mode': 1},
{'name': 'Staple', 'path': './Tracking_results/Defaults/Staple', 'mode': 1},
{'name': 'MDNet', 'path': './Tracking_results/Defaults/MDNet', 'mode': 1},
{'name': 'SiamFC', 'path': './Tracking_results/Defaults/SiamFC', 'mode': 1},
{'name': 'CSRDCF', 'path': './Tracking_results/Defaults/CSRDCF', 'mode': 1},
{'name': 'ECO', 'path': './Tracking_results/Defaults/ECO', 'mode': 1},
{'name': 'CFNet', 'path': './Tracking_results/Defaults/CFNet', 'mode': 1},
{'name': 'BACF', 'path': './Tracking_results/Defaults/BACF', 'mode': 1},
{'name': 'STRCF', 'path': './Tracking_results/Defaults/STRCF', 'mode': 1},
{'name': 'SiamRPN', 'path': './Tracking_results/Defaults/SiamRPN', 'mode': 1},
{'name': 'DaSiamRPN', 'path': './Tracking_results/Defaults/DaSiamRPN', 'mode': 1},
{'name': 'ASRCF', 'path': './Tracking_results/Defaults/ASRCF', 'mode': 1},
{'name': 'TADT', 'path': './Tracking_results/Defaults/TADT', 'mode': 1},
{'name': 'SiamRPN++', 'path': './Tracking_results/Defaults/SiamRPN++', 'mode': 1},
{'name': 'ATOM', 'path': './Tracking_results/Defaults/ATOM', 'mode': 1},
{'name': 'ARCF', 'path': './Tracking_results/Defaults/ARCF', 'mode': 1},
{'name': 'DiMP50', 'path': './Tracking_results/Defaults/DiMP', 'mode': 1},
{'name': 'SiamFC++', 'path': './Tracking_results/Defaults/SiamFC++', 'mode': 1},
{'name': 'GlobalTrack', 'path': './Tracking_results/Defaults/GlobalTrack', 'mode': 2},
{'name': 'AutoTrack', 'path': './Tracking_results/Defaults/AutoTrack', 'mode': 1},
{'name': 'PrDiMP50', 'path': './Tracking_results/Defaults/PrDiMP', 'mode': 1},
{'name': 'SiamCAR', 'path': './Tracking_results/Defaults/SiamCAR', 'mode': 1},
{'name': 'SiamBAN', 'path': './Tracking_results/Defaults/SiamBAN', 'mode': 1},
{'name': 'SiamRCNN', 'path': './Tracking_results/Defaults/SiamRCNN', 'mode': 1},
{'name': 'ROAM', 'path': './Tracking_results/Defaults/ROAM', 'mode': 1},
{'name': 'Super_DiMP', 'path': './Tracking_results/Defaults/Super_DiMP', 'mode': 1},
{'name': 'KYS', 'path': './Tracking_results/Defaults/KYS', 'mode': 1},
{'name': 'TrDiMP', 'path': './Tracking_results/Defaults/TrDiMP', 'mode': 1},
{'name': 'TransT', 'path': './Tracking_results/Defaults/TransT', 'mode': 1},
{'name': 'STMTrack', 'path': './Tracking_results/Defaults/STMTrack', 'mode': 1},
{'name': 'HiFT', 'path': './Tracking_results/Defaults/HiFT', 'mode': 1},
{'name': 'Stark-ST50', 'path': './Tracking_results/Defaults/Stark/Stark50', 'mode': 1},
{'name': 'Stark-ST101', 'path': './Tracking_results/Defaults/Stark/Stark101', 'mode': 1},
{'name': 'KeepTrack', 'path': './Tracking_results/Defaults/KeepTrack', 'mode': 1},
{'name': 'RTS', 'path': './Tracking_results/Defaults/RTS/rts50', 'mode': 1},
{'name': 'ToMP50', 'path': './Tracking_results/Defaults/ToMP/tomp50', 'mode': 1},
{'name': 'ToMP101', 'path': './Tracking_results/Defaults/ToMP/tomp101', 'mode': 1},
{'name': 'Unicorn-Large', 'path': './Tracking_results/Defaults/Unicorn_sot/unicorn_track_large', 'mode': 1},
{'name': 'Unicorn-Tiny', 'path': './Tracking_results/Defaults/Unicorn_sot/unicorn_track_tiny', 'mode': 1},
{'name': 'AiATrack', 'path': './Tracking_results/Defaults/AiATrack/baseline', 'mode': 1},
{'name': 'OSTrack-256', 'path': './Tracking_results/Defaults/OSTrack/vitb_256_mae_ce_32x4_ep300', 'mode': 1},
{'name': 'OSTrack-384', 'path': './Tracking_results/Defaults/OSTrack/vitb_384_mae_ce_32x4_ep300', 'mode': 1},
{'name': 'SLT-TransT', 'path': './Tracking_results/Defaults/SLT_TransT', 'mode': 1},
{'name': 'TCTrack', 'path': './Tracking_results/Defaults/TCTrack', 'mode': 1},
{'name': 'SwinTrack-Tiny', 'path': './Tracking_results/Defaults/SwinTrack-Tiny', 'mode': 2},
{'name': 'SwinTrack-Base', 'path': './Tracking_results/Defaults/SwinTrack-Base', 'mode': 2},
{'name': 'JointNLT', 'path': './Tracking_results/Defaults/JointNLT/swin_b_ep300', 'mode': 1},
{'name': 'SeqTrack-B256', 'path': './Tracking_results/Defaults/SeqTrack/seqtrack_b256', 'mode': 1},
{'name': 'SeqTrack-B384', 'path': './Tracking_results/Defaults/SeqTrack/seqtrack_b384', 'mode': 1},
{'name': 'ARTrack', 'path': './Tracking_results/Defaults/ARTrack/artrack_seq_256_full', 'mode': 1},
{'name': 'DropTrack', 'path': './Tracking_results/Defaults/DropTrack/ostrack/vitb_384_mae_ce_32x4_got10k_ep100', 'mode': 1},
{'name': 'GRM', 'path': './Tracking_results/Defaults/GRM/vitb_256_ep300', 'mode': 1},
{'name': 'MixformerV2-B', 'path': './Tracking_results/Defaults/MixformerV2/mixformer2_vit_online/288_depth8_score', 'mode': 1},
{'name': 'ROMTrack', 'path': './Tracking_results/Defaults/ROMTrack/baseline_stage2', 'mode': 1},
                   ]


Trained_Trackers=[
{'name': 'SiamDT', 'path': './Tracking_results/Trained_with_antiuav410/SiamDT', 'mode': 1},
{'name': 'AiATrack', 'path': './Tracking_results/Trained_with_antiuav410/AiATrack/baseline', 'mode': 1},
{'name': 'ATOM', 'path': './Tracking_results/Trained_with_antiuav410/ATOM/default', 'mode': 1},
{'name': 'DiMP50', 'path': './Tracking_results/Trained_with_antiuav410/DiMP/dimp50', 'mode': 1},
{'name': 'PrDiMP50', 'path': './Tracking_results/Trained_with_antiuav410/DiMP/prdimp50', 'mode': 1},
{'name': 'Super_DiMP', 'path': './Tracking_results/Trained_with_antiuav410/DiMP/super_dimp', 'mode': 1},
{'name': 'GlobalTrack', 'path': './Tracking_results/Trained_with_antiuav410/GlobalTrack', 'mode': 2},
{'name': 'KeepTrack', 'path': './Tracking_results/Trained_with_antiuav410/KeepTrack', 'mode': 1},
{'name': 'KYS', 'path': './Tracking_results/Trained_with_antiuav410/KYS/default', 'mode': 1},
{'name': 'ROAM', 'path': './Tracking_results/Trained_with_antiuav410/ROAM', 'mode': 1},
{'name': 'SiamBAN', 'path': './Tracking_results/Trained_with_antiuav410/SiamBAN', 'mode': 1},
{'name': 'SiamCAR', 'path': './Tracking_results/Trained_with_antiuav410/SiamCAR', 'mode': 1},
{'name': 'Stark-ST101', 'path': './Tracking_results/Trained_with_antiuav410/Stark-ST101', 'mode': 1},
{'name': 'SwinTrack-Tiny', 'path': './Tracking_results/Trained_with_antiuav410/SwinTrack-Tiny', 'mode': 2},
{'name': 'SwinTrack-Base', 'path': './Tracking_results/Trained_with_antiuav410/SwinTrack-Base', 'mode': 2},
{'name': 'TCTrack', 'path': './Tracking_results/Trained_with_antiuav410/TCTrack', 'mode': 1},
{'name': 'ToMP50', 'path': './Tracking_results/Trained_with_antiuav410/ToMP/tomp50', 'mode': 1},
{'name': 'ToMP101', 'path': './Tracking_results/Trained_with_antiuav410/ToMP/tomp101', 'mode': 1},
{'name': 'DropTrack', 'path': './Tracking_results/Trained_with_antiuav410/DropTrack/ostrack/vitb_384_mae_ce_32x4_got10k_ep100', 'mode': 1},
{'name': 'MixformerV2-B', 'path': './Tracking_results/Trained_with_antiuav410/MixFormerV2/mixformer2_vit_online/288_depth8_score', 'mode': 1},
                   ]