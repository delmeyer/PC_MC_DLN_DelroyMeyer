clc;
close all;
clear all;
digits(32);
format short e;
disp('Welcome to "CompCal by Hasan Mert Dinleten*"')
disp('Please Select the Material')
disp('1  Graphite/EPOXY')
disp('2  New Material')
comm=input('>> ');
disp('Please Select the case number')
disp('1.1 (Q/Qbar matrix for the fiber orientations 0, 90, +45, -45 degrees and Qbar graphs ranging from -90� to +90�)')
disp('1.2 (Total stresses and total strains as functions of given mechanical strains and uniform temperature change)')
disp('1.3 (Total strains are given as default strain rather than the mechanical strains given in 1.1)')
disp('----------------------------------------------------------------------------------------------------------------------')
disp('2.1 (Compute and print [A],[B],[D] matrices for a laminate)')
disp('2.2 (Compute [�]� and [K] with given N(N/m) and M(N*m/m) for a laminate)')
disp('2.3 (Compute mechanical stress and total stress at the top and the bottom of each layer for a generic laminate under arbitrary loading, and plot the results as through thickness stress plots.')
cn=input('>> ');
clc
%Mechanical Properties of Graphite/EPOXY
if comm==1
    E1=181e+09;
    E2=10.3e+09;
    v12=0.28;
    v21=(E2/E1)*v12;
    G12=7.17e+09;
    a1=0.02;
    a2=22.5;
    t=6e-03; %common thickness of a lamina
else
    disp('Please enter the material properties')
    disp('Enter the values for extensional and shear modulus in GPa')
    disp('also enter the thermal coefficency of your material and thickness of a lamina')
    eee=1e+09;
    E1=input('E1 = ');
    E1=E1*eee;
    E2= input('E2 = ');
    E2=E2*eee;
    v12= input('v21 = ');
    v21=(E2/E1)*v12;
    G12= input('G12 = ');
    G12=G12*eee;
    a1= input('a1 = ');
    a2= input('a2 = ');
    tttt=input('t = ');
    t=tttt*e-03;
