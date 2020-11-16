function GramSchmidt(V)
% V es la matriz que contiene los vectores considerados almacenados en sus
% columnas
[m n]=size(V); %n vectores, con m componentes
U = zeros(m,n); % una matriz U que tiene el mismo tamaño que la matriz V
U(:,1) = V(:,1); % el primer vector de la matriz V corresponde al primero de la matriz V
%Procedemos a calcular los siguientes vectores U 
for k=2:n 
    S = V(:,k);
    for j=1:k-1
        % Formula de la sumatoria 
        S = S-(dot(V(:,k),U(:,j))/dot(U(:,j),U(:,j)))*U(:,j);
    end
    U(:,k) = S;
end 