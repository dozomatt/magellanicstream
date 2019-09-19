nu = 1420.405751786
freqs = np.asarray(data[freq]) + 1270 # add on the LO that reduces our signal
delta_nu = freqs - nu
c = 3 * (10**10)
v = -(delta_nu / freqs) * c

doppler_v = ugradio.get_projected_velocity(RA, DEC, JD) * 100

fig = plt.figure(figsize = (7, 4))
plt.plot(-np.fft.fftshift(v), np.fft.fftshift(smooth_data), label = 'Rest Velocity', color='orange')
plt.plot(-np.fft.fftshift(v - doppler_v), np.fft.fftshift(smooth_data), label = 'Doppler Velocity', color='b')
plt.xlim(-0.4e8,-0.1e8)
plt.legend(loc='best')
plt.xlabel('Velocity (cm/s)', fontsize=12)
plt.ylabel('Temperature (K)', fontsize=12)
plt.title('Signal Intensity', fontweight='bold', fontsize=15)