end
        %%Stiffness Matrix elements
        q11=(E1/(1-v12*v21));
        q12=(-v12*E2/(1-v12*v21));
        q13=(0);
        q21=q11;
        q22=(E2/1-v12*v21);
        q23=(0);
        q31=q13;
        q32=q23;
        q33=(G12);
        q66=q33;


          Q = [q11     q12     q13  ;
               q21     q22     q23  ;
               q31     q32     q33 ];
        %%Complience Matrix elements
        S = inv(Q);
 %%Case1.1
    if cn==1.1

            for k =-90:1:90

            c = cosd(k); %
            s = sind(k); %
            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)

            %disp(Qbar);
            hold on;
            subplot(3,2,1)
            plot(qbar(1,1),k,'-bo');
            title('Qbar_{11}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');
            hold on;
            subplot(3,2,2)
            plot(qbar(1,2),k,'-bo');
            title('Qbar_{12}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');


            hold on;
            subplot(3,2,3)
            plot(qbar(2,2),k,'-bo');
            title('Qbar_{22}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');

            hold on;
            subplot(3,2,4)
            plot(qbar(3,1),k,'-bo');
            title('Qbar_{16}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');
            hold on;
            subplot(3,2,5)
            plot(qbar(3,2),k,'-bo');
            title('Qbar_{26}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');
            hold on;
            subplot(3,2,6)
            plot(qbar(3,3),k,'-bo');
            title('Qbar_{66}');
            xlabel('Pa(Pascal)');
            ylabel('\theta (degrees)');

            if (k == 0 || k ==-45 || k ==45 || k ==90)
            fprintf('Qbar/Q matrix of %d degree\n', k);
            disp(qbar);

      end
            end


 %%Case1.2
    elseif cn==1.2


        prompt = 'Would you like to enter your own mechanical strain and temperature change?, please write Y/N: ';
        str = input(prompt,'s');
        clc

        if isequal(str, 'Y')

            totST1=input('�1= ');
            totST2=input('�2= ');
            totST3=input('�3= ');
            Temp=input('Please enter the temperature ');

        else
            fprintf('You chose default mechanical strain values as [0.001 / 0.002 / 0.0005]  and Temperature Change -120�C\n\n');

            %Mechanical strains
            totST1=0.001;
            totST2=0.002;
            totST3=0.0005;
            Temp=-120;

        end
    for k =-90:1:90
            c = cosd(k); %
            s = sind(k); %
            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)
            KK = zeros(3,3);
            KK(1,1)=c^2;
            KK(1,2)=s^2;
            KK(1,3)=2*c*s;
            KK(2,1)=s^2;
            KK(2,2)=c^2;
            KK(2,3)=-2*c*s;
            KK(3,1)=-c*s;
            KK(3,2)=c*s;
            KK(3,3)=c^2-s^2;
            T1=inv(KK);
            H=zeros(3,1);
            H(1,1)=totST1;
            H(2,1)=totST2;
            H(3,1)=totST3/2;
            K=zeros(3,1);
            K=T1*H;
            %totalstrain=[T]^-1*localstrain
            E1=K(1,1);
            E2=K(2,1);
            E3=K(3,1)*2;
            ST=zeros(3,1);
            ST(1,1)=E1;
            ST(2,1)=E2;
            ST(3,1)=E3;

            %hydrothermal coefficents
            lclT=zeros(3,1);
            lclT(1,1)=a1;
            lclT(2,1)= a2;
            lclT(3,1)=0;
            tH=T1*lclT;
            %totalhydrothermalmatrix

            ttlHT=zeros(3,1);
            ttlHT(1,1)=tH(1,1);
            ttlHT(2,1)=tH(2,1);
            ttlHT(3,1)=tH(3,1)*2;
            N=ST-(Temp*ttlHT);
            %total stress
            SS=qbar*N;
            fprintf('Total strains for %d degree\n', k);
            disp(ST);
            fprintf('Total stresses for %d degree\n', k);
            disp(SS);
            disp('---------------------------------------------------')
    end



    elseif cn==1.3;
            prompt = 'Would you like to enter your own *Total strain and temperature change?, please write Y/N: ';
            str = input(prompt,'s');
            clc

        if isequal(str, 'Y')

            totSTt1=input('�1= ');
            totSTt2=input('�2= ');
            totSTt3=input('�3= ');
            Tempt=input('Please enter the temperature ');
        else
            fprintf('You chose default *Total strain values as [0.001 / 0.002 / 0.0005]  and Temperature Change -120�C\n\n');

            %Mechanical strains
            totSTt1=0.001;
            totSTt2=0.002;
            totSTt3=0.0005;
            Tempt=-120;
        end
            for k =-90:1:90

            c = cosd(k); %
            s = sind(k); %
            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)
            KK = zeros(3,3);
            KK(1,1)=c^2;
            KK(1,2)=s^2;
            KK(1,3)=2*c*s;
            KK(2,1)=s^2;
            KK(2,2)=c^2;
            KK(2,3)=-2*c*s;
            KK(3,1)=-c*s;
            KK(3,2)=c*s;
            KK(3,3)=c^2-s^2;
            T1=inv(KK);

            totST=zeros(3,1);
            totST(1,1)=totSTt1;
            totST(2,1)=totSTt2;
            totST(3,1)=totSTt3;
            locT=zeros(3,1);
            locT(1,1)=a1;
            locT(2,1)=a2;
            locT(3,1)=0;
            tH=T1*locT;
            ttlHT=zeros(3,1);
            ttlHT(1,1)=tH(1,1);
            ttlHT(2,1)=tH(2,1);
            ttlHT(3,1)=tH(3,1)*2;

            V=totST-(Tempt*ttlHT);
            ST=qbar*V;

            fprintf('Total strains for %d degree\n', k);
            disp(ST);
            disp('---------------------------------------------------')

             end

   %case 2.1
    elseif cn==2.1

        disp('please enter layer stacking, or use default layer stacking as [0/�45/90]s. ');
        disp('---------------------------------------------------------------------------------------------------------')

        prompt = 'Would you like to use your own Layer Stacking ?, Y/N: ';
        str = input(prompt,'s');
        clc

        if isequal(str, 'Y')

            disp('If the Layer Stacking(LS) is [+-30 0]s enter " [30 -30 0 -30 30] " Do Not Forget to Use Brackets [] !!!')
            l=input('Enter LS >> ');
        else
            l=[0 45 -45 90 90 -45 45 0];
        end
        clc

       angs = l;
       k = {};
       N=length(angs);
       h=zeros(N+1);

       h(N+1)=N*t/2;
       qbarK=zeros(3*N,3);


        for k = 1 : N

            c = cosd (angs(k)); %
            s = sind (angs(k)); %

            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)

            %allqbars
            qbarK([3*k-2:3*k],[1:3])=qbar([1:3],[1:3]);
            %all h values
            h(k)=(k-N/2-1)*t;
            %
        end

        A=zeros(3,3);
        B=zeros(3,3);
        D=zeros(3,3);

     for i=1:3
        for j=1:3
            qbar([1:3],[1:3])=qbarK([1:3],[1:3]);
            A(i,j) = qbar(i,j) * (h(2) - h(1));
            B(i,j) = 1/2*(qbar(i,j) * (h(2)^2 - h(1)^2));
            D(i,j) = 1/3*(qbar(i,j) * (h(2)^3 - h(1)^3));

            for k = 2 : N
            qbar([1:3],[1:3]) = qbarK( [3*k-2:3*k] , [1:3] );
            A(i,j) = qbar(i,j) * (h(k+1) - h(k)) + A(i,j);
            B(i,j) = 1/2*(qbar(i,j) * (h(k+1)^2 - h(k)^2)) + B(i,j);
            D(i,j) = 1/3*(qbar(i,j) * (h(k+1)^3 - h(k)^3)) + D(i,j);
        end
        end

     end

    if rem(length(angs),2)==0
    A= A.*[1 1 0 ; 1 1 0 ; 0 0 1];
    B= B.*[0 0 0 ; 0 0 0 ; 0 0 0];
    D= D.*[1 1 1 ; 1 1 1 ; 1 1 1];

    end
    A
    B
    D


