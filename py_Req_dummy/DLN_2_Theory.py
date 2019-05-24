
# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
# 
# ## §2 Composite laminate theory (*based on LEFM*)
# 
# Principles of linear elastic composite laminate theory, pertinent to calculating the elastic engineering constants required to characterize the elastic structural durability of various tested carbon fibre/epoxy laminate coupons, are discussed here.

# # DLN Contents
# 
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

# ## 2.1 Structural mechanics theory of UD composite laminates subject to plane stress
# All of the coupons prepared and tested for this investigation were UD composite laminates; the coupons were subjected to either tensile or compressive plane stress in the 1-2 plane of the composite geometry, as shown below. This is to say that the coupons were only subjected to *in-plane* stress loads (i.e. tensile and compressive loading in the fibre direction):
# 
# ![Image](0.Images/UD_lamina_1-2_plane.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
# 
# *<center> Fig. X - Unidirectional fibre-reinforced lamina (Jones, 1999)</center>*
# 

# ### 2.1.1 A brief overview of linear elastic strain-stress theory (*relevant to the 2-D in-plane stress fields*)
# A comprehensive overview of linear elastic approximations of stress-strain relationships for anisotropic materials can be found in many resources that focus on solid mechanics [(Tuttle, 2004), (Pilkey, 1999)]. A simplification of (linear elastic) stress-strain theory[<sup>1</sup>](#fn1), applied to UD-laminate composites subjected to in-plane stress, is briefly described here. These equations provide the basis for the structural durability calculations of stress-strain effects on the carbon fibre/epoxy coupons.
# 
# **Generalized Hooke's Law**
# The generalized Hooke's law relating a stress field (induced by an applied force) to strain (deformation) response, of a particular material, can be written in the following simple notation notation :
# 
# $$ \mathbf{\sigma_{i}} = \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
# 
# Where: 
# * $\mathbf{\sigma_{i}}$ are the stress components 
# * $\mathbf{C_{ij}}$ is the stiffness matrix
# * $\mathbf{\varepsilon_{j}}$ are the strain components
# 
# The normal and shear stress fields, induced by an applied force, are pictured in Cartesian coordinates below:
# 
# ![Image](0.Images/Stress_Element_Cartesian.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
# 
# *<center> Fig. X - Stresses on a material element (Jones, 1999)</center>*
# 
# **The stain (deformation) response**
# Deformation of the material, responding to the induced stress field, is characterized by *tensor shear strain* ($\mathbf{\varepsilon_{ij}}$) and *engineering shear strain* ($\mathbf{\gamma_{ij}}$). Considering a material element being deformed, the tensor and engineering shear strains are defined, respectively, as:
# 
# $$ \mathbf{\varepsilon_{1}} = \frac{\partial u}{\partial x}, \qquad \mathbf{\varepsilon_{2}} = \frac{\partial v}{\partial y}, \qquad \mathbf{\varepsilon_{3}} = \frac{\partial w}{\partial z}$$
# 
# $$ \mathbf{\gamma_{23}} = \frac{\partial v}{\partial z} + \frac{\partial w}{\partial y}, \qquad \mathbf{\gamma_{31}} = \frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}, \qquad \mathbf{\gamma_{12}} = \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}$$
# 
# **Stress-strain relationships - Stiffness and compliance elasticity constants**
# The integral of the incremental work done (per unit volume) on a material (subjected to an applied force that induces a stress field and subsequent strain (deformation) response to the load, yields a relation between work done on the material and the resultant tensor shear strain:
# 
# $$ \mathbf{W} = \frac{1}{2} \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{i}} \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
# 
# This result relates The second order differentiation of Hooke's Law shows that the stiffness matrix ($\mathbf{C_{ij}}$) is symmetric (*i.e* $\mathbf{C_{ij}} = \mathbf{C_{ji}}$). Similarly, by examining the inverse of the stress-strain relations, the work done on the material can be related to the induced stress field:
# 
# $$ \mathbf{W} = \frac{1}{2} \mathbf{S_{ij}} \cdot \mathbf{\sigma_{i}} \mathbf{\sigma_{j}}, \qquad\quad i,j = 1, ..., 6 $$
# 
# Where: 
# * $\mathbf{S_{ij}}$ is the compliance matrix
# 
# ***Here it's important to note that hygrothermal effects on the deformation of the material are not being considered.*** *This is valid if experimental testing is done with test environment controls and neglecting material temperature changes during tensile/compressive loading.*
# 
# The stiffness and compliance matrices have 36 constants, owing to the six degrees of freedom for considering the (linear elastic) deformation response of a material element. The generalized matrices are as follows:
# 
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\ 
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\ 
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
# 
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\ 
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\ 
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
# 
# **Significance of coupled stress-strain elements (*described with the compliance matrix*)**
# For anisotropic materials, significant coupling occurs between the applied stress and the various strain responses. Examing the compliance matrix, the following stress-strain responses are coupled:
# 
# * The $ S_{11}, S_{22}$ and $S_{33} $ terms each represent extensional response to their respective applied stress components ($ \sigma_{1}, \sigma_{2}, \sigma_{3} $) in the same direction.
# 
# * The $ S_{44}, S_{55}$ and  $S_{66} $ terms represent shear strain response to an applied shear stress in the same plane
# 
# * The $ S_{12}, S_{13}$ and  $S_{23} $ terms represent coupling between dissimilar normal stresses and normal strains (extension-extension coupling more commonly known as the Poisson effect)
# 
# * The $ S_{14}, S_{15}, S_{16}, S_{24}, S_{25}, S_{26}, S_{34}, S_{35}$ and $S_{36} $ terms represent normal strain response to applied shear stress in a more complex manner than for the preceding compliances (shear-extension coupling)
# 
# * Finally, the $ S_{45}, S_{46}$ and $S_{56} $ terms represent shear strain response to shear stress applied in another plane (shear-shear coupling)
# 
# * However, less than 36 of the constants can be shown to actually be independent for elastic materials when important characteristics of the strain energy are considered, such as whether the material behaves anisotropically, orthotropically, monoclinically or traversely isotropically when undergoing deformation.
# 
# [comment]: <> (------------------------------§2.3.2 Footnotes------------------------------)
# __________________________________
# 
# <span id="fn1"> 1. Linear elasticity theory makes a number of assumptions about the elastic/plastic deformation response to stress fields induced by applied force loads, namely that strain responses are infinitesimally small, and that relationships between the components of stress and strain are approximately. Additionally, the theory is valid only for stress states that do not produce yielding.</span>

