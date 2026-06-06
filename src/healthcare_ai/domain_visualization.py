def plot_recording(frame):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(8,3));ax.hist(frame.length_of_stay,bins=range(1,14),edgecolor='white')
    ax.set(xlabel='Simulated length of stay (days)',ylabel='Encounters',title='Synthetic discharge cohort')
    fig.tight_layout();return fig
