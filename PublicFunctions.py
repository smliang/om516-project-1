import matplotlib.pyplot as plt
import matplotlib as mpl

def DrawCombinedxBarAndRCharts(xLabels, sampleMeans, ranges, xBarCenterLine, xBarUCL, xBarLCL, RCenterLine, RUCL, RLCL):
    fig = plt.figure(figsize=(10, 9))
    sf_xBar = plt.subplot(211)
    sf_xBar.set_title('x-bar Chart',color='b')
    sf_xBar.plot(xLabels,sampleMeans,'bs')
    sf_xBar.plot(xLabels,sampleMeans,'b')
    sf_xBar.plot(xLabels,[xBarCenterLine]*len(xLabels),'k--')
    sf_xBar.plot(xLabels,[(2*xBarCenterLine+xBarUCL)/3]*len(xLabels),'y--')
    sf_xBar.plot(xLabels,[(xBarCenterLine+2*xBarUCL)/3]*len(xLabels),'--',color='orange')
    sf_xBar.plot(xLabels,[xBarUCL]*len(xLabels),'r--')
    sf_xBar.plot(xLabels,[(2*xBarCenterLine+xBarLCL)/3]*len(xLabels),'y--')
    sf_xBar.plot(xLabels,[(xBarCenterLine+2*xBarLCL)/3]*len(xLabels),'--',color='orange')
    sf_xBar.plot(xLabels,[xBarLCL]*len(xLabels),'r--')
    sf_R = plt.subplot(212)
    sf_R.set_title('R Chart',color='purple')
    sf_R.plot(xLabels,ranges,'s',color='purple')
    sf_R.plot(xLabels,ranges,color='purple')
    sf_R.plot(xLabels,[RCenterLine]*21,'k--')
    sf_R.plot(xLabels,[(2*RCenterLine+RUCL)/3]*len(xLabels),'y--')
    sf_R.plot(xLabels,[(RCenterLine+2*RUCL)/3]*len(xLabels),'--',color='orange')
    sf_R.plot(xLabels,[RUCL]*len(xLabels),'r--')
    sf_R.plot(xLabels,[(2*RCenterLine+RLCL)/3]*len(xLabels),'y--')
    sf_R.plot(xLabels,[(RCenterLine+2*RLCL)/3]*len(xLabels),'--',color='orange')
    sf_R.plot(xLabels,[RLCL]*len(xLabels),'r--')
    return fig

def ConvertToZScores(values, mu, sigma):
    return (values-mu)/sigma