# ### 2.1.2 UD laminae strain-stress relationships
# The fibre arrangements, of the laminate coupons prepared for these experimental investigations, were classified as orthotropic or transversely isotropic bodies. In UD laminae, all planes whose perpendicular vector is transverse with respect to the fibre direction are planes of symmetry. The UD laminae are transversely isotropic. On planes parallel with the fibre direction it behaves orthotropically (*material properties that differ along three mutually-orthogonal twofold axes of rotational symmetry - a subset of anisotropic materials*)and on an imaginary plane perpendicular to the fibre direction it behaves isotropically (*material properties remain constant in all directions*).
# 
#  **3-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
#  <br>
#  
# With the application of tensile or compressive force loading, parallel to the fibre direction of the UD laminae (in-plane loading), shear-extension and shear-shear coupling can be neglected. As such, the stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\ 
# C_{21} & C_{22} & C_{23} & 0 & 0 & 0 \\ 
# C_{31} & C_{32} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & C_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# and w.r.t. to the ***compliance matrix***:
# 
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\ 
# S_{21} & S_{22} & S_{23} & 0 & 0 & 0 \\ 
# S_{31} & S_{32} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & S_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
# 
# **3-D Isotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# The stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting isotropic behaviour is simplified to:
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\ 
# C_{12} & C_{11} & C_{13} & 0 & 0 & 0 \\ 
# C_{13} & C_{13} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# and w.r.t. to the ***compliance matrix***:
# 
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\ 
# S_{12} & S_{11} & S_{13} & 0 & 0 & 0 \\ 
# S_{13} & S_{13} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & 2(S_{11} - S_{12})  \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$

