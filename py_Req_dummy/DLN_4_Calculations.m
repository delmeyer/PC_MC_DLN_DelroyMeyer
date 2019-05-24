
%%file dispn.m
%%Define Brenden Epps 'DISP(X,N)' function for better visualization of matrix output:
%https://www.mathworks.com/matlabcentral/fileexchange/37025-dispn-x-n-displays-matrix-x-to-n-digits-of-precision

% -------------------------dispn(X,N)-------------------------------------
% DISPN(X,N) displays matrix X to N digits of precision.
%
% Inputs:
%
%   X == 1D vector or 2D matrix
%   N == desired (whole) number of digits of precision
%        N may be a scalar or 
%                 a vector with length equal to number of columns of X
%
% Example:
%       X = rand(4,3)-0.5
%       dispn(X,8)
%       disp(' ')
%       dispn(X,[2,4,6])
%
% See also:
%   DISP(X) displays the matrix in the current screen format.
% -------------------------------------------------------------------------
function [] = dispn(X,N)
[I,J] =   size(X);
   K  = length(N);
if     K == 1   
    
    N = N * ones(1,J);
elseif K ~= J
    
    disp('ERROR: length(N) must either be 1 or equal to the number of columns of X.')
    return
end
for i = 1:I
    string = '';
    
    for j = 1:J
        
        if X(i,j) >= 0
        
            string = [string,'   %.', num2str( N(j) ) ,'f'];
        else
            string = [string,'  %.' , num2str( N(j) ) ,'f'];        
        end
    end
        
    disp( sprintf( string , X(i,:) ) )
end

%Composite material properties

E11 = 148e9;         %Longitudinal Young's modulus (Pa [=] N/m^2)
E22 = 9.65e9;        %Transverse Young's modulus (Pa [=] N/m^2)
G12 = 4.55e9;        %Longitudinal shear modulus (Pa [=] N/m^2)
nu12 = 0.3;          %Longitudinal Poisson's ratio
nu23 = 0.6;          %Transverse Poisson's ratio

%Define distances of each ply from stated reference plane; sign convention is '-ve values' for plies below
%the reference plane & '+ve values' for plies above the reference plane

%%20 plies in composite specimen
z0 = -0.001;
z1 = -0.0009;
z2 = -0.0008;
z3 = -0.0007;
z4 = -0.0006;
z5 = -0.0005;
z6 = -0.0004;
z7 = -0.0003;
z8 = -0.0002;
z9 = -0.0001;
z10 = 0;
z11 = 0.0001;
z12 = 0.0002;
z13 = 0.0003;
z14 = 0.0004;
z15 = 0.0005;
z16 = 0.0006;
z17 = 0.0007;
z18 = 0.0008;
z19 = 0.0009;
z20 = 0.001;

%%Define ply orientation (bottom to top of composite ply layup)
Theta = [0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 45; 45; 45; 45; 45; 45; 45; 45; 45; 45];
%Theta = [0; 0; 45; 45;];

%%

% Define variables for ply orientation
Z = [z0; z1; z2; z3; z4; z5; z6; z7; z8; z9; z10; z11; z12; z13; z14; z15; z16; z17; z18; z19; z20];
%Z = [z0; z1; z2; z3; z4];

%%Compute compliance matrix constants for orthotropic composite plies
%S16 = S26 = 0;
S11 = 1/E11;
S12 = -(nu12/E11);
S22 = 1/E22;
S66 = 1/G12;

%Compute reduced stiffness matrix constants for orthotropic composite plies
%Q16 = Q26 = 0;
% QDN = (S11*S12)-((S12)^2);
% Q11 = S22/QDN;
% Q12 = (-S12)/QDN;
% Q22 = S11/QDN;
% Q66 = 1/S66;
D = 1-((E22/E11)*((nu12)^2));
Q11 = E11/D;
Q12 = (nu12*E22)/D;
Q21 = Q12;
Q22 = E22/D;
Q66 = G12;

%%Define 'x' as a symbolic number (symbolic numbers are exact representations)
x = sym('x');

%%Initialize ABD matrices
A_mat = zeros(3,3);
B_mat = zeros(3,3);
D_mat = zeros(3,3);

%%FOR loop to compute reduced ABD matrices
for n = 1:20
    x = Theta(n,1)*(pi/180);
    s = sin(x);
    c = cos(x);
    Qb11 = (Q11*(c^4)) + (Q22*(s^4)) + ((2*(s^2))*(c^2)*(Q12 + (2*Q66)));
    Qb22 = (Q11*(s^4)) + (Q22*(c^4)) + ((2*(s^2))*(c^2)*(Q12 + (2*Q66)));
    Qb12 = (((c^2)*(s^2))*(Q11+Q22-(4*Q66))) + (((c^4)+(s^4))*Q12);
    Qb66 = (((c^2)*(s^2))*(Q11+Q22-(2*Q12))) + ((((c^2)-(s^2))^2)*Q66);
    Qb16 = c*s*(((c^2)*Q11) - ((s^2)*Q22) - ((c^2)-(s^2))*(Q12+(2*Q66)));
    Qb26 = c*s*(((s^2)*Q11) - ((c^2)*Q22) + ((c^2)-(s^2))*(Q12 + (2*Q66)));
    
    Zk1(n,1) = Z(n+1,1) - Z(n,1);
    Zk2(n,1) = ((Z(n+1,1))^2) - ((Z(n,1))^2);    
    Zk3(n,1) = ((Z(n+1,1))^3) - ((Z(n,1))^3);
    
    Qb(((n-1)*3)+1:((n-1)*3)+3,1:3) = [Qb11 Qb12 Qb16; Qb12 Qb22 Qb26; Qb16 Qb26 Qb66];
    
    A_mat((n*3)+1:(n*3)+3,1:3) = (Qb(((n-1)*3)+1:((n-1)*3)+3,1:3).*Zk1(n,1)) + A_mat(((n-1)*3)+1:((n-1)*3)+3,1:3);
    
    B_mat((n*3)+1:(n*3)+3,1:3) = ((Qb(((n-1)*3)+1:((n-1)*3)+3,1:3).*Zk2(n,1))/2) + B_mat(((n-1)*3)+1:((n-1)*3)+3,1:3);    

    D_mat((n*3)+1:(n*3)+3,1:3) = ((Qb(((n-1)*3)+1:((n-1)*3)+3,1:3).*Zk3(n,1))/3) + D_mat(((n-1)*3)+1:((n-1)*3)+3,1:3);
end


%Define the matrix that describes the in-plane forces & moments on the composite laminate - 
%%describes the response of the laminate to in-plane forces and moments
A = A_mat(61:63,1:3);
B = B_mat(61:63,1:3);
D = D_mat(61:63,1:3);

IPFM = [A B; B D];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IP_inv = inv(IPFM);

alpha = IP_inv(1:3,1:3);
beta = IP_inv(4:6,1:3);
delta = IP_inv(4:6,4:6);



