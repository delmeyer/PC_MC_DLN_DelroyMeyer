
# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
# 
# ## §1: Introduction

# # DLN Contents
# 
# 0. [Materials Characterization Laboratory DLN | A Showcase for Convergent Manufacturing Group Ltd](DLN_0_About_Me.ipynb) - An 'Welcome' message to the Convergent Manufacturing - Materials Characterization Group, explaining the concept of these DLN entries, why I made them out of interest for the team's *Characterization Lab Technician/Scientist* opening, and presenting a brief 'About Me' StoryMap
# <br>
# 
# 1. [§1: Structural durability analyses of carbon fibre & epoxy-based composites - Introduction](DLN_1_Introduction.ipynb) - An introduction to the quasi-fatigue experiments performed on carbon fibre/epoxy composite specimens.
# <br>
# 
# 2. [§2: Structural durability analyses of carbon fibre & epoxy-based composites - Laminate mechanics theory](DLN_2_Theory.ipynb) - A discussion of composite laminate theory, as a basis for performing stress-strain-deformation calculations to characterize the structural durability of composite laminate layups.
# <br>
# 
# 3. [§3: Structural durability analyses of carbon fibre & epoxy-based composites - Experimental results](DLN_3_Experimental.ipynb) - Using Python scientific programming libraries to explore and visualize quasi-fatigue tensile & compressive loading experiments on carbon fibre/epoxy composite test coupons.
# <br>
# 
# 4. [§4: Structural durability analyses of carbon fibre & epoxy-based composites - Matrix calculations](DLN_4_Calculations.ipynb) - Using MATLAB to perform structural durability matrix calculations from carbon fibre/epoxy composite test coupon experimental data.

# # 0. DLN Introduction
# 
# This digital laboratory notebook (DLN) is comprised of four linked entries that are listed in the DLN contents section above. The DLN provides a comprehensive platform that:
# 
# * Discuss composite fatigue and pertinent composite mechanics theory
# * Provide an overview of tensile and compression quasi-static fatigue tests performed on carbon fibre/epoxy composite laminate coupons with varying fibre orientations and ply layers
# * Provides a scientific computing platform to utilize tensile & compressive quasi-static fatigue experiment data for:
#     * Stress-strain data visualization
#     * Statistical data analyses
#     * Store empirically-determined elastic properties of the tested composite coupons for structural durability calculations
#     * Perform matrix calculations to quantify the structural durability of the tested composite laminate coupons materials

# ## I. Experiment log
# * **Date of experiment**: 10.14.2017
# * **Principle investigator**: Delroy Meyer, EIT, BASc
# * **Test operators**: Jürgen Müller, Delroy Meyer, Cintia Oliveria
# * **Lead investigator**: Prof. Dr-mont. Zoltan Major
# * **Course**: LVA Nr. 378.029 - 480ADPTPPBV17 - Polymer Product Design and Engineering III - Graduate Seminar
# * **Location**: Institute of Polymer Materials and Testing (IPMT), JKU Linz - Linz, Austria
#     * Compounding and specimen preparation Lab: *Composite coupon specimen preparation*
#     * Mechanical Lab: *Tensile & compression testing*
# 
# ### i. Experiment test (lab) environment conditions
# *Measurement taken: 10-14-2017 08:45:07*
# <b>
# 
# $T_{test} (°C) = 21.23$ (*within* $ 23 ± 3 °C$ *standard laboratory atmosphere range as per ASTM D5229*)
# <br>
# $RH (\%) = 55.7$ (*within* $ 50 ± 10 \%$ *standard laboratory atmosphere range as per ASTM D5229*)