# ### 2.1.3 2-D UD laminae strain-stress relationships 
# Since the test coupons for this investigation are all UD laminate samples, and tensile/compressive loadings during experiment runs were applied in the 1-2 plane of the samples, the remaining theory discussion will focus on 2-D laminae stress-strain relationships.
# 
# The plane-stress state of the UD composite, in the 1-2 plan, is defined by setting:
# 
# $$ \sigma_{3} = 0, \tau_{23} = 0, \tau_{31} = 0$$
# 
# such that:
# 
# $$ \sigma_{1} ≠ 0, \sigma_{2} ≠ 0, \tau_{21} ≠ 0$$
# <br>
# 
# where $ \sigma_{1}$ and $ \sigma_{2}$ represent the stress components normal to the 1-2 plane of a UD laminate material, w.r.t to the 1 and 2 directions respectively, and $ \tau_{21}$ represents the intralaminar shear stress w.r.t. the 1-2 plane of a UD laminae material.
# 
# **2-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# As such, the 2-D stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & 0 \\ 
# C_{12} & C_{22} & 0 \\ 
# 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# and w.r.t. to the ***compliance matrix***:
# 
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & 0 \\ 
# S_{12} & S_{22} & 0 \\ 
# 0 & 0 & 2(S_{11} - S_{12}) \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right)$$
# 
# These equations effectively describe the deformation response (described by tensor and engineered shear strain components) of the UD laminae in the 1-2 plane, w.r.t. a shear stress field (described by stress components normal to the 1-2 plane and in-plane shear stress components).
# 
# The tensile and compressive tests, performed for the purposes of this investigation, will be conducted with preset force loads. The resulting displacement (strain) measured will determine the engineering constants required to solve the stress-strain equations discussed above.

# ### 2.1.4 Overview of engineering constants for solving strain-stress equations 
# A brief overview of the engineering constants required to solve the 2-D UD laminae stress-strain equations is presented below:
# 
# 1. The slope of (tensile/compressive) stress-strain curve:
#     * $ E = \frac{\sigma}{\varepsilon} $
#     * $ E_{i}$ represents the Young's (extension) moduli in the $ i^{th}$ directions, describing the elastic extension of the material in a specific direction
# 
# 2. The slope of strain-strain curves (Poisson's ratio):
#     * the negative of the ratio of (signed) transverse strain to (signed) axial strain (i.e. extension-extension coupling coefficient)
#     * $ \nu_{ij} = \frac{-\varepsilon_{i}}{\varepsilon_{j}} $
# 
# 3. The shear modulus, $ G_{ij}$, defining the ratio of shear stress to the shear strain in the (i-j) plane, or rather the material's response to shear stress
# 
# **The orthotropic UD laminae case**
# <br>
# 
# From these definitions, the **compliance matrix** can be expressed in terms of these engineering constants as follows:
# 
# $$S =
# \begin{bmatrix} \frac{1}{E_{11}} & - \frac{\nu_{21}}{E_{22}} & 0 \\ 
# - \frac{\nu_{12}}{E_{11}} & \frac{1}{E_{22}} & 0 \\ 
# 0 & 0 & \frac{1}{G_{12}} \\
# \end{bmatrix} $$
# 
# Since the stiffness and compliance matrices are mutually inverse, it follows by matrix algebra that their components are related as follows for orthotropic materials (*limited to the 2-D case*):
# 
# $$ C_{11} = \frac{S_{22}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{1}}{1 - \nu_{12} \nu_{21}} $$
# 
# $$ C_{22} = \frac{S_{11}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{2}}{1 - \nu_{12} \nu_{21}} $$
# 
# $$ C_{12} = \frac{S_{12}}{S_{11} S_{22} - S^{2}_{12}} = \frac{\nu_{12}E_{1}}{1 - \nu_{12} \nu_{21}} = 
# \frac{\nu_{21}E_{1}}{1 - \nu_{12} \nu_{21}} $$
# 
# $$ \frac{C_{11} - C_{12}}{2} = G_{12} $$
# 
# **The isotropic UD laminae case**
# <br>
# 
# Note that for orthotropic UD laminae, there are four independent variables, namely $ E_{1}, E_{2}, \nu_{12} $ and $ G_{12} $. For the isotropic case, we note that:
# * $ S_{11} = \frac{1}{E_{1}} = \frac{1}{E_{2}} = \frac{1}{E} =  S_{22} $, such that $ E_{1} = E_{2} = E $
# * $ S_{12} = - \frac{\nu_{12}}{E_{1}} = - \frac{\nu_{21}}{E_{2}} = - \frac{\nu}{E} $
# * $ \frac{1}{G_{12}} = \frac{1}{G} = \frac{2(1 + \nu)}{E} $

