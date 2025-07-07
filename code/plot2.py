import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
x = ['LR', 'DTR','RFR','BGR', 'GBR', 'MLP']
y_rsme = [[1.4937046497635849, 1.6224234052611028, 1.5128159620979447, 1.5188263420026589, 1.4526338499771998 , 1.4743369817733765], 
          [1.9422089418216215, 2.010460123089262, 1.918275498781776, 1.921220275481479, 1.859069740743164,  1.9027711153030396], 
          [2.1266041436385383, 2.1615964136509875, 2.0645833015695967, 2.0674037500321463, 2.013219643557137, 2.073042392730713]]

y_mae = [[1.1007255894306334, 1.2209761955038023, 1.125502244150249, 1.1299490567322303, 1.0567139266878194, 1.076400637626648], 
         [1.485103340868841, 1.5469634259735288, 1.464004945953909, 1.4693930790699108, 1.4027484358242757, 1.4422779083251953], 
         [1.6524776897499944, 1.673977783634687, 1.5844022687684243, 1.5859603943025489, 1.5269452572588842, 1.588374376296997]]

y_mape = [[0.042159827276660275, 0.04821763900739646, 0.04414609053831907, 0.04429794182725106, 0.041483701943124916, 0.042143430560827255], 
          [0.05801135559896249, 0.061508825213882345,  0.05812047041298815, 0.05826608304477983, 0.055970462923587136, 0.0573125034570694], 
          [0.06524406333066005, 0.0669808225761172, 0.06340386852767248, 0.06349752239251798, 0.06153846722922425, 0.0637076199054718]]

y_r2 = [[0.8676141118021683, 0.8701331906982346, 0.8865402848341396, 0.885613296968225, 0.8940175904791441, 0.8904016017913818], 
        [0.7609114509492743, 0.8041999497325233, 0.8210503414203101, 0.8208170798064733,  0.8296367762674686, 0.8208661675453186], 
        [0.6995697003478522, 0.7745896790702582, 0.7945696785579377, 0.7940409991108747, 0.8018083009290882, 0.788244366645813]]

y_wi =[[0.7824791741586985, 0.7452340128026402, 0.7781904686618359, 0.7762554042110292, 0.7924626575685452, 0.7882356126859118],
       [0.6354273841265523, 0.6106241566965487, 0.645609815985017, 0.6446620651983608, 0.6609378991706001, 0.6509523421034356],
       [0.5643765382339502, 0.5520980546229324, 0.5919939227152056, 0.5906874350912333, 0.6056845733116711, 0.5875993608124255]]
y_pb = [[-0.019072045925809866, -0.4368795406640294, -0.4294338643690722, -0.4524685754899728, 0.12795193191198934, 0.27092860304668326],
        [-0.19469023121832182, -0.8101986588689676, -0.6843365329362938, -0.7170143831587334,  0.1126551345103642, 0.18444909216418132],
        [-0.18788580524133494, -0.9051915929332155, -0.730924258310039, -0.7039647704967356, 0.15103298993605843, 0.30137357359142725]]

scores_data = [y_rsme, y_mae, y_mape, y_r2, y_wi, y_pb]
score_names = ["RSME", "MAE", "MAPE", "R2", "WI", "PBIAS"]
models = ['LR', 'DTR', 'RFR', 'BGR', 'GBR', 'MLP']
days_ahead = ['1-Day Ahead', '2-Day Ahead', '3-Day Ahead']

num_scores = len(score_names)
angles = np.linspace(0, 2 * np.pi, num_scores, endpoint=False) # {Link: Python Graph Gallery https://python-graph-gallery.com/web-radar-chart-with-matplotlib/}
anglesc = np.concatenate((angles, [angles[0]]))  # Close the radar chart shape

fig, axs = plt.subplots(1, 3, figsize=(15, 8), subplot_kw=dict(polar=True)) # {Link: CodeSignal https://codesignal.com/learn/courses/customizing-and-styling-plots/lessons/multi-figure-layouts-with-matplotlib}

# Colors for the models
model_colors = ['skyblue', 'lightcoral', 'yellowgreen', 'coral', 'orchid', 'sandybrown']


for i, day in enumerate(days_ahead):
    ax = axs[i]
    ax.set_theta_offset(np.pi / 2)  # Set the start angle at the top
    ax.set_theta_direction(-1) # Plot clock-wise

    # Set the labels for the axes (scores)
    ax.set_thetagrids(np.degrees(angles), score_names) # {Link: Python Graph Gallery https://python-graph-gallery.com/web-radar-chart-with-matplotlib/}

    # Plot each model's performance on the radar chart for the current day
    for j in range(len(models)):
        values = [scores_data[k][i][j] for k in range(num_scores)] # Get scores for model j for day i
        values = np.concatenate((values, [values[0]]))  # Close the shape
        ax.plot(anglesc, values, 'o-', linewidth=1.5, linestyle=':', color=model_colors[j], label=models[j]) 

    ax.set_title(day, y=1.1) 
    if i == 2: ax.legend(loc='upper right', bbox_to_anchor=(1, 1.3), fontsize='medium')
    ax.grid(True)

plt.tight_layout()
plt.show()