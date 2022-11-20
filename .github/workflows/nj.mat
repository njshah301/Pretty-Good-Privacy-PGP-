% Setup code parameters
n = 12; N = 2^n;
e = 0.1; p = 0.1;
d = 0.5; bec = 0; % as you increase d rate increases! but also rate of error, although for no channel error rate = 0 always!

% Compute the quality of all effective channels
if (bec)
    [biterrd] = polar_bec(n,e);
else
    [biterrd] = polar_bsc(n,p,1000);
end

% Design polar code
f = polar_design(biterrd,d);
A = (f==1/2);
k = sum(A);
rate = k/N;

input_bits = [1 1 0 0 1 1 0 1 0 1 0 1 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 1 0 0 1 1 0 0];
input_length = size(input_bits,2);
output_bits = ones(1,input_length);

if (mod(input_length,k) ~= 0)
    input_bits = [input_bits,zeros(1,mod(input_length,k))];
    input_length = size(input_bits,2);
    output_bits = zeros(1,input_length);
end
for i=1:input_length/k+1
    % Set frozen bits, add random data, and encode
    u = f;
    %u(A) = rand(1,k)<0.5; % input, k is number of input bits, thus when we have input bits pass it in packets of size k. % Packets size is also needed while decoding!
    u(A) = input_bits(:,(k*(i-1)+1):(k*i));
    x = polar_transform(u);

    y = x; % no channel!

    % Decode and compute error rate for info bits
    [uhat,xhat] = polar_decode(y,f);
    output_bits(:,(k*(i-1)+1):(k*i)) = uhat(A);
    biterr(i) = mean(uhat(A)~=u(A));
end