# # 1. Purpose of experiment and data analyses
# These experiments were conducted to investigate the dependency of the structural durability of (high fibre volume fraction) carbon fibre/epoxy laminate composites on fibre orientation. Quasi-static tensile and compressive fatigue tests were performed with unidirectional (UD) carbon/epoxy laminates at angles of 0°, 45° and 90°.
# 
# ## 1.1 Why these investigations are needed
# 1. Short and long-fibre reinforced composites offer advantages over conventional metallic materials for the manufacture of components across many different manufacturing industries (*common examples: aerospace/automotive component manufacture, building materials, sports equipment, chemical process industry components*)
#     * Polymeric laminated composites, like carbon-fibre/epoxy laminates, present high strength-to-weight and stiffness-to-weight ratios when compared with metallic materials
# <br>
# 
# 2. To dimension parts undergoing sustained tensile or compressive forces in application, and the material's consequent deformation response, the quasi-fatigue tensile & compressive characterization testing is necessary
# <br>
# 
# 3. *My personal opinion*: Composite materials design offers, for all practical intents and purposes, virtually limitless options for component design, processing and application-use. Consequently, this mean that, for the foreseeable future, there will be an ongoing need to conduct testing for both existing and novel composite materials design and structural analyses; the evolution of innovation in composite materials development and processing technologies will further expand the scope of testing needed.

# ## 1.2 Fatigue mechanics of composite materials - conceptual theory
# 
# * Due to their inner structure consisting of continuous fibres and matrix material the macroscopic properties of composite materials are anisotropic
#     * UD-lamina layers, themselves, are considered to be transversely isotropic; on planes parallel with the fibre direction they behave orthotropically and on an imaginary plane perpendicular to the fibre direction they behave isotropically
# 
# * The interface between the fibre and the matrix resin and its properties influence the performance of the composite as well
# 
# * When mechanical quasi-static or fatigue loads are applied, a variety of complex damage mechanisms such as matrix microcracking, interfacial fibre/matrix debonding, transverse rupture, fibre rupture or delamination occur on microscopic scale
# 
# * The properties of unidirectional (UD) composites transverse to fibre direction are generally low. Under fatigue loads, the matrix is subjected to strain-controlled fatigue due to the constraint provided by the fibres
# 
# * Higher fibre volume fractions increase mechanical properties such as tensile strength and stiffness in fibre direction
# 
# * The fibres of an CFRPs are what “deliver” its excellent properties but the resin (the matrix) is still required in order to:
#     * provide a cohesive component
#     * direct loads into the fibres
#     * protect the fibres against environmental influences
#     * prevent the fibres from buckling when subjected to compressive stress
#     * *However, this means that*: unfortunately stresses will of necessity now arise in the matrix as well, and also at the interface of the fibres and matrix
# 

# ## 1.3 Structural durability calculations as part of composite fatigue-life prediction
# Structural durability calculations constitute 'one piece in the puzzle' of forming a complete fatigue-life prediction model for composite materials. These calculations rely on the following studies:
# 
# 1. An evaluation of the **load-time-history** of the material
# <br>
# 
# 2. Analyses of the **local anisotropic behaviour** of the material:
# <br>
# 
# 3. Analyses of the **macroscopic behaviour** of the material:
#     * quasi-static stress/time investigations:
#         * data for stress-strain behaviour and strength (elasticity and strength properties)
#     * cyclic stress/cycle investigations (S-N curves)
# <br>
# 
# 4. Consideration of **Lamina input variables**:
#     * lamina thickness
#     * fibre content
#     * type and orientation of reinforcement
#     
# A visual representation of the full workflow for creating a composite fatigue-life prediction model, provided by Mösenbacher et. al. [1], shows how these studies contribute to the workflow.
# 
# ![Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)](0.Images/CFRP_Fatigue_Predict_Wrkflw.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
# 
# *<center> Fig. 1 - Complete workflow for developing a composite fatigue-life prediction model (Mösenbacher, ECCM16, 2016)</center>*

# ## 1.4 Data analysis & calculations to be determined from this investigation
# 
# This DLN will focus on the ***load-time history*** and ***stress-strain*** analysis segments of the **composite fatigue-life prediction model workflow** shown in Figure 1 above.
# 
# The following results will be presented from the tensile and compressive quasi-static fatigue loading experiment runs performed on carbon fibre/epoxy laminate coupons of various fibre orientations and ply layers:
# 
# 1. Empirical determination of tensile/compressive moduli of elasticity
# <br>
# 
# 2. Calculation of stress-strain elastic engineering constants to characterize the structural durability of composite materials undergoing long-term static (force) loading in application
# <br>
