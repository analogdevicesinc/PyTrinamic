################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""This is a Python module to calculate biquad coefficients for TMC4671 and TMC9660.

In TMC4671 the Biquad is implemented with 32bit coefficients, in TMC9660 with 24bit coefficients.
The normalization factors are 2^29/2^20.
The calculation of the biquad output inside TMC9660 is basically this:
    Sum1 = b_0 * X_n ;
    Sum2 = b_1 * X_n_1;
    Sum3 = b_2 * X_n_2;
    Sum4 = a_1 * Y_n_1;
    Sum5 = a_2 * Y_n_2;
    Y_fine = (Sum1 + Sum2 + Sum3 + Sum4 + Sum5)/norm_fac

    X is input value
    Y is filter output value
    index _n indicates this cycle, while _n_1 indicates the previous cycle etc.

The calculation of the biquad filter coefficients is based on a continuous lowpass filter in a structure like this:

Y(s)                         1
---  = G(s) = ------------------------------------------
U(s)          (1/omega_c**2)*s**2 + 2*D/omega_c * s + 1

(Nominal form of a 2nd order lowpass filter with cutoff frequency and damping)
"""

import math
import cmath
from typing import Literal, Optional, Union
from dataclasses import dataclass


@dataclass
class RealBiquadFilterCoefficients:
    a_1: float = 0.0
    a_2: float = 0.0
    b_0: float = 0.0
    b_1: float = 0.0
    b_2: float = 0.0


@dataclass
class NormalizedBiquadFilterCoefficients:
    """The coefficients to be written into the chips register."""
    a_1: int = 0
    a_2: int = 0
    b_0: int = 0
    b_1: int = 0
    b_2: int = 0


@dataclass
class TildeBiquadFilterCoefficients:
    a_0: float = 0.0
    a_1: float = 0.0
    a_2: float = 0.0
    b_0: float = 0.0
    b_1: float = 0.0
    b_2: float = 0.0


@dataclass
class ContinuousBiquadFilterCoefficients:
    """Time continuous filter coefficients."""
    a_0: float = 0.0
    a_1: float = 0.0
    a_2: float = 0.0
    b_0: float = 0.0
    b_1: float = 0.0
    b_2: float = 0.0


@dataclass
class LowPassFilterSpec:
    fc: float # Cutoff frequency
    q: Optional[float] = None # Quality factor in case of an 2nd order low pass filter


@dataclass
class AntiResonanceFilterSpec:
    fp: float # resonance frequency
    fz: float # anti-resonance frequency
    dp: float # damping factor of the resonance frequency
    dz: float # damping factor of the anti-resonance frequency


@dataclass
class _ChipSpec:
    normalization_factor_short: int
    max_value: int
    min_value: int


_chip_spec_map = {
    "TMC4671": _ChipSpec(
        normalization_factor_short=2**29,
        max_value=2**31 - 1,
        min_value=-(2**31),
    ),
    "TMC9660": _ChipSpec(
        normalization_factor_short=2**20,
        max_value=2**23 - 1,
        min_value=-(2**23),
    ),
}


@dataclass
class _Result:
    real_coefficients: RealBiquadFilterCoefficients
    normalized_coefficients: NormalizedBiquadFilterCoefficients
    continuous_coefficients: ContinuousBiquadFilterCoefficients
    tilde_coefficients: TildeBiquadFilterCoefficients


def calculate_biquad_filter_coefficients(chip_type: Literal["TMC4671", "TMC9660"], filter_spec: Union[LowPassFilterSpec, AntiResonanceFilterSpec], *, sample_rate_hz=None, down_sampling_factor=1) -> _Result:
    """
    Function to calculate biquad filter coefficients for Trinamic chip products from a given filter specification.

    :param chip_type: The chip type for which coefficients are calculated. Must be "TMC4671" or "TMC9660".
    :type chip_type: Literal["TMC4671", "TMC9660"]
    :param filter_spec: The filter specification, either a LowPassFilterSpec or AntiResonanceFilterSpec instance.
    :type filter_spec: Union[LowPassFilterSpec, AntiResonanceFilterSpec]
    :param sample_rate_hz: The sample rate in Hz. If None, defaults to the respective chip's default sample rate.
    :type sample_rate_hz: Optional[float]
    :param down_sampling_factor: Down-sampling factor to apply to the sample rate. Must be >= 1.
    :type down_sampling_factor: Optional[int]

    :return: A _Result object containing real, normalized, continuous, and tilde coefficients.
    :rtype: _Result

    :raises ValueError: If chip_type is unknown or down_sampling_factor < 1.
    :raises TypeError: If filter_spec is not a supported type.
    :raises AttributeError: If coefficients are out of range or filter is unstable.
    """
    
    try:
        chip_spec = _chip_spec_map[chip_type]
    except KeyError:
        raise ValueError(f"Unknown chip type: {chip_type}!")
    
    if down_sampling_factor < 1:
        raise ValueError("Down-sampling factor must be at least 1!")
    
    if not sample_rate_hz:
        # 25000 it the default for TMC9660 and TMC4671.
        # This might not be the default for future chips, so this is why sample_rate_hz==None is chosen as "use default".
        sample_rate_hz = 25_000

    sample_rate_hz = sample_rate_hz / down_sampling_factor
    T = 1 / sample_rate_hz

    if isinstance(filter_spec, LowPassFilterSpec):
        # Coefficients for continuous filter
        f_p = filter_spec.fc
        d_p = filter_spec.q

        omega_c = 2.0 * math.pi * f_p
        b_0_cont = 1.0
        b_1_cont = 0.0
        b_2_cont = 0.0
        if d_p is None:
            a_0_cont = 1.0
            a_1_cont = 1.0 / omega_c
            a_2_cont = 0.0
        else:
            a_0_cont = 1.0
            a_1_cont = 2.0 * d_p / omega_c
            a_2_cont = 1.0 / omega_c ** 2.0

    elif isinstance(filter_spec, AntiResonanceFilterSpec):
        # Coefficients for continuous filter
        f_p = filter_spec.fp
        f_z = filter_spec.fz
        d_p = filter_spec.dp
        d_z = filter_spec.dz

        b_2_cont = 1.0 / ((2.0 * math.pi * f_z) ** 2.0)
        b_1_cont = 2.0 * d_z / (2.0 * math.pi * f_z)
        b_0_cont = 1.0

        a_2_cont = 1.0 / ((2.0 * math.pi * f_p) * (2.0 * math.pi * f_p))
        a_1_cont = 2.0 * d_p / (2.0 * math.pi * f_p)
        a_0_cont = 1.0
    else:
        raise TypeError("Invalid Filter Type!")

    cont_coeffs = ContinuousBiquadFilterCoefficients()
    cont_coeffs.b_0 = b_0_cont
    cont_coeffs.b_1 = b_1_cont
    cont_coeffs.b_2 = b_2_cont
    cont_coeffs.a_0 = a_0_cont
    cont_coeffs.a_1 = a_1_cont
    cont_coeffs.a_2 = a_2_cont

    b_2_z = b_0_cont * T ** 2 + 2 * b_1_cont * T + 4 * b_2_cont
    b_1_z = 2 * b_0_cont * T ** 2 - 8 * b_2_cont
    b_0_z = b_0_cont * T ** 2 - 2 * b_1_cont * T + 4 * b_2_cont

    a_2_z = T ** 2 + 2 * a_1_cont * T + 4 * a_2_cont
    a_1_z = 2 * T ** 2 - 8 * a_2_cont
    a_0_z = T ** 2 - 2 * a_1_cont * T + 4 * a_2_cont

    b_2_tilde = b_2_z / a_0_z
    b_1_tilde = b_1_z / a_0_z
    b_0_tilde = b_0_z / a_0_z

    a_2_tilde = a_2_z / a_0_z
    a_1_tilde = a_1_z / a_0_z
    a_0_tilde = a_0_z / a_0_z

    time_disc_coeffs = TildeBiquadFilterCoefficients()
    time_disc_coeffs.b_0 = b_0_tilde
    time_disc_coeffs.b_1 = b_1_tilde
    time_disc_coeffs.b_2 = b_2_tilde
    time_disc_coeffs.a_0 = a_0_tilde
    time_disc_coeffs.a_1 = a_1_tilde
    time_disc_coeffs.a_2 = a_2_tilde

    b_0 = b_2_tilde / a_2_tilde
    b_1 = b_1_tilde / a_2_tilde
    b_2 = b_0_tilde / a_2_tilde

    a_0 = a_2_tilde / a_2_tilde
    a_1 = a_1_tilde / a_2_tilde
    a_2 = a_0_tilde / a_2_tilde

    real_coeffs = RealBiquadFilterCoefficients()
    real_coeffs.b_0 = b_0
    real_coeffs.b_1 = b_1
    real_coeffs.b_2 = b_2
    real_coeffs.a_1 = a_1
    real_coeffs.a_2 = a_2

    norm_coeffs = NormalizedBiquadFilterCoefficients()
    norm_coeffs.b_0 = round(b_0 * chip_spec.normalization_factor_short)
    norm_coeffs.b_1 = round(b_1 * chip_spec.normalization_factor_short)
    norm_coeffs.b_2 = round(b_2 * chip_spec.normalization_factor_short)
    norm_coeffs.a_1 = round(-a_1 * chip_spec.normalization_factor_short)
    norm_coeffs.a_2 = round(-a_2 * chip_spec.normalization_factor_short)

    # Coefficient balancing is needed.
    # The sum of all coefficients needs to be equal to normalization_factor_short. Why is this so?
    # Let"s say the filter input X is steady then we want the filter output Y to be steady as well after a certain time.
    # X shall be Y.
    # Y = (b_0_S24 + b_1_S24 + b_2_S24 + a_1_S24 + a_2_S24) * X/normalization_factor_short
    # as the rounding might take away some portion of the coefficient this needs to be compensated.
    norm_coeffs.a_1 += chip_spec.normalization_factor_short - (
                norm_coeffs.b_0 + norm_coeffs.b_1 + norm_coeffs.b_2 + norm_coeffs.a_1 + norm_coeffs.a_2)

    # Range check for the normalized coefficients, to make sure they fit in the chips register.
    for coeff_name, coeff_value in vars(norm_coeffs).items():
        if not chip_spec.min_value < coeff_value < chip_spec.max_value:
            raise AttributeError(f"Error: {coeff_name} is too small!")

    root = abs(cmath.sqrt(-a_2 / a_0 + a_1 ** 2 / (4 * a_0 ** 2)) - a_1 / (2 * a_0))

    if root > 0.98:
        raise AttributeError("The given filter configuration would result in an unstable filter!")

    return _Result(real_coeffs, norm_coeffs, cont_coeffs, time_disc_coeffs)
