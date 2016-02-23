import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.optimize as scop
import scipy.interpolate as scip
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Arial']


def picard_convergence_pattern(fct, x, max_labels=6, tol=1.0E-4):
    fig, ax = plt.subplots(figsize=(8,6))

    # solve
    fp_p = []
    h_p = []
    while 1:
        print 'x_{0:0>2d} = {1:7.5f}'.format(len(h_p), x)
        h_p.append(x)
        x = fct(x)
        fp_p.append(x)
        if abs(h_p[-1]-fp_p[-1]) < tol:
            break
    
    # the iteration results
    ax.scatter(h_p, fp_p, marker='x', color='blue', s=30)
    
    # the convergence pattern
    x_pattern = [h_p[0]]
    fp_pattern = [fp_p[0]]
    for i in range(1,len(h_p)):
        x_pattern.append(h_p[i])
        fp_pattern.append(fp_p[i-1])
        x_pattern.append(h_p[i])
        fp_pattern.append(fp_p[i])
    ax.plot(x_pattern, fp_pattern, color='green', ls='--')
    
    # the function
    idx_sort = np.argsort(h_p)
    ax.plot(np.array(h_p)[idx_sort], np.array(fp_p)[idx_sort], color='red', alpha=0.5)
    
    # initial guess
    dxt = (np.max(x_pattern)-np.min(x_pattern))/35.
    dyt = (np.max(fp_pattern)-np.min(fp_pattern))/35.
    ax.text(h_p[0]+dxt, fp_p[0]+dyt, '$x_0$')
    for i in range(1, min(max_labels+1, len(h_p))):
        label = ''.join(['$x_', str(i), '$'])
        ax.text(h_p[i]+dxt, fp_p[i]+dyt, label)
    
    ax.set_xlabel('$x$')
    ax.set_ylabel('$g(x)$')
    plt.title('Successive Approximations')
    plt.show()


def root_bracketing_pattern(f, a, b, dx, xbounds=(-0.1,1.4), ybounds=(-5,6)):
    x = np.linspace(a, b, int((b-a)/dx)+1)
    y = f(x)
    fig, ax = plt.subplots(figsize=(16,6))
    ax.plot(x, y, marker='x', color='r')
    switched = False
    for i, xt in enumerate(x):
        ft = str('$f_' + str(i) + '=$' + '${:4.2f}$'.format(y[i]))
        ax.text(xt, y[i], ft)
        if i > 0:
            if not switched and np.sign(y[i]) != np.sign(y[i-1]):
                pass
                ax.plot([x[i],x[i-1]], [y[i],y[i-1]], color='b')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$f(x)$')
    ax.plot([a,b],[0.,0.],color='gray',ls='-.',alpha=0.75)
    ax.set_xlim(a,b)
    ax.set_ylim(-4,1)
    plt.title('Bracketing', fontsize=20)
    plt.show()


def bisection_pattern(f, x1, x2, tol=1.0e-5, inset=True, ixmin=0.4, ixmax=0.7, iymin=-0.25, iymax=0.2, zoom=5, loc0=4, loc1=2, loc2=1):
    fig, ax = plt.subplots(figsize=(10,6))
    plt.title('Bisection', fontsize=20)
    x = np.linspace(x1, x2, 100)
    y = f(x)
    ax.plot(x, y, color='r')
    f1 = f(x1)
    f2 = f(x2)
    x1s = x1
    x2s = x2
    ax.scatter( [x1,x2], [f1,f2], marker='x', s=50)
    virgin = True
    while abs(x1-x2) > tol:
        x3 = 0.5*(x1 + x2)
        f3 = f(x3)
        ax.scatter( [x3], [f3], marker='x', s=50)
        if f2*f3 < 0.0:
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3

    # zero line
    xlim = ax.get_xlim()
    ax.plot([xlim[0],xlim[1]],[0.,0.],color='gray',ls='-.',alpha=0.75)
    ax.set_xlim(xlim)
            
    # zoomed inset
    if inset:
        x1, x2 = x1s, x2s
        axins = zoomed_inset_axes(ax, zoom, loc=loc0)
        x = np.linspace(x1, x2, 100)
        y = f(x)
        axins.plot(x, y, color='r')
        f1 = f(x1)
        f2 = f(x2)
        axins.scatter( [x1,x2], [f1,f2], marker='x', s=50)
        virgin = True
        while abs(x1-x2) > tol:
            x3 = 0.5*(x1 + x2)
            f3 = f(x3)
            axins.scatter( [x3], [f3], marker='x', s=50)
            if f2*f3 < 0.0:
                x1 = x3
                f1 = f3
            else:
                x2 = x3
                f2 = f3
        axins.plot([ixmin,ixmax],[0.,0.],color='gray',ls='-.',alpha=0.75)
        axins.set_xlim(ixmin, ixmax)
        axins.set_ylim(iymin, iymax)
        axins.get_xaxis().set_visible(False)
        axins.get_yaxis().set_visible(False)
        mark_inset(ax, axins, loc1=loc1, loc2=loc2, fc="none", ec="0.5")
        
    xf = (x1 + x2)/2.0
    ax.set_xlabel('$x$')
    ax.set_ylabel('$f(x)$')
    plt.show()