# ## 2.2 UD laminae in-plane strain-stress relationships

# For in-plane stresses of composite plies we assume that stresses and strains to not vary in certain directions, depending on how the ply is force-loaded. When the aforementioned plane-strain condition exists, the three-dimensional analysis simplifies considerably. 
# 
# The UD laminate test coupons, from the experimental trials, were subjected to in-plane stresses (via 1-2 plane tensile and compressive force loading. The fibre arrangements, of the experiment laminate coupons, were classified as orthotropic or (symmetric) transversely isotropic bodies.
# 
# From the general, anisotropic stress-strain systems of equationss,  defined in Eq. [6] and [7] with the stiffness and compliance matrices respectively:
# 
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\ 
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\ 
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
# 
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\ 
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\ 
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
# 
# These equations reduce to the following for in-plane (*plane-stress*) loading of orthotropic composite plies:
# 
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\ 
# Q_{12} & Q_{22} & Q_{26} \\ 
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
# 
# Where:
# 
# $Q_{ij}$ represent the **in-plane** elements of the stiffness matrix subject to the **plane-stress condition** (*differentiated from the general stiffness matrix elements $C_{ij}$*)
# 
# The plane-stress conditioned compliance matrix is the inverse of the plane-stress conditioned stiffness matrix:
# 
# $$ \begin{bmatrix} S'_{11} & S'_{12} & S'_{16} \\ 
# S'_{12} & S'_{22} & S'_{26} \\ 
# S'_{16} & S'_{26} & S'_{66} \\
# \end{bmatrix}^{-1}  =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\ 
# Q_{12} & Q_{22} & Q_{26} \\ 
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix} $$
# 
# Where:
# 
# $S'_{ij}$ represent the **in-plane** elements of the compliance matrix subject to the **plane-stress condition** (*differentiated from the general compliance matrix elements $S_{ij}$*)

# ## 2.3 Stress and strain transformations

