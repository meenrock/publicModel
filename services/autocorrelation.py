
def plot_autocor(data, lags=None):
  plt.figure(figsize = (15,4))
  plt.subplot(221) # w x h x id
  plt.title('series')
  plt.plot(data)
  plt.subplot(222)
  plt.title('histogram of the series')
  plt.hist(data)
  plt.show()
  sm.tsa.graphics.plot_acf(data, lags=lags, zero=False)
  sm.tsa.graphics.plot_pacf(data, lags=lags, zero=False)
  plt.show()