%case2.2
    elseif isequal(cn, 2.2)

        disp('please enter layer stacking, or use default layer stacking as [0/�45/90]s. ');
        disp('---------------------------------------------------------------------------------------------------------')

        prompt = 'Would you like to use your own Layer Stacking ?, Y/N: ';
        str = input(prompt,'s');
        clc

        if isequal(str, 'Y')

            disp('If the Layer Stacking(LS) is [+-30 0]s enter " [30 -30 0 -30 30] " Do Not Forget to Use Brackets [] !!!')
            l=input('Enter LS >> ');
        else
            l=[0 45 -45 90 90 -45 45 0];
        end
        clc


       angs = l;
       k = {};
       N=length(angs);
       h=zeros(N+1);

       h(N+1)=N*t/2;
       qbarK=zeros(3*N,3);

        %qbar calculations
        for k = 1 : N

            c = cosd (angs(k)); %
            s = sind (angs(k)); %

            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)

            %allqbars
            qbarK([3*k-2:3*k],[1:3])=qbar([1:3],[1:3]);
            %all h values
            h(k)=(k-N/2-1)*t;
            %
        end

        A=zeros(3,3);
        B=zeros(3,3);
        D=zeros(3,3);
    %ABD Matrix Calculations
     for i=1:3
        for j=1:3
            qbar([1:3],[1:3])=qbarK([1:3],[1:3]);
            A(i,j) = qbar(i,j) * (h(2) - h(1));
            B(i,j) = 1/2*(qbar(i,j) * (h(2)^2 - h(1)^2));
            D(i,j) = 1/3*(qbar(i,j) * (h(2)^3 - h(1)^3));

            for k = 2 : N
            qbar([1:3],[1:3]) = qbarK( [3*k-2:3*k] , [1:3] );
            A(i,j) = qbar(i,j) * (h(k+1) - h(k)) + A(i,j);
            B(i,j) = 1/2*(qbar(i,j) * (h(k+1)^2 - h(k)^2)) + B(i,j);
            D(i,j) = 1/3*(qbar(i,j) * (h(k+1)^3 - h(k)^3)) + D(i,j);
        end
        end

     end

    if rem(length(angs),2)==0
    A= A.*[1 1 0 ; 1 1 0 ; 0 0 1];
    B= B.*[0 0 0 ; 0 0 0 ; 0 0 0];
    D= D.*[1 1 1 ; 1 1 1 ; 1 1 1];

    end
    %inverses
        Ain=inv(A);
        Bin= -((inv(A))*B);
        Cin= B*(inv(A));
        Din= D - (B*(inv(A))*B);

%midplane
        A1 = Ain-(Bin*(inv(Din))*Cin);
        B1 = Bin*(inv(Din));
        C1 = -(inv(Din))*Cin;
        D1 = inv(Din);

        N= [2000; 1000; 500]; %given
        M= [2; 2; 0]; %given
        EE= A1*N + B1*M;
        KK= C1*N + D1*M;
        fprintf('[�]� \n');
        disp(EE);
        disp('----------------------');
        fprintf('[K] \n');
        disp(KK);