def newton_convergence_pattern(fn, dx, x_0, tol, max_labels0=1, max_labels1=2, inset=True, ixmin=3.0, ixmax=3.2, iymin=-0.1, iymax=0.1, zoom=8, loc0=1, loc1=3, loc2=2, maxiter=100):
    fig, ax = plt.subplots(figsize=(10,6))
    plt.title('Newton', fontsize=20)
    x_n = [x_0]
    y_n = [fn(x_0)]
    
    fx_n = [x_0]
    fy_n = [fn(x_0)]
    
    # solving
    i = 0
    while 1:
        dfdx = (fn(x_n[-1]+dx) - fn(x_n[-1])) / dx
        a = fn(x_n[-1])-(dfdx*x_n[-1])
        x_zero = -a/dfdx
        x_n.append(x_zero)        
        y_n.append(0.)
        fx_n.append(x_zero)
        fy_n.append(fn(x_zero))
        if abs(x_n[-1]-x_n[-2]) < tol:
            break
        x_n.append(x_zero)
        y_n.append(fn(x_zero))
        i = i+1
        if i >= maxiter:
            break
        
    # the iteration results
    ax.scatter(fx_n, fy_n, marker='x', color='blue', s=30)
    
    # the convergence pattern
    ax.plot(x_n, y_n, color='green', ls='--')
        
    # the function
    x = np.linspace( np.min(x_n), np.max(x_n), 50)
    f = fn(x)
    ax.plot(x, f, color='red', alpha=0.5)
    
    # initial guess
    dxt = (np.max(x_n)-np.min(x_n))/35.
    dyt = (np.max(y_n)-np.min(y_n))/35.
    ax.text(fx_n[0]+dxt, fy_n[0]+dyt, '$x_0$')    
    for i in range(1, min(max_labels0+1, len(fx_n))):
        label = ''.join(['$x_', str(i), '$'])
        ax.text(fx_n[i]+dxt, fy_n[i]+dyt, label)

    # zero line
    xlim = ax.get_xlim()
    ax.plot([xlim[0],xlim[1]],[0.,0.],color='gray',ls='-.',alpha=0.75)
    ax.set_xlim(xlim)

    # zoomed inset
    if inset:
        axins = zoomed_inset_axes(ax, zoom, loc=loc0)
        axins.scatter(fx_n, fy_n, marker='x', color='blue', s=30)
        axins.plot(x_n, y_n, color='green', ls='--')
        axins.plot(x, f, color='red', alpha=0.5)
        for i in range(max_labels0+1, min(max_labels0+1+max_labels1,len(fx_n))):
            label = ''.join(['$x_', str(i), '$'])
            axins.text(fx_n[i]+dxt/8., fy_n[i]+dyt/8., label)
        
        axins.plot([ixmin,ixmax],[0.,0.],color='gray',ls='-.',alpha=0.75)
        axins.set_xlim(ixmin, ixmax)
        axins.set_ylim(iymin, iymax)
        axins.get_xaxis().set_visible(False)
        axins.get_yaxis().set_visible(False)
        mark_inset(ax, axins, loc1=loc1, loc2=loc2, fc="none", ec="0.5")
    
    ax.set_xlabel('$x$')
    ax.set_ylabel('$f_n(x)$')
    plt.show()
 