format short
fprintf('MATLAB program output\n');
fprintf('Laminate stiffness matrix\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
dispn(A,0)

format short
fprintf('MATLAB program output\n');
fprintf('Laminate stiffness matrix\n');
fprintf('----------------------------------\n');
fprintf('[B], units: N = \n');
fprintf(' ');
dispn(B,0)


format short
fprintf('MATLAB program output\n');
fprintf('Laminate stiffness matrix\n');
fprintf('----------------------------------\n');
fprintf('[D], units: N*m = \n');
fprintf(' ');
dispn(D,2)

format short
fprintf('MATLAB program output\n');
fprintf('Global laminate compliance matrix\n');
fprintf('----------------------------------\n');
fprintf('[alpha], units: m/N = \n');
fprintf(' ');
disp(alpha)

format short
fprintf('MATLAB program output\n');
fprintf('Global laminate compliance matrix\n');
fprintf('----------------------------------\n');
fprintf('[beta], units: 1/N = \n');
fprintf(' ');
disp(beta)

format short
fprintf('MATLAB program output\n');
fprintf('Global laminate compliance matrix\n');
fprintf('----------------------------------\n');
fprintf('[delta], units: 1/(N*m) = \n');
fprintf(' ');
dispn(delta,5)

%Test: quasi-fatigue (tensile) loading of a symmetric, 4-ply UD 0° carbon fibre/epoxy laminate
%Laminate type: Symmetrical

%%---------------------------------Data inputs---------------------------------------

%%Carbon fibre elastic properties
Ef1 = 230e9;                  %Fibre longitudinal modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Tension applied in 1 (fibre-oriented) direction
E_mod = 113.088392e9;         %Tensile modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%Define no. of each ply orietation for design laminate
o0 = 4;
o90 = 0;
o30 = 0;
o45 = 0;
o60 = 0;

%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45_rad = degtorad(45);
o60_rad = degtorad(60);

%Define ply design details:
tl = 1.02/1000;   %Measured avg. thickness of laminate coupons [m]
np = 4;           %no. of ply layers
t = t1/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;      %total thickness of 0° plies
t90 = t*o90;      %total thickness of 90° plies
t30 = t*o30;      %total thickness of 30° plies
t45 = t*o45;      %total thickness of 45° plies
t60 = t*o60;      %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);  %total thickness of laminate (sanity check: lt == t1)
w = 9.98;          %avg. coupon width [mm]
Ww = w/1000;       %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t1 ~= lt
    error("User has mis-defined laminate ply layer design. Check design ply layer number.\n");
    %break
