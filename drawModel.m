im = imread('pic.PNG');
im = flipud(im);

[x,y] = meshgrid(-18:1:18,-12:1:12);


% Initial sin model
% u = (2.49 * sin(0.369599136 * (y) + 5) + 0.69);
% v = (2.09 * sin(0.224399475 * (x) + 5) + 0.44);

% Linearly manipulated sin model
% u = (1.16323 * sin(0.40547 * (y) + 2.14085) + 0.55023)-(-0.0931 * y-0.0.1265);
% v = (1.1374957 * sin(0.222722 * (x) + 6.60815) + 0.368331);


% Linearly manipulated and transformed sin model
a = 1.1015;
b = -0.0394;
c = -0.1059;
d = 1.0627;
u = (1.16323 * sin(0.40547 * (c * x + d * y) + 2.14085) + 0.55023)-(-0.0931 * (c*x + d*y)-0.1265);
v = (1.1374957 * sin(0.222722 * (a * x + b * y) + 6.60815) + 0.368331);


% POLYNOMIAL SECTION BELOW %
% u = 8.57277822217765E-11*(y.^(12)) + 1.22964317509335E-11*(y.^(11)) ...
%     -3.1667097651394E-08*(y.^10) - 6.78104898620738E-09*(y.^9) ...
%     + 4.28191984236372E-06*(y.^8) +1.47104788236869E-06*(y.^7) ...
%     -0.000266432419165233*(y.^6) -0.000156588462134784*(y.^5)   ...
%     +0.0082857941613217*(y.^4) + 0.00881914596473338*(y.^3) ...
%     -0.153422597606132*(y.^2) -0.11325832901437*(y.^1) ...
%     + 1.77315789473652*(y.^(0))  ;
% 
% 
% 
% v = + 8.94503461399417*(10^(-12))*(x.^10) + 6.46819054271168*(10^(-11))*(x.^9) ...
%     - 7.88368957509758*(10^(-9))*(x.^8) - 4.73489528259461*(10^(-8))*(x.^7) ...
%     + 2.33880223338077*(10^(-6))*(x.^6) + 0.0000129401005498166*(x.^5)   ...
%     - 0.000231123250510157*(x.^4) - 0.00231804648813399*(x.^3) ...
%     - 0.00199999943818308*(x.^2) + 0.233982539432648*(x.^1) ...
%     + 0.732241972868306*(x.^(0))     ;
%

quiver(x,y,u,v,"r"); axis image
hax = gca; %get the axis handle
image([-20,20],[-14,14],im); %plot the image within the axis limits
hold on; %enable plotting overwrite
color = 	[1 1 1];
quiver(x,y,u,v,Color=color) %plot the quiver on top of the image (same axis limits)
set(gca, 'YDir','reverse')
axis equal;