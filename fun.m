function out = fun(in)
%Eventual comment here
out = in + 1;
end

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
% function [] = dispn(X,N)
% [I,J] =   size(X);
%    K  = length(N);
% if     K == 1   
    
%     N = N * ones(1,J);
% elseif K ~= J
    
%     disp('ERROR: length(N) must either be 1 or equal to the number of columns of X.')
%     return
% end
% for i = 1:I
%     string = '';
    
%     for j = 1:J
        
%         if X(i,j) >= 0
        
%             string = [string,'   %.', num2str( N(j) ) ,'f'];
%         else
%             string = [string,'  %.' , num2str( N(j) ) ,'f'];        
%         end
%     end
        
%     disp( sprintf( string , X(i,:) ) )
% end