# Axes transformations are important in stress-strain of materials. Such transformations are required to compute critical values of these (stress-strain) characteristics, as well as to be able to understand the tensorial nature of stress and strain. Other entities, such as moment of inertia and curvature, also transform in a manner similar to stress and strain.
# 
# For the purposes of this DLN the relevant theory related to transformations of stress and strain from a local coordinate system to a global coordinate system will briefly be discussed. Further resources on (stress-strain) tensor transformation theory can be found in [Roylance, 2001].
# 
# ### 2.3.1 Stress and strain transformations for laminate plies
# 
# Stress can be transformed from a local cartesian coordinate system **L(p,q,r)** to a global cartesian coordinate system **G(p,q,r)** via:
# 
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \sigma_{G,r} \\ \tau_{G,qr} \\ \tau_{G,pr} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} T_{\sigma11} & \cdots & T_{\sigma16} \\ 
# \vdots & \ddots & \vdots \\ 
# T_{\sigma61} & \cdots & T_{\sigma66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \sigma_{L,r} \\ \tau_{L,qr} \\ \tau_{L,pr} \\ \tau_{L,pq} \\  \end{array} \right)$$
# 
# Which can be written in the form:
# 
# $$ \mathbf{\sigma_{G}} = [\mathbf{\hat{T}_{\sigma}}] \mathbf{\sigma_{L}} $$
# 
# For composite laminate plies subjected to plane-strain and plane-stress conditions, one is only interested stresses manifested in the G(p-q) and L(p-q) planes; for UD laminate plies this would mean the planes that characterize stresses occurring only in the fibre direction and transverse to the fibre direction. Then the stresses in the **G(p,q,r)** coordinate system are arrived at by rotation about the 'r' axis of the **L(p,q,r)** coordinate system, namely:
# 
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\ 
# s^{2} & c^{2} & -2cs \\ 
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \tau_{L,pq} \\  \end{array} \right)$$
# 
# Where:
# <br>
# 
# $ c = cos\Theta \qquad\quad s = sin\Theta $
# 
# And can be written in the form:
# 
# $$ \mathbf{\sigma_{G}} = [\mathbf{T_{\sigma}}] \mathbf{\sigma_{L}} $$
# 
# Meaning that only the three in-plane strain components are transformed.
# 
# A similar treatment of the strain tensor, relating strains (on a composite laminate ply material) in the local coordinate system to the global coordinate system, yields:
# 
# $$ \left( \begin{array}{c} \varepsilon_{G,p} \\ \varepsilon_{G,q} \\ \gamma_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & cs \\ 
# s^{2} & c^{2} & -cs \\ 
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon_{L,p} \\ \varepsilon_{L,q} \\ \gamma_{L,pq} \\  \end{array} \right)$$
# 
# Where c and s are as previously defined, and can be written alternatively as:
# 
# $$ \mathbf{\varepsilon_{G}} = [\mathbf{T_{\varepsilon}}] \mathbf{\varepsilon_{L}} $$
# 
# The stiffness and compliance matrices, $[\mathbf{C}]$ and $[\mathbf{S}]$ respectively, can be transformed accordingly (*see [Roylance, 2001] for matrix inversion steps*) to yield:
# 
# $$ [\mathbf{C'}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{C}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
# 
# $$ [\mathbf{S'}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
# 
# Thus the transformed stiffness matrix can be computed for composites with fibres of varying orientations, from a reference local coordinate system and using laminate ply material stiffness constants to a global coordinate system, with the stress and strain transforms being:
# 
# $$ [\mathbf{T_{\sigma}}] =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\ 
# s^{2} & c^{2} & -2cs \\ 
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
# 
# $$ [\mathbf{T_{\varepsilon}}] =
# \begin{bmatrix} c^{2} & s^{2} & cs \\ 
# s^{2} & c^{2} & -cs \\ 
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
# 
# ### 2.3.2 In-plane transformed stiffness and compliance matrices
# 
# It follows that, for composite plies subjected to plane-stress conditions, the transformed in-plane stress and strain systems of equations can be derived by substituting the plane-stress conditioned stiffness and compliance matrices (Eqn. [23], [24]) into Eqns. [31] and [32]:
# 
# $$ [\mathbf{\bar{Q}}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{Q}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
# 
# $$ [\mathbf{\bar{S}}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
# 
# 
# ### 2.3.3 References
# 
# 1. Roylance, D. (2001). Transformation of stresses and strains. Lecture Notes for Mechanics of Materials.

# ## 2.4 Laminate structural durability calculations