else
    %%0° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_0 = (Ef1*Vf) + (Em*Vm);                       %Modulus in 1-direction (in fibre direction)
    E11_e = E_mod;                                  %Experimentally-determined modulus
    E22_0 = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));            %Modulus in 2-direction (⊥ to fibre direction)
    nu12_0 = (Vm*num) + (Vf*nuf);                     %Poisson's ratio - contraction in the 2-direction (⊥ to fibre direction) 
                                                      % when an extension is applied in 1-direction (fibre direction)
    G12_0 = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));                %Shear modulus in 2-direction (⊥ to fibre direction) on the plane whose 
                                                      % normal is in direction 1-direction (fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_0 = 1/E11_0;
    S12_0 = -(nu12_0/E11_0);
    S21_0 = S12_0;
    S22_0 = 1/E22_0;
    S66_0 = 1/G12_0;
    
    %%Compliance matrix constants from experimental data
    S11e = 1/E11_e;
    S12e = -(nu12_0/E11_e);
    S21e = S12e;
    S22e = 1/E22_0;
    S66e = 1/G12_0;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_0 = 1-((E22_0/E11_0)*((nu12_0)^2));
    Q11_0 = E11_0/D_0;
    Q12_0 = (nu12_0*E22_0)/D_0;
    Q21_0 = Q12_0;
    Q22_0 = E22_0/D_0;
    Q66_0 = G12_0;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_e = 1-((E22_0/E11_e)*((nu12_0)^2));
    Q11e = E11_e/D_e;
    Q12e = (nu12_0*E22_0)/D_e;
    Q21e = Q12e;
    Q22e = E22_0/D_e;
    Q66e = G12_0;

    %Compile compliance matrix
    S0 = [S11_0 S12_0 0; S21_0 S22_0 0; 0 0 S66_0];
    S0e = [S11e S12e 0; S21e S22e 0; 0 0 S66e];
    %Compile stiffness matrix
    Q0 = [Q11_0 Q12_0 0; Q21_0 Q22_0 0; 0 0 Q66_0];
    Q0e = [Q11e Q12e 0; Q21e Q22e 0; 0 0 Q66e];
    %Sanity check
    Q0_valid = inv(S0);
    Q0e_valid = inv(S0e);

    %Build the stress & strain transformation matrices
    %% transformations are vital in analyses of stress and strain, both because they are needed
    %% to compute critical values of these entities and also because the tensorial nature of stress and
    %% strain is most clearly seen in their transformation properties. Other entities, such as moment of
    %% inertia and curvature, also transform in a manner similar to stress and strain.
    c0 = cos(o0_rad);
    ss0 = sin(o0_rad);
    %Stress transformation matrix
    Tsig0 = [c0^2 ss0^2 2*c0*ss0; ss0^2 c0^2 -2*c0*ss0; -c0*ss0 c0*ss0 ((c0^2)-(ss0^2))];
    %Strain transformation matrix
    Teps0 = [c0^2 ss0^2 c0*ss0; ss0^2 c0^2 -c0*ss0; -2*c0*ss0 2*c0*ss0 ((c0^2)-(ss0^2))];
    %Transformed (reduced) stiffness matrix
    Qb0 = (inv(Tsig0))*Q0*Teps0;
    Qb0e = (inv(Tsig0))*Q0e*Teps0;
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Define lower edge of 0° laminate section
z0 = z1-(lt/2);

%Define upper edge of 0° laminate section

z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_UD04T = (Qb0*zA1) + (Qb0*zA2);
B_UD04T = (Qb0*zB1) + (Qb0*zB2);
D_UD04T = (Qb0*zD1) + (Qb0*zD2);

A_UD04T_e = (Qb0e*zA1) + (Qb0e*zA2);
B_UD04T_e = (Qb0e*zB1) + (Qb0e*zB2);
D_UD04T_e = (Qb0e*zD1) + (Qb0e*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM = [A_UD04T B_UD04T; B_UD04T D_UD04T];

IPFMe = [A_UD04T_e B_UD04T_e; B_UD04T_e D_UD04T_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IP_inv = inv(IPFM);

IP_e_inv = inv(IPFMe);

aA_UD04T = IP_inv(1:3,1:3);
bB_UD04T = IP_inv(4:6,1:3);
dD_UD04T = IP_inv(4:6,4:6);

aA_UD04T_e = IP_e_inv(1:3,1:3);
bB_UD04T_e = IP_e_inv(4:6,1:3);
dD_UD04T_e = IP_e_inv(4:6,4:6);

%%Computation output:
%%----------------------------------------------------------------------------------------
% fprintf('Predicted elastic constant values:\n');
% fprintf('----------------------------------\n');
% fprintf('E11 modulus: %.3f GPa\n', E11/1e9);
% fprintf('E22 modulus: %.3f GPa\n', E22/1e9);
% fprintf('nu12: %.3f\n', nu12);
% fprintf('G12: %.3f GPa\n', G12/1e9);
% fprintf(' \n');
% fprintf('Empirically-determined E11 modulus: %.3f GPa\n', E_mod/1e9);


dispn(A_UD04T_e,3)

B_UD04T_e

D_UD04T_e

dispn(aA_UD04T_e,12)

dispn(bB_UD04T_e,0)

dispn(dD_UD04T_e,6)

%Test: quasi-fatigue (tensile) loading of a symmetric, 8-ply UD 90° carbon fibre/epoxy laminate
%Laminate type: Symmetrical

%%---------------------------------Data inputs---------------------------------------

%%CHECKED
%%Carbon fibre elastic properties
Ef1 = 230e9;                  %Fibre longitudinal modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Tension applied in 1 (fibre-oriented) direction
E_mod_90 = 3.073586e9;        %Tensile modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%%CHECKED
%Define no. of each ply orietation for design laminate
o0 = 0;
o90 = 0;
o30 = 0;
o45 = 8;
o60 = 0;

%%CHECKED
%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%%CHECKED
%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45_rad = degtorad(45);
o60_rad = degtorad(60);

%%CHECKED
%Define ply design details:
t_lam = 1.98/1000;   %Measured avg. thickness of laminate coupons [m]
np = 8;              %total no. of ply layers
t = t_lam/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;          %total thickness of 0° plies
t90 = t*o90;         %total thickness of 90° plies
t30 = t*o30;         %total thickness of 30° plies
t45 = t*o45;         %total thickness of 45° plies
t60 = t*o60;         %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);     %total thickness of laminate (sanity check: lt == t_lam)
w = 20.02;           %avg. coupon width [mm]
Ww = w/1000;         %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t_lam ~= lt
    error("User has mis-defined laminate ply layer design. Please verify design inputs.\n");
    %break
else
    %%90° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_90 = (Ef1*Vf) + (Em*Vm);                    %Modulus in 1-direction (⊥ to fibre direction)
    E11_e90 = E_mod_90;                                  %Experimentally-determined modulus
    E22_90 = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));         %Modulus in 2-direction (in fibre direction)
    nu12_90 = (Vm*num) + (Vf*nuf);                  %Poisson's ratio - contraction in the 2-direction (in fibre direction) 
                                                      % when an extension is applied in 1-direction (⊥ to fibre direction)
    G12_90 = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));             %Shear modulus in 2-direction (in fibre direction) on the plane whose 
                                                      % normal is in direction 1-direction (⊥ to fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_90 = 1/E11_90;
    S12_90 = -(nu12_90/E11_90);
    S21_90 = S12_90;
    S22_90 = 1/E22_90;
    S66_90 = 1/G12_90;
    
    %%Compliance matrix constants from experimental data
    S11e = 1/E11_e90;
    S12e = -(nu12_90/E11_e90);
    S21e = S12e;
    S22e = 1/E22_90;
    S66e = 1/G12_90;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_90 = 1-((E22_90/E11_90)*((nu12_90)^2));
    Q11_90 = E11_90/D_90;
    Q12_90 = (nu12_90*E22_90)/D_90;
    Q21_90 = Q12_90;
    Q22_90 = E22_90/D_90;
    Q66_90 = G12_90;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_e = 1-((E22_90/E11_e90)*((nu12_90)^2));
    Q11e = E11_e90/D_e;
    Q12e = (nu12_90*E22_90)/D_e;
    Q21e = Q12e;
    Q22e = E22_90/D_e;
    Q66e = G12_90;

    %Compile compliance matrix
    S90 = [S11_90 S12_90 0; S21_90 S22_90 0; 0 0 S66_90];
    S90e = [S11e S12e 0; S21e S22e 0; 0 0 S66e];
    %Compile stiffness matrix
    Q90 = [Q11_90 Q12_90 0; Q21_90 Q22_90 0; 0 0 Q66_90];
    Q90e = [Q11e Q12e 0; Q21e Q22e 0; 0 0 Q66e];
    %Sanity check
    Q90_valid = inv(S90);
    Q90e_valid = inv(S90e);

    %Build the stress & strain transformation matrices
    %% In a symmetrical laminate the ply located at a position +z is identical to the ply at −z
    %% Correspondingly, the stiffness matrix [Q]bar of the ply at +z is identical to the stiffness matrix 
    %% of the ply at −z:
    Qb90 = Q90;
    Qb90e = Q90e;
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Define lower edge of 90° laminate section
z0 = z1-(lt/2);

%Define upper edge of 90° laminate section

z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_UD908T = (Qb90*zA1) + (Qb90*zA2);
B_UD908T = (Qb90*zB1) + (Qb90*zB2);
D_UD908T = (Qb90*zD1) + (Qb90*zD2);

A_UD908T_e = (Qb90e*zA1) + (Qb90e*zA2);
B_UD908T_e = (Qb90e*zB1) + (Qb90e*zB2);
D_UD908T_e = (Qb90e*zD1) + (Qb90e*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM = [A_UD908T B_UD908T; B_UD908T D_UD908T];

IPFMe = [A_UD908T_e B_UD908T_e; B_UD908T_e D_UD908T_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IP_inv = inv(IPFM);

IP_e_inv = inv(IPFMe);

aA_UD908T = IP_inv(1:3,1:3);
bB_UD908T = IP_inv(4:6,1:3);
dD_UD908T = IP_inv(4:6,4:6);

aA_UD908T_e = IP_e_inv(1:3,1:3);
bB_UD908T_e = IP_e_inv(4:6,1:3);
dD_UD908T_e = IP_e_inv(4:6,4:6);

%%Computation output:
%%----------------------------------------------------------------------------------------
% fprintf('Predicted elastic constant values:\n');
% fprintf('----------------------------------\n');
% fprintf('E11 modulus: %.3f GPa\n', E11/1e9);
% fprintf('E22 modulus: %.3f GPa\n', E22/1e9);
% fprintf('nu12: %.3f\n', nu12);
% fprintf('G12: %.3f GPa\n', G12/1e9);
% fprintf(' \n');
% fprintf('Empirically-determined E11 modulus: %.3f GPa\n', E_mod/1e9);


format long e
%%Computation output:
fprintf('UD 90 deg, 8-Ply carbon fibre/epoxy coupon - tensile quasi-fatigue loading - Computation output: \n')
disp(' ')
%%----------------------------------------------------------------------------------------
fprintf('Laminate stiffness matrices\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
disp(A_UD908T)
disp(' ')
fprintf('[B], units: N = \n');
fprintf(' ');
disp(B_UD908T)
disp(' ')
fprintf('[D], units: N*m = \n');
fprintf(' ');
disp(D_UD908T)
disp(' ')
fprintf('Laminate compliance matrices\n');
fprintf('----------------------------------\n');
fprintf('[a], units: m/N = \n');
fprintf(' ');
disp(aA_UD908T)
disp(' ')
fprintf('[b], units: 1/N = \n');
fprintf(' ');
disp(bB_UD908T)
disp(' ')
fprintf('[d], units: 1/(N*m) = \n');
fprintf(' ');
disp(dD_UD908T)
disp(' ')

%Test: quasi-fatigue (tensile) loading of a symmetric, 8-ply ±45° carbon fibre/epoxy laminate
%Laminate type: cross-ply, balanced (symmetric, orthotropic)

%%---------------------------------Data inputs---------------------------------------

%%Carbon fibre elastic properties
Ef1 = 230e9;                  %Fibre longitudinal modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Tension applied in 1-direction (±45° from reference)
E_mod_45 = 12.466557e9;         %Tensile modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%Define no. of each ply orietation for design laminate
o0 = 0;
o90 = 0;
o30 = 0;
o45 = 8;
o60 = 0;

%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45p_rad = degtorad(45);
o45m_rad = degtorad(-45);
o60_rad = degtorad(60);

%Define ply design details:
tl = 1.95/1000;   %Measured avg. thickness of laminate coupons [m]
np = 8;           %no. of ply layers
t = t1/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;      %total thickness of 0° plies
t90 = t*o90;      %total thickness of 90° plies
t30 = t*o30;      %total thickness of 30° plies
t45 = t*o45;      %total thickness of 45° plies
t60 = t*o60;      %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);  %total thickness of laminate (sanity check: lt == t1)
w = 20.10;          %avg. coupon width [mm]
Ww = w/1000;       %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t1 ~= lt
    error("User has mis-defined laminate ply layer design. Check design ply layer number.\n");
    %break
else
    %%±45° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_45 = (Ef1*Vf) + (Em*Vm);                       %Modulus in 1-direction (in fibre direction)
    E11_e45 = E_mod_45;                                  %Experimentally-determined modulus
    E22_45 = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));            %Modulus in 2-direction (⊥ to fibre direction)
    nu12_45 = (Vm*num) + (Vf*nuf);                     %Poisson's ratio - contraction in the 2-direction (⊥ to fibre direction) 
                                                      % when an extension is applied in 1-direction (fibre direction)
    G12_45 = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));                %Shear modulus in 2-direction (⊥ to fibre direction) on the plane whose 
                                                      % normal is in direction 1-direction (fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_45 = 1/E11_45;
    S12_45 = -(nu12_45/E11_45);
    S21_45 = S12_45;
    S22_45 = 1/E22_45;
    S66_45 = 1/G12_45;
    
    %%Compliance matrix constants from experimental data
    S11e45 = 1/E11_e45;
    S12e45 = -(nu12_0/E11_e45);
    S21e45 = S12e45;
    S22e45 = 1/E22_45;
    S66e45 = 1/G12_45;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_45 = 1-((E22_45/E11_45)*((nu12_45)^2));
    Q11_45 = E11_45/D_45;
    Q12_45 = (nu12_45*E22_45)/D_45;
    Q21_45 = Q12_45;
    Q22_45 = E22_45/D_45;
    Q66_45 = G12_45;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_e45 = 1-((E22_45/E11_e45)*((nu12_45)^2));
    Q11e45 = E11_e45/D_e45;
    Q12e45 = (nu12_45*E22_45)/D_e45;
    Q21e45 = Q12e45;
    Q22e45 = E22_45/D_e45;
    Q66e45 = G12_45;

    %Compile compliance matrix
    S45 = [S11_45 S12_45 0; S21_45 S22_45 0; 0 0 S66_45];
    S45e = [S11e45 S12e45 0; S21e45 S22e45 0; 0 0 S66e45];
    %Compile stiffness matrix
    Q45 = [Q11_45 Q12_45 0; Q21_45 Q22_45 0; 0 0 Q66_45];
    Q45e = [Q11e45 Q12e45 0; Q21e45 Q22e45 0; 0 0 Q66e45];
    %Sanity check
    Q45_valid = inv(S45);
    Q45e_valid = inv(S45e);

    %Build the stress & strain transformation matrices
    %% transformations are vital in analyses of stress and strain, both because they are needed
    %% to compute critical values of these entities and also because the tensorial nature of stress and
    %% strain is most clearly seen in their transformation properties. Other entities, such as moment of
    %% inertia and curvature, also transform in a manner similar to stress and strain.
    
    %%Define tranformation angles for +45° plies from reference
    c45 = cos(o45p_rad);
    ss45 = sin(o45p_rad);
    
    %%Define tranformation angles for -45° plies from reference
    c45m = cos(o45m_rad);
    ss45m = sin(o45m_rad);

    %For +45° ply layers
    %Stress transformation matrix
    Tsig45 = [c45^2 ss45^2 2*c45*ss45; ss45^2 c45^2 -2*c45*ss45; -c45*ss45 c45*ss45 ((c45^2)-(ss45^2))];
    %Strain transformation matrix
    Teps45 = [c45^2 ss45^2 c45*ss45; ss45^2 c45^2 -c45*ss45; -2*c45*ss45 2*c45*ss45 ((c45^2)-(ss45^2))];
    
    %For -45° ply layers
    Tsig45m = [c45m^2 ss45m^2 2*c45m*ss45m; ss45m^2 c45m^2 -2*c45m*ss45m; -c45m*ss45m c45m*ss45m ((c45m^2)-(ss45m^2))];
    %Strain transformation matrix
    Teps45m = [c45m^2 ss45m^2 c45m*ss45m; ss45m^2 c45m^2 -c45m*ss45m; -2*c45m*ss45m 2*c45m*ss45m ((c45m^2)-(ss45m^2))];
    
    %Transformed (reduced) stiffness matrix
    Qb45 = (inv(Tsig45))*Q45*Teps45;
    Qb45e = (inv(Tsig45))*Q45e*Teps45;
    Qb45m = (inv(Tsig45m))*Q45*Teps45m;
    Qb45em = (inv(Tsig45m))*Q45e*Teps45m; 
    
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Approximate z0 as the distance covered by the sum total of the +45° plies from the reference plane
z0 = z1-(lt/2);

%Approximate z2 as the distance covered by the sum total of the -45° plies from the reference plane
z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_pm458T = (Qb45*zA1) + (Qb45m*zA2);
B_pm458T = (Qb45*zB1) + (Qb45m*zB2);
D_pm458T = (Qb45*zD1) + (Qb45m*zD2);

A_pm458T_e = (Qb45e*zA1) + (Qb45em*zA2);
B_pm458T_e = (Qb45e*zB1) + (Qb45em*zB2);
D_pm458T_e = (Qb45e*zD1) + (Qb45em*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM = [A_pm458T B_pm458T; B_pm458T D_pm458T];

IPFMe = [A_pm458T_e B_pm458T_e; B_pm458T_e D_pm458T_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IP_inv = inv(IPFM);

IP_e_inv = inv(IPFMe);

aA_pm458T = IP_inv(1:3,1:3);
bB_pm458T = IP_inv(4:6,1:3);
dD_pm458T = IP_inv(4:6,4:6);

aA_pm458T_e = IP_e_inv(1:3,1:3);
bB_pm458T_e = IP_e_inv(4:6,1:3);
dD_pm458T_e = IP_e_inv(4:6,4:6);

format long e
%%Computation output:
fprintf('+/- 45 deg, 8-Ply carbon fibre/epoxy coupon - tensile quasi-fatigue loading - Computation output: \n')
disp(' ')
%%----------------------------------------------------------------------------------------
fprintf('Laminate stiffness matrices\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
disp(A_pm458T_e)
disp(' ')
fprintf('[B], units: N = \n');
fprintf(' ');
disp(B_pm458T_e)
disp(' ')
fprintf('[D], units: N*m = \n');
fprintf(' ');
disp(D_pm458T_e)
disp(' ')
fprintf('Laminate compliance matrices\n');
fprintf('----------------------------------\n');
fprintf('[a], units: m/N = \n');
fprintf(' ');
disp(aA_pm458T_e)
disp(' ')
fprintf('[b], units: 1/N = \n');
fprintf(' ');
disp(bB_pm458T_e)
disp(' ')
fprintf('[d], units: 1/(N*m) = \n');
fprintf(' ');
disp(dD_pm458T_e)
disp(' ')

%Test: quasi-fatigue (tensile) loading of a symmetric, 8-ply UD 45° carbon fibre/epoxy laminate
%Laminate type:

%%---------------------------------Data inputs---------------------------------------

%%Carbon fibre elastic properties
Ef1 = 230e9;                  %Fibre longitudinal modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Tension applied in 1-direction (45° from reference)
E_mod_45d = 8.989689e9;         %Tensile modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%Define no. of each ply orietation for design laminate
o0 = 0;
o90 = 0;
o30 = 0;
o45 = 8;
o60 = 0;

%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45_rad = degtorad(45);
o60_rad = degtorad(60);

%Define ply design details:
tl = 2.01/1000;   %Measured avg. thickness of laminate coupons [m]
np = 8;           %no. of ply layers
t = t1/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;      %total thickness of 0° plies
t90 = t*o90;      %total thickness of 90° plies
t30 = t*o30;      %total thickness of 30° plies
t45 = t*o45;      %total thickness of 45° plies
t60 = t*o60;      %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);  %total thickness of laminate (sanity check: lt == t1)
w = 20.06;          %avg. coupon width [mm]
Ww = w/1000;       %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t1 ~= lt
    error("User has mis-defined laminate ply layer design. Check design ply layer number.\n");
    %break
else
    %%45° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_45 = (Ef1*Vf) + (Em*Vm);                       %Modulus in 1-direction (in fibre direction)
    E11_e45 = E_mod_45d;                                %Experimentally-determined modulus
    E22_45 = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));            %Modulus in 2-direction (⊥ to fibre direction)
    nu12_45 = (Vm*num) + (Vf*nuf);                     %Poisson's ratio - contraction in the 2-direction (⊥ to fibre direction) 
                                                         % when an extension is applied in 1-direction (fibre direction)
    G12_45 = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));                %Shear modulus in 2-direction (⊥ to fibre direction) on the plane whose 
                                                         % normal is in direction 1-direction (fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_45 = 1/E11_45;
    S12_45 = -(nu12_45/E11_45);
    S21_45 = S12_45;
    S22_45 = 1/E22_45;
    S66_45 = 1/G12_45;
    
    %%Compliance matrix constants from experimental data
    S11e45 = 1/E11_e45;
    S12e45 = -(nu12_0/E11_e45);
    S21e45 = S12e45;
    S22e45 = 1/E22_45;
    S66e45 = 1/G12_45;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_45 = 1-((E22_45/E11_45)*((nu12_45)^2));
    Q11_45 = E11_45/D_45;
    Q12_45 = (nu12_45*E22_45)/D_45;
    Q21_45 = Q12_45;
    Q22_45 = E22_45/D_45;
    Q66_45 = G12_45;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_e45 = 1-((E22_45/E11_e45)*((nu12_45)^2));
    Q11e45 = E11_e45/D_e45;
    Q12e45 = (nu12_45*E22_45)/D_e45;
    Q21e45 = Q12e45;
    Q22e45 = E22_45/D_e45;
    Q66e45 = G12_45;

    %Compile compliance matrix
    S45 = [S11_45 S12_45 0; S21_45 S22_45 0; 0 0 S66_45];
    S45e = [S11e45 S12e45 0; S21e45 S22e45 0; 0 0 S66e45];
    %Compile stiffness matrix
    Q45 = [Q11_45 Q12_45 0; Q21_45 Q22_45 0; 0 0 Q66_45];
    Q45e = [Q11e45 Q12e45 0; Q21e45 Q22e45 0; 0 0 Q66e45];
    %Sanity check
    Q45_valid = inv(S45);
    Q45e_valid = inv(S45e);

    %Build the stress & strain transformation matrices
    %% transformations are vital in analyses of stress and strain, both because they are needed
    %% to compute critical values of these entities and also because the tensorial nature of stress and
    %% strain is most clearly seen in their transformation properties. Other entities, such as moment of
    %% inertia and curvature, also transform in a manner similar to stress and strain.
    
    %%Define tranformation angles for +45° plies from reference
    c45 = cos(o45_rad);
    ss45 = sin(o45_rad);
    
    %For +45° ply layers
    %Stress transformation matrix
    Tsig45 = [c45^2 ss45^2 2*c45*ss45; ss45^2 c45^2 -2*c45*ss45; -c45*ss45 c45*ss45 ((c45^2)-(ss45^2))];
    %Strain transformation matrix
    Teps45 = [c45^2 ss45^2 c45*ss45; ss45^2 c45^2 -c45*ss45; -2*c45*ss45 2*c45*ss45 ((c45^2)-(ss45^2))];
    
    %Transformed (reduced) stiffness matrix
    Qb45 = (inv(Tsig45))*Q45*Teps45;
    Qb45e = (inv(Tsig45))*Q45e*Teps45;
    
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Approximate z0 as the distance covered by the sum total of the +45° plies from the reference plane
z0 = z1-(lt/2);

%Approximate z2 as the distance covered by the sum total of the -45° plies from the reference plane
z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_UD458T = (Qb45*zA1) + (Qb45*zA2);
B_UD458T = (Qb45*zB1) + (Qb45*zB2);
D_UD458T = (Qb45*zD1) + (Qb45*zD2);

A_UD458T_e = (Qb45e*zA1) + (Qb45e*zA2);
B_UD458T_e = (Qb45e*zB1) + (Qb45e*zB2);
D_UD458T_e = (Qb45e*zD1) + (Qb45e*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM = [A_UD458T B_UD458T; B_UD458T D_UD458T];

IPFMe = [A_UD458T_e B_UD458T_e; B_UD458T_e D_UD458T_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IP_inv = inv(IPFM);

IP_e_inv = inv(IPFMe);

aA_UD458T = IP_inv(1:3,1:3);
bB_UD458T = IP_inv(4:6,1:3);
dD_UD458T = IP_inv(4:6,4:6);

aA_UD458T_e = IP_e_inv(1:3,1:3);
bB_UD458T_e = IP_e_inv(4:6,1:3);
dD_UD458T_e = IP_e_inv(4:6,4:6);

format long e
%%Computation output:
fprintf('UD 45 deg, 8-Ply carbon fibre/epoxy coupon - tensile quasi-fatigue loading - Computation output: \n')
disp(' ')
%%----------------------------------------------------------------------------------------
fprintf('Laminate stiffness matrices\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
disp(A_UD458T_e)
disp(' ')
fprintf('[B], units: N = \n');
fprintf(' ');
disp(B_UD458T_e)
disp(' ')
fprintf('[D], units: N*m = \n');
fprintf(' ');
disp(D_UD458T_e)
disp(' ')
fprintf('Laminate compliance matrices\n');
fprintf('----------------------------------\n');
fprintf('[a], units: m/N = \n');
fprintf(' ');
disp(aA_UD458T_e)
disp(' ')
fprintf('[b], units: 1/N = \n');
fprintf(' ');
disp(bB_UD458T_e)
disp(' ')
fprintf('[d], units: 1/(N*m) = \n');
fprintf(' ');
disp(dD_UD458T_e)
disp(' ')

%Test: quasi-fatigue (compression) loading of a symmetric, 4-ply UD 0° carbon fibre/epoxy laminate
%Laminate type: Symmetric, orthotropic

%%---------------------------------Data inputs---------------------------------------

%%Carbon fibre elastic properties (compression)
Ef1 = 230e9;                %Fibre longitudinal compression modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Compression applied in 1 (fibre-oriented) direction
E_Cmod = 99.225986e9;         %Compression modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%Define no. of each ply orietation for design laminate
o0 = 4;
o90 = 0;
o30 = 0;
o45 = 0;
o60 = 0;

%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45_rad = degtorad(45);
o60_rad = degtorad(60);

%Define ply design details:
tl = 1.01/1000;   %Measured avg. thickness of laminate coupons [m]
np = 4;           %no. of ply layers
t = t1/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;      %total thickness of 0° plies
t90 = t*o90;      %total thickness of 90° plies
t30 = t*o30;      %total thickness of 30° plies
t45 = t*o45;      %total thickness of 45° plies
t60 = t*o60;      %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);  %total thickness of laminate (sanity check: lt == t1)
w = 9.98;          %avg. coupon width [mm]
Ww = w/1000;       %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t1 ~= lt
    error("User has mis-defined laminate ply layer design. Check design ply layer number.\n");
    %break
else
    %%0° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_0C = ((Ef1*Vf) + (Em*Vm));                       %Modulus in 1-direction (in fibre direction)
    E11_eC = E_Cmod;                                     %Experimentally-determined modulus
    E22_0C = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));              %Modulus in 2-direction (⊥ to fibre direction)
    nu12_0C = (Vm*num) + (Vf*nuf);                       %Poisson's ratio - contraction in the 2-direction (⊥ to fibre direction) 
                                                           % when an extension is applied in 1-direction (fibre direction)
    G12_0C = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));                 %Shear modulus in 2-direction (⊥ to fibre direction) on the plane whose 
                                                           % normal is in direction 1-direction (fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_0C = 1/E11_0C;
    S12_0C = -(nu12_0C/E11_0C);
    S21_0C = S12_0C;
    S22_0C = 1/E22_0C;
    S66_0C = 1/G12_0C;
    
    %%Compliance matrix constants from experimental data
    S11eC = 1/E11_eC;
    S12eC = -(nu12_0/E11_eC);
    S21eC = S12eC;
    S22eC = 1/E22_0C;
    S66eC = 1/G12_0C;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_0C = 1-((E22_0C/E11_0C)*((nu12_0C)^2));
    Q11_0C = E11_0C/D_0C;
    Q12_0C = (nu12_0C*E22_0C)/D_0C;
    Q21_0C = Q12_0C;
    Q22_0C = E22_0C/D_0C;
    Q66_0C = G12_0C;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_eC = 1-((E22_0C/E11_eC)*((nu12_0C)^2));
    Q11eC = E11_eC/D_eC;
    Q12eC = (nu12_0C*E22_0C)/D_eC;
    Q21eC = Q12eC;
    Q22eC = E22_0C/D_eC;
    Q66eC = G12_0C;

    %Compile compliance matrix
    S0C = [S11_0C S12_0C 0; S21_0C S22_0C 0; 0 0 S66_0C];
    S0eC = [S11eC S12eC 0; S21eC S22eC 0; 0 0 S66eC];
    %Compile stiffness matrix
    Q0C = [Q11_0C Q12_0C 0; Q21_0C Q22_0C 0; 0 0 Q66_0C];
    Q0eC = [Q11eC Q12eC 0; Q21eC Q22eC 0; 0 0 Q66eC];
    %Sanity check
    Q0C_valid = inv(S0C);
    Q0eC_valid = inv(S0eC);

    %Build the stress & strain transformation matrices
    %% transformations are vital in analyses of stress and strain, both because they are needed
    %% to compute critical values of these entities and also because the tensorial nature of stress and
    %% strain is most clearly seen in their transformation properties. Other entities, such as moment of
    %% inertia and curvature, also transform in a manner similar to stress and strain.
    c0C = cos(o0_rad);
    ss0C = sin(o0_rad);
    %Stress transformation matrix
    Tsig0C = [c0C^2 ss0C^2 2*c0C*ss0C; ss0C^2 c0C^2 -2*c0C*ss0C; -c0C*ss0C c0C*ss0C ((c0C^2)-(ss0C^2))];
    %Strain transformation matrix
    Teps0C = [c0C^2 ss0C^2 c0C*ss0C; ss0C^2 c0C^2 -c0C*ss0C; -2*c0C*ss0C 2*c0C*ss0C ((c0C^2)-(ss0C^2))];
    %Transformed (reduced) stiffness matrix
    Qb0C = (inv(Tsig0C))*Q0C*Teps0C;
    Qb0eC = (inv(Tsig0C))*Q0eC*Teps0C;
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Define lower edge of 0° laminate section
z0 = z1-(lt/2);

%Define upper edge of 0° laminate section

z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_UD04C = (Qb0C*zA1) + (Qb0C*zA2);
B_UD04C = (Qb0C*zB1) + (Qb0C*zB2);
D_UD04C = (Qb0C*zD1) + (Qb0C*zD2);

A_UD04C_e = (Qb0eC*zA1) + (Qb0eC*zA2);
B_UD04C_e = (Qb0eC*zB1) + (Qb0eC*zB2);
D_UD04C_e = (Qb0eC*zD1) + (Qb0eC*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM_C = [A_UD04C B_UD04C; B_UD04C D_UD04C];

IPFMe_C = [A_UD04C_e B_UD04C_e; B_UD04C_e D_UD04C_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IPC_inv = inv(IPFM_C);

IPC_e_inv = inv(IPFMe_C);

aA_UD04C = IPC_inv(1:3,1:3);
bB_UD04C = IPC_inv(4:6,1:3);
dD_UD04C = IPC_inv(4:6,4:6);

aA_UD04C_e = IPC_e_inv(1:3,1:3);
bB_UD04C_e = IPC_e_inv(4:6,1:3);
dD_UD04C_e = IPC_e_inv(4:6,4:6);

%%Computation output:
%%----------------------------------------------------------------------------------------
% fprintf('Predicted elastic constant values:\n');
% fprintf('----------------------------------\n');
% fprintf('E11 modulus: %.3f GPa\n', E11/1e9);
% fprintf('E22 modulus: %.3f GPa\n', E22/1e9);
% fprintf('nu12: %.3f\n', nu12);
% fprintf('G12: %.3f GPa\n', G12/1e9);
% fprintf(' \n');
% fprintf('Empirically-determined E11 modulus: %.3f GPa\n', E_mod/1e9);


format long e
%%Computation output:
fprintf('UD 0 deg, 4-Ply carbon fibre/epoxy coupon - compression quasi-fatigue loading - Computation output: \n')
disp(' ')
%%----------------------------------------------------------------------------------------
fprintf('Laminate stiffness matrices\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
disp(A_UD04C_e)
disp(' ')
fprintf('[B], units: N = \n');
fprintf(' ');
disp(B_UD04C_e)
disp(' ')
fprintf('[D], units: N*m = \n');
fprintf(' ');
disp(D_UD04C_e)
disp(' ')
fprintf('Laminate compliance matrices\n');
fprintf('----------------------------------\n');
fprintf('[a], units: m/N = \n');
fprintf(' ');
disp(aA_UD04C_e)
disp(' ')
fprintf('[b], units: 1/N = \n');
fprintf(' ');
disp(bB_UD04C_e)
disp(' ')
fprintf('[d], units: 1/(N*m) = \n');
fprintf(' ');
disp(dD_UD04C_e)
disp(' ')

%Test: quasi-fatigue (compression) loading of a symmetric, 8-ply UD 90° carbon fibre/epoxy laminate
%Laminate type: Symmetrical

%%---------------------------------Data inputs---------------------------------------

%%Carbon fibre elastic properties (compression)
Ef1 = 230e9;                %Fibre longitudinal compression modulus (Pa)
Ef2 = 15e9;                   %Fibre transverse modulus (Pa)
Vf = 0.55;                    %Fibre volume fraction
Gf12 = 15e9;                  %Fibre longitudinal shear modulus (Pa)
nuf = 0.2;                    %Fibre Poisson's ratio

%%Epoxy matrix elastic properties
Vm = 1 - Vf;                  %Matrix volume fraction
Em1 = 4e9;                    %Matrix longitudinal modulus (Pa)
Em2 = 4e9;                    %Matrix transverse modulus (Pa)
Gm12 = 1.481e9;               %Matrix longitudinal shear modulus (Pa)
num = 0.35;                   %Matrix Poisson's ratio

%%Experimental composite properties (measured)
%% Compression applied in 1 (fibre-oriented) direction
E_Cmod90 = 6.099093e9;        %Compression modulus of elasticity from experiment (Pa)

%%Build ply orientation (bottom to top of composite ply layup)
%NOTES:
%% 1. Code is only applicable for symmetric laminate designs
%% 2. Code only accounts for 0°, ±30°, ±45°, ±60° and 90° fibre orientations
%% 3. h = 2(o0 + o90 + o30 + o45 + o60) MUST follow
%%
%% symmetric ply layup convention:
%% [0/o0/90/o90/30/o30/45/o45/60/o60]
%% where:
%% o0:  no. of 0° plies
%% o90: no. of 90° plies
%% o30: no. of ±30° plies
%% o45: no. of ±45° plies
%% o60: no. of ±60° plies

%Define no. of each ply orietation for design laminate
o0 = 0;
o90 = 8;
o30 = 0;
o45 = 0;
o60 = 0;

%MATLAB has no simple function to add numeric values - store ply count in a vector
ply_v = [o0 o90 o30 o45 o60];

%Total number of plies in the laminate coupon
nmp = sum(ply_v);

%Ply orientatioms in radians for transform matrix calcs
o0_rad = degtorad(0);
o90_rad = degtorad(90);
o30_rad = degtorad(30);
o45_rad = degtorad(45);
o60_rad = degtorad(60);

%Define ply design details:
tl = 2.02/1000;   %Measured avg. thickness of laminate coupons [m]
np = 8;           %no. of ply layers
t = t1/np;        %Avg. ply layer thickness [m]
t0 =  t*o0;      %total thickness of 0° plies
t90 = t*o90;      %total thickness of 90° plies
t30 = t*o30;      %total thickness of 30° plies
t45 = t*o45;      %total thickness of 45° plies
t60 = t*o60;      %total thickness of 60° plies
t_vec = [t0 t90 t30 t45 t60]; %Vector for ply thicknesses
lt = sum(t_vec);  %total thickness of laminate (sanity check: lt == t1)
w = 19.98;          %avg. coupon width [mm]
Ww = w/1000;       %avg. coupon width [m]

%Compute ply-layer compliance and stiffness constants
if np ~= nmp | t1 ~= lt
    error("User has mis-defined laminate ply layer design. Check design ply layer number.\n");
    %break
else
    %%90° orientation orthotropic composite ply layers
    %%----------------------------------------------------------------------------------------
    %%Calculated engineering constants (with reference to principle axes)
    E11_90C = ((Ef1*Vf) + (Em*Vm));                       %Modulus in 1-direction (in fibre direction)
    E11_e90C = E_Cmod90;                                     %Experimentally-determined modulus
    E22_90C = (Ef2*Em) / ((Vm*Ef2)+(Vf*Em));              %Modulus in 2-direction (⊥ to fibre direction)
    nu12_90C = (Vm*num) + (Vf*nuf);                       %Poisson's ratio - contraction in the 2-direction (⊥ to fibre direction) 
                                                           % when an extension is applied in 1-direction (fibre direction)
    G12_90C = (Gm*Gf)/((Vm*Gf)+(Vf*Gm));                 %Shear modulus in 2-direction (⊥ to fibre direction) on the plane whose 
                                                           % normal is in direction 1-direction (fibre direction)

    %%Compliance matrix constants by rule-of-mixture
    S11_90C = 1/E11_90C;
    S12_90C = -(nu12_90C/E11_90C);
    S21_90C = S12_90C;
    S22_90C = 1/E22_90C;
    S66_90C = 1/G12_90C;
    
    %%Compliance matrix constants from experimental data
    S11e90C = 1/E11_e90C;
    S12e90C = -(nu12_90C/E11_e90C);
    S21e90C = S12e90C;
    S22e90C = 1/E22_90C;
    S66e90C = 1/G12_90C;

    %Compute reduced stiffness matrix constants by rule-of-mixture
    D_90C = 1-((E22_90C/E11_90C)*((nu12_90C)^2));
    Q11_90C = E11_90C/D_90C;
    Q12_90C = (nu12_90C*E22_90C)/D_90C;
    Q21_90C = Q12_90C;
    Q22_90C = E22_90C/D_90C;
    Q66_90C = G12_90C;
    
    %%Compute reduced stiffness matrix constants from experimental data
    D_e90C = 1-((E22_90C/E11_e90C)*((nu12_90C)^2));
    Q11e90C = E11_e90C/D_e90C;
    Q12e90C = (nu12_90C*E22_90C)/D_e90C;
    Q21e90C = Q12e90C;
    Q22e90C = E22_90C/D_e90C;
    Q66e90C = G12_90C;

    %Compile compliance matrix
    S90C = [S11_90C S12_90C 0; S21_90C S22_90C 0; 0 0 S66_90C];
    S90eC = [S11e90C S12e90C 0; S21e90C S22e90C 0; 0 0 S66e90C];
    %Compile stiffness matrix
    Q90C = [Q11_90C Q12_90C 0; Q21_90C Q22_90C 0; 0 0 Q66_90C];
    Q90eC = [Q11e90C Q12e90C 0; Q21e90C Q22e90C 0; 0 0 Q66e90C];
    %Sanity check
    Q90C_valid = inv(S90C);
    Q90eC_valid = inv(S90eC);

    %Build the stress & strain transformation matrices
    %% transformations are vital in analyses of stress and strain, both because they are needed
    %% to compute critical values of these entities and also because the tensorial nature of stress and
    %% strain is most clearly seen in their transformation properties. Other entities, such as moment of
    %% inertia and curvature, also transform in a manner similar to stress and strain.
    c90C = cos(o90_rad);
    ss90C = sin(o90_rad);
    %Stress transformation matrix
    Tsig90C = [c90C^2 ss90C^2 2*c90C*ss90C; ss90C^2 c90C^2 -2*c90C*ss90C; -c90C*ss90C c90C*ss90C ((c90C^2)-(ss90C^2))];
    %Strain transformation matrix
    Teps90C = [c90C^2 ss90C^2 c90C*ss90C; ss90C^2 c90C^2 -c90C*ss90C; -2*c90C*ss90C 2*c90C*ss90C ((c90C^2)-(ss90C^2))];
    %Transformed (reduced) stiffness matrix
    Qb90C = (inv(Tsig90C))*Q90C*Teps90C;
    Qb90eC = (inv(Tsig90C))*Q90eC*Teps90C;
end


%%LAMINATE response to quasi-fatigue loading
%%----------------------------------------------------------------------------------------
%Define reference axis, z1: the mid-plane of the symmetric laminate layup
z1 = 0;

%Define lower edge of 0° laminate section
z0 = z1-(lt/2);

%Define upper edge of 0° laminate section

z2 = z1+(lt/2);

%Define A, B and D matrix z multiplicatives
zA1 = z1-z0;
zA2 = z2-z1;
zB1 = ((z1^2)-(z0^2))/2;
zB2 = ((z2^2)-(z1^2))/2;
zD1 = ((z1^3)-(z0^3))/3;
zD2 = ((z2^3)-(z1^3))/3;

%Compute the A, B and D matrices - stiffness matrices of the laminate
% These matrices describe the in-plane forces & moments on the composite laminate
A_UD908C = (Qb90C*zA1) + (Qb90C*zA2);
B_UD908C = (Qb90C*zB1) + (Qb90C*zB2);
D_UD908C = (Qb90C*zD1) + (Qb90C*zD2);

A_UD908C_e = (Qb90eC*zA1) + (Qb90eC*zA2);
B_UD908C_e = (Qb90eC*zB1) + (Qb90eC*zB2);
D_UD908C_e = (Qb90eC*zD1) + (Qb90eC*zD2);

%Compile the global in-plane forces/moments response matrix
IPFM_90C = [A_UD908C B_UD908C; B_UD908C D_UD908C];

IPFMe_90C = [A_UD908C_e B_UD908C_e; B_UD908C_e D_UD908C_e];

%Compute the matrix that describes the strain and curvatures imposed on the laminate
IPC90_inv = inv(IPFM_90C);

IPC90_e_inv = inv(IPFMe_90C);

aA_UD908C = IPC90_inv(1:3,1:3);
bB_UD908C = IPC90_inv(4:6,1:3);
dD_UD908C = IPC90_inv(4:6,4:6);

aA_UD908C_e = IPC90_e_inv(1:3,1:3);
bB_UD908C_e = IPC90_e_inv(4:6,1:3);
dD_UD908C_e = IPC90_e_inv(4:6,4:6);

%%Computation output:
%%----------------------------------------------------------------------------------------
% fprintf('Predicted elastic constant values:\n');
% fprintf('----------------------------------\n');
% fprintf('E11 modulus: %.3f GPa\n', E11/1e9);
% fprintf('E22 modulus: %.3f GPa\n', E22/1e9);
% fprintf('nu12: %.3f\n', nu12);
% fprintf('G12: %.3f GPa\n', G12/1e9);
% fprintf(' \n');
% fprintf('Empirically-determined E11 modulus: %.3f GPa\n', E_mod/1e9);


format long e
%%Computation output:
fprintf('UD 90 deg, 8-Ply carbon fibre/epoxy coupon - compression quasi-fatigue loading - Computation output: \n')
disp(' ')
%%----------------------------------------------------------------------------------------
fprintf('Laminate stiffness matrices\n');
fprintf('----------------------------------\n');
fprintf('[A], units: N/m = \n');
fprintf(' ');
disp(A_UD908C_e)
disp(' ')
fprintf('[B], units: N = \n');
fprintf(' ');
disp(B_UD908C_e)
disp(' ')
fprintf('[D], units: N*m = \n');
fprintf(' ');
disp(D_UD908C_e)
disp(' ')
fprintf('Laminate compliance matrices\n');
fprintf('----------------------------------\n');
fprintf('[a], units: m/N = \n');
fprintf(' ');
disp(aA_UD908C_e)
disp(' ')
fprintf('[b], units: 1/N = \n');
fprintf(' ');
disp(bB_UD908C_e)
disp(' ')
fprintf('[d], units: 1/(N*m) = \n');
fprintf(' ');
disp(dD_UD908C_e)
disp(' ')
