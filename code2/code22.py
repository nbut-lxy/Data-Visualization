import matplotlib.pyplot as plt;
from matplotlib import patheffects;
import numpy as np;
data = np.random.randn(20);
fontsize =18;
plt.plot(data);
title = 'This is title';
x_label='x axis';
y_label='y_axis';
title_obj = plt.title(title,fontsize=fontsize,verticalalignment='bottom');
title_obj.set_path_effects([patheffects.withSimplePatchShadow()]);
offset_xy = (1,-1);
rgb = (1.0,0.0,0.0);
alpha=0.8;
pe = patheffects.withSimplePatchShadow(offset_xy,rgb,alpha);
xlabel_obj = plt.xlabel(x_label,fontsize=fontsize,alpha=0.5);
xlabel_obj.set_path_effects([pe]);
ylabel_obj = plt.ylabel(y_label,fontsize=fontsize,alpha=0.5);
ylabel_obj.set_path_effects([pe]);
plt.show();