# ### 2.4.1 Stiffness matrices for in-plane stress conditioned laminates
# 
# Eqn.s [35] and [36] represent the plane-stressed conditioned stiffness and compliance matrices for individual plies. To approximate the stress-strain relationships of entire laminates (multi-layer manufactured plies), we define the [A], [B] and [D] stiffness matrices:
# 
# $$ [\mathbf{A}] = \int_{-h_{b}}^{h_{t}} [\bar{\mathbf{Q}}]dz $$, and each $[A_{ij}]$ element defined by:
# 
# $$ A_{ij} = \int_{-h_{b}}^{h_{t}} \bar{Q_{ij}}dz $$
# 
# Where:
# 
# * $h_{b}$ represents the distance of the laminate plies from the reference plane to the bottom surface of the entire laminate structure
# * $h_{t}$ represents the distance of the laminate plies from the reference plane to the top surface of the entire laminate structure
# * Recall that $[\bar{Q}]$ represents the in-plane stress conditioned, transformed stiffness matrix of each ply
# 
# The variable '$\mathbf{z}$' in Eqn. [37] defines the distance of the '$\mathbf{z^{th}}$' ply from the reference plane
# 
# $$ [\mathbf{B}] = \int_{-h_{b}}^{h_{t}} z[\bar{\mathbf{Q}}]dz $$, and each $[B_{ij}]$ element defined by:
# 
# $$B_{ij}] = \int_{-h_{b}}^{h_{t}} z\bar{Q_{ij}}dz $$
# 
# and 
# 
# $$ [\mathbf{D}] = \int_{-h_{b}}^{h_{t}} z^{2}[\bar{\mathbf{Q}}]dz $$, and each $[D_{ij}]$ element defined by:
# 
# $$ D_{ij} = \int_{-h_{b}}^{h_{t}} z^{2}\bar{Q_{ij}}dz $$
# 
# From the assumption that the composite plies and laminates, tested for the quasi-static fatigue loading investigations, exhibit linear elastic behaviour, it is assumed that $[\bar{Q}]$ is constant across each ply. Thus, the laminate stiffness and compliance integrals above can be replaced by the summations:
# 
# $$ A_{ij} = \sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z_{k}-z_{k-1}) $$
# 
# $$ B_{ij} = \frac{1}{2}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{2}_{k}-z^{2}_{k-1}) $$
# 
# $$ D_{ij} = \frac{1}{3}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{3}_{k}-z^{3}_{k-1}) $$

# ## 2.5 Mechanics of in-plane stress-conditioned composite laminates

