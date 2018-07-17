# Create figure with 3x3 sub-plots.
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
      pass
    
# use vmin and vmax to normalize the color
ax.imshow(image, vmin=w_min, vmax=w_max, cmap='seismic')
    
# print time usage with better formatting
from datetime import timedelta
str(timedelta(seconds=5))  # 00:00:05