%Case 2.3
    elseif cn== 2.3

        disp('please enter layer stacking, or use default layer stacking as [0/�45/90]s. ');
        disp('---------------------------------------------------------------------------------------------------------')

        prompt = 'Would you like to use your own Layer Stacking ?, Y/N: ';
        str = input(prompt,'s');
        clc

        if isequal(str, 'Y')

            disp('If the Layer Stacking(LS) is [+-30 0]s enter " [30 -30 0 -30 30] " Do Not Forget to Use Brackets [] !!!')
            l=input('Enter LS >> ');
        else
            l=[0 45 -45 90 90 -45 45 0];
        end
        clc

       angs = l;
       k = {};
       N=length(angs);
       h=zeros(N+1);

       h(N+1)=N*t/2;
       qbarK=zeros(3*N,3);

        %qbar calculations
        for k = 1 : N

            c = cosd (angs(k)); %
            s = sind (angs(k)); %

            %Transformed Reduced Stiffness Matrix
            qbar =zeros(3,3);
            qbar(1,1) = q11*(c^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(s^4);
            qbar(1,2) = q12*((s^4)+(c^4)) + (q11 + q22 - 4*q66)*(s^2)*(c^2);
            qbar(1,3) = (q11 - q12 -2*q66)*s*(c^3) + (q12 - q22 - 2*q66)*(s^3)*c;
            qbar(2,1) = qbar(1,2);
            qbar(2,2) = q11*(s^4) + 2*(q12 + 2*q66)*(s^2)*(c^2) + q22*(c^4);
            qbar(2,3) = (q11 - q12 -2*q66)*c*(s^3) + (q12 - q22 - 2*q66)*(c^3)*s;
            qbar(3,1) = qbar(1,3);
            qbar(3,2) = qbar(2,3);
            qbar(3,3) = (q11 + q22 - 2*q12 - 2*q66)*(s^2)*(c^2) + q66*((s^4)+(c^4));
            %Qbar(1,6) = Qbar(3,1) = Qbar(1,3)
            %Qbar(2,6) = Qbar(2,3) = Qbar(3,2)

            %allqbars
            qbarK([3*k-2:3*k],[1:3])=qbar([1:3],[1:3]);
            %all h values
            h(k)=(k-N/2-1)*t;
            %
        end

        A=zeros(3,3);
        B=zeros(3,3);
        D=zeros(3,3);
    %ABD matrix calculations
     for i=1:3
        for j=1:3
            qbar([1:3],[1:3])=qbarK([1:3],[1:3]);
            A(i,j) = qbar(i,j) * (h(2) - h(1));
            B(i,j) = 1/2*(qbar(i,j) * (h(2)^2 - h(1)^2));
            D(i,j) = 1/3*(qbar(i,j) * (h(2)^3 - h(1)^3));

            for k = 2 : N
            qbar([1:3],[1:3]) = qbarK( [3*k-2:3*k] , [1:3] );
            A(i,j) = qbar(i,j) * (h(k+1) - h(k)) + A(i,j);
            B(i,j) = 1/2*(qbar(i,j) * (h(k+1)^2 - h(k)^2)) + B(i,j);
            D(i,j) = 1/3*(qbar(i,j) * (h(k+1)^3 - h(k)^3)) + D(i,j);
        end
        end

     end

    if rem(length(angs),2)==0
    A= A.*[1 1 0 ; 1 1 0 ; 0 0 1];
    B= B.*[0 0 0 ; 0 0 0 ; 0 0 0];
    D= D.*[1 1 1 ; 1 1 1 ; 1 1 1];

    end
    %inverses
        Ain=inv(A);
        Bin= -((inv(A))*B);
        Cin= B*(inv(A));
        Din= D - (B*(inv(A))*B);
       %midplane
        A1 = Ain-(Bin*(inv(Din))*Cin);
        B1 = Bin*(inv(Din));
        C1 = -(inv(Din))*Cin;
        D1 = inv(Din);

%given Forces and Moments
        N= [2000; 1000; 500];
        M= [2; 2; 0];
        EE= A1*N + B1*M;
        KK= C1*N + D1*M;

        %top graphs
        for z= -0.024:0.006:0.018

           top = EE + (z*KK);

           disp('Top of PLY');
           disp(top);
           fprintf('with \n %d mm\n\n', z);
           subplot(2,3,1);
           hold on;
           plot(top(1,1),z,'-o');
           title('Top of PLY �x');
           ylabel('mm');
           subplot(2,3,2);
           hold on;
           plot(top(2,1),z,'-o');
           title('Top of PLY �y');
           ylabel('mm');
           subplot(2,3,3);
           hold on;
           plot(top(3,1),z,'-o');
           title('Top of PLY &xy');
           ylabel('mm');
        end%according to common thickness

        %bottom graphs
         for z=-0.018:0.006:0.024
             bot = EE + (z*KK);
            disp('Bottom of PLY');
            disp(bot);
            fprintf('with \n %d mm\n\n', z);
            subplot(2,3,4);
            hold on;
            plot(bot(1,1),z,'-*');
            title('Bottom of PLY Ex');
            ylabel('mm');
            subplot(2,3,5);
            hold on;
            plot(bot(2,1),z,'-*');
            title('Bottom of plys Ey');
            ylabel('mm')
            subplot(2,3,6);
            hold on;
            plot(bot(3,1),z,'-*');
            title('Bottom of PLY Exy');
            ylabel('mm');
         end%according to common thickness
    end