# ### 2.5.1 In-plane forces and moments
# 
# From the [A], [B] and [D] in-plane stiffness matrix elements described in Eqns. [43] through [45], the in-plane forces and moments of the laminate can be related to the in-plane strain and curvature response of the laminate. For a laminate subject to the in-plane stress condition in the 1-2 plane, this relationship is:
# 
# $$ \left( \begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right) =
# \begin{bmatrix} A_{11} & A_{12} & A_{16} & B_{11} & B_{12} & B_{16} \\ 
# A_{21} & A_{22} & A_{26} & B_{21} & B_{22} & B_{26} \\ 
# A_{61} & A_{62} & A_{66} & B_{61} & B_{62} & B_{66} \\
# B_{11} & B_{12} & B_{16} & D_{11} & D_{12} & D_{16} \\
# B_{21} & B_{22} & B_{26} & D_{21} & D_{22} & D_{26} \\
# B_{61} & B_{62} & B_{66} & D_{61} & D_{62} & D_{66} \\
# \end{bmatrix} 
# \cdot
# \left( \begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) $$
# 
# Inversion of Eqn. [46] defines the strain and curvature of the laminate in terms of the in-plane force loading and moments of the laminate. For a laminate force-loaded in the 1-2 plane:
# 
# $$ \left(\begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) =
# \begin{bmatrix} \alpha_{11} & \alpha_{12} & \alpha_{16} & \beta_{11} & \beta_{12} & \beta_{16} \\ 
# \alpha_{21} & \alpha_{22} & \alpha_{26} & \beta_{21} & \beta_{22} & \beta_{26} \\ 
# \alpha_{61} & \alpha_{62} & \alpha_{66} & \beta_{61} & \beta_{62} & \beta_{66} \\
# \beta_{11} & \beta_{12} & \beta_{16} & \delta_{11} & \delta_{12} & \delta_{16} \\
# \beta_{21} & \beta_{22} & \beta_{26} & \delta_{21} & \delta_{22} & \delta_{26} \\
# \beta_{61} & \beta_{62} & \beta_{66} & \delta_{61} & \delta_{62} & \delta_{66} \\
# \end{bmatrix} 
# \cdot
# \left(\begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right)
#  $$
#  
#  ### 2.5.2 Importance of the [A], [B] and [D] matrices to laminate structural durability analyses
#  
#  The [A], [B] and [D] matrices characterize the stiffness of the laminates, the degree to which the composite laminate will elastically deform, when subjected to certain force-loading conditions.
#  
#  For the purposes of the quasi-static fatigue (tensile and compressive) in-plane force-loading of carbon fibre/epoxy laminate composite coupons (the experiments designed to investigate the *linear* elastic structural durability of these composite materials), the significance of these matrices are as follows:
#  
#  1. The $A_{ij}$ stiffness matrix elements relate the in-plane forces, imposed on the laminate coupons, to the in-plane (*elastic*) deformations manifested in the laminates (*under tensile or compressive force-loading*)
#  
#  2. The $B_{ij}$ stiffness matrix elements are the in-plane–out-of-plane coupling stiffnesses that relate the:
#      * in-plane forces, imposed on the laminate coupons, to the resultant curvatures of the laminate
#      * moments, imposed on the laminate, to the resultant in-plane deformation of the laminate
#      
#  3. The $D_{ij}$ stiffness matrix elements are the bending stiffnesses that relate the moments, imposed on the laminate, to the resultant curvatures of the laminate
#  
# Examination of the [A], [B], and [D] matrices show that different types of couplings may occur. For the experimental (tensile and compressive force-loading) of the composite laminate coupons in the 1-2 plane, the following important force-moment-curvature-deformation couplings are worth noting:
# 
# 1. **Extension–shear coupling**
#     * When the elements $A_{16}$, $A_{26}$ (of the $A_{ij}$ elements) are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause shear deformation ($\gamma^o_{1-2}$), and a twist force ($N_{1-2}$) causes elongations in the 1 and 2 directions 
# 
# 2. **Bending–twist coupling** 
#     * When the elements $D_{16}$, $D_{26}$ are not zero, bending moments ($M_{1}, M_{2}$) may cause a twisting of the laminate ($\kappa_{1-2}$), and a twist moment ($M_{1-2}$) causes curvatures in the 1–3 and 2–3 planes
#     
# 3. **Extension–twist and bending–shear coupling**
#     * When the elements $B_{16}$, $B_{26}$ are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause twist ($\kappa_{1-2}$), and bending moments ($M_{1}, M_{2}$) result in shear deformation ($\gamma^o_{1-2}$)
#     
# 4. **In-plane–out-of-plane coupling**
#     * When the $B_{ij}$ stiffness matrix elements are not zero, in-plane forces ($N_{1}, N_{2}, N_{1-2}$) cause out-of-plane deformations (curvatures) of the laminate, and moments ($M_{1}, M_{2}, M_{1-2}$) cause in-plane deformations in the 1-2 plane. 
#     
# It is worth noting that these four types of coupling are characteristic of composite materials and do not occur in homogeneous isotropic materials. The following two couplings occur in both composite and isotropic materials:
# 
# 5. **Extension–extension coupling**
#     * When the element $A_{12}$ is not zero, a normal force $N_{1}$ causes elongation in the 2 direction ($\varepsilon^o_{2}$), and a normal force $N_{2}$ causes elongation in the 1 direction ($\varepsilon^o_{1}$)
# 
# 6. **Bending–bending coupling**
#     * When the element $D_{12}$ is not zero, a bending moment $M_{1}$ causes curvature of the laminate in the 2-3 plane ($\kappa_{2}$), and a bending moment $M_{2}$ causes curvature of the laminate in the 1–3 plane ($\kappa_{1}$)

# ## 2.6 Applications of [A], [B], [D] ( [$\alpha$], [$\beta$], [$\delta$] ) matrices to the (*elastic*) structural durability characterization of experiment carbon fibre/epoxy composite coupons

# * [§3: Structural durability analyses of carbon fibre & epoxy-based composites - Experimental results](DLN - §3 - Structural durability analyses of carbon fibre & epoxy-based composites - Experimental.ipynb) is the DLN entry that uses Python scientific programming libraries to explore and visualize quasi-fatigue tensile & compressive loading experiments on carbon fibre/epoxy composite test coupons. From analyses of the experiments, the elastic properties of the test coupons are determined.
# <br>
# 
# * [§4: Structural durability analyses of carbon fibre & epoxy-based composites - Matrix calculations](DLN - §2 - Structural durability analyses of carbon fibre & epoxy-based composites - Calculations.ipynb) is the DLN entry that uses MATLAB to perform structural durability matrix calculations from carbon fibre/epoxy composite test coupon experimental data. The $[A], [B], [D]$ $([\alpha], [\beta], [\delta])$ matrices are calculated for each of the test laminate coupons.
# 
