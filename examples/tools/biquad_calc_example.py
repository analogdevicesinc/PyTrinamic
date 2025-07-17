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

The plot shows the theoretical continuous filter behavior and the expected behavior of the discreet filter.
"""

from pytrinamic.tools import calculate_biquad_filter_coefficients, LowPassFilterSpec, AntiResonanceFilterSpec


f_s = 25_000  # configure you targets sampling rate
down_sampling_factor = 1  # configure you targets down-sampling factor

# chose one of the following three filter types and update the filter specification to your needs
filter_spec = LowPassFilterSpec(f_p=400.0)
#filter_spec = LowPassFilterSpec(f_p=1000.0, d_p=0.6)
#filter_spec = AntiResonanceFilterSpec(f_p=1000.0, f_z=500.0, d_p=4.0, d_z=0.0)

# select if you like a bode plot to show up or not
plot_bode = True

result = calculate_biquad_filter_coefficients(
    chip_type="TMC4671",  # you may also input "TMC9660" here
    f_s=f_s,
    down_sampling_factor=down_sampling_factor,
    filter_spec=filter_spec
)

print(result.normalized_coefficients) # Normalized coefficients to be written to the chip's biquad registers

if plot_bode:
    import matplotlib.pyplot as plt
    import control as ct
    cont_coffs = result.continuous_coefficients
    disc_coffs = result.tilde_coefficients
    s = ct.tf("s")
    g2 = (cont_coffs.b_2*s**2 + cont_coffs.b_1*s + cont_coffs.b_0) / (cont_coffs.a_2*s**2 + cont_coffs.a_1*s + cont_coffs.a_0)
    z = ct.tf([1, 0], [0, 1], dt=down_sampling_factor/f_s)
    g_lp = (disc_coffs.b_2*z**2 + disc_coffs.b_1*z**1 + disc_coffs.b_0) / (disc_coffs.a_2*z**2 + disc_coffs.a_1*z**1 + disc_coffs.a_0)
    g_lp.minreal()
    fig, (mag_ax, phase_ax) = plt.subplots(2, 1)
    ct.bode_plot(g2, Hz=True, ax=(mag_ax, phase_ax), label="Continuous Filter")
    ct.bode_plot(g_lp, Hz=True, ax=(mag_ax, phase_ax), label="Discrete Filter")
    mag_ax.legend()
    mag_ax.set_xlim([10, 12500])
    phase_ax.legend()
    phase_ax.set_xlim([10, 12500])
    plt.show()
