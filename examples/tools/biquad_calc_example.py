################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example script that calculates biquad-filter Coefficients by giving a filter specification.

The resulting filters frequency response is plotted in a "Bode magnitude plot"

The bode plot is created using a MATLAB-like bode plot function.
Required Python Packages for the bode plot:
    * matplotlib `pip install matplotlib`
    * control `pip install control`

The plot shows the theoretical continuous filter behavior and the expected behavior of the discrete filter.
"""

from pytrinamic.tools import calculate_biquad_filter_coefficients, LowPassFilterSpec, AntiResonanceFilterSpec

# Set to the targets sampling rate. 25kHz is the default PWM frequency for TMC9660 and TMC4671.
sample_rate_hz = 25_000
# Set to the targets down-sampling factor
down_sampling_factor = 1  

# Chose one of the following three filter types and update the filter specification to your needs.
filter_spec = LowPassFilterSpec(fc=400.0)
#filter_spec = LowPassFilterSpec(fc=1000.0, q=0.7071)
#filter_spec = AntiResonanceFilterSpec(fp=1000.0, fz=500.0, dp=4.0, dz=0.0)

# Select if you like a bode plot to show up or not.
plot_bode = True

result = calculate_biquad_filter_coefficients(
    chip_type="TMC4671",  # you may also input "TMC9660" here
    filter_spec=filter_spec,
    sample_rate_hz=sample_rate_hz,
    down_sampling_factor=down_sampling_factor,
)

# Output the normalized coefficients to be written to the chip's biquad registers.
print(result.normalized_coefficients)

if plot_bode:
    import matplotlib.pyplot as plt
    import control as ct
    cont_coffs = result.continuous_coefficients
    disc_coffs = result.tilde_coefficients
    s = ct.tf("s")
    g2 = (cont_coffs.b_2*s**2 + cont_coffs.b_1*s + cont_coffs.b_0) / (cont_coffs.a_2*s**2 + cont_coffs.a_1*s + cont_coffs.a_0)
    z = ct.tf([1, 0], [0, 1], dt=down_sampling_factor/sample_rate_hz)
    g_lp = (disc_coffs.b_2*z**2 + disc_coffs.b_1*z**1 + disc_coffs.b_0) / (disc_coffs.a_2*z**2 + disc_coffs.a_1*z**1 + disc_coffs.a_0)
    g_lp.minreal()
    fig, (mag_ax, phase_ax) = plt.subplots(2, 1)
    ct.bode_plot(g2, Hz=True, ax=(mag_ax, phase_ax), label="Continuous Filter")
    ct.bode_plot(g_lp, Hz=True, ax=(mag_ax, phase_ax), label="Discrete Filter")
    mag_ax.legend()
    mag_ax.set_xlim([10, sample_rate_hz/2])
    phase_ax.legend()
    phase_ax.set_xlim([10, sample_rate_hz/2])
    plt.show()
